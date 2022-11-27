---
created_at: 2022-04-25 17:23:49
updated_at: 2022-04-25 17:23:49
slug: kubernetes-resource-in-action
---

>  文章描述由一个问题引起的解决方案思路的探究以及最终的实践，具有借鉴参考意义。

<!--more-->

# 问题

我们的使用场景是应用多、访问量小，细化一下

- 应用数量接近20
- 如果每个pod都设置replicas为2，则需要40个pod
- 日常稳定运行时每个pod占用10m核、500Mi左右。40个pod也不过占用400m核、20Gi
- 目前我们使用两台2c16g配置ECS作为worker节点，用于应对日常需求。外加三个ECI节点，用于ECS资源不足时的扩展。

时间下来有如下问题

- 希望设置2个副本的应用pod均匀地分布在两个worker节点，于是设置强制性的应用反亲和（和自己反亲和），但在滚动升级时因为临时出现超过2个副本而报资源不足
- 对ECI节点使用不熟悉，拿不准pod什么时候会被分配上去
- 应用启动慢，60s往上

# 应用分布标准方案

为了解决上述问题，首先需要了解Kubernetes为应用分布提供的标准方法，总计四种。

- 节点亲和性

  让应用强制或优先分配到某些或某类节点。具体[参考手册](https://kubernetes.io/zh/docs/tasks/configure-pod-container/assign-pods-nodes-using-node-affinity/)

- 应用亲和性/反亲和性

  让应用强制或优先和某些或某类应用所属的节点上。具体[参考手册](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/assign-pod-node/#inter-pod-affinity-and-anti-affinity)

- 污点容忍度

  亲和性的反向操作，用于节点选择应用而不是应用选择节点（具有污点的节点，如果应用不显式声明容忍该污点，则无法被分配到该节点）。具体[参考手册](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/)

- 拓扑分布约束

  让应用按照某个维度均匀分布，维度自定义，通过节点标签指定。常见的如可用区、节点等。具体[参考手册](https://kubernetes.io/zh/docs/concepts/workloads/pods/pod-topology-spread-constraints/)

四者互相辅助能完成大多数应用分配的需求。我们首要的需求是：多个副本的应用均匀地分布在两个worker节点，有两种实现方式

- 方式一：非强制的应用反亲和配置 + ECI污点

  前者使得应用尽量在节点上均匀分布，但由于这些配置只是给kube scheduler提建议，不一定采纳，我们能做的也只是调大weight值到100，实测有用；后者是为了pod不被分配到ECI节点上。

  一个配置的例子

  ```yaml
  spec:
    template:
      spec:
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
              - podAffinityTerm:
                  labelSelector:
                    matchLabels:
                      app: foundation-payment
                  topologyKey: kubernetes.io/hostname
                # 写到最大
                weight: 100
  ```

- 方式二：拓扑分布约束 + ECI污点

  ECI污点作用同上；拓扑分布约束则是直接意义上的均匀分布，这应该是最标准的处理方式，实测也是有效的。如下是一个配置的例子

  ```yaml
  spec:
    template:
      spec:
        topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: ScheduleAnyway
            labelSelector:
              matchLabels:
                app: foundation-payment
  ```

> 尝试过的无效方法：设置非强制的节点亲和性，ECI节点无污点。有一点点作用，但pod还是很容易在ECS还有大量资源的情况下被分配到ECI节点。

# 阿里云的virtual-kubelet-autoscaler

上面，我们解决了pod数大于节点数均匀分布的问题。但是ECS节点资源不足时自动分配到ECI节点的需求还没有解决。

这个问题，可以通过安装virtual-kubelet-autoscaler插件实现，相关的几篇文档

- https://www.xingsuyun58.com/8654.html
- https://zhuanlan.zhihu.com/p/81238854
- https://developer.aliyun.com/ask/423342

其原理是在ECI打上污点，使得平时应用不会分配上去，但检测到pod因为资源不足而创建失败的事件时，会重新尝试分配到ECI节点。十分适合我们想要的场景。

> 值得注意的是，virtual-kubelet-autoscaler并不是终点，如果应用访问量上来了，日常资源占用增多，在一两个节点上挤太多应用可能出现驱逐事件，造成服务短暂宕机，而宕机的时间取决于应用启动的时间。此时弹性伸缩ECS，或者直接分配ECI才是长久的解决方式。

# 应用启动慢解决

主要是Java应用启动慢，当前为每个Java应用分配的cpu资源为 requests: 100m；limits: 200m。受到[这篇文章](https://heapdump.cn/article/2429542)启发，为每个应用分配limits: 1000m，启动速度问题得以解决，实测不加链路追踪时启动时间下降为25s；加链路追踪时启动时间也不过43s左右。

> 而关于cpu设置为1000m的限制会不会对其它应用产生影响，在官方手册[节点压力驱逐](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/node-pressure-eviction/)一节并没有说明CPU高压时会怎样，而根据[这篇文章](https://www.1024sou.com/article/288103.html)，CPU属于可压缩资源，不会造成节点驱逐，最坏的情况也不过是应用反应慢。因此为节点设置CPU阈值报警可以及时知晓问题，作出调整。
