---
created_at: 2019-10-27 18:12:25.0
updated_at: 2021-02-16 23:24:25.056
slug: kubernetes-stateful-set-introduction
---

什么是有状态pod，即pod的运行状态与该pod耦合，当发生pod调度时新创建的pod必须和原有pod保持一致的状态，否则会出现状态丢失。前面我们所学习的pod都是由RC或RS创建的，然而他们无法满足pod对状态的需求。于是我们有了StatefulSet，它是专门定制的一类应用，这类应用的每个实例都是不可替代的个体，都拥有稳定的名字和状态。
<!-- more -->
## StatefulSet和RS或RC对比

RS或RC的实例挂掉后，会重新创建一个与之前并不相关的实例。而对SS来说，当一个实例挂掉后，新创建的实例会保持原有实例的名称、网络和状态。下面我们来看它是如何做到的

### 稳定的网络标识

与RS不同，SS创建的pod拥有规则的命名和主机名，这样方便管理。

由于每个有状态的pod之间的都是不一样的，所以经常需要定位到某一具体的pod，所以一个SS要求我们创建一个用来记录每个pod网络标记的headlessService。通过这个service，每个pod将拥有独立的DNS记录，这样集群中其它的pod就能通过主机名方便地找到它。

至于扩缩容，pod的命名是依照其先后顺序的索引，缩容时是先删除索引号最大的那个pod，这个比较好明确。且为了保证分布式应用的安全性，缩容时k8s每次只会操作一个pod实例，以免同时操作多个pod实例带来的潜在的数据丢失风险。

### pod的专属存储

RS由于pod是无状态的，因此再多pod实例都是当做一个实例看待，因此所有实例共享同样的卷。SS由于需要保存实例状态，因此每个pod实例需要单独的存储卷，这是通过为每个pod实例绑定一个卷声明做到的。如下

![image-20191027173409275](
https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20StatefulSet/image-20191027173409275.png)

新增pod时，会使用SS的PVC模板创建新的PV和PVC。删除pod时，由于数据的重要性，为防止误删，k8s只会删除pod，对应的PV和PVC都不会释放，而是需要用户手动删除。如果不手动删除，当再次创建pod时，之前的PV和PVC会被重新挂载到该pod上。该pod也会运行到和删除之前一样的状态。

![image-20191027173733318](
https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20StatefulSet/image-20191027173733318.png)

### at-most-one

一种场景：对于有状态pod，如果因为k8s对pod状态判断不准确，导致在一个pod还在运行时又创建了一个新的pod，产生了两个pod抢夺状态的情况，这是不被允许的。因此SS必须保证pod有at-most-one语义。实现方式为，如果SS无法确定一个pod的状态，将拒绝扩容的请求，此时需要用户手动强制删除该pod。

## 使用SS 

使用SS部署应用需要按照如下三步走

- 创建存储数据文件的持久卷
- 创建一个headless的控制Service
- 创建SS本身

前两个的创建不再多说，可以查看前面有关服务和卷的章节，这里只说创建SS，yaml文件如下。SS创建pod时，由于有状态集群在两个节点之间的竞争是非常敏感的，因此node是一个启动成功再启动新的pod，故速度会比较慢。

```yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: kubia
spec:
  serviceName: kubia	# 前面创建的headlessService
  replicas: 2
  template:
    metadata:
      labels:
        app: kubia
    spec:
      containers:
      - name: kubia
        image: zou8944/kubia
        ports:
        - name: http
          containerPort: 8080
        volumeMounts:
        - name: data
          mountPath: /var/data
volumeClaimTemplates:	# 这是RC和RS所没有的
- metadata:
  name: data
  spec:
    resources:
      requests:
        storage: 1Mi
    accessModes:
    - ReadWriteOnce
```

创建SS后，就可以开始使用了。最简单的方式就是使用Kubernetes API进行访问。还记得之前说的Kubectl proxy吗，可以在本地运行一个代理，然后通过代理访问API。命令如下

```shell
# API 路径
<apiServerHost>:<port>/api/v1/namespaces/default/pods/kubia-0/proxy/<path>
# 此处访问pod0的地址为
127.0.0.1:8001/api/v1/namespaces/default/pods/kubia-0/proxy/
```

此时的访问结构如下

![image-20191027175851844](
https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20StatefulSet/image-20191027175851844.png)

## 在SS中发现伙伴pod

如何在一个有状态pod中找到同SS中的另一个pod呢？肯定不能通过Kubernetes API访问，这会使应用和k8s耦合。答案是使用SRV记录。SRV记录是用来指向提供指定服务的服务器的主机名和端口号。k8s通过一个headless service创建SRV记录来指向pod的主机名。当一个pod想要获取SS中其它pod列表时，要做的只是触发一次SRV DNS查询，而每种语言都提供了特定的方式。对于命令行，可以通过dig查看

```shell
dig SRV kubia.default.svc.cluster.local
```