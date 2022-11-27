---
created_at: 2020-03-28 20:41:32.0
updated_at: 2021-02-16 23:22:07.482
slug: backend-develop-about-sign-in-with-apple
tags: 
- Sign In with Apple
---

本周新做一个需求，为IOS APP接入苹果第三方登录。查看官方文档，发现其在IOS端操作描述是非常细致的，但在用户服务端的讲解实在是不知所云，让人头大。只能借助广大网友的智慧。本文并非完全原创，因为无论概念解读，还是操作方式，都是从各个文章处抄来的。本文最大的作用，在于针对自己和团队内部的开发记录，防止多次踩坑。

Sign in with Apple，对IOS和其它平台的处理方式是有很大差别的。本文只针对IOS平台，其它平台可以参考[这篇文章](https://sarunw.com/posts/sign-in-with-apple-4/)，说得非常详细

<!-- more -->

# 说明

本文主要以官方文档为主线，辅以自己的理解。依赖于[Sign in with Apple REST API](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api)页面，其分为两部分

- 用户授权和验证 - Authentication and Verification of Users

- 获取公钥和生成&验证token的API介绍

IOS上的苹果登录与一般的第三方登录最大的区别，在于IOS在客户端已经获取了必要的用户信息，以加密的形式发送给服务端，服务端需要做的验证并应用即可；而一般的第三方登录流程是需要在服务端请求用户信息的。秉持这一基础认识很重要，否则会云里雾里。

# 客户端

该部分对应 [Authenticating Users with Sign in with Apple](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple)

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/notes/image-20210216221623082.png" style="zoom:150%;" />

客户端授权流程如上主要有如下几步

1. 调用API发起授权请求
2. 设备弹出授权框，请求用户授权
3. 用户授权成功，API调用Apple ID 服务，请求用户信息
4. 请求成功，Apple ID服务以返回三个字段：identity token、authorization code、user identifier

## identity token

identity token是一个JWT，使用解析工具解开后如下，包含了基本的用户信息。

```json
{
     kid: "86D88Kf",
     alg: "RS256"
}.
{
     iss: "https://appleid.apple.com",
     aud: "com.mampod.enlighten",
     exp: 1585110701,
     iat: 1585110101,
     sub: "001230.15f855de99ef4b788a18d18b7b45b053.0400",
     nonce: "123",
     c_hash: "lGYaArOB6z6IFuCOx2Z64A",
     email: "d6yuqtqhv3@privaterelay.appleid.com",
     email_verified: "true",
     is_private_email: "true",
     auth_time: 1585110101,
     nonce_supported: true
}.
[signature]
```

每个字段解读如下

头部：

kid: key id，在token验证时用于选取公钥的ID

alg: algorithm，算法

载荷部分：

- iss: isser的缩写，即JWT发布人
- aud: audience的缩写，客户，对应APP的开发者。对应Apple开发者账户中的client_id
- exp: expire的缩写，即过期时间
- iat: issue at的缩写，即该token的发布时间
- sub: subject，即加密对象，这是关键，**它是用户的唯一标识符，很重要**。
- nonce: 即随机字符串。用于绑定客户端会话和token的字符串值，用于防止重复攻击。
- nonce_supported: 指示对待nonce的方式
  - true: 如果授权请求时有给nonce，但返回的token不含nonce，则说明此次请求失败
  - false: 不支持nonce，忽略nonce
- c_hash: authorizationCode的hash值，用于验证authorizationCode
- email: 用户邮箱
- email_verified: 邮箱是否经过验证，总是为true
- is_private_email:  是否是加密邮箱，即上面说的xxx@privaterelay.appleid.com
- auth_time: 请求授权的时间

## authorization code

authorization code用于和Apple ID服务交互，这里暂时用不到，忽略。

## user identifier

JWT中的sub字段，对应了用户唯一标识符，即identifier，它具有如下特性

- 唯一且稳定
- 同一个苹果开发账户的所有APP对应的同一个用户的identifier是唯一的
- 不同的开发账户的APP对应一个用户的不同identifier
- 对于用户从APP注销，再登录，identifier是不会变的
- 可以用于唯一标示用户，即应该用它而不是邮箱嵌入我们的业务数据库

## Private email

授权时，用户可以选择隐藏真是邮箱，于是我们会获取到一个xxx@privaterelay.appleid.com格式的用户邮箱，该邮箱具有一定限制

- 邮箱具有全局唯一性
- 发往该邮箱的信息将会被转发到真实的用户邮箱
- 对于同一个开发者的所有APP，一个用户对应一个邮箱；对于不同开发这的不同APP，一个用户对应多个邮箱
- 该邮箱一旦生成，会一直生效，无论用户是否有登录你的APP，或已经删除APP
- 要想向该邮箱发送信息，需要在Apple注册发送邮箱的邮箱域名，否则不会发送成功。

## 客户端最后一步

为了将用户与我方APP服务端用户系统绑定，需要将上面获取的的identity token、authorization code、user identifier等信息发送APP服务端。

# 服务端

这部分对应 [Verifying a User](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/verifying_a_user)，也是最令人头大的一部分。相同地，他也提供了一个流程图，描述如何使用authorization code换取用户信息和refresh token。对IOS登录的后台验证毫无帮助，相反会起到混淆视听的作用。请直接忽略。

对于IOS登录，由于IOS客户端已经通过客户端API获取了必要的用户信息：唯一标识符、name、email等，我们已经没有必要再次获取这些信息，只需要验证他们的真实性即可。

而对于其它平台的登录，如果你觉得看不懂这里的文档，强烈建议你按照这篇文章的方式操作——[Sign in with Apple Tutorial, Part 4: Web and Other Platforms](https://sarunw.com/posts/sign-in-with-apple-4/)

## 验证identity token

identity token的签名是Apple ID服务使用私钥加密的，需要从[这里](https://appleid.apple.com/auth/keys)获取公钥解密验证。取得的公钥以JWKS的形式呈现，如下。

```json
{
    "keys": [
    {
        "kty": "RSA",
        "kid": "86D88Kf",
        "use": "sig",
        "alg": "RS256",
        "n": "iGaLqP6y-SJCCBq5Hv6pGDbG_SQ11MNjH7rWHcCFYz4hGwHC4lcSurTlV8u3avoVNM8jXevG1Iu1SY11qInqUvjJur--hghr1b56OPJu6H1iKulSxGjEIyDP6c5BdE1uwprYyr4IO9th8fOwCPygjLFrh44XEGbDIFeImwvBAGOhmMB2AD1n1KviyNsH0bEB7phQtiLk-ILjv1bORSRl8AK677-1T8isGfHKXGZ_ZGtStDe7Lu0Ihp8zoUt59kx2o9uWpROkzF56ypresiIl4WprClRCjz8x6cPZXU2qNWhu71TQvUFwvIvbkE1oYaJMb0jcOTmBRZA2QuYw-zHLwQ",
        "e": "AQAB"
    },
    {
        "kty": "RSA",
        "kid": "eXaunmL",
        "use": "sig",
        "alg": "RS256",
        "n": "4dGQ7bQK8LgILOdLsYzfZjkEAoQeVC_aqyc8GC6RX7dq_KvRAQAWPvkam8VQv4GK5T4ogklEKEvj5ISBamdDNq1n52TpxQwI2EqxSk7I9fKPKhRt4F8-2yETlYvye-2s6NeWJim0KBtOVrk0gWvEDgd6WOqJl_yt5WBISvILNyVg1qAAM8JeX6dRPosahRVDjA52G2X-Tip84wqwyRpUlq2ybzcLh3zyhCitBOebiRWDQfG26EH9lTlJhll-p_Dg8vAXxJLIJ4SNLcqgFeZe4OfHLgdzMvxXZJnPp_VgmkcpUdRotazKZumj6dBPcXI_XID4Z4Z3OM1KrZPJNdUhxw",
        "e": "AQAB"
    }
    ]
}
```

公钥不止一个，需要取kid字段与JWT头部的kid字段匹配的那个。

这里我们使用了使用人数较多的库[java-jwt](https://github.com/auth0/java-jwt)、[jwks-rsa-java](https://github.com/auth0/jwks-rsa-java)。

```scala
val jwt = JWT.decode(/*客户端上传的JWT*/)
val jwk = new UrlJwkProvider("https://appleid.apple.com/auth/keys").get(jwt.getKeyId)
val algorithm = Algorithm.RSA256(jwk.getPublicKey.asInstanceOf[RSAPublicKey], null)
Try {
    algorithm.verify()
} match {
    case Success(_) => // 验证通过
    case Failure(e) => // 验证不通过
}
```

## 验证其它内容

根据官方手册，总计需要验证如下内容

- 使用公钥验证JWT签名，上一步已验证
- 验证nonce，可选，这里不验证
- 验证iss，必须为apple签发，即必须包含https://appleid.apple.com字符串
- 验证aud，必须为开发者账户的client_id
- 验证exp，即过期时间

使用现成库的好处之一是可以直接获取JWT的标准字段，如下

```scala
Try {
    assert(jwt.getAudience.get(0) == clientId, "aud incorrect")
    assert(jwt.getIssuer.contains("https://appleid.apple.com"), "iss must contains https://appleid.apple.com")
    assert(jwt.getSubject == request.identifier, "identifier invalid")
    assert(jwt.getExpiresAt.getTime > System.currentTimeMillis(), "Identity token expired")
} match {
    case Success(_) =>  // 验证通过
    case Failure(e) => // 验证不通过
}
```

## 优化 - 缓存Algorithm实例

上述验证步骤中，在获取公钥和构建Algorithm实例时耗费较长时间——超过1秒

```scala
val jwk = new UrlJwkProvider("https://appleid.apple.com/auth/keys").get(jwt.getKeyId)
val algorithm = Algorithm.RSA256(jwk.getPublicKey.asInstanceOf[RSAPublicKey], null)
```

为了加快响应速度，可以缓存Algorithm实例，但由于apple提供的公钥可能变化，因此需要使用一定的策略兼顾效率和正确性。

实际操作如下

```scala
def verifySignature(force: Boolean = false) = {
    if (force) jwkCache.remove(jwt.getKeyId)
    jwkCache.get(jwt.getKeyId, () => {
        val jwk = new UrlJwkProvider("https://appleid.apple.com/auth/keys").get(jwt.getKeyId)
        Algorithm.RSA256(jwk.getPublicKey.asInstanceOf[RSAPublicKey], null)
    }).map(algorithm => Try {
        algorithm.verify(jwt)
    } match {
        case Success(_) => Unit
        case Failure(e) => Future.failed(e)
    })
}

verifySignature()
.recoverWith[Any] { case _: Throwable => verifySignature(force = true) }
```

# 总结

相对于传统第三方登录，IOS的登录流程略有不同

## 一般流程

客户端

- 用户被导入登录服务提供商，如微信、支付宝等
- 用户扫码或输入账号密码授权
- 服务提供商将用户重定向回客户端，并附带token
- 客户端凭借该token进行登录

服务端

- 应用服务端凭借该token向服务提供商验证登录真实性并获取用户信息
- 使用获取到的用户信息绑定自建的用户系统

## IOS登录流程

客户端

- IOS客户端上弹出授权框
- 用户刷脸授权
- Apple同样将用户重定向回应用，附带token，但同时使用客户端API想Apple Server获取用户信息，以JWT形式提供
- 客户端将JWT发送给应用服务端

服务端

- 验证JWT
- 使用JWT附带的用户信息绑定自建的用户系统

可以看到，其最主要的不同还是在于IOS客户端已经获取了用户信息，在服务端仅需要验证JWT即可，与一般流程相比，IOS登录的应用后端少了一步请求用户信息的步骤。

## 没涉及的部分

文章到这里也只介绍了在IOS客户端接入Sign in with apple的后端操作步骤，并没有设计到IOS之外平台的处理方式，对此，可以参考[这篇文章](https://sarunw.com/posts/sign-in-with-apple-4/)，它有很好的讲解。

# 更多

关于更多授权相关知识，这里列举了一些学习资源

- [Oauth](https://oauth.net/2/)
- [OpenID Connect](https://openid.net/connect/)
- [JWT](https://jwt.io/introduction/)
- [JWK](https://self-issued.info/docs/draft-ietf-jose-json-web-key.html)

# 参考文档

1. [Authenticating Users with Sign in with Apple](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple)
2. [Verifying a User](https://developer.apple.com/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/verifying_a_user)

3. [Fetch Apple's public key for verifying token signature](https://developer.apple.com/documentation/sign_in_with_apple/fetch_apple_s_public_key_for_verifying_token_signature)

4. [iOS 13 苹果账号登陆与后台验证相关](https://juejin.im/post/5d551d11e51d4561cf15dfae#heading-15)
5. [Sign in with Apple Tutorial, Part 3: Backend – Token verification](https://sarunw.com/posts/sign-in-with-apple-3/)