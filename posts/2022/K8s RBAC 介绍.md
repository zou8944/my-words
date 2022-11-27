---
created_at: 2022-01-01 00:00:00
updated_at: 2022-02-02 00:00:00
slug: kubernetes-rbac-introduction
tags:
- Kubernetes
- RBAC
---

前面介绍过Kubernetes的结构组成，其中API Server用于与外界的交互，我们常用的命令行工具kubectl、UI工具lens、云服务商提供的WebUI，最终都是通过Restfule API的形式，走HTTP协议，到达API Server。此时就带来权限控制问题。

<!-- more -->

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211203153658776.png" alt="image-20211203153658776" style="zoom:80%;" />

如上图，对来自外部的请求，Api Server会经过三个组件

- Authentication：认证，验证用户的合法性，并从中提取出用户信息，如用户名、组等
- Authorization：鉴权，鉴定该用户是否有权限访问指定资源
- Admission：准入，它可以修改或拒绝请求

## 认证

与用户相关的概念，有用户、组、ServiceAccount，但只有ServiceAccount才在Kubernetes中以资源的形式存在，用户、组并不会以资源的形式存在，它们只是一个字符串，在使用的地方如RoleBinding时被引用，理解这一点很重要。

从集群内部，即pod中访问API Server时，需要ServiceAccount来标识身份；从集群外部访问API Server时，则需要走外部验证，包括：客户端证书、密码、普通令牌、引导令牌。

### ServiceAccount

每个命名空间都会有一个默认的ServiceAccount。一个典型的ServiceAccount如下

```shell
gd % kubectl --kubeconfig ~/.kube/config-test get sa -o yaml
apiVersion: v1
items:
- apiVersion: v1
  imagePullSecrets:
  - name: acr-credential-560b66540f01e51c18524b09ad7f575f
  - name: acr-credential-6731ef77d88edc24b279ebf20860f30f
  - name: acr-credential-5dee66918cdf5d93de4aa5cd90247f73
  - name: acr-credential-be55512166dd26eda658d0706de5a06a
  - name: acr-credential-bab42ef118a2913b05cd8cdb95441d70
  kind: ServiceAccount
  metadata:
    creationTimestamp: "2020-11-10T06:48:55Z"
    name: default
    namespace: default
    resourceVersion: "100598603"
    selfLink: /api/v1/namespaces/default/serviceaccounts/default
    uid: 4ef6a2d3-19ad-47cf-a2de-135f2c9d86b5
  secrets:
  - name: default-token-vrqk9
kind: List
metadata:
  resourceVersion: ""
  selfLink: ""
```

可以看到它其实包含两部分：secrets、imagePullSecrets，其中，前者会被挂载到pod的容器内，用于在访问API Server时提供信息；后者则用于pod从私有仓库拉取镜像时使用的秘钥。也就是说，ServiceAccount的作用也就是这两部分了。本文重点关注secrets部分。

当一个pod创建时，它会默认拥有该ServiceAccount，这一点可以通过查看一个已经存在的pod得以验证

```shell
gd % kubectl --kubeconfig ~/.kube/config-test get pod app-bosslist-backend-67c59b8d94-k75kj -o yaml | grep service
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
  serviceAccount: default
  serviceAccountName: default
```

而该token包含两部分信息：服务端证书、token值的BASE64编码。

```shell
g % kubectl --kubeconfig ~/.kube/config-test get secret default-token-vrqk9 -o yaml
apiVersion: v1
data:
  ca.crt: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURHakNDQWdLZ0F3SUJBZ0lCQURBTkJna3Foa2lHOXcwQkFRc0ZBREErTVNjd0ZBWURWUVFLRXcxaGJHbGkKWVdKaElHTnNiM1ZrTUE4R0ExVUVDaE1JYUdGdVozcG9iM1V4RXpBUkJnTlZCxxxxx
  namespace: ZGVmYXVsdA==
  token: ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklteEthMkpUUm1GbFVFZFlWRmhsUTBKcE1VTjJkbmd6TVZCRWVtSjNkSFZHUVVWU1RFWXhjak5DTlhjaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFxxxxx
kind: Secret
metadata:
  annotations:
    kubernetes.io/service-account.name: default
    kubernetes.io/service-account.uid: 4ef6a2d3-19ad-47cf-a2de-135f2c9d86b5
  creationTimestamp: "2020-11-10T06:48:55Z"
  name: default-token-vrqk9
  namespace: default
  resourceVersion: "38744013"
  selfLink: /api/v1/namespaces/default/secrets/default-token-vrqk9
  uid: 64ee0b11-9919-47b1-97e9-e055f47f3732
type: kubernetes.io/service-account-token
```

token值是JWT，解码结果如下

