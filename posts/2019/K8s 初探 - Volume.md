---
created_at: 2021-12-09 20:12:21.0
updated_at: 2021-12-09 23:25:03.283
slug: kubernetes-volume-introduction
---

卷只是一个概念，和Docker中的卷是一个意思，可以理解为一个存储挂载点，将pod内部的文件系统与pod外部的文件系统挂载起来，以便pod数据的持久化。

与Docker不同的是，Kubernetes支持非常多种类型的卷（超过二十种）

卷是pod容器的组成部分，并非K8S中的顶级资源，其生命周期和pod一致。可以在pod的文件系统的任何位置挂在卷。如下两张图展示了同一个pod中存在多个容器时，在有卷和没有卷时的区别，可以看到在没有卷时，由于三个容器的文件系统分离，因此都各自操作自己的目录，即使他们在功能上是重复的；有卷时，将同一个卷挂在到两个容器的文件系统中，让他们共享这一块存储，既节省空间，也省去了从一个容器向另一个容器中复制的步骤。
<!-- more -->
![1571731921904](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E5%8D%B7/1571731921904.png)

![1571731875603](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E5%8D%B7/1571731875603.png)

卷消失后，卷的文件可能会保持原样，并且挂载到新的卷。这取决于卷的类型。

## 卷的类型

分为通用卷（k8s系统都会有的）和特殊卷（特殊用途或特殊k8s环境提供的卷）。这里仅介绍最常用的卷。

### emptyDir - 创建空目录

最简单的卷类型，它就是一个空目录，容器可以向其中写入任何数据。与pod声明周期一致，pod消失时，卷的内容会丢失。

当pod创建时，就创建一个新的空目录，没有别的额外操作，当pod消失时，该目录随pod一起被删除，这个比较好理解，熟悉容器的应该知道，pod内新建的文件系统与宿主机是隔离的，专属于pod本身，pod删除时，它自然被删除。

尽管它是最简单的卷，但是其它类型的卷都是在它的基础上发展而来的。比如gitRepo卷，是创建一个空目录，再拉取git仓库的文件；其它类型的卷，是创建一个空目录，然后再将指定的目录挂载到该空目录下。

创建emptyDir卷时需要在pod配置文件中指定

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: fortune
spec:
  containers:
    - image: luksa/fortune
      name: html-generator
      volumeMounts:
        - name: html
          mountPath: /var/htdocs
    - image: nginx:apline
      name: web-server
      volumnMounts:
        - name: html
        mountPath: /usr/share/nginx/html
        readOnly: true
  ports:
    - containerPort: 80
      protocol: TCP
  volumes:
    - name: html
      emptyDir: {}	# 默认是存在磁盘上的，也可以按照如下方式配置在内存中
    #emptyDir:
    #  medium: Memory
```

### gitRepo - 挂载git仓库文件（弃用）

来源于emtryDir卷，它是在pod启动时检出git仓库中特定版本的内容填充到目录中。

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: gitrepo-volume-pod
spec:
  containers:
    - image: nginx:apline
      name: web-server
      volumnMounts:
        - name: html
        mountPath: /usr/share/nginx/html
        readOnly: true
  ports:
    - containerPort: 80
      protocol: TCP
  volumes:
    - name: html
      gitRepo: 
        repository: http://git.dev.moumoux.com/ergedd/ergeddUtils
        revisioin: master
        directory: . # 将内容克隆到卷的根目录
```

由于gitRepo卷是在卷创建时从git克隆一次代码，因此当git仓库更新时pod是无法同步的。要做到同步，有如下两种方式

- 删除pod再创建
- 新建一个sidecar容器，用于同步卷中内容。Docker hub中搜索“git syc”可以看到很多相关的实现。

### hostPath - 挂载工作节点上的文件

hostPath卷指向pod所属节点上的特定文件路径，同一个节点运行的两个pod通过hostPath卷可以看到相同的内容。它是一种持久存储的卷，因为节点文件系统中的内容并不会随着pod的释放而被删除。

它的缺点是对于pod来说不稳定，因为当发生pod调度时，可能被调度到另一个节点，这样对于这个pod来说之前写在节点上的文件就不见了。

使用场景

- 只读访问节点上的文件，比如某些pod专门用于访问节点上的日志
- 有状态应用的pod，需要将数据存入节点，且pod分配稳定。比如Kubernetes的存储组件——etcd

