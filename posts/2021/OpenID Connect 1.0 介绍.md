---
created_at: 2021-12-23 20:52:58
updated_at: 2021-12-23 20:52:58
slug: openid-connect-1.0-introduction
tags:
  - OpenID Connect
---

OpenID Connect 1.0是建立在OAuth 2.0上的一个身份验证机制，它允许客户端通过授权服务对用户进行认证并获取简单的用户信息。

> 前置知识：读者需要了解OAuth2.0的授权码模式和隐藏模式两种工作流程，要了解JWT、JWE、JWS等概念。这在我的前两篇文章都有详细讲解

<!--more-->

## 概览

### 名词解释

- OP：OpenID Provider，即OAuth2.0中的授权服务，用于对用户鉴权

- RP：Relying Part，依赖方，即OAuth2.0中的客户端，它从OP除获取对用户的鉴权和用户信息

- ID Token：是一个JWT，包含本次授权的基本信息。具体包含字段如下

  | 字段      | 必须？ | 说明                                                         |
  | --------- | ------ | ------------------------------------------------------------ |
  | iss       | 是     | 发布者，一个https开头的地址                                  |
  | sub       | 是     | 主体，OP对用户的唯一标识，不超过255个ASCII字符               |
  | aud       | 是     | 客户，即使用者。值为OAuth2.0协议中客户端注册的client_id      |
  | exp       | 是     | 过期时间，遵从RFC 3339协议，即epoch seconds                  |
  | iat       | 是     | 签发时间，同上                                               |
  | auth_time | 可选   | 鉴权时间                                                     |
  | nonce     |        | 随机值。两个作用<br />一是RP发送时带上，OP响应时带上，用于RP对比<br />二是防重放攻击 |
  | acr       | 可选   | Authentication Context Class Reference，暂不知义，忽略       |
  | amr       | 可选   | Authentication Methods References，暂不知义，忽略            |
  | azp       | 可选   | Authorized party，暂不知义，忽略                             |

  

### 总体流程

类似OAuth2.0，有一个总体流程和若干细分模式的流程，OpenID Connect协议总体流程为：RP发起请求 -> OP对用户鉴权并获取授权 -> OP响应RP并带上ID Token和Access Token -> RP通过访问凭证向OP请求用户信息 -> OP返回用户信息给RP

```shell
+--------+                                   +--------+
|        |                                   |        |
|        |---------(1) AuthN Request-------->|        |
|        |                                   |        |
|        |  +--------+                       |        |
|        |  |        |                       |        |
|        |  |  End-  |<--(2) AuthN & AuthZ-->|        |
|        |  |  User  |                       |        |
|   RP   |  |        |                       |   OP   |
|        |  +--------+                       |        |
|        |                                   |        |
|        |<--------(3) AuthN Response--------|        |
|        |                                   |        |
|        |---------(4) UserInfo Request----->|        |
|        |                                   |        |
|        |<--------(5) UserInfo Response-----|        |
|        |                                   |        |
+--------+                                   +--------+
```

## 客户鉴权

客户鉴权即OP对客户端进行鉴权，然后将鉴权结果返回给RP。鉴权流程有三种方式：授权码模式、隐藏模式、混合模式。如果了解OAuth2.0，对前两个模式一定不会模式，OpenID流程类似，而混合模式则是前两种模式的结合。具体OP采用什么模式，取决于RP请求时`response_type`给的值。

| response_type       | 采用的模式 |
| ------------------- | ---------- |
| code                | 授权码模式 |
| id_token            | 隐藏模式   |
| Id_token token      | 隐藏模式   |
| code id_token       | 混合模式   |
| code token          | 混合模式   |
| code id_token token | 混合模式   |

> 规律：id_token和token等同：只有id_token或/和token的使用隐藏模式，只有code的使用授权码模式i，同时存在他们的则使用混合模式

### 授权码模式

总计八个步骤

