---
created_at: 2022-04-21 17:16:44
updated_at: 2022-04-21 17:16:44
slug: k3s-and-rancher-experience
---

> 记一记k3s+rancher搭建遇到的问题，使用感受。

<!--more-->

# 事情经过

因为一个临时的发布需求，购买了一台临时的海外ECS。虽然都在阿里云上，但由于不同地域，因此并不能将其加到现有ACK管理，于是我有以下几种选择

- 方案一：ECS裸用，使用进程管理工具如superctl对应用发布进行管理；或者直接用docker管理
- 方案二：新建同地域ACK，将ECS作为工作节点加入
- 方案三：也别用ECS了，直接建一个该地域的ASK吧

- 方案四：自建K8s，但要足够轻量

方案一不好管控，不停机方案比较难搞；方案二、方案三的附加费用可能比这台ECS还高；方案四，有k3s这种易于安装，占用资源低的k8s版本，值得一试。

ACK有Web UI，新建的k3s也得有一个UI管理界面吧，不然命令行管理可不大人道。于是又有几个选择

- lens
- rancher
- kubesphere

lens的优点在于简洁，但它是本地客户端，无法给别人使用，且资源编辑时只能编辑yaml文件，不够友好；rancher和阿里云提供的Web UI类似，将k8s资源一一映射为具体的UI组件；kubesphere更加抽象，对无k8s基础的人来过更加友好。

rancher和k3s是一家，选用rancher。至此，我们有了k3s+rancher这对组合

# 手册

使用前先读手册，可以避免绝大多数坑，不要想一下子成功，那样只会花费更多时间，还会怀疑自己的智商，或者抱怨设计不易用。易用不易用，你已经用了。

- [K3S](https://docs.rancher.cn/docs/k3s/_index/) ，重点关注几个点
  - [安装方式](https://docs.rancher.cn/docs/k3s/quick-start/_index) ，注意有国内安装方式
  - 安装好后的[集群访问方式](https://docs.rancher.cn/docs/k3s/cluster-access/_index)
  - [卷和存储](https://docs.rancher.cn/docs/k3s/storage/_index) ：了解如何使用本地磁盘作为存储卷（而不是云盘）
  - [网络](https://docs.rancher.cn/docs/k3s/networking/_index)：了解如何使用本地端口暴露一个Service（而不是负载均衡）
- [Rancher](https://docs.rancher.cn/rancher2.5/) ，关注以下
  - [Rancher是什么](https://docs.rancher.cn/docs/rancher2.5/overview/architecture/_index)：Rancher是一个容器编排管理平台——管理管理容器的平台。核心优势是能够托管多个平台的K8s
  - [裸机安装，直接docker run](https://docs.rancher.cn/docs/rancher2.5/installation/other-installation-methods/single-node-docker/_index/)
  - [安装在k8s集群内](https://docs.rancher.cn/docs/rancher2.5/installation/install-rancher-on-k8s/_index/)

# 安装

## 安装K3s

一键安装，但要注意的是加上安装节点所在的IP地址，否则在导出kubeconfig使用时会报证书不可用

```shell
curl -sLS https://get.k3s.io | INSTALL_K3S_EXEC='server --tls-san 198.11.180.138' sh -
```

## 安装Rancher

同样是一键安装，没有特殊注意事项。

如果是安装在集群，需要用ingress将rancher-server暴露出来。

不过我的安装过程是，安装在k3s -> 卸载后安装rancher agent -> rancher server安装在单独的机器，因此遇到过一些问题，下一节记录

## 问题记录

**问题：从集群中删除rancher server时，几个命名空间无法删除**

参考[这篇文章](https://www.xtplayer.cn/kubernetes/forces-delete-terminated-namespace/#rancher-自定义-k8s-集群或者导入-rancher-管理的-k8s-集群)解决。因为卡在依赖资源的删除上。



**问题：删除rancher-server，重新安装rancher-agent时，报错，报错内容如下**

```shell
Error from server (InternalError): error when creating "STDIN": Internal error occurred: failed calling webhook "rancher.cattle.io": failed to call webhook: Post "https://rancher-webhook.cattle-system.svc:443/v1/webhook/mutation?timeout=10s": service "rancher-webhook" not found
```

参考[这篇文章](https://forums.rancher.com/t/rancher-webhook-fails-due-to-not-existing-rancher-webhook-tls-secret/36211/2)解决，主要是重新安装时有一个资源不会被重建，这里删除然后重新执行安装命令。

```shell
kubectl delete -n cattle-system MutatingWebhookConfiguration rancher.cattle.io
```

这一问题在官方手册得以佐证：https://docs.rancher.cn/docs/rancher2.5/releases/v2.5.12/

![image-20220421185559558](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421185559558.png)



**问题：安装rancher-agent启动时提示ca token找不到**

再次执行rancher删除命令，完成后重新安装



**问题：安装rancher-agent启动时提示`the server could not find the requested resource`**

是rancher 2.5.12不支持k8s 1.21及以上：https://forums.rancher.com/t/install-fail-the-server-could-not-find-the-requested-resource/20974/2

![image-20220421185707248](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421185707248.png)

解决方法是切换到rancher 2.6

**问题：rancher 2.6没有切换中文的按钮**

自己添加cookie

![image-20220421185748342](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421185748342.png)

# 使用体验

## K3s

如果我们把k3s当做单机的增强，那它简直是完美，应用管理用的k8s的方式，端口、ip地址等却还是依照单机的方式，还要啥自行车。目前为止，使用下来唯一的不便是traefik ingress controller替换nginx ingress controller带来的，需要使用Middleware进行路径前缀截断。

## Racher

类似各大云厂商的Web UI，Rancher的UI与K8s资源基本上是一一对应的，差别就在于呈现方式了。算是风格问题，这方面，我认为优缺点如下

- 优点：多命名空间可同页展示

  

- 优点：控制台和日志同页显示，查看方便

  ![image-20220421191229102](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421191229102.png)

- 缺点：页面跳转太多，一些短小配置的编写如ingress都要跳转新的页面，使用者容易失焦，不如阿里云

- 缺点：页面没有按照资源的从属关系引导，如从deployment进入pod，没有按钮回到deployment页

  <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421191549227.png" alt="image-20220421191549227" style="zoom:80%;" />

- 缺点：应用页面显示内容太少，仅显示了应用引用的资源，未显示引用应用的资源如service、ingress（有，但是不显示），不如阿里云

**总的来说，就是操作链不完整，中途会断**

# 所有集群都用Rancher统一管理好不好

首先，我觉得rancher并不好用。用不用都看情况。

如果用Rancher统一管理，我能想到的理由是

- 跨云平台统一管理K8s，减少登录多个云账号的麻烦

如果不用Rancher管理，我能想到的理由是

- UI交互不够友好
- 各云厂商有针对自己的K8s实现在Web UI上做优化，使用Rancher可能抹平这个优点
