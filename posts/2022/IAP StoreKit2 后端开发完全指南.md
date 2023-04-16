---
created_at: 2022-05-13 16:02:44
updated_at: 2022-05-13 16:02:44
slug: iap-store-kit-2-guide
---

> TL;DR;
>
> 2021年10月，苹果发布了StoreKit2。新API和流程看起来更加简化，但是苹果官方文档并没有让开发者接入变得简单，调试起来也是各种问题，这方面和StoreKit1一样做的不好。梳理是必要的。

<!--more-->

# 文档研读

## 文档目录

官方文档虽然有组织结构，但不清晰，按照如下结构去通读，还是很有必要的。

- [概览页](https://developer.apple.com/cn/in-app-purchase/)
- 购买项目配置
  - [配置流程](https://help.apple.com/app-store-connect/?lang=zh-cn#/devb57be10e7)
  - [创建购买项目](https://help.apple.com/app-store-connect/?lanng=zh-cn#/devae49fb316)
- [StoreKit2概览](https://developer.apple.com/cn/storekit/)
  - [客户端StoreKit SDK](https://developer.apple.com/documentation/storekit)
  - [服务端API概览](https://developer.apple.com/documentation/appstoreserverapi)
- [服务端通知](https://developer.apple.com/documentation/appstoreservernotifications)
  - [在App Store Connect中配置回调URL](https://help.apple.com/app-store-connect/?lang=zh-cn#/dev0067a330b)
  - [服务端通知 Changelog](https://developer.apple.com/documentation/appstoreservernotifications/app_store_server_notifications_changelog)
  - [通知接收概览](https://developer.apple.com/documentation/appstoreservernotifications/receiving_app_store_server_notifications)
    - [通知的数据结构](https://developer.apple.com/documentation/appstoreservernotifications/responsebodyv2decodedpayload)
    - [如何响应通知（重要：阐述了通知重试机制、通知丢失的补救措施）](https://developer.apple.com/documentation/appstoreservernotifications/responding_to_app_store_server_notifications)
- [服务端API概览（没错，和上面重复了，这里提出来凸显重要性）](https://developer.apple.com/documentation/appstoreserverapi)
  - 访问Apple Server API的凭证 
    - [创建API Key](https://developer.apple.com/documentation/appstoreserverapi/creating_api_keys_to_use_with_the_app_store_server_api)
    - [构建JWT Token](https://developer.apple.com/documentation/appstoreserverapi/generating_tokens_for_api_requests)
  - [获取交易历史](https://developer.apple.com/documentation/appstoreserverapi/get_transaction_history)
  - [获取所有订阅状态](https://developer.apple.com/documentation/appstoreserverapi/get_all_subscription_statuses)
- 如何测试
  - [在沙盒中测试](https://developer.apple.com/cn/documentation/storekit/in-app_purchase/testing_in-app_purchases_with_sandbox/)

总体来说，阅读步骤应该如下

1. 概览页，对IAP有初步认识，了解购买项目类型、在App Store Connect控制台 配置、使用StoreKit开发、使用沙盒环境测试等。

2. StoreKit2的客户端SDK和服务端API。

   了解客户端如何操作，作为后端，要关心的是服务端在操作完成后会得到一个Transaction，于StoreKit2，该Transaction和回调通知中的Transation、以及交易历史中的Transation具有同样的结构和内容，也就是说，我们的APP可以直接将其发送到业务后端进行验证。

   还能了解到服务端API其实主要就提供两个接口：获取交易历史、获取订阅状态

3. 阅读服务端通知。将了解到通知的数据结构、类型，以及安全机制。这一点很重要。

4. 详细阅读服务端API，将了解访问API的凭证如何生成，交易历史的结构、订阅状态的结构等

5. 阅读沙盒测试。了解如何在沙盒环境中测试。

> 文档阅读过程中，由于来回跳转，很可能会去到StoreKit1的文档，它们也可能描述交易流程、支付收据、收据验证等信息，非常容易和StoreKit2混淆，注意区分。区分的主要方式：StoreKit1或Original API这俩关键字

> Apple文档的不合理之处在于——没有目录、没有支付流程说明、没有demo、没有专门针对后端人员的说明（我们很可能对客户端并不熟悉）

## 信息提取

下面针对文档中的关键信息进行说明

### 商品类型

IAP中，可供购买的商品类型分为如下四种。

- 消耗型：购买后，一次使用即失效
  - 可重复购买
  - 例：金币
- 非消耗型：一次购买，永不过期
  - 例：照相软件的某一款滤镜
- 自动续期订阅：购买后一段时间内有效
  - 到期后会自动续期
  - 例：腾讯视频会员
- 非续期订阅：购买后一段时间内有效
  - 到期后不会自动续期
  - 例：没用过🤔

本文的讨论，几种在自动续期订阅的商品类型。

### 理解交易（Transaction）

Transation，交易。[官方手册](https://developer.apple.com/documentation/storekit/transaction)说：Transaction代表了app中对某个产品的购买。用户的每次购买或续费都会产生一个新的Transation对象，看起来已经说得够清楚了，但还不够，它只说了定义，没有说不通场景下的含义。有时候它出现的地方会让人困惑，比如回调通知中必然会带有交易信息，但像降级、退订这种通知的交易信息的意义何在呢？我们如何知道它代表着什么呢？

为此，我总结了三个关于交易的要点。

交易要点1：**只要用户发生了扣费，就会产生一个新的Transaction —— 扣费=交易**。穷举所有会产生扣费的场景

- 订阅成功，包括如下
  - 初次订阅
  - 过期后重新订阅
  - 自动续期的订阅到期时自动续订

- 订阅升级成功

  IAP中，几个产品组成一个订阅组，产品之间可以设置等级，用户可以再同一个订阅组内的产品之间互相切换，当从低级产品切换到高级产品时，马上生效（将原低级产品为使用的部分折算成钱退回账户，马上产生对高级产品的订阅，即扣费）

对同一个App，一个用户（体现为一个Apple ID账号）可能因为上述操作产生多个交易，这些交易组成了交易历史。

交易要点2：**一个用户针对同一个App的交易历史中，只有最近一条是有效的**。这个可以证明，在上述会产生扣费的场景中，订阅成功的case都是建立在前一个订阅失效的前提下；订阅升级的case中，前一个低级订阅会因为马上退款而失效。因此，产生的众多交易中，有且仅有最近的那条交易是有效的。

交易要点3：**一个用户针对同一个App的所有交易中，originalTransactionId是一样的**。这里第一次出现originalTransactionId，它是第一次购买时的交易ID，今后用户的所有交易，都是基于它串成交易历史。

### 交易历史

交易历史作为Apple提供的唯二API之一，需要注意如下几点

- 消耗型商品的交易不会出现在交易历史中
- 手册宣称默认按照购买时间从早到晚排序，但实测并不严格，可能出现局部顺序不对的情况，拿到后还是要自己排一次
- 如上所说，最近一条才是有效的。开发时应以最近一条作为判断依据

### 订阅升降级

对于自动续期订阅的产品，可以设定订阅顺序，如下截图App Store Connect控制台的设置例子

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220514172920979.png" style="zoom: 40%;" />

要点

- 等级越高越靠前，上面高级会员顺序为1，普通会员顺序为2，用户由普通会员切换到高级会员为升级，反之则为降级

- 同一等级能够设置多个商品。同一等级内商品之间切换不算升降级，只会改变当前订阅到期后下次自动续订的产品。

  举例：用户购买了包月高级会员，但一天后，通过设置切换为了包年高级会员。则此时用户的订阅状态依旧是包月高级会员，待一个月后，包月会员过期，App Store会自动为用户续费包年高级会员。

那么，用户如何能够在不同产品之间切换呢？有两个途径

- App暴露的UI
- 设置 - 用户设置页面 - 订阅 - 具体App

前者一般仅用于初次订阅，订阅后会将订阅按钮隐藏；后者则可以任意切换。

以知乎为例，App暴露的购买API如下

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/IMG_5914.PNG" alt="IMG_5914" style="zoom:25%;" />

在设置中呈现如下

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/IMG_5915.PNG" alt="IMG_5915" style="zoom:25%;" />

### 支付流程

如果只有客户端，那么支付流程如下

1. 客户端通过StoreKit SDK拉起支付
2. 用户输入密码或Face ID完成支付
3. StoreKit回调客户端并传入Transaction
4. 客户端校验该Transaction，校验通过后发放权益

如果有服务端，权益发放在服务端，则流程如下

- 客户端流程
  1. 客户端通过StoreKit SDK拉起支付
  2. 用户输入密码或FaceID完成支付
  3. StoreKit回调客户端并传入Transaction
  4. 客户端校验该Transaction，校验通过后，将Transaction发送给服务端
- 服务端流程1
  1. 接收来自客户端的Transaction并校验，校验通过后，为用户发放权益
- 服务端流程2
  1. 接收来自Apple Server的回调通知，根据通知的内容，对用户发放权益
- 服务端流程3
  1. 定期调用交易历史查询接口，为在回调通知漏掉的交易补发权益。

其中，服务端流程1和流程2是分开并行存在的，且流程1可选（回调通知较慢，加上流程1能够提升用户体验）；流程2必须有，是唯一能够及时知悉所有交易发生的时机；流程3用于补单或者恢复购买。

> 注意事项：对于服务端流程3，由于交易历史查询接口需要输入originalTransactionId，所以如果用户的首次交易被遗漏，是没有办法查询的。所以它需要客户端协助：客户端获取当前Apple ID的任意一条交易上传服务端，服务端取其中的originalTransactionId查询交易历史，再取交易历史的最近一条交易作为发放权益的依据。

### 通知类型

回调通知通过notificationType和subType两个字段区分，自动续期订阅相关通知如下

| notificationType | subType | 说明 | 要处理吗？ |
| ---------------- | ------- | ---- | ------ |
| DID_CHANGE_RENEWAL_PREF | DOWNGRADE | 降级，降级下个周期生效 | v |
| DID_CHANGE_RENEWAL_PREF | UPGRADE | 升级，升级马上生效 | v |
| DID_CHANGE_RENEWAL_PREF |  | 取消降级 | v |
| DID_CHANGE_RENEWAL_STATUS | AUTO_RENEW_ENABLED | 开启自动续期 |  |
| DID_CHANGE_RENEWAL_STATUS | AUTO_RENEW_DISABLED | 关闭自动续期；退款后也会发送这个通知 |  |
| DID_FAIL_TO_RENEW | GRACE_PERIOD | 自动续期失败，因为卡里没钱了，但在宽限期内还是提供服务 |  |
| DID_RENEW |  | 续订成功 | v |
| DID_RENEW | BILLING_RECOVERY | 开始付费失败，后来恢复订阅了 | v |
| EXPIRED | VOLUNTARY | 因为用户关闭自动续期而过期 |  |
| EXPIRED | BILLING_RETRY | 尝试扣费失败而过期 |  |
| EXPIRED | PRICE_INCREASE | 用户不同意涨价而过期 |  |
| GRACE_PERIOD_EXPIRED |  | 宽限期已过 |  |
| PRICE_INCREASE | PENDING | 涨价，用户还没同意 |  |
| PRICE_INCREASE | ACCEPTED | 涨价，用户已同意 |  |
| REFUND |  | 用户退款成功 | v |
| REFUND_DECLINED |  | 苹果商店拒绝退款(来自开发者) |  |
| RENEWAL_EXTENDED |  | 苹果商店延长了订阅的续订日期(来自开发者) |  |
| REVOKE |  | 订阅购买者撤销了家庭共享 |  |
| SUBSCRIBED | INITIAL_BUY | 初次购买 | v |
| SUBSCRIBED | RESUBSCRIBE | 再次订阅之前订阅的内容/或通过家庭共享得到之前订阅的内容 | v |

**理解不同类型通知中交易信息的含义**

每个通知中都会携带交易信息，位于 data -> signedTransactionInfo 字段，它总是当时（发送通知那一刻）生效的交易，举例

- 初次购买时，携带的购买成功的交易信息
- 升级时，携带的升级之后，购买的高级商品的交易信息。原低级产品需要自己通过交易历史才能查询得到
- 降级时，不会马上生效，携带的是上次购买成功的交易信息
- 关闭自动续费时，携带的是上次购买成功的交易信息
- 退款时，携带的是上次购买成功的交易信息（这是我猜的，没有实测过，因为无法触发退款通知）

> 你可能会想，区分这么多通知类型有什么用？的确，对于发放权益来说，大多数通知都是没用的，但如果加上推广、用户留存、营销就很有用了。比如检测到用户关闭自动订阅，可以定点向该用户推送营销信息，或者推出专门的优惠套餐等。
>

# 技术点

## 业务用户识别

Apple服务的回调通知中，并不会携带Apple ID信息，因此无法区分该通知属于哪个具体业务用户。Apple的提供的方式是appAccountToken字段，该字段在客户端发起支付时指定，在通知中携带，以便业务后端区分。关于它注意几个点

- appAccountToken由业务后端自己生成维护
- 如果用户自行在控制台操作，可能出现回调通知不带appAccountToken的情况。此时可以从交易历史中查询（第一条交易一定会带appAccountToken，因为首次发起购买一定是从我们的APP客户端，就一定会设置）

## JWS签名验证

StoreKit2的一个重要变化是，大部分信息都采用JWS进行组织。Transaction是JWS、通知也是JWS。上面说的交易流程中，客户端交易成功上传Transaction时，后端需要验证其有效性；接收到通知时，也要验证其有效性。

> 注意这是JWS并非JWT，二者的差别在于，JWT是基于JWS构建的，赋予了更多的业务意义，即Token的意义，主要体现在payload中的字段，JWT定义了标准的字段如aud、exp等，具体可以参考我的[这篇文章](https://zou8944.com/2021/12/20/JWT/)。而JWS并未对payload的内容做出约束，只定义了Header.Payload.Signature的组成方式、定义了Header中加密字段的含义。
>
> 值得一提的是，Sign In with Apple就用的JWT作为登录成功后的Token。
>
> 至于使用的库嘛，使用一般的JWT库都可以，只不过在验证整个加密字符串时，验证Claims咩有作用，此时关注的是验证Signature。

### 客户端上传交易信息的验证

对于后端的处理，官方并没有规定一定要将客户端得到的Transaction传到服务端，加这一步只是我们为了实时性而做的。此时的签名就要我们自己来处理了。其实是有两种方式进行确认的

1. 在业务系统已有的安全传输条件下直接传输交易信息，比如业务系统已有登录鉴权，可以相信经过登录后传输的信息是可信的
2. 将整个原始的Transaction JWS传输给后端，后端自己验证，验证逻辑同下文“通知的签名验证”一致。

### 通知的签名验证

这一点是最多人搞不清楚的，我们观察任意一个通知的Header如下。没有kid字段，取而代之的是x5c，这代表提供验证公钥的是一个证书X.509证书链。我们需要先验证证书链的正确性，再用证书链提供的公钥验证整个JWS的正确性。

```json
{
  "alg": "ES256",
  "x5c": [
    "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"
  ]
}
```

验证逻辑如下

1. 从[Apple官网](https://link.juejin.cn/?target=https%3A%2F%2Fwww.apple.com%2Fcertificateauthority%2FAppleRootCA-G3.cer)下载根证书
2. 取证书链的最后一个，和上述下载的根证书对比，如果不同则验证失败
3. 验证证书链：第一个证书用第二个证书验证、第二个用第三个验证、以此类推，全都成功才算通过
4. 从第一个证书取得公钥
5. 用上一步得到的公钥验证整个JWS

库使用`com.auth0:java-jwt:3.18.2`，编程语言使用Kotlin，验证逻辑如下

```Kotlin
private val appleRootCert = PathMatchingResourcePatternResolver()
        .getResources("classpath:cert/AppleRootCA-G3.cer").first().inputStream.readBytes()

// 解码并验证时接收到的通知
fun decodeAndVerifyAppleNotification(rawNotification: String): AppleNotificationPayload {
  try {
    return JWT.decode(rawNotification)
    .apply { verifyAppleNotificationSignature(verifyAppleNotificationCertsThenReturnPublicKey(this), this) }
    .getPayload(AppleNotificationPayload::class.java)
  } catch (e: Exception) {
    throw Exception("${e.message}\nnotificationPayload: $rawNotification", e)
  }
}

private fun verifyAppleNotificationCertsThenReturnPublicKey(jwt: DecodedJWT): PublicKey {
  val certFactory = CertificateFactory.getInstance("X.509")
  val appleRootCert = certFactory.generateCertificate(ByteArrayInputStream(appleRootCert)) as X509Certificate
  val jwsCertChain = jwt.getHeaderClaim("x5c").asList(String::class.java).map {
    certFactory.generateCertificate(ByteArrayInputStream(Base64.getDecoder().decode(it)))
  }
  // 关键点1：验证根证书
  if (jwsCertChain.last() != appleRootCert) throw Exception("根证书错误")
  // 关键点2：验证证书链
  for (index in 0..jwsCertChain.size - 2) {
    jwsCertChain[index].verify(jwsCertChain[index + 1].publicKey)
  }
  // 关键点3：第一个证书的公钥即为验证整个JWS的公钥
  return jwsCertChain.first().publicKey
}

private fun verifyAppleNotificationSignature(publicKey: PublicKey, jwt: DecodedJWT) {
  // 这里做了API转换，证书用的是javax.security的API，而JWT验证用的是引入的java-jwt的API
  val keyProvider = object : ECDSAKeyProvider {
    override fun getPublicKeyById(keyId: String?): ECPublicKey {
      val keyFactory = KeyFactory.getInstance(publicKey.algorithm)
      return keyFactory.generatePublic(X509EncodedKeySpec(publicKey.encoded)) as ECPublicKey
    }

    override fun getPrivateKey(): ECPrivateKey {
      throw NotImplementedError()
    }

    override fun getPrivateKeyId(): String {
      throw NotImplementedError()
    }
  }
  JWT.require(Algorithm.ECDSA256(keyProvider)).build().verify(jwt)
}
```

> 官方文档并没有较为明确的阐述，如下两个文档可以作为参考
>
> - [X.509 数字证书的基本原理及应用](https://zhuanlan.zhihu.com/p/36832100)
>
> - [JWS X.509证书链验证](https://juejin.cn/post/7039970403770433544)

## Apple服务端点访问凭证

需要访问Apple Server的交易历史接口，而Apple Server的所有API访问时都需要携带凭证。步骤如下

1. 在App Store Connect控制台中生成并下载Private Key，步骤参考[官方文档](https://developer.apple.com/documentation/appstoreserverapi/creating_api_keys_to_use_with_the_app_store_server_api)
2. 按照[官方文档](https://developer.apple.com/documentation/appstoreserverapi/generating_tokens_for_api_requests) 指定的方式构建JWT。其实就是JWT的标准生成方式，但需要注意的是各字段的填充，**该JWT不只是访问的凭证，还有部分字段会参与查询**。遇到过一个问题：bid字段设置错误，和真实的bundleId不一致，访问交易历史接口时，响应正常，但signedTranstions字段始终是空数组，该问题阻拦了我大半天。
3. 访问时，将其放在bear token中，即添加头部 Authorization bear ${your token}

生成JWT代码如下

```kotlin
fun constructJWT4IAP(): String {
  val header: MutableMap<String, Any> = HashMap()
  header["alg"] = "ES256"
  header["kid"] = "${下载的Private Key ID}"
  header["typ"] = "JWT"

  val payload: MutableMap<String, Any> = HashMap()
  payload["iss"] = "${申请Private Key时同时生成的issuer ID}"
  payload["iat"] = DateUtils.currentSecond()
  payload["exp"] = DateUtils.currentSecondPlusMinute(${token有效期时间})
  payload["aud"] = "appstoreconnect-v1"
  payload["nonce"] = UUID.randomUUID().toString()
  payload["bid"] = "${App的Bundle ID}"

  val algorithm = Algorithm.ECDSA256(ES256KeyProviderBuilder.build(${下载的Private Key}, ${下载的Private Key ID}))
  
  return JWT.create().withIssuer(prop.jwt.issuerId)
  .withHeader(header)
  .withPayload(payload)
  .sign(algorithm)
}
```

以访问交易历史来说，在Spring Boot的RestTemplate API下的使用方式如下

```kotlin
fun listAppleTransactionHistory(appleEnv: AppleEnvironment, originalTransactionId: Long): List<AppleTransactionInfo> {
  val bearerToken = constructJWT4IAP()
  val baseUrl = when (appleEnv) {
    AppleEnvironment.Production -> BusinessConstants.APPLE_PAY_SERVER_GET_TRANSACTION_HISTORY_URL
    AppleEnvironment.Sandbox -> BusinessConstants.APPLE_PAY_SANDBOX_SERVER_GET_TRANSACTION_HISTORY_URL
  }
  val rawUrl = "${baseUrl.trimEnd('/')}/$originalTransactionId"

  val signedTransactions = mutableListOf<String>()
  var revision: String? = null
  do {
    val transactionHistoryResponse = listAppleTransactionHistory(bearerToken, rawUrl, revision)
    signedTransactions.addAll(transactionHistoryResponse.signedTransactions)
    revision = transactionHistoryResponse.revision
  } while (transactionHistoryResponse.hasMore)

  return signedTransactions.map { JwtHelper.decodeAppleTransaction(it) }.sortedBy { it.purchaseDate }
}

private fun listAppleTransactionHistory(token: String, rawUrl: String, revision: String?): GetTransactionHistoryVO {
  val url = if (revision == null) rawUrl else "$rawUrl?revision=$revision"
  val headers = org.springframework.http.HttpHeaders().apply {
    // 关键点：JWT的使用方式
    this.add("Authorization", "Bearer $token")
  }
  val entity = HttpEntity<String>(headers)
  val res = retry {
    restTemplate.exchange(url, HttpMethod.GET, entity, GetTransactionHistoryVO::class.java)
  }
  if (!res.statusCode.is2xxSuccessful) {
    logger.error("apple server 访问失败. $res")
    throw BusinessException(ResErrCode.COMM_ERROR)
  }
  return res.body!!
}
```

# 业务接入

上面描述了简单的流程，这里考虑加入业务场景——[每记APP](https://apps.apple.com/cn/app/%E6%AF%8F%E8%AE%B0/id1572586388)的自动续期订阅。简要描述值得注意的

> 广告时间：“小小日记，大大不同”，每记是一款操作简单、功能强大的日记应用，目前已迭代到2.0版本，基本功能成熟可用，未来还有更多惊喜功能等着搭建，欢迎大家加入到每记用户的大家庭。

## 需求及分析

需要增加自动续期订阅功能。需要有两种级别——普通、高级；两种周期——包月、包年。

于是在IAP中，我们需要建立四个商品，并将他们放在同一个订阅组下，设置两个优先级，普通转高级算升级；高级转普通算降级。

- 高级包月，优先级设置1
- 高级包年，优先级设置1
- 普通包月，优先级设置2
- 普通包年，优先级设置2

## 交易流程

相比上面提到的交易流程，修正如下

1. 客户端从服务端请求当前登录用户对应的appAccountToken
2. 客户端从服务端请求当前App已经在App Store Connect中配置好的商品信息
3. 客户端用上面两个信息拉起支付
4. 剩下和前面提到的流程一致

服务端和上面提到的流程一致。

## 订阅周期、扣费周期、权益周期

分析产品功能时，我们说有包年、包月；查看IAP手册，我们知道自动续期订阅有按月、按年扣费；默认情况下，我们认为这二者是相同的，称作订阅周期。实际不一样，即使它们表现得一样，也是我们主动处理的结果。我更愿意将前者称作权益周期、后者称作扣费周期。

**扣费周期**：来自IAP，开发者不可干预，一般来说时间很准，什么时候自动续期扣费，Apple说了算，我们只能被动接受通知

**权益周期**：来自APP，由开发者全权控制，我们也可以设置其开始结束时间完全和扣费周期一致（Transaction信息中purchaseDate作为周期起点，ExpireDate作为周期终点）。但实际操作时并不建议这么做

- 因为在沙盒环境下，一个月可被设置为3分钟，年也有对应缩短，意味着权益周期也会相应缩短，这样不便于测试真实日期的计算方式。而且每记是一个跨端应用，目前我们有IOS、Mac OS、Android三端应用，支付平台需要有IAP、微信、支付宝。支付服务和业务服务必须解绑，支付只负责扣费，权益发放交给业务，职责清晰。

- 当出现服务器宕机等情况，服务端未能及时处理用户续期支付成功的通知，理论上可以延迟数小时到数天不等，如果此时还按照Transaction中的过期时间作为权益周期的过期时间，则用户会凭空损失与延迟时间相等的会员权益。这样是不大好的。

而因为支付成功通知的延迟处理（多多少少都会有些延迟），可能造成权益周期比扣费周期整体延后，我称之为周期偏移。要注意到这个现象的存在。

## 可靠性考量

### 服务器宕机

如果因为服务端宕机或代码bug等原因，为能正确处理Apple Server通知，Apple Server会进行重试。重试时间分别是：在上一次尝试的基础上间隔1, 12, 24, 48, 72小时。也就是说，6天13小时后，将放弃通知重试，这期间还没能正确处理通知，将发生掉单。

此外，如果等不及通知重试，也可以主动查询交易历史进行补单。

> 注意：交易历史查询接口需要originalTransactionId作为路径参数，所以如果是丢了初次购买的交易信息，是无法补单的。

### 通知乱序

理论上通知存在乱序的可能：初次订阅，此时服务器未能正确处理交易信息，接着客户马上在设置界面升级，触发升级通知。会出现先收到升级通知，再收到初次订阅通知的情况。正确的处理方式是以升级通知的交易为准，忽略初次订阅通知。

为保证无论什么时候来通知，都能正确处理，可以在每次回调时都先查询交易历史，如果通知中的交易信息是最新的，则处理，否则忽略。

### 恢复购买

前面说，丢了初次订阅信息的单光靠服务端是找不回来的，此时需要客户端通过恢复购买操作拿到之前购买的交易信息，然后传递给服务端，服务端提取originalTransactionId再调用交易历史进行查询。

# 测试姿势

## 熟悉App Store Connect控制台

要调试IAP，必须熟悉App Store Connect控制台，这个自己上去东点西点就能熟悉了。这里提两个点

1. 添加测试用户时，电子邮件不要是已经注册过Apple ID的，否则会提示邮箱已经被使用，也不必是真实的电子邮件，不会接收验证码，在沙盒环境登录时，只需要输入电子邮件和密码即可。

   ![image-20220516143502001](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220516143502001.png)

2. 重新测试时，最好将测试账号的购买历史记录清除，这样最接近真实情况。而历史记录的清除可能需要好几分钟，因此注册多个测试账号，切换测试会比较方便。

   ![image-20220516143816984](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220516143816984.png)

3. 自动续期订阅的设置在 App - 具体App - 功能 - 订阅 中设置，而不是在App 内购买项目设置

   <img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220516144209209.png" alt="image-20220516144209209" style="zoom:80%;" />

## 沙盒环境

IAP测试阶段只能通过沙盒环境进行测试。从客户端SDK到服务端Apple Server，都有沙盒对应的版本。对客户端，它是另外的API，对服务端，它是另外的端点。对用户端，需要在手机端进行设置。

手机端登录：设置 - App Store - 沙盒账户。点击 沙盒账户 - 管理，能够进入当前App的购买项目管理界面（购买过一次后才会出现），这里可以测试左右横跳。

## 日志是个好东西

诚然，我们可以通过将Apple的通知回调URL设置为本地的内网穿透地址，但直接设到测试服地址，再将必要信息输出到日志存储系统才是长久的解决方式。对每个通知，至少需要这几样日志

- 通知的原始信息，遇到问题时候可以直接复制到本地调试
- 解析后的通知信息，方便查看通知类型
- 解析后的交易信息，方便查看交易信息

![image-20220516145506230](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20220516145506230.png)

## 测试场景列举

列举能够遇到的场景

- 订阅成功
  - 初次订阅成功
  - 到期后续订成功
  - 过期后重新订阅成功
- 订阅失败
  - 因扣款问题导致订阅失败，可在App Store Connect控制台模拟
- 订阅到期
  - 用户关闭自动续期后到期
- 订阅商品切换
  - 同等级切换
  - 低级升高级
  - 高级降低级
  - 等级恢复：先降级再升级。（先升级再降级不属于订阅恢复，因为升级马上生效，降级要本周期到期后生效）

## 无法测试的场景

退款是通过IAP售后申请，非常规渠道，无法测试。

## 测试数据demo

看IAP手册最困惑的地方就是没有真实数据作参考，这里给出一些

### 通知

- 原始信息：[iap-storekit2-notification-raw-json](https://gist.github.com/zou8944/7e223ba95c312abd95dc9bc70d171719#file-iap-storekit2-notification-raw-json-json)
- 解密信息：[iap-storekit2-notification-json](https://gist.github.com/zou8944/7e223ba95c312abd95dc9bc70d171719#file-iap-storekit2-notification-json-json)
- data.signedTransactionInfo：[iap-storekit2-notification-data-signedtransactioninfo-json](https://gist.github.com/zou8944/7e223ba95c312abd95dc9bc70d171719#file-iap-storekit2-notification-data-signedtransactioninfo-json)
- data.signedRenewalInfo：[iap-storekit2-notification-data-signedrenewalinfo-json](https://gist.github.com/zou8944/7e223ba95c312abd95dc9bc70d171719#file-iap-storekit2-notification-data-signedrenewalinfo-json)

### 交易历史

- [iap-storekit2-transaction-history-json](https://gist.github.com/zou8944/7e223ba95c312abd95dc9bc70d171719#file-iap-storekit2-transaction-history-json)

# 总结

StoreKit2说起来算是简单的，了解了以下几点，开发时才会相对顺利

- 了解基础知识：JWS、JWT、X.509证书及验证
- 正确理解交易、交易历史的概念
- 正确理解商品间相互切换时对应的订阅切换逻辑
- 熟知用户对IAP的操作入口
- 应考虑到一些关乎安全性的边缘case
- 要有明确的测试方式，如果只在本地debug不大方便
