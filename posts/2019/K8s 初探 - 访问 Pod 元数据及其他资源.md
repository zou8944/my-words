---
created_at: 2019-10-26 11:49:30.0
updated_at: 2021-02-16 23:24:42.019
slug: kubernetes-introduction-pod-meta
---

对于特殊的pod，比如系统监控应用，知晓应用运行环境的各项参数是很常见的功能。Kubernetes对此也提供了很好的支持，用户可以通过环境变量、文件、API等多种方式获取到相关数据。
<!-- more -->

## 通过Downward API

想要获得预先无法知晓的数据，比如POD的IP、主机名等，可以通过Downward API获取。虽然名叫API，但它允许我们通过环境变量或者downward卷传递pod中的数据，而不是通过发送请求的方式。其结构如下

![image-20191026095824633](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026095824633.png)

通过Downward API，我们可以获得如下pod数据

- 名称
- IP
- 命名空间
- 节点名称
- 所属服务账户名称
- 每个容器请求的CPU和内存
- 每个容器可以使用的CPU和内存的限制
- 标签和注解

### 环境变量

通过如下方式将其暴露在环境变量中

```yaml
......
# 这里接着一个container项的env
env:
  - name: POD_NAME
    valueFrom:
      fieldRef:
        fieldPath: metadata.name
  - name: POD_NAMESPACE
    valueFrom:
      fieldRef:
        fieldPath: metadata.namespace
  - name: POD_IP
    valueFrom:
      fieldRef:
        fieldPath: metadata.podIP
  - name: NODE_NAME
    valueFrom:
      fieldRef:
        fieldPath: spec.nodeName
  - name: SERVICE_ACCOUNT
    valueFrom:
      fieldRef:
        fieldPath: spec.serviceAccountName
  - name: CONTAINER_CPU_REQUEST_MILLICORES
    valueFrom:
      resourceFieldRef:
        resource: requests.cpu
        divisor: 1m
  - name: CONTAINER_MEMORY_LIMIT_KIBIBYTES
    valueFrom:
      resourceFieldRef:
        resource: limits.memory
        divisor: 1Ki
```

其实对应如下图所示

![image-20191026101622624](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026101622624.png)

### downward卷

挂载的方式如下

```yaml
# 如下接着container标签写
      volumeMounts:
        - name: downward
          mountPath: /etc/downward
   volumes:
     - name: downward
       downwardAPI:
         items:
           - path: "podName"
             fieldRef:
               fieldPath: metadata.name
            ...... # 接下来写的和环境变量中的配置类似，这里不再赘述
```

完成配置后结果如下

![image-20191026102038019](image-20191026102038019.png)

## 通过Kubernetes API

### 探究k8s API

可以像正常那样通过k8s提供的restful API访问，但如下图所示，这些地址都是采用https传输，因此跟他们交互也不是意见特别容易的事情。

![image-20191026103024214](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026103024214.png)

为此，k8s提供了代理。运行如下命令可启动一个代理，该代理替我们处理好了一切，我们只需要访问它即可。

![image-20191026103637438](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026103637438.png)

访问该代理地址，可以得到所有可用的API地址

![image-20191026103733430](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026103733430.png)

访问这些地址中的一个，可以得到进一步的地址

![image-20191026103807750](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026103807750.png)

再访问这些地址，可以得到最终结果

![image-20191026103845268](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026103845268.png)

### 从POD内部访问API

上面仅介绍了从本机访问API，这里介绍如何在POD内部访问。

POD中就没有kubectl可用了，于是只有老老实实进行授权和验证操作，主要有以下几个步骤。

- 确定访问ip和端口

  通过查看POD的`KUBERNETES_SERVICE`环境变量可得到ip地址和端口

  ```bash
  root@curl:/# env | grep KUBERNETES_SERVICE
  KUBERNETES_SERVICE_PORT=443
  KUBERNETES_SERVICE_HOST=10.107.0.1
  KUBERNETES_SERVICE_PORT_HTTPS=443
  ```

  又由于每个服务都会自动获得一个DNS入口，因此也可以直接访问https://kubernetes

- 安全验证

  通过运行`kubectl describe pod curl`可以看到该pod中有挂载了一个secret卷，它是创建pod时候自动创建的。

  ![image-20191026110236335](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026110236335.png)

  访问改地址，可以看到如下结构

  ![image-20191026110731625](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026110731625.png)

  其中ca.crt是CA证书，用于客户端验证服务端身份；token用于客户端发送请求时加到Authorization请求头中，用户服务端验证客户端请求；namespace则是客户端执行增删改查时需要传递的命名空间信息。

  于是我们可以通过如下命令访问API

  ```shell
  # 将证书挂载到环境变量
  export CURL_CA_BUNDLE=/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
  # 将token挂载到环境变量
  export TOKEN=/var/run/secrets/kubernetes.io/serviceaccount/token
  # 带上头访问即可
  curl -H "Authorization: Bearer $TOKEN" https://kubernetes
  ```

- 使用namespace

  如上面所说，namespace用于增删改查时的指定，这里展示

  ```shell
  export NS=/var/run/secrets/kubernetes.io/serviceaccount/namespace
  curl -H "Authorization: Bearer $TOKEN" https://kubernetes/api/v1/namespace/$NS/pods
  ```

下面展示了三者之间的关系

![image-20191026112434344](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026112434344.png)

### ambassador容器

上述步骤实在是太麻烦了，这里介绍一个简单的方法：ambassador容器。其原理是在同一个pod中新建一个应用，它依旧使用绑定的Secret信息与k8s API进行安全通信，但暴露HTTP接口给我们的主应用访问，使得主应用访问时不用每次都指定那些安全参数。

其建立方式如下

```yaml
......
spec:
  container:
    - name: main
      ......
    - name: ambassador
      image: luksa/kubectl-proxy:1.6.2  # ambassador容器，和运行kubectl proxy命令一样的效果。
```

这样建立后，由于pod内各应用共享ip，应用之间又是http通信，因此可以直接通过`localhost:8001`的方式直接访问。

![image-20191026113239941](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E8%AE%BF%E9%97%AEpod%E5%85%83%E6%95%B0%E6%8D%AE%E5%8F%8A%E5%85%B6%E5%AE%83%E8%B5%84%E6%BA%90/image-20191026113239941.png)

### 客户端库访问

如果有复杂的访问请求，可以使用各种语言的访问库，可以网上找找Kubernetes API客户端库。

如果是想要概览研究API，强烈推荐Swagger UI的方式访问，默认该服务没有开启，但可手动启动。