1. RP准备用于鉴权请求的参数
2. RP发送请求，给OP
3. OP对用户鉴权
4. OP手机用户的鉴权信息和授权信息
5. OP发送授权码给RP
6. RP使用授权码向一个端点换取访问凭证。协议称之为Token端点，但没说这个端点是不是由OP提供的。不过一般来说是
7. RP收到访问凭证，包含ID Token、Access Token
8. 客户端验证ID Token，并从中提取用户的唯一标识。前面说过这是一个JWT，唯一标识就是subject identifier

**授权码的请求与响应**

其中RP准备的请求参数包含OAuth2.0规定的所有字段，也包含一些额外的字段

| 参数          | 必须？ | 来自OAuth2.0？ | 说明                                                         |
| ------------- | ------ | -------------- | ------------------------------------------------------------ |
| scope         | 是     | 是             | 写死，openid                                                 |
| response_type | 是     | 是             | 写死，code                                                   |
| client_id     | 是     | 是             | RP在OP处注册得到的唯一标识                                   |
| redirect_uri  | 是     | 是             | 用于OP鉴权成功后的回调地址，RP在OP处注册时提供               |
| state         | 推荐   | 是             | 请求来回中包含的不透明值，用户防范CSRF攻击                   |
| response_mode | 否     | 是             | OP返回数据的模式                                             |
| nonce         | 否     | 否             | 会被放在ID Token的nonce字段，用于防重放攻击                  |
| display       | 否     | 否             | 定义OP通过什么方式展示用户鉴权界面<br />page：完整的网页<br />popup：弹窗<br />touch：触摸设备<br />wap："feature phone" type display |
| prompt        | 否     | 否             | 定义OP通过什么方式对用户二次鉴权<br />none：不进行二次鉴权<br />login：重新登录<br />consent：获取用户同意使用上次采集到的结果即可<br />select_account：选择用户账户 |
| max_age       | 否     | 否             | 本次鉴权的有效期。超过该时间后，OP必须对用户再次进行鉴权     |
| ui_locales    | 否     | 否             | 用户使用的区域信息                                           |
| Id_token_hint | 否     | 否             | 忽略                                                         |
| login_hint    | 否     | 否             | 忽略                                                         |
| acr_values    | 否     | 否             | 忽略                                                         |

如果授权成功，得到的返回会包含code、state等参数，举个例子

```shell
HTTP/1.1 302 Found
Location: https://client.example.org/cb?code=SplxlOBeZQQYbYS6WxSbIA&state=af0ifjsldkj
```

