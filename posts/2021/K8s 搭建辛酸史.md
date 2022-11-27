---
created_at: 2021-12-18 16:03:49
updated_at: 2021-12-18 16:03:49
slug: kubernetes-build-process
---

我有一个树莓派3B，1G内存版本，以前用来当做linux主机，随便玩一玩，谢谢python，点个灯。但最近我想搭建一个Kubernetes集群，用来学习，不过集群诶，怎么能只有一台机器呢？于是在咸鱼上又购买了两台树莓派4B，一台4GB内存，一台2GB内存。为什么想用树莓派呢？一来因为还算OK的云服务器贵得离谱，对个人来说实在不划算，二来树莓派可玩性比较高。

然而搭建过程几经波折，浪费了大量的时间，想来，最主要的问题有两个：cgroup的开启失败和墙的问题。

<!-- more -->

## 系统选择

为尽量满足应用的兼容性，选择64位操作系统；又自己对Ubuntu系操作系统比较熟，于是选择Ubuntu 20.04LTS Server版。为此，到Ubuntu官网下载镜像，通过树莓派官方的Raspberry Pi Imager制作TF卡系统盘。需要严格按照[官方教程](https://ubuntu.com/tutorials/how-to-install-ubuntu-on-your-raspberry-pi#4-boot-ubuntu-server)来，需要注意几个问题

- 如果直接网线连接路由器，则网络配置不需要
- 如果需要开机自动连接wifi，则需要修改系统盘根目录下network-config文件，在插入树莓派之前用读卡器修改
- 默认账号ubuntu，默认密码ubuntu
- 开机第一次登录会强制要求修改密码，到时候注意修改
- MacBook Pro m1版能够完美运行Raspberry Pi Imager

## 搭建过程

目前市场上有常规k8s、ubuntu的microk8s、rancher的k3s可供选择，最令人动心的还是microk8s，其功能齐全，还相对轻量，非常适合学习，而k3s则阉割替换了很多东西。

### 搭建microk8s

参考[官方手册](https://ubuntu.com/tutorials/how-to-kubernetes-cluster-on-raspberry-pi?&_ga=2.152469631.732019699.1639280743-1880426195.1638801725#1-overview)，关键点有以下几步：

1. 开启cgroup，在`/boot/firmware/cmdline.txt`文件添加`cgroup_enable=memory cgroup_memory=1`然后重启
2. 直接snap安装：`sudo snap install microk8s --classic`

那么问题来了，我的三台机器，按照这种方式，死活无法开启cgroup，microk8s自然也无法正常工作，网上的资料，都指向一个问题

- 根据系统的版本，开启cgroup配置的方式可能不在`/boot/firmware/cmdline.txt`中。但我确认ubuntu 20.04就是在这个文件

有的人确实是这个问题，有的人却不是，那些不是的，最终也没有得到明确的解决方案。

于是，我被卡住了，暂时弃坑。

### 再次尝试搭建microk8s

时间来到周末，我有时间来接着搞这个问题，然后尝试了新的方式：**在还没启动系统时直接在TF卡上修改cmdline.txt文件，加上cgroup启动参数**，这次看起来成功了，但由于我重装了系统，需要重新snap安装microk8s，可由于墙的问题，安装过程异常缓慢，尝试了一两个小时，依旧没有安装成功。这加上下面几个原因，动摇了我使用microk8s的信心

- 前一次即使安装成功，其命令响应时间还是非常慢
- microk8s都这样，那原版kubernetes还得了？
- 看来留给我选择的空间不多了——k3s

再次弃坑。

### kubeadm+云服务器

恰逢双十二，腾讯云有一台轻量应用服务器2C4G版只需要74元一年。经过上面两次在树莓派上搭建集群的失败，我开始怀疑自己，搭建kubernetes的目的是为了研究它，而不是为了玩，应该以最短的时间完成它。那么就用kubeadm在这台新购的服务器上搭建它吧——它绝对不会有cgroup的问题。

对此，也有[官方手册](https://kubernetes.io/zh/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)，步骤看起来不复杂，我做了这么些事

#### 安装kubadm

- 允许iptables桥接流量

- 在云服务器安全组打开所有端口

- 安装运行时，我选择了docker，直接`sudo apt install docker.io`，很方便

- 安装kubeadm、kubectl、kubelet。这里需要添加kubernetes的源，然后它被墙了。。。。。。

  于是参考[这篇文章](https://zhuanlan.zhihu.com/p/46341911)使用中科大的源

  ```shell
  # 添加中科大的源
  cat <<EOF > /etc/apt/sources.list.d/kubernetes.list
  deb http://mirrors.ustc.edu.cn/kubernetes/apt kubernetes-xenial main
  EOF
  
  # 执行这一步会报错，提示GPGkey的问题
  sudo apt update
  
  # 这了解决那个错误，将下面的<publickey>更换为实际报错的key
  gpg --keyserver keyserver.ubuntu.com --recv-keys <publickey>
  gpg --export --armor <publickey> | sudo apt-key add -
  
  # 再次执行
  sudo apt-get update
  # 安装
  sudo apt-get install -y kubelet kubeadm kubectl
  # 锁定版本
  sudo apt-mark hold kubelet kubeadm kubectl
  ```

- 配置cgroup驱动程序

  这一步我是按照一个视频配置的，但其实应该按照[官网配置](https://kubernetes.io/zh/docs/tasks/administer-cluster/kubeadm/configure-cgroup-driver/)

- 关闭swap：`sudo swapoff -a`

#### kubeadm init

然后执行主节点的初始化工作，这里会遇到问题：kubernetes的所有组件以镜像的形式提供，是从google的容器服务gcr拉取的，然而它又被墙了。。。需要更换国内源，我们使用别人放在阿里云仓库的镜像，按照如下方式做

```shell
# 先拉取
kubeadm config image pull --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers
# 再启动
kubeadm init --image-repository=registry.cn-hangzhou.aliyuncs.com/google_containers
```

启动成功后会有如下提示，关键信息有三点

1. 创建~/.kube/config文件，方便kubectl访问
2. 需要马上安装网络插件
3. 如果需要加入工作节点，使用这里指定的端点和token

```shell
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 10.0.20.5:6443 --token qi250a.gmbet3podjq1bcwg \
        --discovery-token-ca-cert-hash sha256:68147e1e117e54dbeb8fce34be6c83c7d7fb918c1ad2923b404c4d03f439a178
```

对于网络插件，去它提示的那个网站，进入想要的插件主页，会有提示信息

![image-20211218165103556](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211218165103556.png)

执行`kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`，安装flannel插件。

再等十来分钟，主节点应该就能用了，`kubectl get ndoes`能够查看效果。

```shell
ubuntu@VM-20-5-ubuntu:~$ sudo kubectl get nodes
NAME             STATUS   ROLES                  AGE     VERSION
vm-20-5-ubuntu   Ready    control-plane,master   4h23m   v1.23.1
```

#### kubeadm join

我有发现，华为云也有41块钱的1C2G机器可以买，加上我原来UCloud的1C2G的机器，是不是可以构建一个拥有三个不同云服务厂商节点的异构集群🤔。

要这么做，首先要解决的一个问题是，如何通过外网访问上面搭建的主节点？经验告诉我，找到config配置文件，将集群地址改为该云服务器的公网地址然后放在本地的`~/.kube/config`就行了，我确实这么做了，但使用kubectl连接时还是报了个错：提示服务器证书不允许外网访问来源。对此的解决办法参考[这篇文章](https://blog.csdn.net/yy_diego/article/details/109362884)，思路是重新生成API Server的证书。算是解决了外网访问的问题。

理所当然地，我在kubeadm join的命令中也把内网地址替换为公网地址。但最终还是报错了：提示kubeadmin-config这个configmap找不到，而它居然使用了内网地址去访问🤔。这就有点麻烦了，网上搜索了一下，**外网集群搭建起来会涉及到很多网络问题，属实没必要去研究**。性价比太低。

不行，已经在这个上面耗费太多时间了，就用这个主节点吧。也算有一些成果

### 搭建k3s

树莓派的事情，还是有点不甘心的，明明困扰了好长一段时间的cgroup解决了，却不能安装集群。。。划不来呀。好歹，我得尝试一下k3s呀。

于是，我参考了[官方文档](https://docs.rancher.cn/docs/k3s/installation/install-options/_index)和[这篇文章](https://www.yuweizhan.cn/articles/2020/07/18/1595040455803.html)。这里的关键是使用官方提供的国内加速地址，用国外地址很可能会安装失败。

主节点

```shell
# 什么都不设置，直接安装，默认是作为主节点的
curl -sfL http://rancher-mirror.cnrancher.com/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```

工作节点

```shell
# 在主节点上执行:获取主节点的token
cat /var/lib/rancher/k3s/server/node-token

# 在从节点上执行
export K3S_TOKEN=<上面得到的token>
export K3S_URL=https://<master_ip>:6443
curl -sfL http://rancher-mirror.cnrancher.com/k3s/k3s-install.sh | INSTALL_K3S_MIRROR=cn sh -
```

在创建工作节点时，遇到过从节点起不来的问题，提示passwd不匹配，参照[这篇文章](https://cloud.tencent.com/developer/article/1594895)解决了。

然后，就搭建完成了，此时在主节点上可以看到这两个节点

```shell
root@ubuntu:/home/ubuntu# kubectl get nodes
NAME             STATUS   ROLES                  AGE    VERSION
ubuntu           Ready    control-plane,master   3h8m   v1.21.7+k3s1
raspberry-4c2g   Ready    <none>                 70m    v1.21.7+k3s1
```

## 总结

这三种kubernetes的搭建方式，其实都不复杂，被卡住的原因都是墙，属实蛋疼。这其中，K3s提供的支持最为友好，不但有中文资料，还有官方国内加速地址，完全不会有其它两种方式的问题。microk8s如果在网络环境允许的情况下，应该也挺简单的，它类似kubeadm，也是通过init、join这样简单的命令去构建集群，可惜的是不明原因导致在我的环境中用起来卡卡的。kubeadm相对而言是最复杂的，kubectl等软件包的软件源需要更换，镜像源也要更换。

不过一番折腾下来，我好歹是拥有两个kubernetes集群，一个拥有两个节点的树莓派集群和一个拥有一个节点的在腾讯云上的集群，学习用是够了。但为什么这篇文章是（上）呢？因为其它两台外网服务器，我还想要折腾一下，不过不是最近，而是等我kubernetes足够熟练之后。

总结一下我们遇到的问题

- 树莓派cgroup开启失败：在启动系统之前修改cmdline.txt
- kubernetes的apt源无法访问：更换中科大或阿里云的源
- gcr镜像仓库无法访问：更换阿里云的镜像仓库
- k3s安装脚本执行缓慢：使用官方提供的国内专用安装脚本
- k3s从节点启动失败：手动将主节点的/etc/rancher/passwd复制到从节点

总结一下这次的教训：折腾两三天整这么个玩意儿是很划不来的，最完美的方式，是在一个云服务厂家购买两三台中配的机器，以此搭建，这样既不会遇到cgroup问题，也不会遇到公网访问问题，还是标准的kubernetes环境。而且我们可以只买一两个月，不用了再释放掉，不会花多少钱。长远看是成本最低的一种方式。毕竟，三台树莓派的价格，也上千元了，如果再加上交换机和配件，则更贵。搭建出来的集群，还不是官方原版🤔。
