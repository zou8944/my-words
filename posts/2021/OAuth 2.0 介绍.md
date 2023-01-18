---
created_at: 2021-12-23 19:48:39
updated_at: 2021-12-23 19:48:39
slug: oauth-2.0-introduction
tags:
  - OAuth2.0
---

本文深入OAuth2.0协议，以及基于其上的OpenID Connect身份认证协议。前者解决授权第三方服务访问资源的问题；后者解决身份认证的问题。主要资料来源是官方协议手册：[RFC6749](https://www.rfc-editor.org/rfc/pdfrfc/rfc6749.txt.pdf)、[OpenID Connect Specification](https://openid.net/specs/openid-connect-core-1_0.html)。

当然还有更多其它说的好的第三方资源，比如[阮一峰这个](https://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)，它的优点是只针对协议讲解，没有举那些无助于理解的复杂例子。

<!--more-->

> 考虑到文章的长度，OpenID Connect移到下篇文章再说

OAuth2.0解决了授权的问题。在只有客户端和资源服务器的简单架构中，资源服务器仅有简单的权限验证功能，如果一个用户想要授权第三方客户端访问自己位于资源服务器上的资源，能够做的方式唯有提供自己的账号密码。这样无疑会有很大问题

- 首先账号密码是不安全的
- 其次由于资源服务器没有复杂的权限验证功能，因此无法实现权限的精细化控制，被授权方能够很容易地获取过大的权力
- 并且账号密码是全局的，收回权限的方式是改密码，但是改密码会影响到所有使用该账号密码的用户及第三方服务

OAuth就是为了解决该问题被提出，它引入一个授权层，即将权限管理独立出来，专门管理。目前OAuth最新版为2.0，2.0与1.0不兼容。授权层的作用是经过用户同意后，向第三方发放权限受限的访问凭证，即access token，该凭证约束了访问范围、生命周期（即过期时间）等。

协议规定了参与角色、各方之间交流的模式、凭证的规范等。

# 参与方

传统的授权，只有三个参与方：用户（资源所有者）、资源服务、客户端（第三方服务）。OAuth2.0增加了授权服务，总计四个参与方。其中，资源服务和授权服务只是逻辑上的独立概念，实现上他们可以是一个，即一个服务同时扮演授权鉴权和资源分发的角色。

这其中尤其需要注意客户端。

- 定义了两种客户端：可信的、公开的。前者能够自己保护密码，如后端应用；后者不能，如前端应用
- 客户端可能由不同部分组成，如一个客户端同时拥有前端和后端

# 工作模式

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211221222733051.png" alt="image-20211221222733051" style="zoom:80%;" />

协议的通用工作模式总体来说如上图，分为三个步骤

- 客户端向用户请求授权凭证（Authorization Grant）
- 客户端使用得到的授权凭证向授权服务器请求访问凭证
- 客户端使用访问凭证访问最终的资源

在获取access token之后的逻辑都是一样的，但获取access token的实际应用情况有很多种，具体分成了四种具体的工作模式

- 授权码模式（Authorization Code）：最常用的，安全性最高。适合在客户端有后端服务的情况，前端只能够接触到授权码，后端存储access token。
- 隐藏(授权码)模式（Implicit）：适用于客户端只有前端的情况。只有前端，就不需要中间凭证（授权码）了。
- 用户密码模式（Resource Owner Password Credentials）：客户端直接使用用户的账号密码向服务器要access token，前两者不可用时，用它
- 客户端凭证模式（Client Credentials）：客户端自己向授权服务器索要，用户不参与，不知道这种模式存在的意义，我们忽略

## 授权码模式

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211222212026728.png" alt="image-20211222212026728" style="zoom:67%;" />

该模式流程图如上，大家可以联想平时自己在第三方网站上如何通过微信授权登录的

- A: 客户端将用户的UA导向**授权端点**，授权端点由授权服务器提供；导向授权端点时，客户端会带上自己的标识、请求的范围、自定义状态以及一个用于授权完成后充定向的地址

  该步骤客户端向授权服务发出的请求包含参数

  | 字段          | 是否必须 | 说明                                               |
  | ------------- | -------- | -------------------------------------------------- |
  | response_type | 必须     | 写死 code                                          |
  | client_id     | 必须     | 客户端唯一标识，需要提前在授权服务器注册           |
  | redirect_uri  | 可选     | 重定向地址                                         |
  | scope         | 可选     | 请求授权的范围                                     |
  | state         | 推荐要有 | 一个不透明的值，用于在回调时进行比对，防止跨域攻击 |

  举例

  ```shell
  GET /authorize?response_type=code&client_id=s6BhdRkqt3&state=xyz&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb HTTP/1.1
  Host: server.example.com
  ```

- B: 授权服务器通过UA对用户进行验证，并确认用户是否同意授权给客户端。可能的方式是授权服务将上述接口重定向到自己提供的用户登录页，用户登录确认后再将信息收集到授权服务，这个操作由授权服务自己完成，所以都归在了这个步骤中。

- C: 如果用户同意授权，授权服务器将用户的UA重定向回客户端，依据的URI是A步骤给的。重定向的URI会将授权码带在参数，同时带上的还有A步骤给的自定义状态

  重定向UA时，带的参数如下

  | 字段  | 说明                       |
  | ----- | -------------------------- |
  | code  | 授权码，Authorization Code |
  | state | 步骤A有时，这就会有        |

  举例

  ```shell
  HTTP/1.1 302 Found
  Location: https://client.example.com/cb?code=SplxlOBeZQQYbYS6WxSbIA&state=xyz
  ```

- D: 客户端使用C步骤得到的授权码、A步骤提供的重定向地址，向**token发放端点**换取access token

  该步骤的请求参数如下

  | 字段         | 是否必须 | 说明                    |
  | ------------ | -------- | ----------------------- |
  | grant_type   | 必须     | 写死 authorization_code |
  | code         | 必须     | C步骤得到的授权码       |
  | redirect_uri | 必须     | 和A步骤给的参数一样     |
  | client_id    | 必须     | 客户端标识              |

  举例

  ```shell
  POST /token HTTP/1.1
  Host: server.example.com
  Content-Type: application/x-www-form-urlencoded
  
  grant_type=authorization_code&code=SplxlOBeZQQYbYS6WxSbIA&redirect_uri=https%3A%2F%2Fclient%2Eexample%2Ecom%2Fcb
  ```

- E: 授权服务器对收到的授权码进行验证，比对收到的重定向地址和A步骤给的是否一致，如果通过，则发放access token，并且可选地发放refresh token

  这个响应包含的参数如下

  | 字段          | 说明                                                         |
  | ------------- | ------------------------------------------------------------ |
  | access_token  | 即发放的访问凭证                                             |
  | token_type    | token的类型，只有在客户端理解了token的类型后才能正确使用<br />比如bearer、mac等，一般由授权服务器指定 |
  | expires_in    | token过期时间                                                |
  | refresh_token | 用来换取新access_token的token                                |
  | scope         | 如果响应的scope和A步骤请求的scope一致，则可给可不给，否则，一定要给 |

  举例

  ```shell
  HTTP/1.1 200 OK
  Content-Type: application/json;charset=UTF-8
  Cache-Control: no-store
  Pragma: no-cache
  {
    "access_token":"2YotnFZFEjr1zCsicMWpAA",
    "token_type":"example",
    "expires_in":3600,
    "refresh_token":"tGzv3JOkF0XG5Qx2TlKWIA",
    "example_parameter":"example_value"
  }
  ```

**等等，上面几个步骤看起来很奇怪不是吗？为什么要向客户端发送授权码，客户端再用授权码去更换访问凭证？而不是直接发访问凭证，**不是多此一举吗？

其实上面的D步骤有一点没说，即在兑换access token时，要求授权服务对客户端进行鉴权，即保证客户端是可信的。而实际应用中保证可信的方式是前后端分离，即客户端由前端和后端组成，授权码发给前端，前端再将授权码传给自己的后端，后端再用来兑换access_token并保存。前端暴露在UA中，不可信，因此授权码一般生命周期很短，以微信为例，只能使用一次；后端可信，因此能够持有最终的access_token。这样看，authorization code和access token分开发就不多余了。

如果并没有分前后端，authorization code + access token的方式确实多此一举，因此针对这种情况，把授权码去掉了，就有了隐藏授权码模式。

## 隐藏(授权码)模式

这种模式经常只用在只有纯客户端的情况。其流程如下

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211222221933160.png" alt="image-20211222221933160" style="zoom:67%;" />

- A：客户端将用户导向授权端点，导入时带上客户端标识、scope、state、重定向URI

  请求包含的参数

  | 字段          | 是否必须 | 说明                                               |
  | ------------- | -------- | -------------------------------------------------- |
  | response_type | 必须     | 写死 token                                         |
  | client_id     | 必须     | 客户端唯一标识，需要提前在授权服务器注册           |
  | redirect_uri  | 可选     | 重定向地址                                         |
  | scope         | 可选     | 请求授权的范围                                     |
  | state         | 推荐要有 | 一个不透明的值，用于在回调时进行比对，防止跨域攻击 |

- B：授权服务器通过UA对用户进行验证，并确认用户是否同意授权给客户端。

- C：如果用户同意，在重定向回客户端，在URI中带上access token，注意四在URI中带，而不是在参数中。

  响应包含的参数

  | 字段          | 说明                                                         |
  | ------------- | ------------------------------------------------------------ |
  | access_token  | 即发放的访问凭证                                             |
  | token_type    | token的类型，只有在客户端理解了token的类型后才能正确使用<br />比如bearer、mac等，一般由授权服务器指定 |
  | expires_in    | token过期时间                                                |
  | refresh_token | 用来换取新access_token的token                                |
  | scope         | 如果响应的scope和A步骤请求的scope一致，则可给可不给，否则，一定要给 |

  举例

  ```shell
  HTTP/1.1 302 Found
  Location: http://example.com/cb#access_token=2YotnFZFEjr1zCsicMWpAA&state=xyz&token_type=example&expires_in=3600
  ```

- D：UA将访问凭证存在本地，然后向客户端方的资源服务器请求

- E：资源服务器响应一个能够从URI中解析出访问凭证的脚本

- F：UA执行该脚本，提取出访问凭证

- G：将访问平衡提供给客户端

> 可以看到，隐藏模式相比授权码模式，有两处改动：省掉了授权码；增加了获取解析访问凭证的脚本的步骤
>
> 不过，这种模式并没有见过实际应用，所以不大能理解。尤其是步骤D\E请求获取凭证的脚本那一步，并看不出必要性在哪里。

## 用户密码模式

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211222230023551.png" alt="image-20211222230023551" style="zoom:67%;" />

- A：用户向客户端提供用户名和密码
- B：客户端使用得到的用户名和密码向授权服务发起请求，同时带上自己的访问凭证
- C：授权服务对客户端进行鉴权，同时验证用户的用户名和密码，如果通过，则发放access token

这种情况下，用户要非常信任客户端才可以。

# 关于Refresh Token

为什么有了Access Token，还要Refresh Token？如果发放Refresh Token，岂不是用户可以拥有永不过期的访问凭证？这样安全吗？

协议上只规定了两个点

- Refresh Token由授权服务器颁发给客户端，用于在当前Access Token失效或过期时获取新的访问令牌，或者获取具有相同或更窄范围的附加访问令牌。
- Refresh Token是可选的

我想，可以从两方面理解

- 首先是用户体验，Access Token有效期一般不会特别长，过期时，有两种方式重新获得它：再执行一次授权逻辑；或提供一种能够直接获取Access Token的方式，即Refresh Token。前者会影响用户体验，后者肯定更好。
- 其次是安全性，同样是Token，Access Token和Refresh Token泄露带来的风险其实差不了太多，泄露后都丧失了对资源的保护；唯一的差别是Refresh Token的有效期会更长。但是一旦检测到凭证丢失，授权服务都能使他们失效。而且我们可以通过刷新时撤销Refresh Token的方式检测丢失

# 安全考量

- 授权码、访问凭证的传输必须走HTTPS

- 授权码阶段的防范

  - 防止篡改RedirectURI，篡改重定向地址可以让授权服务把授权码导向其它地址，因此授权服务需要在客户端注册时指定RedirectURI，后续步骤需要比对
  - 授权码可能丢失，因此必须是短失效的。并且，授权服务在发放授权码时需要对客户端进行认证
  - 隐藏模式中，访问凭证放在URI中，可能泄露出去，使用时要注意

- 访问凭证发放阶段的防范

  - 授权服务器处理来自客户端的scope请求时，需要根据客户端的可信程度决定是否采纳其scope请求建议

  - 访问凭证和刷新凭证需要无规律，不可推测

  - 授权服务器处理来自客户端的scope请求时，需要根据客户端的可信程度决定是否采纳其scope请求建议

  - Refresh Token很重要，授权服务只能发放给跑在后端的服务和Native应用，如IOS应用。基于浏览器的应用不能签发

    并且，它只能在客户端和授权服务之间流通，不能放到别处

  - Refresh Token的撤销，可以在刷新Token时同时撤销原来的Refresh Token，这样如果Refresh Token泄露并且被用过一次，则正常用户的Refresh Token会失效报错，就能识别到该系列的Refresh Token失效。

- 防止CSRF攻击，授权请求时携带state参数，可以防止跨域攻击

- 防范钓鱼攻击，这个就只能加强用户教育了
