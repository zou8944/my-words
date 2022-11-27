---
title: gitops实践总结
created_at: 2022-04-21 14:55:15
updated_at: 2022-04-21 14:55:15
slug: gitops-in-action-summary
---

> Infrastructure as Code，将基础设施以代码的形式管理起来，放在git仓库中。Kubernetes的清单文件就是一种
> gitops = Infrastructure as Code + version control + Pull/Push Request + CI/CD流水线。即，将维护在git仓库中的基础设施代码，以git仓库的方式进行开发、权限管理，再在CI中做正确性检查，然后CD交付到具体基础设施。
> 此处，需要维护的基础设施，即Kubernetes。

<!--more-->

# 问题

当前应用发布方式。

1. 应用创建：在仓库中创建应用，生成清单文件，kubectl apply到目标集群
2. CI：镜像打包上传远端仓库后，通过kubectl edit Deployment set 命令修改目标镜像

这样做的缺点

1. kubectl属于主动push，多个集群就要维护多套配置
2. 当前的清单文件仓库鸡肋，只能够初始化应用，无法跟踪应用状态
3. Runner依赖：依赖于有kubectl和配置的Runner
4. Kubernetes访问配置文件外泄，安全性不高

这个问题的解决方式——gitops

# 选型

目前三种技术比较流行：argo cd、jenkins x、flux cd，考虑到我们使用gitlab作为版本控制管理工具，还有gitlab kubernetes agent可供考虑。至于怎么选，只是一个CD工具而已，功能大差不差。看起来肯定是gitlab最好，最流行的是argo cd，如果我用jenkins作为流水线，可能会考虑jenkins x。而gitlab kubernetes agent仅是高级版本支持，我们使用了社区版自建，因此无缘。于是顺理成章用到了argo cd。

# 实践

argo cd的手册算是写得很详细，按照手册做，就没问题了。这里只列出值得注意的问题

## 注意事项

### 工作原理

argo cd基于拉模式，是安装在K8S集群内部的，而当实现一个argocd实例管理多个集群时，被管理的外部集群则不需要安装任何argocd组件，因为它是基于RBAC进行访问。

其工作组件主要如下

```shell
zouguodong@zouguodongdeMacBook-Pro ~ % kubeoverseas get deployment -n argocd
NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
argocd-applicationset-controller   1/1     1            1           4d17h
argocd-redis                       1/1     1            1           4d17h
argocd-notifications-controller    1/1     1            1           4d17h
argocd-dex-server                  1/1     1            1           4d17h
argocd-repo-server                 1/1     1            1           4d17h
argocd-server                      1/1     1            1           4d17h
```

- argocd-server：中枢
- argocd-repo-server ：git仓库的本地缓存
- argocd-applicationset-controller：一个k8s控制器，用于比较原版本和目标版本
- argocd-dex-server：一个SSO服务
- argocd-redis ：一次性缓存
- argocd-notifications-controller：给用户发送通知

### argocd服务外部访问方式

端口转发、ingress、slb service。端口转发在我电脑上会出现自动断开的情况，不明原因。ingress倒是可以用，但在没有配置证书时，会出现无线重定向的问题。两个解决方案

- 给ingress配置正确的证书
- 关闭argocd-server的安全选项，在启动参数添加 --insecure

### 引用私有git仓库

如果manifest文件来自自建git仓库，需要配置两个东西

- 私钥
- unknown host

