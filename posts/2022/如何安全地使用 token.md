---
created_at: 2022-08-10 11:26:55
updated_at: 2022-08-10 11:26:55
slug: how-to-use-token-safely
tags:
- Token
- 安全
---

通常在带有登录功能的业务中，我们会向用户（客户端）发放访问凭证，往后一段时间，用户持该凭证即可在应用内畅行。不同应用可能有不同的名字：access_token、token、xxxid，也可能有不同的形式：不透明字符串、JWT等。本文讨论访问凭证的安全性。

<!--more-->

考虑到一般发放JWT的系统都将其当做无状态token使用，不适用本文讨论范文，故忽略。

# 原则

总的说来，应该在如下两方面做好

- 用户体验：登录操作成本很高，不能经常让用户重新登录，会劝退。最离线的情况是：正常用户永远能够正常使用
- 安全性：token不能丢，即使丢失，风险也应当可空

分别讨论

## 用户体验

两种方式可使得用户免于重新登录

- 发放一个永不过期的token
- 发放一个短期的token，到期后主动刷新token，效果和永久token一致

## Token安全性

风控系统将防御分为事前、事中、事后。类似地，我们可以套用

- 事前：如何防御token不丢失
- 事后：token丢失后如何使得损失最小

### 不丢Token

- 防中间人：HTTPS协议、客户端屏蔽代理、客户端预埋证书
- 防XSS：web将token放在Cookie并添加httpOnly和Secure属性，防XSS导致的token泄露
- 防CSRF：csrf token

### Token丢失后止损

如果token丢失，**短时间内造成的损失不可挽回，只能考虑如何止损**

- 尽快让token失效，有几种方式，可以叠加使用
  - token过期机制：token限制有效期，过期自动失效
  - token失活机制：超过n天未使用的token主动失效
  - token滚动机制：如果用户通过登录或刷新触发了新token的生成，则之前的token设为无效。
  - token驱逐机制：提供交互让用户选择主动驱逐token
- 限制token的使用环境
  - 将token和用户使用环境绑定起来，验证token时同步验证环境。稳定可用可获取的环境包括
    - 设备型号：永远不会变
    - 操作系统版本：只会升级，不会降级
    - app版本：只会升级，不会降级
    - 设备ID：至少单次会话期间是稳定的
- token使用行为监测，分析出敏感操作

# 讨论

## 为什么大公司可以发长期token?

我们常用的Google、Bilibili、微博等网站和应用，似乎登录一次就再也不需要登录，通过抓包的方式去查看它们的访问凭证，会怀疑它们很可能发放了一个长期有效的凭证，按上面的分析，长期的token一旦丢失将造成无可挽回的损失，这样岂不是很不安全？原因主要还是他们有自己的风控系统，能够根据用户使用环境、行为习惯识别风险，采取主动失效、通知用户等操作及时止损。

一篇文章自觉不错：[这里](https://www.linkedin.com/pulse/why-your-app-needs-short-session-timeout-google-facebook-geoff-wilson)

## refresh_token如何？

大公司有风控系统，有足够的底气发长时token，小公司没有风控系统，发长时token无异于作死，看起来token刷新是一个不错的办法。

access_token + refres_token的组合很多人都熟悉，知道它大多源自OAuth2协议，前者用于访问，后者用于刷新得到新的token。Auth0在refresh_token上又增加了令牌轮换和重用检测机制保障刷新操作的安全

- 令牌轮换：执行token刷新后，原refresh_token会失效，换发新的refresh_token，减轻了refresh_token泄露的风险
- 重用检测：当检测到已经被用过的refresh_token刷新操作时，说明refresh_token已经泄露，此时服务将所有access_token和refresh_token都失效，强制用户重新登录，进一步保证了refresh_token的安全性

参考文档

- [OAuth2](https://www.rfc-editor.org/rfc/rfc6749)
- [Auth0](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/)

> 没有令牌轮换和重用检测的refresh_token机制是不安全的。一种说法是refresh_token传输频率较低，所以安全，但在当前HTTPS标配的情况下，中间人攻击已不容易，诚然降低的传输频率会增加一点安全性，但没有本质的变化，相对鸡肋。

# 方案

提一个适用于仅在用户系统中保障token安全性的方案，主要包含如下几个部分

- 简单的风控：token验证时同时验证设备型号、操作系统（可从UA获取）、设备ID，如不一致说明token可能丢失
- 短期的token：token有效期两个小时（根据需求自定义）
- token刷新
  - access_token和refresh_token都是一个token，不引入refresh_token：token有过期时间，也有刷新的过期时间
  - 令牌轮换：token刷新后，将换发新的token，且原token不能再用于刷新
  - 重用检测：当检测到已经被用于刷新的token再次执行刷新操作，将所有token都失效，强制用户重新登录
- token活动检测机制：记录token访问时间，如果token超过x天未访问，将自动过期，强制用户重新登录