### 网络存储卷

总结一下上面说的三种卷

- Empty：在pod内部创建一个空目录，与pod外部无关
- gitRepo：在pod内部创建一个空目录，然后从git仓库拉取文件到该目录，与pod外部无关
- hostPath：在pod内部创建一个空目录，然后将其所在工作节点的文件挂载到该目录，与工作节点有关

还有一个场景未覆盖到：将pod的数据存储在一个与工作节点无关的独立的位置——网络存储（NAS），比如运行一个有状态应用mongodb，然后挂载GCE磁盘：

![image-20211209113455988](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211209113455988.png)

下面展示了几种合适的卷

```yaml
# 基于GCP持久盘的卷
......
spec:
  volumes:
    - name: mondodb-data
      gcpPersistentDisk:
        pdName: mondoDb
        fsType: ext4
  containers:
    - image: nginx:apline
      name: web-server
      volumnMounts:
        - name: mondodb-data
          mountPath: /usr/db
......
# 基于AWS持久盘的卷
......
spec:
  volumes:
    - name: mondodb-data
      awsElasticBlockStore:
        volumnId: my-volume
        fsType: ext4
......
# 基于普通共享NFS存储的卷
......
spec:
  volumes:
    - name: mondodb-data
      nfs:
        server: 1.2.3.4
        path: /some/path
......
```

> 当然，除了云服务厂商提供的磁盘，还可以挂载nfs卷，访问自建的网络磁盘

### 其它

