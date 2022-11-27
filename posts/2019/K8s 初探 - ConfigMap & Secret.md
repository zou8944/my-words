---
created_at: 2019-10-24 21:12:48.0
updated_at: 2021-02-16 23:24:57.593
slug: kubernetes-configmap-secret-introduction
---

根据应用的开发进程，应用的配置一般会经历先嵌在应用本身，或通过命令行参数的形式传入。到测试生产阶段随着配置的增多会抽取为一个或多个配置文件。对于容器化应用，我们还可以为容器设置环境变量，应用中读取该变量即可。而对于K8S，还可以使用gitRepo卷作为配置文件的载体。但这些都还是太笨重了，K8S提供了更加简单的方法：ConfigMap，用于提供普通配置；Secret用于提供需要加密的配置。
<!--more-->
## 容器化应用的配置

我们先来看容器本身可执行的配置方法

### 使用命令行和参数

#### Docker的方式

```dockerfile
FROM ubuntu
RUN apt-get update ; apt-get -y install fortune
ADD fortuneloop.sh /bin/fortuneloop.sh
ENTRYPOINT ["/bin/fortuneloop.sh"]
CMD ["10"]
```

上面的dockerfile定义了一个镜像，基于ubuntu，安装下载fortune，并将本地的fortuneloop脚本复制到镜像中，然后定义ENTRYPOINT运行，并且给该脚本一个参数：10。注意ENTRYPOINT有两种方式

- ENGTYPOINT["/bin/fortuneloop.sh"]: exec形式，在shell环境下运行该脚本。即首先启动shell进程，再在该进程下运行这个脚本
- ENTRYPOINT /bin/fortuneloop.sh: shell形式，直接运行该脚本

一般采用exec形式。

上面定义后，可以在运行docker时传递一个参数覆盖CMD参数

```shell
docker run -it <docker name> 15 # 15会覆盖上面的10
```

#### K8S的方式

上面用ENTRYPOINT和CMD共同决定了容器的运行命令。在POD声明时可以覆盖这二者。

```yaml
......
spec:
  containers:
    - image: zou8944/kubia
      command: ["node hello.js"]  # 覆盖dockerfile中的ENTRYPOINT
      args: ["10"]   # 覆盖dockerfile中的CMD
......
```

### 使用环境变量

容器之间相互隔离，因此可为每个容器设置各自的环境变量。

```yaml
......
spec:
  containers:
    - image: zou8944/kubia
      env:
        - name: ENVNAME  # 设置了一个名为ENVNAME，值为lalal的环境变量
          value: "lalal"
        - name: ENVNAME2
          value: "${ENVNAME} dd"  # 设置名为ENVNAME2，值为lalal dd的环境变量，这里有引用其它变量名
......
```

但是，使用上面的方式会将配置和pod耦合起来，很明显不科学。

## ConfigMap

和其它对象一样，ConfigMap也是一种资源，其本质上是一个键值对，值可以是字面量，也可以是配置文件。应用不用直接读取ConfigMap的内容，因此不会感知到它的存在。

### 创建（命令行）

```yaml
# 创建了一个含有两个key-value的configmap。
kubectl create configmap my-config 
  --from-literal=interval=5  # 从字面量创建
  --from-file=myfile.conf  # 将整个配置文件中的内容导入为配置
  --from-file=mykey=myfile.conf  # 导入一个key为mykey,value为myfile.config的键值对配置
  --from-file=/path/dir    # 导入一个文件夹，将其中所有命名符合要求的文件名作为key，文件内容作为value
```

### 创建（yaml）

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: myConfig
data:
  key1: "value1"
  key2: "value2"
```

### 使用

- 单独引用配置中的一个条目

  ```yaml
  ......
  spec:
    containers:
      - image: zou8944/kubia
        env:
          - name: ENVNAME  
            valueFrom:
              configMapKeyRef:
                name: myconfig  # ConfigMap的名称
                key: interval  # 键名
                optional: true # 就算该ConfigMap或key不存在也照常启动。不设置时不会启动
  ......
  ```

- 将整个配置文件全部引入

  ```yaml
  ......
  spec:
    containers:
      - image: zou8944/kubia
        envFrom:
          - prefix: CONFIG_  # 在每个键前加上前缀
            configMapRef:
              name: myconfig
  ......
  ```

- 将ConfigMap条目暴露为文件

  假设有如configmap-files文件夹，其中包含两个文件，my-nginx-config.conf和sleep-internal

  ![image-20191024202924093](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20ConfigMap%E5%92%8CSecret/image-20191024202924093.png)

  通过`kubectl create configmap myconfig --from-file=configmap-files`创建一个ConfigMap，可通过如下配置将其暴露为卷。

  ```yaml
  # 挂在整个文件， 此时就相当于将configmap-files中的两个文件放到了nginx的配置文件夹/etc/nginx/conf.d中
  ......
  spec:
    containers:
      - image: nginx.alpine
        name: web-server
        volumeMounts:
          - name: config
            mountPath: /etc/nginx/conf.d
            readOnly: true
    volumes:
      - name: config
        configMap:  # 将configMap暴露为卷
          name: myconfig
  ......
  
  # 挂在单个条目， 此时就相当于/etc/nginx/conf.d中只有一个文件gzip.conf，该文件的内容是my-nginx-config.conf中的内容
  ......
    volumes:
      - name: config
        configMap:  
          name: myconfig
          defaultMode: "6600"  # 为文件设置默认权限
          items:
            - key: my-nginx-config.conf
              path: gzip.conf
  ......
  ```

- 注意事项

  如果将ConfigMap挂载在某个特定的文件夹下，则该文件夹下已存在的文件会被隐藏。所以推荐挂载在文件，或新建一个文件夹。

### 热更新ConfigMap

ConfigMap修改后，挂载它的卷中的文件也会被更新。其原理是使用符号链接，ConfigMap卷中的文件其实是一个符号链接，指向实际的文件，更新后，k8s创建新的文件，然后将链接指向新文件，然后就生效了。

需要注意的一点是更新ConfigMap是有延迟的，如果有多个POD，则可能会出现某个时段不一致的情况。

## Secret

Secret的使用方法和ConfigMap一毛一样。其保证安全性的方法是：

- 仅将Secret分发到需要的pod所在的机器节点
- Secret只存在内存中，不保存在磁盘上

### 创建

有两种创建方式，命令行和yaml，由于Secret中字段值会被Base64处理，因此使用命令行直接处理比较好。

```shell
# 证书文件都是事先生成好的
kubectl create secret generic myhttps --from-file=https.key --from-file=https.cert
```

查看创建好的secret如下，可以看到都变成加密的了。

![image-20191024210340290](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20ConfigMap%E5%92%8CSecret/image-20191024210340290.png)

尽管这里看是加密的，但当其被设置为环境变量或Secret卷时填充的却是解码后的内容。

### 使用

还是以nginx配置为例

```yaml
... ...
spec:
  containers:
    - image: nginx.alpine
      name: web-server
      volumeMounts:
        - name: config
          mountPath: /etc/nginx/conf.d
          readOnly: true
        - name: certs
          mountPath: /etc/nginx/certs/	# 将文件挂在到certs文件夹下，再在Nginx中配置即可使用https
          readOnly: true
  volumes:
    - name: config
      configMap:  # 将configMap暴露为卷
        name: myconfig
    - name: certs:
      secret:
        secretName: myhttps
......
```

将Secret设置为环境变量的方式和ConfigMap一致，不再赘述。