```shell
{
  "iss": "kubernetes/serviceaccount",
  "kubernetes.io/serviceaccount/namespace": "default",
  "kubernetes.io/serviceaccount/secret.name": "default-token-vrqk9",
  "kubernetes.io/serviceaccount/service-account.name": "default",
  "kubernetes.io/serviceaccount/service-account.uid": "4ef6a2d3-19ad-47cf-a2de-135f2c9d86b5",
  "sub": "system:serviceaccount:default:default"
}
```

### 普通用户、组

API Server都是通过客户端自声明的方式得到用户名、组等信息，自己并不会存储。而客户端提供自己身份的方式有几种：客户端证书、密码、普通令牌、引导令牌。具体官方手册有说明：https://kubernetes.io/zh/docs/reference/access-authn-authz/authentication/。我们重点关注客户端证书的方式。

很重要的点是API Server将证书中的CN当做用户名，O当做组名。于是，我们要做的，就是创建自己的key、csr，在让API服务端签发证书，就能使用key+crt的方式以预期的身份合法访问API Server了。

具体步骤可参见下文“最佳实践 - 创建一个只能操作Deployment的用户”前两步。

## 鉴权 - RBAC

认证确认了用户的合法身份，鉴权则是根据用户的身份和访问的资源确定是否具有访问的权限。[官方手册在这](https://kubernetes.io/zh/docs/reference/access-authn-authz/authorization/)。从以前到现在，Kubernetes支持如下几种方式:

- Node：节点鉴权，专门对 kubelet 发出的 API 请求进行鉴权
- ABAC：基于属性的鉴权
- RBAC：基于角色的鉴权
- Webhook：即回调自定义的HTTP接口，决定是否可访问

我们关注RBAC鉴权模式。

### Role和RoleBinding

Role是角色，是一堆资源操作的权限集合；RoleBinding将Role和用户绑定起来，绑定的对象可以是用户、组、ServiceAccount。看两个例子就一目了然。

首先是Role的定义，如下表示角色cirole允许对default命名空间下的deployment资源进行get、list、update、patch

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: cirole
  namespace: default
rules:
  - verbs:
      - get
      - list
      - update
      - patch
    apiGroups:
      - apps
    resources:
      - deployments
```

其次是RoleBinding，如下表示将角色cirole和用户ciuser进行绑定

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: cirolebinding
  namespace: default
subjects:
  - kind: User
    apiGroup: rbac.authorization.k8s.io
    name: ciuser
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: cirole

```

上述两个声明应用后，就能实现ciuser对default命名空间下的deployment的操作，可以通过kubectl auth can-i命令检测权限

```shell
# 检查ciuser是否能够获取deployment
gd % kubectl --kubeconfig ~/.kube/config-test auth can-i get deployments --as ciuser
yes
# 检查ciuser是否能够获取secrets
gd % kubectl --kubeconfig ~/.kube/config-test auth can-i get secrets --as ciuser
no
```

### ClusterRole和ClusterRoleBinding

Role和RoleBinding是有命名空间限制的，只能限制命名空间内的资源，有下面两个场景其无法满足

- 一个用户需要访问多个命名空间下的资源时，按照Role的做法，需要在每个命名空间下定义Role，然后定义多个RoleBinding将用户与角色绑定，太多复杂
- 一些并不存在的资源的访问控制，仅仅是一个URL路径，比如/healthz
- 一些不属于任何命名空间的资源的访问控制，比如Node、PV等

此时就需要ClusterRole，话不多说，直接看他们的定义即可

```yaml
# 这里节选了drain-node的角色定义，可发现其最大的不同就是少了namespace
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: drain-node
rules:
  - verbs:
      - get
      - list
    apiGroups:
      - extensions
      - apps
    resources:
      - daemonsets
```

```yaml
# 节选了system:node的角色绑定
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: system:node
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:node
```

### 默认角色

Kubernetes提供了大量默认角色和角色绑定，都是Cluster级别，我们看几个

- admin：管理员角色
- view：对除了Secrets之外的资源的访问，在授权只读用户时尤其有效
- edit：对除了角色和角色绑定之外的资源的访问和编辑，不能操作角色和角色绑定是防止授权扩张

这里强烈案例一个Kubernetes可视化管理软件——[lens](https://k8slens.dev/)，用它，去查看默认角色们吧

![image-20211203164001619](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211203164001619.png)

## kubeconfig文件

使用kubectl访问API Server时，实际上是需要客户端凭证的，对于Linux系操作系统，它的位置在：~/.kube/config，关于kubeconfig，大致介绍，详细看[官方手册](https://kubernetes.io/zh/docs/concepts/configuration/organize-cluster-access-kubeconfig/)。

一个config文件由四部分组成

- 集群地址和集群CA证书，该证书用作HTTPS加密传输时用，可以有多个
- 用户凭证，使用证书认证时存的是用户证书和加密key，可以有多个
- 上下文，集群地址和用户凭证的绑定，可以有多个
- 当前上下文，决定当前处于激活状态下的上下文。即当前以哪个用户连接哪个集群地址

多个config文件可合并

- 如果设置了KUBECONFIG环境变量，指明了多个config文件，则这些文件会以一定的规则合并，这个可以在本地管理时方便使用。

## 阿里云RAM与RBAC

阿里云的RAM，对容器服务只有管理和读取两个权限，对资源的具体权限管理需要使用RBAC，在阿里云容器服务控制台有简单的RBAC配置 —— 授权管理。

如下，它的最细粒度，能够管理某个子账号对指定集群的指定命名空间的指定角色的绑定管理。其实就是对角色绑定的封装。

![image-20211203165229100](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211203165229100.png)

你可能会想，子账号对应的集群内用户是什么呢？我们可以从控制台给出的连接信息看出端倪

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211203165546184.png" alt="image-20211203165546184" style="zoom:80%;" />

对一个管理员账号的证书进行解析，可以发现它的用户名(CN)就是阿里云子账号的ID，用户组为system:users

![image-20211203165743823](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211203165743823.png)

而如果我们对某个用户指定了自定义权限，则会创建多条RoleBinding，命名规则为 `<userid>-<namespace>-<role>-rolebinding`，比如

![image-20211203170002236](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211203170002236.png)

## 准入

这就是一堆前置处理器，称之为准入处理器，忽略，有需要去看[手册](https://kubernetes.io/zh/docs/reference/access-authn-authz/admission-controllers/)

## 最佳实践

### 一些快速的命令

```shell
# 快速创建一个pod
kubectl run podname --image=luksa/kubectl-proxy -n default
# 编辑一个资源的yaml文件
kubectl edit pod xxx
# 快速创建role
kubectl create role service-reader --verb=get --verb=list --resource=services -n bar
# 快速创建rolebinding
kubectl create rolebinding test --role=service-reader --serviceaccount=foo:default -n foo
## 快速创建clusterrole
kubectl create clusterrole pv-reader --verb=get,list --resource=persistentvolumes
# 快速创建clusterrolebinding
kubectl create clusterrolebinding pv-test --clusterrole=pv-reader --serviceaccount=foo:default
# 快速检测权限：我能在default命名空间创建deployment吗？
kubectl auth can-i create deployment -n default
# 快速检测权限：我能在default命名空间以用户test来创建deployment吗？
kubectl auth can-i create deployment -n default --as test
```

### 创建一个只能操作Deployment的用户

以证书的方式，先在本地创建用户，再在k8s服务器签发，然后创建角色和角色绑定，最后将用户注册到本地config文件，就能访问了

1. 创建用户

   ```shell
   # 生成秘钥
   openssl genrsa -out ciuser.key 2048
   # 生成csr，注意CN代表用户名；O代表组名
   openssl req -new -key ciuser.key -out ciuser.csr -subj "/CN=ciuser/O=ci"
   # 将csr做base64编码
   cat ciuser.csr | base64 | tr -d "\n"
   ```

2. k8s服务器签发证书

   创建csr请求，其中的request是第一步商城的csr做的base64编码

   csr.yaml

   ```yaml
   apiVersion: certificates.k8s.io/v1beta1
   kind: CertificateSigningRequest
   metadata:
     name: ciuser
   spec:
     groups:
     - system:authenticated
     request: xxxxxxxxxxxxxxxxxxxxxx
     signerName: kubernetes.io/kube-apiserver-client
     usages:
     - client auth
   ```

   ```shell
   kubectl --kubeconfig ~/.kube/config-test apply -f csr.yaml
   ```

3. 创建角色和角色绑定

   ```shell
   kubectl --kubeconfig ~/.kube/config-test create role cirole --verb=get --verb=list --verb=update --verb=patch --resource=deployments -n default
   kubectl --kubeconfig ~/.kube/config-test create rolebinding cirolebinding --role=cirole --user=ciuser -n default
   ```

4. 在config文件注册用户和上下文

   ```shell
   # 添加用户凭证； --embed-certs=true表示将证书写入config文件，而不是引用
   kubectl --kubeconfig ~/.kube/config-test config set-credentials ciuser --client-key=ciuser.key --client-certificate=ciuser.crt --embed-certs=true
   # 添加上下文
   kubectl --kubeconfig ~/.kube/config-test config set-context ciuser --cluster=kubernetes --user=ciuser
   # 切换上下文
   kubectl --kubeconfig ~/.kube/config-test config use-context ciuser
   # 接下来，就按照正常操作即可
   kubectl --kubeconfig ~/.kube/config-test get deployments
   ```

## 参考

1. [Kubernetes API访问控制](https://kubernetes.io/zh/docs/concepts/security/controlling-access/)
