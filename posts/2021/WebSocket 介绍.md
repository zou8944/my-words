---
created_at: 2021-09-03 18:39:28.815
updated_at: 2021-09-03 18:39:28.815
slug: websocket-introduction
tags: 
- WebSocket
---

> 本文主要包含三部分
>
> - WebSocket协议、STOMP协议、SockJS协议三部分的理论介绍
> - 使用Spring实现一个简单的消息推送服务
> - 使用Postman调试STOMP服务

WebSocket我们大概都知道是个啥东西，原理上挺简单，使用起来却没那么容易。因为我们会发现，无论是Spring的WebSocket部分的手册，还是网络上的一大票文章，无不涉及到三个关键词——WebSocket、SockJS、STOMP。以至于我们想找一篇介绍只使用WebSocket构建服务的文章都十分困难。究其原因，我想大致有这么几个

- WebSocket协议在数据层面还是太底层了，需要STOMP这样的应用层协议供大家使用；而STOMP又涵盖了消息中心的大部分使用场景，因此变得很必要。
- 对前端来说，sockjs-client库很多时候是接入WebSocket的较好的方式，于是SockJS协议映入眼帘。

<!-- more -->

所以，无论如何，这三个协议本身，我们是必须搞清楚的。

## WebSocket

十分建议详细阅读一下WebSocket的协议标准——[RFC6455](https://www.rfc-editor.org/rfc/pdfrfc/rfc6455.txt.pdf)

关于WebSocket需要明白的重点

- 由HTTP升级而来
- 与HTTP共用端口，即80和443(HTTPS)
- 升级后CS之间通信与HTTP无任何关系，而是采用类似TCP的二进制帧进行的

### WebSocket的设计哲学

- 设计足够简单，使得能够被用来支撑其它应用，如STOMP。STOMP之于WebSocket，好比HTTP之于TCP。
- 相较于TCP，它仅仅是被赋予了web的一些特性。如：origin安全模型、类似http 的uri地址模型等
- 其它。。。就没有其它了

### 协议介绍

一个完整的WebSocket通信流程包括：握手 -> 全双工通信 -> 关闭连接

#### 握手

握手是纯HTTP请求，这为WebSocket鉴权带来了方便。我们依旧可以使用之前HTTP体系下的鉴权方式。

客户端握手请求示例

```html
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: http://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

服务端响应示例

```html
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: chat
```

对比较陌生的请求头予以说明

| 请求头                                             | 说明                                                         |
| -------------------------------------------------- | ------------------------------------------------------------ |
| Upgrade: websocket                                 | 表明协议升级的目标协议。<br />如果有注意到，从HTTP1.1升级到HTTP2.0，也是采用一样的方式 |
| Connection: Upgrade                                | 表明本次请求是协议升级                                       |
| Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==        | 客户端生成的随机数的BASE64编码结果                           |
| Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo= | 服务端根据客户端给的随机数通过固定的算法计算出的结果；<br />客户端收到后会以相同的算法计算结果并对比，以证明这是一个合法的响应 |
| Sec-WebSocket-Protocol: chat, superchat            | 子协议选择，客户端列出可选子协议，服务端选择支持的子协议<br />由于WebSocket过于底层，因此支持子协议以适应不同应用场景 |
| Sec-WebSocket-Version: 13                          | WebSocket版本                                                |
| HTTP/1.1 101 Switching Protocols                   | 101表示升级成功，即握手成功                                  |

#### 协议帧

握手成功之后就是正常的通信。WebSocket通信时以帧为单位进行数据的收发，一条完整的信息可能被分为多个帧进行传输，到远端后再被拼接在一次。

协议帧结构如下，是不是很熟悉，有点TCP协议帧的味道。这也是说它很底层的原因。各bit的详细含义，参见RFC

![image-20210902223211949]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210902223211949.png)

#### 协议帧类型

WebSocket协议帧有两种类型：数据帧和控制帧。数据帧顾名思义，用于传输数据；我们这里重点关注数据帧

- Close：用于关闭连接
- Ping：心跳发起
- Pong：心跳响应，Ping、Pong总是成对出现

注意，协议虽然定义了新跳帧，但是否使用，需要使用者决定。

## SockJS

同样，十分建议阅读一下SockJS的协议标准——[它并非ITEF拟定的，而是一个开源项目](https://sockjs.github.io/sockjs-protocol/sockjs-protocol-0.3.3.html)

我们知道，早在WebSocket出现之前，从服务端向客户端推数据这个需求，就一直存在。其中最常用的尝试就有轮询、长轮询等，后面又有了EventSource之类的机制。而SockJS，就是集合了现今所有这类方式的库（包含websocket）。如今，SockJS已经成为了一个协议标准，主流语言都有了支持的库，尤其是web前端。

简单地说，SocketJS定义了一个服务端必须有哪些HTTP端点，以便使用不同的通信方式。定义了帧结构，用于传输数据

### 端点

这里列出关键的端点，省略了域名和base url

- /info：用于查询客户端支持的通信方式，如是否支持WebSocket。可以理解为通信协商

  ```json
  # 这里展示一个典型地info响应
  {
    "entropy":2143307232,
    "origins":[
      "*:*"
    ],
    "cookie_needed":true,
    "websocket":true
  }
  ```

- /(server_id)/(session_id)/websocket：暴露的websocket端点，用于websocket通信

- /(server_id)/(session_id)/xhr，/(server_id)/(session_id)/xhr_send：暴露的长连接端点，用于ajax长连接

- /(server_id)/(session_id)/eventsource：eventsource端点

- /websocket：这是一个外挂，该端点直接走裸的websocket协议，这为SockJS服务端直接使用WebSocket客户端库提供了条件

SockJS协议通信分为两步：访问/info询问支持的通信方式；访问对应的端点进行通信

### 帧结构

SockJS是一个协议，也有自己的帧定义，但它的帧定义足够简单，就几个字符

- o：通信开启帧
- h：心跳帧，服务端下发
- a：消息数组
- c：通信关闭帧

### SockJS的缺点

- 出于安全原因，在协议层面就不支持自定义请求头，我们应该能发现所有sockjs客户端库都无法添加请求头吧。[原因看这](https://github.com/sockjs/sockjs-client/issues/196)
- 与WebSocket是包含关系，而非兼容关系。如果一个服务端暴露SockJS服务，客户端是没办法直接将这个端点用在WebSocket库的，而是要通过SockJS暴露出的websocket原生端点进行访问（即base url/websocket），不大友好

## STOMP

再次，十分建议阅读一下STOMP的协议标准——[它也是一个开源项目](https://stomp.github.io/stomp-specification-1.2.html)

STOMP是一个高级的应用协议，用于异步消息传输，支持点对点发送、发布订阅等消息传递方式。它的设计哲学就是足够简单，这也体现在协议长度上，如果看过AMQP、MQTT之类的消息协议，就能体会什么叫简单。

### 帧结构

这是它的帧结构，就是纯文本帧。包含命令、头部、body三部分。最后以ascii为0的字符结尾。

- 命令：表明帧类型
- 头部：额外的帧属性，如心跳配置、content-type等
- body：消息体，只有消息帧时才有

```html
COMMAND
header1:value1
header2:value2

Body^@
```

### 帧类型

帧类型也足够简单

| Side   | 命令               | 说明                     |
| ------ | ------------------ | ------------------------ |
| 客户端 | CONNECT            | 发起连接                 |
|        | DISCONNECT         | 断开连接                 |
|        | SEND               | 发送消息                 |
|        | SUBSCRIBE          | 订阅                     |
|        | UNSUBSCRIBE        | 取消订阅                 |
|        | ACK/NACK           | 响应                     |
|        | BEGIN/COMMIT/ABORT | 事务相关                 |
| 服务端 | CONNECTED          | 连接成功                 |
|        | MESSAGE            | 发送订阅的消息给客户端   |
|        | RECEIPT            | 凭据，如果客户端需要的话 |
|        | ERROR              | 错误通报                 |

## 所以这三个协议的关系？

WebSocket、SockJS、STOMP三者，从前往后，层级依次上升，就像洋葱，WebSocket在里面，SockJS其次，STOMP在最外面。如果我们使用建立在SockJS协议上的STOMP服务，而SockJS又选择WebSocket作为底层的通信协议。在通信过程中，STOMP帧会被组装成SockJS的帧；SockJS的帧会被组装成WebSocket的帧；再深一点，WebSocket的帧会被组装成TCP的帧；TCP的帧被组装成IP层的帧，然后传输；到远端后执行相反操作。

从分类上说，WebSocket和SockJS都只是通用的数据传输协议；而STOMP是一种消息协议，抽象层级更高。

## 心跳

三个协议都定义了心跳，其中

- WebSocket只定义了心跳帧，但发送的时机与策略，由具体实现来定。目前来看，默认情况下WebSocket库是不会自动发送心跳的，需调用者手动发送
- SockJS规定服务端必须发送心跳，默认25秒一次，可配，不需要调用者手动开启
- STOMP也定义了心跳，默认不开启，一般实现库都有提供，只需手动配置开启即可。需要说明的是，开启了STOMP的心跳，会关闭掉SockJS的心跳。

## Spring实现一个消息推送服务

Spring对WebSocket的支持看[这里](https://docs.spring.io/spring-framework/docs/4.3.x/spring-framework-reference/html/websocket.html)。

我们实现一个简单的需求

- 暴露STOMP端点
- 提供主题，供用户订阅，支持对单个用户广播。即，需要鉴权
- 提供一个STOMP地址，用户向该地址发送数据时，从其订阅的主体下发消息

### 配置

配置类如下，这不是一个完全可用的类，直接复制很可能无法正常运行。

```kotlin
// 配置类
@Configuration
@EnableWebSocketMessageBroker
class WebSocketConfig : WebSocketMessageBrokerConfigurer {

    @Autowired
    lateinit var objectMapper: ObjectMapper

    override fun registerStompEndpoints(registry: StompEndpointRegistry) {
      	// 暴露STOMP端点
        registry.addEndpoint("/stomp")
      			// 添加握手拦截器，用于做权限验证
            .addInterceptors(AuthHandshakeInterceptor(objectMapper))
      			// 握手处理器
            .setHandshakeHandler(AuthHandshakeHandler())
            .setAllowedOriginPatterns("*")
            .withSockJS()
    }

    override fun configureMessageBroker(registry: MessageBrokerRegistry) {
        // 用于发送心跳的调度器，一定要有。其它层级协议的心跳不能替代STOMP层级的心跳
        val scheduler = TaskSchedulerBuilder().build().apply { initialize() }
        registry.enableSimpleBroker("/topic").setTaskScheduler(scheduler)
        registry.setApplicationDestinationPrefixes("/app")
        // 订阅/user/打头的destination时，STOMP可自动将每个用户对应一个主题，实现向指定用户发送消息的能力
        registry.setUserDestinationPrefix("/user/")
    }

}

private class AuthHandshakeInterceptor(val objectMapper: ObjectMapper) : HandshakeInterceptor {

    override fun beforeHandshake(request: ServerHttpRequest, response: ServerHttpResponse, wsHandler: WebSocketHandler, attributes: MutableMap<String, Any>): Boolean {
      	// 从request的header或query中提取用户，具体逻辑自己实现
        val user = request.parseUser(objectMapper)
        if (user == null) {
          	// 
            val error = ResErrCode.NEED_AUTHORIZE
            response.setStatusCode(error.httpStatus)
            response.headers.contentType = MediaType.APPLICATION_JSON
            response.body.write(objectMapper.writeValueAsBytes(R.fail(error)))
            return false
        }
        attributes["user"] = user
        return true
    }

    override fun afterHandshake(request: ServerHttpRequest, response: ServerHttpResponse, wsHandler: WebSocketHandler, exception: Exception?) {
			// 这里啥也没做
    }

}

private class AuthHandshakeHandler : DefaultHandshakeHandler() {

    override fun determineUser(request: ServerHttpRequest, wsHandler: WebSocketHandler, attributes: MutableMap<String, Any>): Principal? {
        return attributes["user"] as Principal?
    }

}
```

### 使用

- 暴露接收用户信息的地址。

  这里的关键在于MessageMapping和SendToUser两个注解的使用，它们能够直接在Controller中使用。

  前者将用户发送的消息导入；后者将方法返回的内容发送给对应的用户。

  ```kotlin
  @Controller
  class WebSocketController {
  
      /**
       * 手动触发拉取通知，随便发个啥，都会触发一次拉取通知
       */
      @MessageMapping("/triggerPullNotification")
      @SendToUser(destinations = ["topic/pullNotification"])
      fun echo(income: String, principal: Principal): Any {
          log.info("trigger pull notification manually: user {}; message: {}", principal.name, income)
          return STOMP_USER_PULL_NOTIFICATION_PAYLOAD
      }
  
  }
  ```

  上面的例子，STOMP客户端向/app/triggerPullNotification发送消息时，会进入echo方法，发送的内容被传递到income参数中，发送消息的用户被传递到principal参数中。echo返回的对象会被发送给订阅了/user/topic/pullNotification主题的当前session的用户，即触发这个消息的用户。

- 在其他地方向指定用户发送消息

  这里的关键是注入SimpMessagingTemplate

  ```kotlin
  @Service
  class ExampleService(val stomp: SimpMessagingTemplate) {
    
    fun test() {
      // 这里是你的自由逻辑
      ...
      // 发送给某个用户
      stomp.convertAndSendToUser(12345, "/topic/pullNotification", "your payload")
    }
    
  }
  ```

### 测试连接

JS测试脚本

```javascript
// 连接并订阅
function connect() {
    const socket = new SockJS('https://apitest.wemore.com/mylogs/stomp?X-5E-TOKEN=qhMtjBjVozY3zYLrOfMStgvffeFjBofY');
    stompClient = Stomp.over(socket);
    stompClient.connect({
    }, function (frame) {
        setConnected(true);
        stompClient.subscribe('/user/topic/pullNotification', function (data) {
            // console.log('received: ' + data);
        });
    });
}
// 发送消息给服务端
function trigger() {
    stompClient.send("/app/triggerPullNotification", {}, JSON.stringify({'name': '啥呀'}));
}
```

使用Chrome进行测试，在点击连接时，我们能看到先通过info询问，再调用websocket

![image-20210903174636617]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210903174636617.png)

info的响应

![image-20210903174721948]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210903174721948.png)

websocket的消息流：可以看到就是SockJS帧套STOMP帧。

![image-20210903174749633]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210903174749633.png)

其中的["\n"]和a["\n"]是STOMP的心跳，我们把视线转移到console看得更为直观，它详细地展示了STOMP的通信过程

![image-20210903174948448]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210903174948448.png)

此时如果我们再触发一次消息，可以观察到消息的发出和接收

![image-20210903175110240]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210903175110240.png)

### 强调几点

1. `HandShakeIntercepter`和`HandShakeHandler`的区别

   - `HandShakeIntercepter`前者能够拦截握手的请求，并且可操作直接对握手请求进行响应

   - `HandShakeHandler`用于处理握手成功后的细节问题，尤其是允许我们自己设置当前session的用户
   - 我们在`HandShakeIntercepter`进行鉴权；在`HandShakeHandler`将鉴权得来的用户设置为当前session的用户

2. 心跳

   STOMP服务端的心跳一定要配：如果客户端直接采用了WebSocket连接，没有心跳配置，连接可能随时会断

3. 标记用户

   这是Spring Stomp为我们提供的方便的功能。它使得我们可以方便地只发送消息给订阅某个主题的单个用户。要完成它，必须有这么几步

   - 注入我们的用户逻辑，可以迁入Spring Security，也可以自定义。本文中我们在`HandShakeHandler`中将自己用户体系中的user传递给了Stomp作为用户标记。记得给user实现Principal接口哦。

   - 配置用户地址前缀。并不是每个主题都能支持这样的功能的，我们需要设置一个固定的前缀，那么订阅了这些指定前缀主题的用户，就具有了被标记的能力

     ```kotlin
     override fun configureMessageBroker(registry: MessageBrokerRegistry) {
       			... ...
             // 订阅/user/打头的destination时，STOMP可自动将每个用户对应一个主题，实现向指定用户发送消息的能力
             registry.setUserDestinationPrefix("/user")
         }
     ```

   - 使用规则

     需要对地址`/topic/pullNotification`赋予用户标记的能力，在配置OK后，使用方法

     - 客户端订阅地址：`/user/topic/pullNotification`
     - 服务端向指定用户发送消息时，使用：`stomp.convertAndSendToUser(12345, "/topic/pullNotification", "your payload")`

## 用Postman调试STOMP服务

Postman提供WebSocket调试功能，但却不支持调试STOMP服务，这让人感到可惜。但是，如果我们实在想要直接用Postman访问STOMP服务的话。依在下愚见，唯一的办法就是，硬用。即，手动编辑STOMP帧，然后发送。

手动编辑有个问题，STOMP帧是以ASCII码表中值为0的字符结尾的，即`'\u0000'`，无法通过文本表达。于是只能通过二进制发送。

以上面的服务为例，我们要订阅一个STOMP服务，首先要连接上STOMP端点，然后发送CONNECT帧，然后是SUBSCRIBE帧，帧的二进制编码通过代码生成

```kotlin
fun main() {
    val connectMessage = """
        CONNECT
        heart-beat:5000,5000
        accept-version:1.2
        host:127.0.0.1
    """.trimIndent()

    val subscription = """
        SUBSCRIBE
        id:0
        destination:/user/topic/pullNotification
        ack:client
    """.trimIndent()

    fun String.generate(): String {
        val builder = StringBuilder()
        builder.append(this)
        builder.append('\n')
        builder.append('\n')
        builder.append('\u0000')
        return builder.toString().toByteArray().joinToString(separator = "") { String.format("%02x", it) }
    }

    println(connectMessage.generate()) // 434f4e4e4543540a6163636570742d76657273696f6e3a312e320a686f73743a3132372e302e302e310a0a00
    println(subscription.generate()) // 5355425343524942450a69643a300a64657374696e6174696f6e3a2f757365722f746f7069632f70756c6c4e6f74696669636174696f6e0a61636b3a636c69656e740a0a00
}
```

上面暴露的是SockJS服务，我们有两种方式连接websocket

- 使用SockJS暴露的原生WebSocket端点，即/websocket
- 使用SockJS协议内容的WebSocket端点，即/server_id/sessioin_id/websocket

我们用第一种，然后步骤是

1. 输入ws端点：wss://<我的域名>/stomp/websocket，点击连接

2. 以二进制格式发送连接帧，重点是选择二进制哦

   ![企业微信截图_160e941c-6adc-4459-96bf-bbba2d15e4ad](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/企业微信截图_160e941c-6adc-4459-96bf-bbba2d15e4ad.png)

   出现如下响应，说明连接成功

   ![企业微信截图_293f66bf-25ab-49c4-8312-2f8cba9da8e5](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/企业微信截图_293f66bf-25ab-49c4-8312-2f8cba9da8e5.png)

3. 发送订阅帧

4. 使用刚才的脚本触发一次echo，你就可以看到我们能够正常收到消息了

   ![image-20210903181047727]( https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/image-20210903181047727.png)

### 有一个问题

你会发现，通过Postman尽管连上了，但在最后一次通信的60s后，连接自动断开了！！！

![企业微信截图_26269104-19a8-4c63-82dc-af94ce05534e](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/企业微信截图_26269104-19a8-4c63-82dc-af94ce05534e.png)

这是因为我们没发心跳呀啊啊啊啊啊啊啊啊啊。由于我将服务部署在nginx后，我们的nginx设置为60s不活动的TCP连接都将被关闭。

如何解决呢，要解决，只有两个方法

- 60s内发心跳续命
- 不停进行消息通信

反正就是不停发就行了。

## 总结

要使用WebSocket，那么SockJS和STOMP都是必须了解的，最好的了解方式是去看协议。

文中的示例代码，不能直接用，只能当做参考。

Postman调试STOMP？可以用来熟悉协议，但实际用来调试，还是算了吧。

本文重点：三种协议关键点介绍、Spring的STOMP用户标记功能、通过Postman学习STOMP协议帧。

## 参考文档

1. [RFC6455](https://www.rfc-editor.org/rfc/pdfrfc/rfc6455.txt.pdf)
2. [SockJS Protocol](https://sockjs.github.io/sockjs-protocol/sockjs-protocol-0.3.3.html)
3. [STOMP Specification](https://stomp.github.io/stomp-specification-1.2.html)
4. [Spring WebSocket](https://docs.spring.io/spring-framework/docs/4.3.x/spring-framework-reference/html/websocket.html)

