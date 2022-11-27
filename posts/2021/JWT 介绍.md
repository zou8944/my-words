---
created_at: 2021-12-20 19:48:39
updated_at: 2021-12-20 19:48:39
slug: jwt-introduction
---

本文介绍JWT组成原理及适用范围。

<!--more-->

## 概览

JWT，全称JSON Web Token，是一种包含信息的Token，相较于普通的Token，唯一多的内容是：包含部分信息。与JWT相关的协议比较简单，但数量较多，本文只是对此加以总结。

- JWS-[rfc7515](https://www.rfc-editor.org/rfc/pdfrfc/rfc7515.txt.pdf)
- JWE-[rfc7516](https://www.rfc-editor.org/rfc/pdfrfc/rfc7516.txt.pdf)
- JWK-[rfc7517](https://www.rfc-editor.org/rfc/pdfrfc/rfc7517.txt.pdf)
- JWA-[rfc7518](https://www.rfc-editor.org/rfc/pdfrfc/rfc7518.txt.pdf)
- JWT-[rfc7519](https://www.rfc-editor.org/rfc/pdfrfc/rfc7519.txt.pdf)

## 术语说明

这其中会涉及到很多简写，先介绍一下

- JWS：JSON Web Signature，表示使用基于JSON的数据结构，对内容进行数字签名或MAC。具体内容下文详述。
- JWE：JSON Web Encryption，类似JWS，但这里是加密，而非数字签名。
- JWK：JSON Web Key，以JSON的形式表示一个加密key。
- JWA：JSON Web Algorithms，表示上面的签名、加密支持的算法。
- JWT：JSON Web Token，使用JSON表示的Token形式，可以采用JWS或JWE进行签名或加密。
- JOSE：JSON Object Signature and Encryption，即对上面JWS和JWE的统称。标准中常提到JOSE Header，代表的是JWS的Header或JWE的Header。

## JWS

### 组成

JWS包含三部分

- 头部（JOSE Header），即一些键值对

  - typ：type，即这一整个JWS代表的类型，典型值为JWT
  - alg：algorithm，算法，当前JWS签名或加密所采用的算法，需要在JWA中存在才可以用
  - jku：JWK Set URL，存放公钥的地址，必须遵守JWK规范
  - jwk：JSON Web Key，用于签名的秘钥，以JSON的形式发放，详情参考JWK
  - kid：key id，即秘钥id，jwk可能返回多个密码，kid精确指定
  - x5系列：X.509证书相关，这里忽略

  - 其它

- 载荷（JWS Payload），即主要的正文内容

- 签名（JWS Signature），签名方式如下

  - 待签名内容：`ASCII(BASE64URL(UTF8(JWS Protected Header)) || ’.’ || BASE64URL(JWS Payload))`
  - 签名算法：头部alg字段指定的算法

### 两种序列化格式

- 压缩方式：一种压缩的、URL安全的序列化方式

  最终输出格式如下，即三个部分除头部需额外处理外，其余均进行BASE64及URL编码，将结果通过点号连接起来。这也是我们最常见的JWT的形式。

  ```shell
  BASE64URL(UTF8(JWS Protected Header)) || ’.’ ||
  BASE64URL(JWS Payload) || ’.’ ||
  BASE64URL(JWS Signature)
  ```

- JSON方式：序列化结果就是一个JSON，签名等用字段表示

  最终输出格式如下，这种格式不常见，我们仅作了解就好

  ```json
  {
    "protected": BASE64URL(UTF8(JWS Protected Header)),
    "header": "<不受保护的头部>",
    "payload": BASE64URL(JWS Payload),
    "signature": BASE64URL(JWS Signature)
  }
  ```

  这里的不受保护的头部，指的是不参与签名的头部，即在完整性上不受保护。这只在JSON方式中会出现。

> 注意：特殊情况下，alg可以为"none"，此时的JWS是不安全的

### 举例

以协议中的例子呈现，假设我们要以HMAC SHA256算法签名一个载荷

- 待签名的载荷如下

  ```json
  {
    "iss":"joe",
  	"exp":1300819380,
  	"http://example.com/is_root":true
  }
  ```

  则`BASE64URL(JWS Payload)`计算得到的值为`eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ`

- 其对应的头部就会是这样（type不是必须的）

  ```json
  {
    "type": "JWT",
    "alg": "HS256" // 这表示使用HMAC SHA256的签名方式
  }
  ```

  则`BASE64URL(UTF8(JWS Protected Header))`计算的值为`eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9`

- 签名，对头部和载荷进行计算`ASCII(BASE64URL(UTF8(JWS Protected Header)) || ’.’ || BASE64URL(JWS Payload)) `，得到的签名然后做Base64计算得到的值为`dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk`

采用紧凑型的序列化格式，我们可以得到最终的结果为：

```shell
eyJ0eXAiOiJKV1QiLA0KICJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJqb2UiLA0KICJleHAiOjEzMDA4MTkzODAsDQogImh0dHA6Ly9leGFtcGxlLmNvbS9pc19yb290Ijp0cnVlfQ.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk
```

这是JWT的最为典型的呈现形式。

## JWE

有了对JWS的了解，理解JWE就容易多了。JWS是对内容签名，JWE就是对内容进行加密。要理解它需要一些加密算法相关知识，这里我们只简单有个印象。

### 组成

- 头部（JOSE Header），头部依旧有不少，这里不再列举，需要去查看协议手册
- 加密秘钥（JWE Encrypted Key）
- 初始向量（JWE Initialization Vector）
- 额外的认证数据（JWE Additional Authenticated Data value）
- 加密的密文（JWE Ciphertext），即加密结果
- 认证标签（JWE Authentication Tag）

### 两种序列化格式

和JWS一样，也有紧凑型和JSON型，我们这次只关注紧凑型，其输出方式如下

```shell
BASE64URL(UTF8(JWE Protected Header)) || ’.’ ||
BASE64URL(JWE Encrypted Key) || ’.’ ||
BASE64URL(JWE Initialization Vector) || ’.’ ||
BASE64URL(JWE Ciphertext) || ’.’ ||
BASE64URL(JWE Authentication Tag)
```

### 举例

我对加密算法不算了解，为了不曲解原文意思，又觉得在这里给出一个示例会好很多，所以直接引用原文吧

>This example encrypts the plaintext "The true sign of intelligence is not knowledge but imagination." to the recipient. 
>
>The following example JWE Protected Header declares that: 
>
>- The Content Encryption Key is encrypted to the recipient using the RSAES-OAEP [RFC3447] algorithm to produce the JWE Encrypted Key.
>
>- Authenticated encryption is performed on the plaintext using the AES GCM [AES] [NIST.800-38D] algorithm with a 256-bit key to produce the ciphertext and the Authentication Tag.
>
>  ` {"alg":"RSA-OAEP","enc":"A256GCM"} `
>
>Encoding this JWE Protected Header as BASE64URL(UTF8(JWE Protected Header)) gives this value: 
>
>`eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ`
>
>The remaining steps to finish creating this JWE are:
>
>- Generate a random Content Encryption Key (CEK)
>- Encrypt the CEK with the recipient’s public key using the RSAES- OAEP algorithm to produce the JWE Encrypted Key
>- Base64url-encode the JWE Encrypted Key
>- Generate a random JWE Initialization Vector
>- Base64url-encode the JWE Initialization Vector
>- Let the Additional Authenticated Data encryption parameter be ASCII(BASE64URL(UTF8(JWE Protected Header)))
>- Perform authenticated encryption on the plaintext with the AES GCM algorithm using the CEK as the encryption key, the JWE Initialization Vector, and the Additional Authenticated Data value, requesting a 128-bit Authentication Tag output
>- Base64url-encode the ciphertext
>- Base64url-encode the Authentication Tag
>- Assemble the final representation: The Compact Serialization of this result is the string `BASE64URL(UTF8(JWE Protected Header)) || ’.’ || BASE64URL(JWE Encrypted Key) || ’.’ || BASE64URL(JWE Initialization Vector) || ’.’ || BASE64URL(JWE Ciphertext) || ’.’ || BASE64URL(JWE Authentication Tag)`
>
>The final result is
>
>```shell
>eyJhbGciOiJSU0EtT0FFUCIsImVuYyI6IkEyNTZHQ00ifQ.
>OKOawDo13gRp2ojaHV7LFpZcgV7T6DVZKTyKOMTYUmKoTCVJRgckCL9kiMT03JGe
>ipsEdY3mx_etLbbWSrFr05kLzcSr4qKAq7YN7e9jwQRb23nfa6c9d-StnImGyFDb
>Sv04uVuxIp5Zms1gNxKKK2Da14B8S4rzVRltdYwam_lDp5XnZAYpQdb76FdIKLaV
>mqgfwX7XWRxv2322i-vDxRfqNzo_tETKzpVLzfiwQyeyPGLBIO56YJ7eObdv0je8
>1860ppamavo35UgoRdbYaBcoh9QcfylQr66oc6vFWXRcZ_ZT2LawVCWTIy3brGPi
>6UklfCpIMfIjf7iGdXKHzg.
>48V1_ALb6US04U3b.
>5eym8TW_c8SuK0ltJ3rpYIzOeDQz7TALvtu6UG9oMo4vpzs9tX_EFShS8iB7j6ji
>SdiwkIr3ajwQzaBtQD_A.
>XFBoMYUZodetZdvTiFvSkQ

## JWK

这是对JWS和JWE中用到的秘钥的提供方式，所以叫做JSON Web Key。以JSON的形式将秘钥的各项参数呈现，具体有哪些参数，需要据该秘钥的类型而定，比如

```json
{
  "kty":"EC",
	"crv":"P-256",
	"x":"f83OJ3D2xF1Bg8vub9tLe1gHMzV76e8Tus9uPHvRVEU",
	"y":"x_FEzRu9m36HLN_tue659LNpXW6pCyStikYjKIWI5a0",
	"kid":"Public key used in JWS spec Appendix A.3 example"
}
```

它也可以是个数组，此时就称作JWKs，提供一组秘钥，通过kid进行挑选。

对于JWK，我们需要关注主要是它能包含哪些参数，总共有两类

- 通用参数

  - kty：key type，秘钥类型，表示秘钥族，比如RSA、EC等。

  - use：Public Key Use，表明公钥的用途，有两个可选项
    - sig：用作签名
    - enc：用作加密

  - key_ops：Key Operations，表明本秘钥的用途，可选选项
    - sign：签名
    - verify：验证签名
    - encrypt：加密
    - decrypt：解密
    - wrapKey：加密key
    - unWrapKey：解密key
    - deriveKey
    - deriveBits

  - alg：表明本秘钥将被用在什么算法中

  - kid：即本秘钥的id

  - x5xxx：X.509相关

- 算法相关参数

  - 比如上面的额x、y、crv，都是和EC的公钥相关的参数，具体会需要哪些参数，JWA协议中有详细的规定。

## JWA

JWA协议中详细列举了支持的算法，以及算法所需秘钥的表现形式。如有需要，[可以翻一番](https://www.rfc-editor.org/rfc/pdfrfc/rfc7518.txt.pdf)

## JWT

至此，我们知道了JWS用于对指定载荷进行签名，JWE用于对普通文本进行加密。而JWT是基于这二者的。这里有两个重点

- JWT的主体内容是声明，即所谓Claim，它是JSON形式的键值对

- JWT在网络上传输时，需要被JWS签名，或者被JWE加密，并且使用的都是紧凑的序列化方式

  而我们大多数时候看到的，是被JWS签名的紧凑的序列化方式

JWS和JWE上面我们都熟悉过了，这里就只剩下Claim，我们看看JWT的声明包含哪些内容

- iss：JWT发布者
- sub：JWT的主体，在发布者的系统内唯一
- aud：JWT的目标接收者，接受该JWT的一方，必须验证此值，如果该值和预期的不一致，则应该拒绝该JWT
- exp：过期时间，数字化的时间类型，即时间戳，（苹果是秒为单位）
- nbf：Not Before，规定的生效时间，必须在这个时间之后才能处理它
- iat：issue at，JWT签发时间
- jti：JWT ID， 为JWT提供一个唯一的ID，JTI用作防止JWT的重放

协议还规定，可以自定义一些字段，只要JWT发出方和接收方协商一致即可。

我们给一个IOS登录时，苹果签发的JWT作为例子

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

> JWT在协议上只规定了能够声明的内容，而最终的呈现形式，是JWS协议提供的，这点注意区分。

## 适用场景 - 与token-session对比

所谓token-session模式，即服务端存储用户数据，根据用户标识生成id或token，发放给客户端，客户端依次作为访问凭证，可以获取用户信息，可以访问所有具有权限的资源。传统的session、自己签发的token，本质上都可归于这一类，他们都有共同的特点——中心化，即有一个或一组节点负责管理。

那么JWT能带来什么呢？JWT只是一组带有签名的一组规定好的数据，有两个点（就。。。数字证书）

- 能够包含信息
- 带有签名，能够验证真实性，无法伪造

其中，可通过签名验证真伪这一点，能带来一个最大的好处——去中心化。JWT使用者不需要再和签发方沟通以验证真伪。看起来很好，但它有一个致命的缺点

- 在JWT过期前（exp字段决定），由于使用方只验证签名，没有对该凭证本身做验证，因此无法手动使一个token失效

此时普遍的补救方法是，增加一个JWT验证的步骤，即每次使用前，向签发方发送请求验证JWT是否已经被手动失效。但这样，岂不是又退化为了传统的token-session模式？

那么，JWT的应用场景究竟是怎样的呢？首先参考一下[iOS的登录方式](https://zou8944.com/2020/03/28/Sign%20in%20with%20Apple%20-%20IOS%E5%B9%B3%E5%8F%B0%E6%9C%8D%E5%8A%A1%E7%AB%AF%E7%9A%84%E5%A4%84%E7%90%86-signinwithapple-ios%E5%B9%B3%E5%8F%B0%E6%9C%8D%E5%8A%A1%E7%AB%AF%E7%9A%84%E5%A4%84%E7%90%86/)：在客户端调用登录API后，苹果服务端主要返回两个内容

- identity-token：这是一个JWT，内部包含了用户在苹果服务器内部的唯一ID，以及用户的邮箱信息。
- authorization code：这是OAuth 2.0的授权码，用于向苹果服务器换取access token和refresh token，这里忽略。

这里JWT只是被用来签发用户ID，而对数据的访问凭证和用户详细信息的获取还是走OAuth 2.0——JWT只用来发布信息，并没有被用来当做访问凭证。**这也是我比较赞同的使用方式**。作为访问凭证，JWT并不能实现去中心化的目的。

总结一下，如果使用JWT替换传统的token，会得到一个好处

- 非敏感的用户信息可以放在JWT中，从而省去了获取用户信息这一步骤

但同时会带来两个新的问题

- 需要增加密码分发方式
- 并不能节省token验证这一步骤

## 总结

应该注意到，我们经常所谓的JWT，其实都是JWS签名和序列化后的结果，而从协议上看，它还可以是JWE加密结果。

本质上，JWT带给我们的只是安全传输数据的方式。比较好的使用场景是数据分发，而不是作为访问凭证。就算作为访问凭证，他也不是替代传统token-session的方式，而只是将传统的token进行了增强，但增强的同时，复杂度也会加大。
