---
created_at: 2021-12-30 15:04:30
updated_at: 2021-12-30 15:04:30
slug: ldap-introduction
tags:
- LDAP
---

> 本文试图清晰明白的讲述LDAP是什么、应用场景、使用方法。

开篇照例一波吐槽。LDAP这个名字大家不会陌生，即所谓轻量级目录访问协议。无论博客还是论坛，网上对它的讲解太多了，但在我看来，都不得要领。它们中的大多数都仅介绍了冰山一角，还不注明资料来源。想来，作者很可能也不知道这些知识从哪里来的，这篇文章看看、那篇文章参考一下，东拼西凑，再看看库的API，写写代码，然后...it works!!!，再然后就没有然后了吧🤔。

本文试图从协议本身出发，尽量做到系统化。就算读者看了这篇文章还是不能掌握，也可以自己翻看协议文档解决问题。毕竟一手资料才是最可靠的。

<!--more-->

## 协议介绍

与LDAP相关的协议很多，但主要是两个系列，这里列出。读者可以不看本文后面内容，直接去翻协议了。

- [X.500系列协议](https://www.itu.int/rec/dologin_pub.asp?lang=e&id=T-REC-X.500-200811-S!!PDF-E&type=items)

  目录服务的最初协议，完整地描述了目录、目录服务的组成、目录结构等内容。X.500本身只是一个概览，各部分的实现在其子协议如X.501、X.502中，所以说X.500是一个系列协议。

  值得一提的是，常见的X.509公钥证书也属于该系列协议。

- [LDAP系列协议](https://www.rfc-editor.org/rfc/pdfrfc/rfc4510.txt.pdf)

  LDAP并非只有一个协议文件，其涉及到方方面面，每个方面单独由一个协议文件描述，加星号的必看

  - RFC4511*：通过TCP传输消息的方式，规定了传输层面的消息类型、消息内容，如绑定、查询等
  - RFC4512*：信息模型，规定了schema、object class、attribute type等内容
  - RFC4513*：规定了鉴权方式和安全机制：TLS、SASL
  - RFC4514：规定了DN的字符串表示方式
  - RFC4515：规定了过滤器的格式，过滤器用于查找时指定条件
  - RFC4516：规定了统一资源定位符的格式，即LDAP端点长啥样
  - RFC4517*：语法和匹配规则，列举了所有允许的语法和匹配规则
  - RFC4518：字符串国际化
  - RFC4519*：应用程序的schema，列举了所有允许的object class和attribute type
  - RFC2377*：推荐的DIT组织方式，即目录服务的树的组织方式

## 缩写

LDAP文章也好、协议也好，总是会有一大堆缩写，让人不明所以，这里列出常见的

- DAP - Directory Access Protocol，即目录访问协议
- LDAP - Lightweight Directory Access Protocol，轻量级目录访问协议
- DIB - Directory Information Base，目录信息库
- DIT - Directory Information Tree，目录信息树
- DUA - Directory User Agent，用户代理
- DN - Distinguished Name，可区别名称，即唯一名称
- RDN - Relative Distinguished Name，相对唯一名称，指DIT内某个节点上的名称，上层节点的DN配合上本节点的RDN，能够构成本节点的DN
- 一些属性类型的介绍
  - c - country name，国家名
  - cn - common name，通用名称
  - dc - domain component，域名组件
  - o - organization name，机构名
  - ou - organization unit name，机构的单位名
  - sn - surname，姓
  - st - state or province name，州或省

## Directory - 目录or电话簿？

国内将Directory翻译成目录，但如果用Google翻译协议中涉及到的相关内容，会被翻译成电话簿，哪种更好理解呢？从树形结构上看，貌似目录更容易理解，从历史原因看，后者更容易理解。这里顺便解释两个概念

- 白页：个人通信目录，这个在上世纪的美国电影中能见到。为什么是白页—以前使用白色纸张记录个人通信目录。黄页也是这个原因。
- 黄页：企业和团体通信目录，例如80、90后熟知的hao123网址黄页

要我看，翻译成两者都没有问题，但读者要掌握的核心是——树、查找。即Directory服务内部的数据组织形式是树形结构，这样做的目的是方便查找。其最开始存在的目的是做白页、黄页类应用，而我们可以利用这个结构做其它事情，比如用一个LDAP服务管理公司内所有地方的用户信息。

> 为了统一，本文将Directory翻译成“目录”

## X.500协议

如果不看X.500协议，LDAP中的很多东西是看不懂的。X.500定义了目录服务，LDAP只是它的轻量级实现。我们看看它规定了什么。

### 定义目录系统

Directory旨在提供一个用户友好的name-address类的映射，其中name不可变，address允许动态变化，即key-value结构。Directory由一批系统组成，每个系统持有对应现实世界的逻辑数据，这些存储的数据叫做**DIB**，即目录信息库。整体架构如下

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103110714678.png" alt="image-20220103110714678" style="zoom:80%;" />

一个标准的目录系统，有以下几部分

- 目录服务
- 目录服务的用户
- 目录服务用来暴露自己的访问端点
- 用户和服务之间使用协议如LDAP进行交互
- 用户使用LDAP客户端访问目录服务

### DIB与DIT

目录信息库，由DIT（目录信息树）、节点Entry、Entry中的属性及属性值构成。

- Entry代表一个节点，类型可以是object，也可以是alias，后者表示一个object entry的别名
- 一个Entry内可以拥有多个属性
- 一个属性内可以拥有一个Type，以及多个Value

下图展示了一个DIT的树形结构：

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103111254326.png" alt="image-20220103111254326" style="zoom:80%;" />

一个假设的DIT如下，则DN：{C=GB, L=Winslow, O=Graphic Services, CN=Laser Printer}代表了Laser Printer。

![image-20220103111455870](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103111455870.png)

你可能会想，DIB和常见的数据库有什么关系呢？实际上他们没什么关系，类似HTTP和TCP。硬要说有关系的话，DIB更加垂直吧🤔，仅适用于这种树形存储结构，查询多、更新少；数据库则更加通用，相对而言也更加底层。DIB只是规定了一种存储键值对数据的树形结构，可以用任何方式实现DIB，包括关系型数据库。理论上，HTTP也可以是其它实现，比如QUIC。

### 目录服务

X.500规定了目录复制支持的一些典型的操作，我们大致列举一下

- 读操作
  - Read：读指定的entry。LDAP不支持此操作
  - Compare：比较给的值和指定entry的值是否一致。这个在验证密码时有用
  - List：列出指定entry的所有子entry
  - Search：列出满足指定过滤器的所有entry
  - Abandon：放弃，作用在一个挂起请求上，标识客户端对该请求不在感兴趣
- 修改操作
  - 添加entry
  - 移除entry
  - 修改entry
  - 修改DN，修改某个entry的相对名称。如果该entry有子节点，则子节点的这部分名字也会被修改
- 其它可能的输出
  - 错误
  - 转移（referral）：可能当前服务无法处理这个请求，它会返回一个新的端点，类似HTTP的重定向

### 分布式Directory

Directory支持分布式操作，此时的服务端组成如下

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103112541253.png" alt="image-20220103112541253" style="zoom:80%;" />

- DSA：Directory System Agent。用来连接服务和DUA。他可以缓存Directory数据，可以用本地数据直接响应，也可以单纯做一个转发
- LDAP Server：是Directory Service的一部分。他可以直接使用本地数据，也可以转发到其它LDAP Server获取数据

### 其它

协议还规定了目录服务的访问安全、备份等操作，这里暂时忽略。之后值得探究的倒是其安全协议X.509。

## LDAP协议

通过X.500我们知道了目录服务内部由DIT实现，每个节点上放置的数据貌似可以自由指定，那为什么无论看文章还是自己搭建的LDAP服务，总是以dc、cn之类的属性指定dn呢？这一点我们在schem、dit的组织方式两节解释。目录服务规定了几种访问方式，在LDAP是如何体现的呢？这点在访问一节中解释。

### Schema

LDAP通过RFC4512、RFC4517、RFC4519，对DIT进行了详尽的规定。限制了节点的类型、属性的类型、值的类型，这些限制，叫做schema。具体来说，有几点

- 规定了Syntax，即“语法”。规定了attribute value的存储结构

- 规定了attribute type，即属性的种类

- 规定了object class，对象类，类之间可以继承，一个类由多个attribute type组成。一个entry必须是某个object class。

  object class规定了该entry可以包含哪些属性

- 规定了匹配规则，用于在执行查找和比较操作时对库中的属性值和请求的属性值进行比较

以面向对象的思维是很好理解的，object class是类、attribute type是属性、Syntax则是属性的类型，齐活。

列举常见数据类型

| 语法             | 举例                                                         |
| ---------------- | ------------------------------------------------------------ |
| Bit String       | ’0101111101’B                                                |
| Boolean          | TRUE/FALSE                                                   |
| Country String   | UA、AU：两个可打印字符                                       |
| Directory String | This is a value of Directory String containing：UTF8字符串   |
| DN               | CN=John Smith\, III,DC=example,DC=net：DN的表示              |
| IA5 String       | 零个或多个International Alphabet 5的字符                     |
| Integer          | 整形                                                         |
| Octet String     | 八进制字符串                                                 |
| OID              | Object Identifier，对象唯一标识符，比如： 1.3.6.1.4.1.1466.115.121.1.38 |

列举常见匹配规则

| 规则                | 说明                             |
| ------------------- | -------------------------------- |
| bitStringMatch      | 每一个bit都要相等                |
| booleanMatch        | 布尔匹配                         |
| caseIgnoreListMatch | 列表匹配，列表中的内容忽略大小写 |
| integerMatch        | 整型匹配                         |

列举常用属性种类

| 种类         | 父类 | 语法             | 匹配方式           | 说明                                                         |
| ------------ | ---- | ---------------- | ------------------ | ------------------------------------------------------------ |
| name         | -    | Directory String | caseIgnoreMatch    | 名字，是所有名字类种类的父类                                 |
| c            | name | Country String   |                    | country name，国家名                                         |
| cn           | name | 同name           | 同name             | common name，通用名字                                        |
| dc           | -    | IA5 String       | caseIgnoreIA5Match | domain component，域名组件<br />即域名的一部分，比如example.com<br />由dc=example,dc=com两个dc组成 |
| l            | name | 同name           | 同name             | locality name，地点名                                        |
| o            | name | 同name           | 同name             | orgnazation name，机构名                                     |
| ou           | name | 同name           | 同name             | orgnazation unit name，机构单位名                            |
| sn           | name | 同name           | 同name             | surname，姓                                                  |
| st           | name | 同name           | 同name             | state or province name，州或省                               |
| uid          | -    | Directory String | caseIgnoreMatch    | user id，用户唯一标识                                        |
| userPassword | -    | Octet String     | octetStringMatch   | 用户密码                                                     |

列举常用object class。

| class        | 父类 | 必包含 | 可选包含                                         | 说明     |
| ------------ | ---- | ------ | ------------------------------------------------ | -------- |
| country      | top  | c      | searchGuide\description                          | 国家     |
| dcObject     | top  | dc     | -                                                | 域名对象 |
| device       | top  | cn     | serialNumber\seeAlso\owner\ou\o\l\description    | 设备     |
| organization | top  | o      | userPassword\searchGuide...超多                  | 组织     |
| person       | top  | sn\cn  | userPassword\telephoneNumber\seeAlso\description | 个人     |

### DIT组织方式

schema有了，那么是不是所有节点都可以是任何object class类型呢？理论上是的，但LDAP有推荐的方式构建DIT——RFC2377。我们实际中创建的LDAP服务，也是以这种建议进行构建的。其主要特点是以DNS为基础进行构建，总体如下

- DIT的上部使用dc，将域名转换为dc类型的entry。比如某公司域名为foo.com，则其根节点的DN为`dc=foo,dc=com`;它有一个子域名，为account.foo.com，则该节点位于根节点下，其RDN为`dc=account`，合起来DN为`dc=account,dc=foo,dc=com`。
- DIT的下部，可以是个人、组、机构等。建议使用uid或cn来描述RDN。比如account.foo.com下有一个账户名为zou8944，则其DN为`cn=zou8944,dc=account,dc=foo,dc=com`

>这种组织方式看起来理所应当，但其前身X.500却并不是这么规定的。由于历史原因，它使用权威注册的组织机构命名作为DIT的上层。比如`o="Nadir Networks, Inc.", st=New Jersey, c=US`，这表示，在美国的新泽西州的Nadir网络公司。
>
>这样做有两个问题：权威的组织机构注册非常麻烦；跨国公司不好办。于是有了新的基于DNS的划分方式。

### 访问

X.500定义了读、写方面的操作，LDAP又如何呢？这一块位于RFC4511，本文并不打算深入研究，毕竟我不需要去实现一个LDAP库。我们知道几点就好了

- LDAP传输可以建立在TCP协议之上
- 主要的消息类型
  - Bind：绑定，TCP建立连接后首先绑定。绑定时会进行鉴权。只有绑定后才能进行其它操作。
  - Unbind：解绑
  - Search：搜索
  - Modify：修改entry的值
  - Add：添加entry
  - Delete：删除entry
  - Modify DN：修改某个entry的DN
  - Compare：比较，比如进行账号密码登录时就可以用Compare操作
  - Abandon：取消一个未完成的操作
  - Extended：本协议的扩展操作，目录服务自定义的操作

### 安全

LDAP的安全主要有三个方面

- 使用TLS安全传输
- 提供简单的匿名和账号密码认证
- 支持SASL构建鉴权和安全服务层

这块仔细研究还挺复杂的，后面单独研究。

## 最佳实践 - 搭建LDAP服务

我们将LDAP服务搭建在Kubernetes中，按照本文的Manifest，一定能够搭建成功，本文搭建的特点是

- 搭建两个服务：OpenLDAP-提供LDAP服务；phpldapadmin-提供LDAP的UI服务
- OpenLDAP的数据挂载在emptyDir卷，重启后原数据会丢失。如不想这样，请自行创建pv，修改pvc。也可以直接挂载volume
- 两个服务的账号密码，参考脚本中的环境变量
- phpldapadmin从集群中暴露出来的方式，这里未定义，需要读者自己加
  - 如果在云服务，可以直接再创建一个带外网地址的Service
  - 如果有域名，可以配置Ingress指向phpldapadmin的Service
  - 如果在自己局域网内，则可以直接访问

### LDAP服务

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: ldap
  namespace: ldap
  labels:
    app: ldap
spec:
  selector:
    matchLabels:
      app: ldap
  template:
    metadata:
      labels:
        app: ldap
    spec:
      containers:
      - name: ldap
        image: 'osixia/openldap'
        ports:
        - name: tcp-389
          containerPort: 389
          protocol: TCP
        - name: tcp-636
          containerPort: 636
          protocol: TCP
        env:
        - name: LDAP_ORGANISATION
          value: devops
        - name: LDAP_DOMAIN
          value: zou8944.com
        - name: LDAP_ADMIN_PASSWORD
          value: test123
        - name: LDAP_CONFIG_PASSWORD
          value: test123
        - name: LDAP_BACKEND
          value: mdb
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 100m
            memory: 100Mi
        volumeMounts:
        - name: ldap-config-pvc
          mountPath: /etc/ldap/sldap.d
        - name: ldap-data-pvc
          mountPath: /var/lib/ldap
      volumes:
      - name: ldap-config-pvc
        emptyDir: {}
      - name: ldap-data-pvc
        emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: ldap-svc
  namespace: ldap
  labels:
    app: ldap-svc
spec:
  ports:
  - name: tcp-389
    port: 389
    protocol: TCP
    targetPort: 389
  - name: tcp-636
    port: 636
    protocol: TCP
    targetPort: 636
  selector:
    app: ldap
```

### LDAP管理服务

```yaml
kind: Deployment
apiVersion: apps/v1
metadata:
  name: phpldapadmin
  namespace: ldap
  labels:
    app: phpldapadmin
spec:
  selector:
    matchLabels:
      app: phpldapadmin
  template:
    metadata:
      labels:
        app: phpldapadmin
    spec:
      containers:
      - name: phpldapadmin
        image: 'osixia/phpldapadmin:stable'
        ports:
          - name: tcp-80
            containerPort: 80
            protocol: TCP
        env:
          - name: PHPLDAPADMIN_HTTPS
            value: 'false'
          - name: PHPLDAPADMIN_LDAP_HOSTS
            value: ldap-svc
        resources:
          limits:
            cpu: 500m
            memory: 500Mi
          requests:
            cpu: 10m
            memory: 10Mi
---
apiVersion: v1
kind: Service
metadata:
  name: phpldapadmin-svc
  namespace: ldap
  labels:
    app: phpldapadmin-svc
spec:
  ports:
  - name: tcp-80
    port: 80
    protocol: TCP
    targetPort: 80
  selector:
    app: phpldapadmin
```

### 试试

`kubectl apply -f xxx.yaml`执行上面的manifest文件，能够得到创建结果

![image-20220103131116477](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103131116477.png)

这里我多创建了一个phpldapadmin-svc-internet，一个具有外部访问地址的Service，方便访问，然后我们访问一下，来到如下界面。

![image-20220103131256572](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103131256572.png)

点击左侧的login，输入管理员的DN，password，得以进入

![image-20220103131418677](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103131418677.png)

进入之后的界面如下

![image-20220103131515385](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103131515385.png)

其中，左侧的树形结构，就是DIT。上面的schema可以查看当前LDAP服务支持的object class、attribute type等类型；search能够进行查找；导入导出能够将DIB导出成文件。

![image-20220103131732221](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103131732221.png)

搜索界面也很好理解

- Base DN：从哪个entry下开始搜索
- Search Scope：搜索子树、同级、父节点
- Search Filter：搜索过滤器，可以指定entry的类型、属性的类型、属性的值等
- Show Attributes：搜索结果展示的属性

![image-20220103131800516](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220103131800516.png)

## LDAP客户端

至此，我们已经掌握了目录服务的工作原理，了解DIT的结构、Schema，了解了LDAP访问的类型：也无非是CRUD。

实现LDAP库并不难，按照RFC4511，抽象出Object Class、Attribute、DN、各种操作等即可。

[Spring LDAP](https://docs.spring.io/spring-ldap/docs/current/reference/#spring-ldap-introduction-overview)就提供了这方面的能力，主要操作都集中在LdapTemplate，它提供了DSL，相比于独立的库，它简化了操作的过程，简化了代码。

看了下Vertx，目前尚不支持LDAP操作，仅支持使用LDAP做鉴权操作。

这里我就不再描述Spring LDAP的能力了，毕竟官方手册不长，而且就是各种自己实现的抽象，我没必要去搬一些API，对读者造成不必要的误导。

## 总结

本文从X.500开始，较为系统第介绍了LDAP的定义、实现方式、Schema约束，并实际动手在Kubernetes上搭建了一个临时的LDAP服务。

总体而言，LDAP是简单的、易于实现的、应用场景小而典型的数据存储及服务方式。