如果授权失败，也会有相应的错误码，具体[参考手册](https://openid.net/specs/openid-connect-core-1_0.html#toc)的3.1.2.6

**凭证的请求与响应**

这个就完全和OAuth2.0一样了。

请求上主要包含：`grant_type`写死`authorization_code`、`code`填上一步获取的授权码、`redirect_uri`填上一步的重定向地址，举个例子

```shell
POST /token HTTP/1.1
Host: server.example.com
Content-Type: application/x-www-form-urlencoded
# 你可能注意到这里有个Basic鉴权，这是因为Client也是需要被验证的
Authorization: Basic czZCaGRSa3F0MzpnWDFmQmF0M2JW

grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA&redirect_uri=https%3A%2F%2Fclient.example.org%2Fcb
```

响应上多出一个`id_token`字段，举例如下

```json
HTTP/1.1 200 OK
Content-Type: application/json
Cache-Control: no-store
Pragma: no-cache

{
  "access_token": "SlAV32hkKG",
  "token_type": "Bearer",
  "refresh_token": "8xLOxBtZp8",
  "expires_in": 3600,
  "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6IjFlOWdkazcifQ.ewogImlzc
    yI6ICJodHRwOi8vc2VydmVyLmV4YW1wbGUuY29tIiwKICJzdWIiOiAiMjQ4Mjg5
    NzYxMDAxIiwKICJhdWQiOiAiczZCaGRSa3F0MyIsCiAibm9uY2UiOiAibi0wUzZ
    fV3pBMk1qIiwKICJleHAiOiAxMzExMjgxOTcwLAogImlhdCI6IDEzMTEyODA5Nz
    AKfQ.ggW8hZ1EuVLuxNuuIJKX_V8a_OMXzR0EHR9R6jgdqrOOF4daGU96Sr_P6q
    Jp6IcmD3HP99Obi1PRs-cwh3LO-p146waJ8IhehcwL7F09JdijmBqkvPeB2T9CJ
    NqeGpe-gccMg4vfKjkM8FcGvnzZUN4_KSP0aAp1tOJ1zZwgjxqGByKHiOtX7Tpd
    QyHE5lcMiKPXfEIQILVq0pc_E2DzL7emopWoaoZTF_m0_N0YzFC6g6EJbOEoRoS
    K5hoDalrcvRYLSrQAZZKflyuVCyixEoV9GfNQC3_osjzw2PAithfubEEBLuVVk4
    XUVrWOLrLl0nx7RkKU8NXNHq-rvKMzqg"
}
```

> 在上面的每一方，比如OP收到请求、RP收到响应，都会对得到的数据进行验证，我们都忽略了，不过这里重点将RP收到ID Token后的验证逻辑列出来
>
> 1. 依据JWT协议解密该Token
> 2. iss字段必须匹配RP提前获取到的OP的issuer值
> 3. aud字段必须是RP在OP处注册时填写的client_id
> 4. 如果包含多个aud字段，则还要验证azp字段
> 5. 如果azp字段存在，则它的值必须是RP在OP处注册时填写的client_id
> 6. 如果ID Token是RP直接从OP处获取，没有走授权码这一步（比如走隐藏模式的流程），必须走JWS流程验证该JWT的签名
> 7. alg的值要么为默认的RS256，要么是RP在OP处注册时通过id_token_signed_response_alg字段指定的算法
> 8. exp所展示的时间必须比当前时间晚
> 9. iat可以用来识别签发时间过久的JWT，太久的可以拒掉，多久算久，这个取决于RP自己
> 10. nonce必须和请求授权码时对应上
> 11. acr必须和请求授权码时对应上
> 12. 接和auth_time、max_age，可以判断举例上一次时间是不是太久，从而决定是否需要重新发起鉴权请求

### 隐藏模式

这个模式就比较简单了

1. RP准备请求参数
2. RP发送请求
3. OP认证用户
4. OP获取用户的认证和授权信息
5. OP发送ID Token，可能还有Access Token给RP
6. RP验证ID Token，提取用户的标识

**请求**

请求参数和授权码模式基本一样，这里列出差别

- response_type：id_token，或者`id_token token`，差别是，如果加上token，步骤5会返回Access Token，否则就么有
- redirect_uri：处于安全考虑，这个地方必须使用HTTPS传输
- nonce：这个变成了必须的

**响应**

给个例子就好了

```shell
HTTP/1.1 302 Found
Location: https://client.example.org/cb#
  access_token=SlAV32hkKG
  &token_type=bearer
  &id_token=eyJ0 ... NiJ9.eyJ1c ... I6IjIifX0.DeWt4Qu ... ZXso
  &expires_in=3600
  &state=af0ifjsldkj
```

> 与前面不同的是，这里会多一个Access Token的验证，它要结合ID Token中的at_hash字段验证
> 
> - 使用ID Token中头部alg字段指定的算法对Access Token进行哈希
> - 对哈希值进行base64url编码，取左半边
> - 上一步得到的值必须和ID Token中的at_hash字段指定的值匹配
>

### 混合模式

1. RP准备请求
2. RP发送请求给OP
3. OP对用户鉴权
4. OP采集用户的鉴权和授权信息
5. OP发送给RP授权码，同时根据请求时指定的`response_type`，发送额外的参数
6. RP通过授权码向OP请求
7. RP从OP处得到ID Token和Access Token
8. RP验证ID Token，解析用户的唯一标识

**授权码请求**

混合模式在response_type上做文章，允许的值包括：`code id_token`、`code token`、`code id_token token`。可以看出，在授权码请求这一步，可能会返回授权码、ID Token、Access Token。下面是一个返回授权码和ID Token的例子

```shell
HTTP/1.1 302 Found
Location: https://client.example.org/cb#
code=SplxlOBeZQQYbYS6WxSbIA
&id_token=eyJ0 ... NiJ9.eyJ1c ... I6IjIifX0.DeWt4Qu ... ZXso
&state=af0ifjsldkj
```

> 如果返回值有ID Token，它会包含授权码的签名，对应其c_hash字段，计算方式和隐藏模式的Access Token验证差不多。

至此，混合模式看起来很奇怪，体现在两处

- ID Token既能在授权码请求时返回，也能在Access Token请求时返回
- Access Token也有上面的情况

这样做有什么意义呢？

### 小结

ID Token的意义，主要在于以安全的方式分发用户的唯一标识，Access Token才是用来作为访问凭证的。

## 获取用户信息

上面介绍了获取访问凭证之前的动作，这里介绍使用访问凭证访问ID Token指定的用户的信息的问题。

### 能获得什么

获得的内容和请求访问凭证时传的scope有关，具体如下。

| 字段                  | scope   | 说明                                                       |
| --------------------- | ------- | ---------------------------------------------------------- |
| sub                   | -       | 唯一标识，对应JWT的sub                                     |
| name                  | profile | 用户全名                                                   |
| given_name            | profile | 名                                                         |
| family_name           | profile | 姓                                                         |
| middle_name           | profile | 中间名，这个某些文化有关                                   |
| nickname              | profile | 昵称                                                       |
| perferred_username    | profile | 用户希望展示给RP的名字                                     |
| profile               | profile | 用户的概览信息的页面URI                                    |
| picture               | profile | 用户图片的URI                                              |
| website               | profile | 用户的网站或者博客URI                                      |
| email                 | email   | 用户邮箱                                                   |
| email_verified        | email   | 邮箱是否通过验证。如果没有，这可能是用户随便填写的一个邮箱 |
| gender                | profile | 性别                                                       |
| birthdate             | profile | 生日                                                       |
| zoneinfo              | profile | 用户所处时区信息                                           |
| locale                | profile | 用户所处地域，语言环境                                     |
| phone_number          | phone   | 电话号码                                                   |
| phone_number_verified | phone   | 电话号码是否通过验证                                       |
| address               | address | 地址，这是一个JSON对象                                     |
| updated_at            | profile | 用户的这些信息最后一次被更新的时间，epoch seconds          |

> scope可以指定多个值，得到的结果就是并集。比如`scope=profile email phone address`

一个成功的例子

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "sub": "248289761001",
  "name": "Jane Doe",
  "given_name": "Jane",
  "family_name": "Doe",
  "preferred_username": "j.doe",
  "email": "janedoe@example.com",
  "picture": "http://example.com/janedoe/me.jpg"
}
```

### 另类获取信息的方式 - claims

可以在请求时加上claims参数，指定能够从用户信息端点或者在ID Token中包含什么信息，它是一个类似json schema的东西，如下是例子：要求给的字段，以及字段是否必要。

```json
{
  "userinfo":
  {
    "given_name": {"essential": true},
    "nickname": null,
    "email": {"essential": true},
    "email_verified": {"essential": true},
    "picture": null,
    "http://example.info/claims/groups": null
  },
  "id_token":
  {
    "auth_time": {"essential": true},
    "acr": {"values": ["urn:mace:incommon:iap:silver"] }
  }
}
```

## 总结

理解了OAuth2.0的工作流程，再理解OpenID Connect就很容易了，相较而言，它的特点如下

- OP = 授权服务+资源服务，资源服务的唯一作用就是分发用户信息
- 规定了用户信息包含的内容
- Token响应中多了ID Token，它用来指定用户ID，以便在访问用户信息时作为标识
- ID Token使用了JWT
- 多了混合模式