具体参考[这里](https://argo-cd.readthedocs.io/en/stable/user-guide/private-repositories/#managing-ssh-known-hosts-using-the-cli)

### 同步逻辑

默认三分钟从清单仓库同步一次，但还支持UI和命令行的手动同步，以及WebHook同步（可用于CI）

### 命名问题

argocd的应用名全局唯一。下面解释原因

- argocd只对存在于argocd命名空间下的资源进行解析和管理，应用名就是资源名
- 根据k8s的命名规则，同一命名空间下的资源名不能相同

这会造成一个问题：如果想用一个argocd实例管理对应两个环境的两个集群，它们是平行的世界，按理来说对应的argocd应用名也应该一致，然而现实却无法做到。因此你只能为它们添加前缀进行区分。

### 忘记密码

如果忘记管理员密码

```shell
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

## 最佳实践

### 使用app-of-apps

这是官方推荐的应用安装方式。这儿有一篇[相关文章](https://medium.com/dzerolabs/turbocharge-argocd-with-app-of-apps-pattern-and-kustomized-helm-ea4993190e7c)

> 说白了，[App of Apps Pattern](https://argoproj.github.io/argo-cd/operator-manual/cluster-bootstrapping/#app-of-apps-pattern)让我们定义了一个根 ArgoCD Application（Root App）。根应用程序不是指向应用程序清单，而是指向一个文件夹，该文件夹包含Application应用程序包（子应用程序）指向的每个微服务的 YAML 定义。然后，每个微服务的ApplicationYAML 指向一个包含应用程序清单的目录。

实际体验下来，这种方式最大的方便，就是只需要手动创建父应用，子应用就能够声明式创建。

### secrets的存放方式

k8s的secret资源，肯定是不能明文存放在版本库的。推荐使用[sealed-secrets](https://github.com/bitnami-labs/sealed-secrets)。它通过CRD+Server+Client的方式工作，Server负责秘钥分发、CRD转Secret资源；Client负责本地加密并创建CRD。加密时需要从Server处获取秘钥。

### CI脚本

对gitlab ci，可以使用扩展+模板的方式达成。如下主要关注脚本修改版本库文件和kustomize edit命令的使用。需要了解git over http。且它要在docker类型的gitlab runner运行，否则会污染本地git配置

```yaml
variables:
  # 用户密码在环境变量中给出
  GITOPS_USERNAME: xxx
  GITOPS_PASSWORD: xxx
  # 应用名、环境、镜像需要用户给出
  GITOPS_APP_NAME: demo
  GITOPS_ENVIRONMENT: prod
  IMAGE: xxx

.deploy-k8s:
  stage: deploy
  image: cnych/kustomize:v1.0
  tags:
    - docker
  before_script:
    - git clone https://${GITOPS_USERNAME}:${GITOPS_PASSWORD}@git.mampod.work/g1/platform/kubernetes-manifest.git
    - git config --global user.name "gitops"
    - git config --global user.email "gitops@mampod.com"
  script:
    - git checkout -B master
    - cd kubernetes-manifest/kustomize/${GITOPS_APP_NAME}/overlays/${GITOPS_ENVIRONMENT}
    - kustomize edit set image ${GITOPS_APP_NAME}=${IMAGE}:${CI_COMMIT_SHORT_SHA}
    - cat kustomization.yaml
    - git commit -am "[skip ci] update image of app ${GITOPS_APP_NAME} - ${GITOPS_ENVIRONMENT} to $IMAGE:$CI_COMMIT_SHORT_SHA"
    - git push origin master

```

### kustomize最佳实践

- base不要有多级，一来违反kustomize默认规则，二来层数过多应用间耦合加深，也不好管理
- base仅定义最通用的，差异配置放overlays，方便调试，典型的差异配置如下
  - ingress域名、证书等
  - deployment的亲和性、健康检查等待时间、资源分配大小等

![image-20220421164003128](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421164003128.png)

### 多集群管理

考虑到命名问题，个人认为argocd比较适合多集群分别对应不同应用的场景，而不是多集群对应不同环境；如果不介意命名，则所有场景都可以用。

多集群管理时要结合project工作，能够起到资源隔离的效果。每个project，有单独的可用仓库、目标集群、角色。

### 关于datree

datree是用于检查清单文件正确性的技术，可以直接检查kustomize。但在调试时因为遇到网络问题，检查过慢，且经常检查失败，无疾而终。

不过从其作用来看，如果复杂度上去，是可以考虑引入的。

## 更大的潜力

翻看argocd手册，列举了支持的功能。看起来，它能做SSO集成、能做权限管理、能查看应用启停状态、能方便地查看日志。**那是不是对普通开发人员，可以用它对k8s做屏蔽**🤔。

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220421170307442.png" alt="image-20220421170307442" style="zoom:80%;" />



# 知识地图

按照下面的路线学习了解，能够对使用argo cd搭建gitops有比较形象的认识。

## gitops

- [官网](https://www.gitops.tech/) 
- [Nana的视频介绍](https://www.youtube.com/watch?v=f5EpcWp0THw) 

## argo cd

- [官方手册（建议通篇浏览）](https://argo-cd.readthedocs.io/en/stable/) 
- [Nana的视频介绍](https://www.youtube.com/watch?v=MeU5_k9ssrs)

## gitlab kubernetes agent

资料较少，如果只看官方手册会让人发晕，加上下面列举的两篇文章会好得多。

重点是明白它的架构和工作原理，否则根本不知道在配置什么

- [官方手册](https://docs.gitlab.com/ee/user/clusters/agent/gitops.html)
- [写的不错的文章1](https://xie.infoq.cn/article/45bfd162146b3b5bf47ae0faf)
- [写的不错的文章2](https://xie.infoq.cn/article/45bfd162146b3b5bf47ae0faf)
