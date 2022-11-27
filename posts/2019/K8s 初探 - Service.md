---
created_at: 2019-10-22 20:11:44.0
updated_at: 2021-02-16 23:25:10.499
slug: kubernetes-service-introduction
---

第一篇文章已经说过了Service存在的意义，主要是由于POD机制无法对外提供一个稳定的地址，因此需要服务进行固定地址的暴露和负载均衡。官方一点的话：k8s的服务是一种为一组功能相同的pod提供单一不变的接入点的资源。
<!-- more -->
## 基础

### 创建服务

#### 方法一

通过expose命令创建

```shell
kubectl expose rc kubia --type=LoadBalancer --name kubia-http
```

#### 方法二

使用yaml创建，如下针对所有具有标签app=kubia的node创建了一个服务，对外端口为80，对内端口为8080

```yaml
apiVersion: v1
kind: Service
metadata:
  name: kubia
spec:
  sessionAffinity: ClientIP # 会话亲和性：同一个客户端请求到的POD会是同一个。（可选）
                            # 支持none/ClientIP，不支持cookie，因为k8s并非基于http，而是TCP
  ports:
    # 端口可以暴露多个
    - name:  http  # 名字是可选的
      port: 80
      targetPort: 8080
    - name: https
      port: 443
      targetPort: 8443
    selector:
      app: kubia
```

会话亲和性：正常情况下，每次来自客户端的请求都会被服务随机转发到一个pod，但如果想要一个客户端的请求一直在单个pod中执行，就需要向上面那样配置会话亲和性。

### 服务发现

#### 方法一 环境变量

此方法前提是服务创建早于pod的创建。可通过在pod中执行env获取环境变量，会有响应服务的IP和端口

#### 方法二 DNS

通过k8s的系统pod——kube-dns实现，具体操作方式尚不知晓

####  方法三 FQDN

Full Qualified Domain Name(FQDN)，全限定域名。一个服务的全限定名长这样，访问它就可以

`backend database.default svc cluster. l ocal`

## 连接集群外的服务

即不要让服务将连接重定向到集群中的pod，而是重定向到外部的IP和端口。

### Endpoint

就是暴露一个服务的IP和端口列表的k8s资源

创建服务时指定的标签选择器，在访问服务时并不会直接将请求重定向到匹配到的pod，而是通过标签获取到的pod构建一个IP和端口列表（endpoints列表）。客户端请求时再从这些endpoint中选择一个，然后重定向过去

### 操作一波

既然endpoint和服务是分开的，那么我们可以创建一个没有endpoint的服务，然后手动配置endpoint即可。

创建服务时候不指定标签选择器即可创建没有endpoint的服务。

```yaml
# 创建一个没有Endpoints的服务
apiVersion: v1
kind: Service
metadata:
  name: external-service
spec:
  ports:
    - port: 80
```

```yaml
# 创建Endpoint
apiVersion: v1
kind: Endpoints
metadata:
  name: external-service  # name必须和service匹配
subsets:
  - address:
    - ip: 1.1.1.1  # 目标地址
    - ip: 2.2.2.2
    ports:
      - port: 80  # 目标端口
```

## 暴露服务给外部

### 通过NodePort暴露

将服务设置为NodePort类型，这样每个节点都为服务保留一个相同的端口，客户端直接访问任意节点的该端口和clusterIP都可以访问到该服务。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: kubia-service
spec:
  type: NodePort
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30111  # 每个节点保留该端口作为服务端口
  selector:
    app: kubia
```

上面设置后可以从外部访问，但还需要设置GCP的防火墙以允许外部访问

```shell
gcloud compute firewall-rules create kubia-svc-rule --allow=tcp:30111
```

现在的问题就是找到node的IP地址了，可以通过如下JSONPath进行查询

```shell
kubectl get nodes -o jsonpath='{.items[*].status.addresses[?(@.type=="ExternalIP")] .address}' 
```

### 通过负载均衡暴露

将服务设置为LoadBalancer类型，这样可以调用其所在环境的负载均衡服务。如果k8s的运行环境没有负载均衡服务，则会表现的和NodePort类型一样，因为LoadBalancer是NodePort的扩展类型。

```yaml
apiVersion: v1
kind: Service
metadata：
  name: kubia-service