卷有很多种类型，远不止上述那些，详情参考[官方手册](https://kubernetes.io/zh/docs/concepts/storage/volumes/)。在查看时，尤其注意几个卷类型

- local：挂载本地磁盘、分区或目录
- configmap：挂载ConfigMap
- secret：挂载Secret

## 持久卷

上面创建的持久化的卷，需要开发人员在配置pod时配置NAS的网络存储位置，使得开发人员、pod与底层的实际存储技术和存储地址耦合了起来。不符合k8s的策略，即对开发人员将底层技术抽象、解耦。

于是引入了**持久卷**和**持久卷声明**的概念，即**PV**和**PVC**

持久卷（PersistentVolume）：封装了底层的存储技术，不属于任何命名空间，整个k8s共享，属于基础资源。是k8s集群管理员需要创建的资源。

持久卷声明（PersistentVolumeClaim）：用于开发人员声明需要的存储容量和访问模式，在命名空间内部。是开发人员自己需要创建的资源。

> 持久卷，很好理解：卷是将pod外部的存储挂载到pod的挂载方式的声明，但每次都要在创建pod时声明，持久卷，就是对这种挂在方式声明的持久化，方便直接使用。

二者都是k8s的顶级资源，需要单独创建，且不属于任何命名空间。

> 注意：引入PV和PVC整体而言是提升了复杂度，但如果一个团队有系统管理员负责维护PV和PVC，开发人员的工作会减少。

一个常规的创建PV和PVC的流程如下

![](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211209120814344.png)

与不使用持久卷相比，好处显而易见

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211209122252200.png" alt="image-20211209122252200" style="zoom:80%;" />

### 创建持久卷

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: mogodb-pv
spec:
  capacity:
    storage: 1Gi  # 声明卷的大小
  accessModes:
    - ReadWriteOnce  # 可以被单个用户挂载为读写模式
    - ReadOnlyMany  # 可以被多个用户挂在为只读模式
  persistentVolumeReclaimPolicy: Retain  # 当声明被释放后，PersistentVolume将会被保留
  gcePersistentDisk:
    pdName: mongodb
    fsType
```



### 创建持久卷声明

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongodb-pvc
spec:
  resources:
    requests:
      storage: 1Gi  # 声明需要1Gi存储空间
  accessModes:
    - ReadWriteOnce  # 声明需要的访问模式为RWO
  storageClassName: ""
```

该声明和上面的持久卷是相匹配的，因此使用该声明时上述持久卷会被分配。

### 使用持久卷

```yaml
# 创建pod时的关于卷的声明如下
......
volumes:
  - name: mongodb-data
    persistentVolumeClaim:
      claimValue: mongodb-pvc
......
```

使用后的结构

![1571738187793](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E5%8D%B7/1571738187793.png)

### 持久卷的回收机制

- Retain: 持久卷声明被释放后依然保留该持久卷，当PVC释放它后，它保持为释放状态，无法再被新的PVC引用。并且以后可以再配置给其它pod使用（文章是这么说，但我的问题是既然无法再被新的PVC引用，新的pod又如何去用这个被释放了的持久卷呢？）。删除该持久卷的唯一方式是手动删除持久卷资源。
- Recycle: 持久卷声明被释放后，该持久卷可以被新的PVC引用（数据应该还存在）
- Delete: 释放后删除持久卷

## StorageClass

上面我们看到了持久卷的用法，但它还有一个问题是需要集群管理员维护存储卷资源，这样不够科学。于是有了StorageClass这个资源。它是一个顶级资源，并且和持久卷一样，也是不属于任何命名空间的。

StorageClass定义了一个策略，在开发者使用PVC时创建一个新的持久卷，好处是不用管理员维护，并且与预先设置的持久卷不同，他不会耗尽持久卷存储。

### 谁提供存储

听起来很好，只声明存储类，不声明PV，那么最终的存储设备是谁提供呢？答案是集群供应商，这是他们提供的插件。比如下面的GCE，在minikube这样的本地集群中也有相应的插件来管理。

- 对于云服务商，一般会根据PVC的需求创建一个云盘
- 对于minikube

### 使用

```yaml
# 声明一个StorageClass，这部分一般由管理员去做
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast
provisioner: kubernetes.io/gce-pd  # 这是用于配置持久卷的插件，可以指定别的插件
parameters:  # 这是传给上述插件的参数
  type: pd-ssd
  zone: europe-west1-b

# PVC声明
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongodb-pvc
spec:
  storageClassName: fast
  resources:
    requests:
      storage: 100Mi
    accessModes:
      - ReadWriteOnce
```

![1571746264340](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20%E5%8D%B7/1571746264340.png)

### 创建没有StorageClass的PVC

创建PVC时不指定SC，会被分配一个默认的SC。通过`kubectl get sc`可以查看默认的存储类。

### 强制将预先设置的PV绑定到PVC

```yaml
......
kind: PersistentVolumeClaim
spec:
  storageClassName: ""  # 将该字段设置为空，则是绑定到预先手动配置的PV，而不是动态配置的PV
......
```

## 最佳实践 - minikube部署Redis集群

首先我们需要了解：minikube是运行在隔离环境中的，比如VM、容器。在我的macbookpro m1上，它运行在docker中，因此要先将本地文件挂载minikube中，然后才能挂载到pod。

### 挂载到minikube

```shell
mkdir ~/.minikube/data:/data
minikube mount ~/.minikube/data:/data
```

### 创建PV

我们的集群有三个节点，因此需要三个数据卷，因此我们创建三个PV，分别对应三个不同的文件夹，他们每个都只能被使用一次。

注意这里我们没有创建PVC，因为集群是有状态应用，其PVC实配置在volumeClaimTemplates中的，所以后面再配。

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv1
spec:
  capacity:
    storage: 10Mi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  local:
    path: /data/redis-data-1
  storageClassName: ""
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - minikube
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv2
spec:
  capacity:
    storage: 10Mi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  local:
    path: /data/redis-data-2
  storageClassName: ""
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - minikube
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: redis-pv3
spec:
  capacity:
    storage: 10Mi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  local:
    path: /data/redis-data-3
  storageClassName: ""
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - minikube
```

### 创建Redis集群配置文件

三个节点，每个节点的配置文件都长得一样

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: redis-cluster
data:
  update.sh: |
    #!/bin/sh
    REDIS_NODES="/data/nodes.conf"
    sed -i -e "/myself/ s/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/${POD_IP}/" ${REDIS_NODES}
    exec "$@"
  redis.conf: |+
    bind 0.0.0.0
    cluster-enabled yes
    cluster-require-full-coverage no
    cluster-node-timeout 30000
    cluster-config-file /data/nodes.conf
    cluster-migration-barrier 1
    appendonly yes
    protected-mode no
```

### 创建网络

```yaml
apiVersion: v1
kind: Service
metadata:
  name: redis-cluster
  labels:
    app: redis
spec:
  ports:
  - name: redis-port
    port: 6379
  clusterIP: None
  selector:
    app: redis-cluster
```

### 创建集群

这是一个StatefulSet，注意volumeClaimTemplates，它指定的存储大小和上面的PV要匹配。

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: redis-cluster
spec:
  serviceName: redis-cluster
  replicas: 3
  selector:
    matchLabels:
      app: redis-cluster
  template:
    metadata:
      labels:
        app: redis-cluster
    spec:
      containers:
      - name: redis
        image: redis:6.2.1-alpine
        ports:
        - containerPort: 6379
          name: client
        - containerPort: 16379
          name: gossip
        command: ["/conf/update.sh", "redis-server", "/conf/redis.conf"]
        env:
        - name: POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        volumeMounts:
        - name: conf
          mountPath: /conf
          readOnly: false
        - name: data
          mountPath: /data
          readOnly: false
      volumes:
      - name: conf
        configMap:
          name: redis-cluster
          defaultMode: 0755
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 10Mi
      storageClassName: ""
```

### 跑起来

可以发现它们确实跑起来了

```shell
zouguodong@zouguodongdeMBP redis-cluster % kubectl get statefulset
NAME            READY   AGE
redis-cluster   3/3     9m48s

zouguodong@zouguodongdeMBP redis-cluster % kubectl get pods
NAME              READY   STATUS    RESTARTS   AGE
redis-cluster-0   1/1     Running   0          9m53s
redis-cluster-1   1/1     Running   0          9m34s
redis-cluster-2   1/1     Running   0          9m31s

zouguodong@zouguodongdeMBP redis-cluster % kubectl get pvc
NAME                   STATUS   VOLUME      CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-redis-cluster-0   Bound    redis-pv1   10Mi       RWO                           10m
data-redis-cluster-1   Bound    redis-pv2   10Mi       RWO                           9m42s
data-redis-cluster-2   Bound    redis-pv3   10Mi       RWO                           9m39s

zouguodong@zouguodongdeMBP redis-cluster % kubectl get pv
NAME        CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                          STORAGECLASS   REASON   AGE
redis-pv1   10Mi       RWO            Retain           Bound    default/data-redis-cluster-0                           12m
redis-pv2   10Mi       RWO            Retain           Bound    default/data-redis-cluster-1                           12m
redis-pv3   10Mi       RWO            Retain           Bound    default/data-redis-cluster-2                           12m
```

可以查看一个PVC的yaml输出，可以发现它使用了volumeName强绑定了一个pv。

```shell
zouguodong@zouguodongdeMBP redis-cluster % kubectl get pvc data-redis-cluster-0 -o yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    pv.kubernetes.io/bind-completed: "yes"
    pv.kubernetes.io/bound-by-controller: "yes"
  creationTimestamp: "2021-12-09T06:42:12Z"
  finalizers:
  - kubernetes.io/pvc-protection
  labels:
    app: redis-cluster
  name: data-redis-cluster-0
  namespace: default
  resourceVersion: "20518"
  uid: ceedaaf5-704b-4cfa-a91b-66fb2e6793b1
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Mi
  storageClassName: ""
  volumeMode: Filesystem
  # 这里强绑定了，也是StatefulSet的特点
  volumeName: redis-pv1
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 10Mi
  phase: Bound
```

### 后续

到这里，集群建立还没完成，因为现在每个集群都是主节点，还没构成一个集群。如果要构成一个完整的集群，需要执行更多操作，具体可参考[这篇文章](https://github.com/Lancger/opsfull/blob/master/redis/K8s%E4%B8%8A%E8%BF%90%E8%A1%8CRedis%E9%9B%86%E7%BE%A4%E6%8C%87%E5%8D%97.md#4%E5%88%9B%E5%BB%BAheadless-service)

## 总结

重点是理解几个概念

- 卷Volume
- PV
- PVC
- StorageClass

此外，本文未涉及的一些概念同样重要，读者可以通过官方手册学习

- CSI：Kubernetes定义的容器存储标准接口，就像CRI（容器运行标准接口）
- projected卷：即将多个卷来源合并成一个卷，目前支持secret、downwardAPI、configMap、serviceAccountToken
- 卷克隆：从已有的卷克隆
- 临时卷：即不需要保存的卷
- 卷快照：见名知意

## 参考

- 首先教你入门——《Kubernetes in Action》
- 然后必须看——[官方手册](https://kubernetes.io/zh/docs/concepts/storage/)