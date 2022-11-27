---
created_at: 2022-06-12 11:03:36
updated_at: 2022-06-12 11:03:36
slug: x-509-introduction
tags:
  - X.509
---

> 我每篇博客的书写都是有动机的，它们或是对一段时间的工作总结、或是对某个事物的感悟。这次要写X.509的博客，是因接入IAP时，从网上搜索的各种问题发现一个惊人的事实：很多人不知道X.509证书的验证方式，当然也包括我。

<!--more-->

初识X.509证书，多半是HTTPS协议，SSL或TLS握手阶段，需要用证书传输公钥，建立加密的传输信道。于是在印象中X.509就和HTTPS绑定在了一起。这种绑定有些许先入为主。实际上X.509证书的用途不止如此。

## 现成的知识

网上已经很多写得好的文章，推荐一篇：[X.509数字证书的基本原理及应用](https://zhuanlan.zhihu.com/p/36832100)。从中我们可以总结出几个要点

- 数字证书的目的在于安全地分发公钥
- 数字证书 = 公钥 + 公钥所属实体 + 签名
- 数字证书分多级，一般有根证书、中间证书、叶子证书，根证书安装在系统中，叶子证书和中间证书需要根证书进行验证

除此之外，没有更多的理论信息。博客的输出往往只是作者知识学习过程的输出，常很片面，仅能作为知识交流和了解的方式，不能作为严肃学习的主要来源（包括我这篇）。优秀如此文，看完也还是虚空之感，因为我们不知道还有多少相关知识是不知道的。

## 原材料

学习X.509的误区之一，是将它与HTTPS、TLS等协议结合在一起，然后被这些协议的其它知识点搞得头昏目眩。就像JWT，如果只是和登录鉴权结合在一起，就会忽略它本身的特性。

> 我们往往对一个技术的支撑技术缺乏了解，甚至缺乏了解的耐心。

最好的方式还是阅读RFC，相关文档如下

- [RFC5280](https://datatracker.ietf.org/doc/html/rfc5280)：主协议，描述X.509用途、结构、验证方式等
- [RFC2560](https://datatracker.ietf.org/doc/html/rfc2560#legend)：OCSP协议，在线证书状态协议，描述如何实时获取证书的状态，即有效性
- [RFC4491](https://datatracker.ietf.org/doc/html/rfc4491)、[RFC3279](https://datatracker.ietf.org/doc/html/rfc3279#legend)、[RFC4055](https://datatracker.ietf.org/doc/html/rfc4055#legend)：附加协议，描述了在证书中使用的加密算法

其中，RFC5280需要认真阅读，其它协议选读，了解即可。

## RFC5280

### 基础

- 证书是什么

  全面地说应该叫做公钥证书，它是一种数据结构，用来绑定公钥值，该绑定加上了CA签名让它变得可信。CA通过技术手段使得这种可信变得有保证。一般来说，这种技术手段是操作系统内置根证书+证书的路径验证。

- 用途

  - 网站通信，即常规的HTTPS

  - 电子邮件

  - 用户鉴权，可参考JWS的x5c字段

  - IPsec

- 证书生命周期

  证书的证书的生命周期，是根据它的签名内容而定的，即证书并不是永久的。因为证书可能被仿冒。

  > 现在很多以年为单位，这可能只是业务上的生命周期，并不一定是技术上的生命周期，理论上说这有一定的安全隐患。

- **证书path**

  用户拿到证书，如果不拥有颁发该证书的CA的可信的公钥，此时需要另一个证书来获取该CA的可信公钥。这样可以形成一个证书链，这叫做证书路径。

- 证书分类

  - **CA证书**

    - 交叉证书：签发方和证书主体来自不同的实体。用于描述两个CA的互信关系
    - 自签发证书：签发方和证书主体是同一个实体
    - 自签名证书：属于自签发证书的一种，它的签名可以用证书自带的公钥验证。这个用在证书路径的根部，即根证书

  - 终端实体证书

    颁发给无权颁发证书的实体

- 证书撤回

  签发的证书在实际有效期前可以被撤销，是通过Certificate Revoke List的方式，即CA定期发布CRL，使用证书的系统，除了验证证书本身的有效性，还需要检查证书是不是在CRL，如果在，则证书不可用。

  > 一些情况下，客户端需要马上知道证书的有效性，如金融和证券行业，CRL无法满足这个实时性需求，于是有了OCSP，它提供在线查询某个证书是否有效的服务

### 证书结构

协议中的结构描述过于严谨和复杂，这里借用前面提到的博客的截图，比较易于理解。

<img src="https://pic1.zhimg.com/v2-9b7cbd5eb1b56c6e6632f1ccb1c4a448_r.jpg" alt="preview" style="zoom:50%;" />

### 证书验证方式

RFC5280第六小结阐述了客户端如何处理证书路径的算法，所有使用证书的客户端都必须实现该算法。

**路径验证的主要目标是根据信任目标的公钥验证证书主题的名称（或备用名称）和证书主题公钥之间的绑定**。具体来说，验证的是路径是否满足如下条件

1. 对于{1, ..., n-1} 中的所有 x ，证书x的主题是证书x+1的颁发者
2. 证书1由信任目标颁发，即我们常说的根证书，一般是提前下载到操作系统
3. 证书n是要验证的目标证书，即叶子证书
4. 对于所有证书x，都必须在有效时间内

现实应用的举例：

- 在JWS规定的头部中的x5c字段，会将整个证书路径全部给出，根据这些证书我们可以验证1、3、4条件，至于2，则是根据具体厂商的不同而不同，比如IAP Storekit2提供的JWS，就需要我们从apple开发者网站手动下载可信的根证书。

- DNS证书是我们接触得最多的证书，其本身是一个叶子证书，证书内部指明了签发该证书的中间证书，中间证书指向安装在本地的根证书，由三个证书构成一条路径，验证可完全满足上述条件。

  以知乎为例，查看其证书信息

  <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220612151129845.png" alt="image-20220612151129845" style="zoom:50%;" />

  <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220612151246083.png" alt="image-20220612151246083" style="zoom:40%;" />

  > 还可以看到，DNS证书的域名是主题名称和备用名称的并集，比如RFC官网的证书，域名是datatracker.ietf.org，主题名称却是sni.cloudflaressl.com，备用名称是datatracker.ietf.org
  >
  > <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220612151643845.png" alt="image-20220612151643845" style="zoom:50%;" />
  >
  > <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220612151609922.png" alt="image-20220612151609922" style="zoom:50%;" />
  >
  > <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220612151628066.png" alt="image-20220612151628066" style="zoom:50%;" />

  > 可以多看几个证书的结构，加深印象

- 抓包工具fiddler或charles，如果需要抓取HTTPS，需要自己安装根证书，解决的就是受信的问题。

### CA机构之间的关系

**为什么会有中间证书**？

证书需求量巨大，根证书处理不过来，于是将部分证书签发的权限分发给其它CA供应商。这种结构在RFC5280第三节中的管理协议和操作协议中有所阐述，即PKI各个实体之前的关系

- CA可以授权给下一级CA，也可以授权给RA
- RA即注册授权机构，只能颁发证书，其证书签发者是上层CA
- CA可以颁发证书和CRL，签发者可以是自己（根证书），也可以是上层CA
- CRL签发机构，权限来自上层CA下放，只能颁发CRL

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220612152408807.png" alt="image-20220612152408807" style="zoom:50%;" />

> **什么是PKI？**
>
> 即Public Key Infrastructure，公钥基础设施，即利用公开秘钥机制建立起来的基础设施，上图就描述了PKI的主要组成部分。
>
> PKI users即普通个人或公司，用终端实体表示，我们申请证书的机构就是RA或CA，CA又是有层级的。这一堆东西，构成了当前网络访问的安全基础设施。因此，PKI指的是整个证书分发机制构成的宏大系统。

## 其它协议

其它协议都很短，RFC2560看看摘要就知道什么是OCSP了，就是一个普通的状态查询接口。

## 实践

这里展示代码验证IAP证书路径的过程（暂时忽略了有效期的验证）

```kotlin
private val appleRootCert = PathMatchingResourcePatternResolver()
        .getResources("classpath:cert/AppleRootCA-G3.cer").first().inputStream.readBytes()

// 解码并验证时接收到的通知
fun decodeAndVerifyAppleNotification(rawNotification: String): AppleNotificationPayload {
  ... ...
  // 验证证书链，并获取叶子证书携带的公钥
  val targetPublicKey = verifyAppleNotificationCertsThenReturnPublicKey(this)
  ... ...
}

private fun verifyAppleNotificationCertsThenReturnPublicKey(jwt: DecodedJWT): PublicKey {
  val certFactory = CertificateFactory.getInstance("X.509")
  // 根证书，已经提前下好了
  val appleRootCert = certFactory.generateCertificate(ByteArrayInputStream(appleRootCert)) as X509Certificate
  // 放在x5c字段中的证书链
  val jwsCertChain = jwt.getHeaderClaim("x5c").asList(String::class.java).map {
    certFactory.generateCertificate(ByteArrayInputStream(Base64.getDecoder().decode(it)))
  }
  // 关键点1：验证根证书
  if (jwsCertChain.last() != appleRootCert) throw Exception("根证书错误")
  // 关键点2：验证证书链，证书x签发了证书x+1
  for (index in 0..jwsCertChain.size - 2) {
    jwsCertChain[index].verify(jwsCertChain[index + 1].publicKey)
  }
  // 关键点3：第叶子证书的公钥即为验证整个JWS的公钥
  return jwsCertChain.first().publicKey
}
```

## 总结

写得再好的博客文章，都是经过别人消化系统呈现的冰山一角，会经历知识衰减。永远比不上一手资料，即使是不仔细看的一手资料。

回到X.509证书本身，抓住几个重点

1. 证书结构：主题（包括主题机构、名、公钥信息）、签发者、有效期、签名（又叫做指纹）
2. 证书路径：通过主题名或主题备用名与签发者串联，能够产生证书路径，即证书链
3. 证书如何使用：通过证书路径验证即可保证证书是可信的，使用的目标是证书携带的公钥（证书只是安全携带公钥的工具而已）
4. 众多CA、RA共同构成了PKI