spec:
  type: LoadBalancer
  ports:
    - port: 80   # 不指定端口时负载均衡器将会自动分配一个端口
      targetPort: 8080
  selector:
    app: kubia
```

其工作原理，还是基于NodePort，客户端访问负载均衡器，负载均衡器通过ClusterIP和节点IP访问服务，服务再定位到具体的POD。相对于NodePort，只是多了一层负载均衡器。

### 通过Ingress暴露

没给LoadBalancer服务都需要自己的负载均衡器及独立的公网IP地址。使用Ingress可以只用一个公网IP提供多个服务的暴露。并且由于Ingress在应用层，因此可以提供cookie亲和性功能。

![1571650418897](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kubernetes%20-%20Service/1571650418897.png)

Ingress控制器是此方式工作的前提条件。不同的k8s环境提供的控制器可能不同，有些环境还不提供Ingress控制器，例如GCP使用了负载均衡器来提供Ingress功能。

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: kubia
spec:
  rules:
    # host可以配置多个
    - host: kubia.example.com
      http: 
        paths:
          # path可以配置多个
          - path: /
            backend:
              serviceName: kubia-nodeport
              servicePort: 80
```

上述Ingress创建后，只要确保kubia.example.com能够解析到Ingress控制器即可工作。

**Ingress工作原理**

客户端访问DNS服务解析得到的IP地址，到达Ingress控制器，控制器确定该请求要访问哪个服务，然后查询该服务的Endpoints列表，从中选一个IP，从而定位到某个确定的POD。可见其没有经过服务进行访问，只是用了服务的endpoint表

**Ingress处理TLS传输**

客户端和Ingress控制器之间的传输是TLS连接时，控制器在和POD交流时将终止TLS传输，要使得Ingress具有TLS传输能力，需要进行配置

```shell
# 首先创建secret资源
openssl genrsa -out tls. key 2048 
openssl req -new - x509 -key tls.key -out tls.cert -days 360 -subj /CN=kubia.example.com
kubectl create secret tls tls-secret --cert=tls.cert - -key=tls .key 
```

```yaml
# 然后在创建Ingress时指定sercret
......
spec:
  tls:
    - hosts:
      - kubia.example.com
      secretName: tls-secret
......
```

## POD 就绪了吗

服务需要在POD就绪后再将请求发送到POD，以便带来更好的响应速度。

### 就绪探针 

探测POD是否准备好接收请求的探针。和存活探针类似，也有exec、http、tcp三种。就绪探针探测到失败的节点时，会将该节点从服务中移除。

就绪探针是一定要有的，否则可能在pod刚启动时就纳入服务，导致访问失败。

### 创建就绪探针

就绪探针要在POD托管对象的模板中定义，比如RC

```yaml
......
kind: ReplicationController
......
spec:
  ...
  template:
    spec:
      containers:
        - name: kubia
          image: zou8944/kubia
          readinessProbe:
            exec:
              command:
                - ls
                - /var/ready
          ......
```

## 获取所有POD地址

在某些场景下会需要获取所有POD的地址，此时使用服务就不行了。可以创建一个headless服务，即没有clusterIP的服务，然后通过某个容器中的nslookup进行DNS查找，步骤如下：

- 创建headless服务

```yaml
apiVersion: v1
kind: Service
metadata:
  name: kubia-headless
spec:
  clusterIP: None
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: kubia
```

- 创建一个有nslookup的pod

```shell
kubect1 run dnsutils --image=tutum/dnsutils --generator=run-pod/v1 --command -- sleep infinity
# run-pod/v1意味着运行一个临时pod，没有任何rc会托管它
```

- 在该节点上执行nslookup，能够看到所有已经准备就绪的pod地址

```shell
kubectl exec dnsutils nslookup kubia-headless
```

#