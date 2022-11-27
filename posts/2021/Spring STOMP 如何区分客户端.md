---
created_at: 2021-09-16 18:51:53.051
updated_at: 2021-09-16 18:51:53.051
slug: how-to-distinguish-client-in-spring-stomp
tags: 
- Spring
- WebSocket
- STOMP
---

## 背景

现有使用Spring WebSocket库搭建的STOMP通知中心，使用Spring自带功能，能够区分到用户，向来自同一用户的多个连接（会话）广播数据。

这正是我们的使用场景：当用户调用服务端指定接口时，服务端向该用户所在的所有用户发送通知。

现有的配置，在WebSocket握手阶段验证TOKEN，解析成用户ID，存入WebSession；在接口访问时带上TOKEN，再通过SimpMessagingTemplate.convertAndSendToUser()向该用户进行广播。

<!-- more -->

## 说明

- X-GD-UID：客户端提供设备识别码的请求头名
- X-GD-TOKEN：客户端提供TOKEN的请求头名
- uid：设备识别码在服务端内部的流转名
- deviceId：设备识别码在服务端内部的流转名
- user：用户在服务端内部的流转名
- WebSocketSession：WebSocket的Session，一般来说，一个WebSocket连接对应一个Session。该session对应的sessionId，单个服务器
- STOMP Session：STOMP的Session，和WebSession等价。源码中，将来自WebSocket的消息包装成STOMP消息，可以直接看到二者的设置关系：

    ```java
    // 位置：org.springframework.web.socket.messaging.StompSubProtocolHandler#handleMessageFromClient
    @Override
    public void handleMessageFromClient(WebSocketSession session,...) {
    	... ...
    	headerAccessor.setSessionId(session.getId());
    	... ...
    }
    ```

## 优化需求

按照上面的方式，对一个用户广播，会通知到所有设备，即使该设备是通知触发方。逻辑上讲，通知触发方是不应该收到通知的。这正是我们需要实现的需求。

## 方案

### 设备识别

当前只能通过TOKEN识别用户。但没有识别设备的方式，我们可能有两种

- IP地址：不可取。网络环境复杂，经过层层转发，我们不一定能保证获取到稳定的IP地址；即时能够获取到，因为SNAT的存在，对处在同一局域网下的多台设备，也不一定能够区分。
- 设备识别码：取客户端设备的唯一识别码，这是最保险的方法。但根据“客户端不可信原则”。userId+设备识别码才是理论上最靠谱的方式。

### 放在哪

设备识别码这个参数，比较中性，可以在其他业务上用，因此放在头部比较合适，暂定X-GD-UID。客户端所有请求，都带上该头部。

### 服务端方案

1. WebSocket握手时，解析user和uid，放入WebSocketSession。该WebSocketSession会在后面的每次交互中带上此两个参数。
2. 在STOMP进行CONNECT时，我们能够在入方向的拦截器中获取到上一步存放的user、uid，以及新建的STOMP session，我们将他们缓存起来，以便后面使用。
3. 发送STOMP通知时，指定要忽略哪个uid，我们能够在出方向上的拦截器中拦截该消息，如果发现当前通知即将发送的目标设备和指定的uid匹配，则拦截掉该通知。
4. 连接断开时，清除缓存

### 缓存放哪

三个地方备选，综合来看，放在Redis是比较好的选择。不过需要小心的是Redis的重启

- 本地：多实例时会出问题
- Redis：Redis数据库本身的声明周期和项目不一致，有可能在项目运行到一半时关闭
- 数据库：生命周期大于项目，是理论上最安全的位置，但访问速度可能会比较慢

## 实施

全流程配置忽略，这里只说关键部分的代码。我们将与当前功能相关的逻辑都放在一个类中，如下。本节其它小节将会直接引用该类中的方法

```kotlin
@Component
class DeviceHolder(private val redisTemplate: StringRedisTemplate) {

    fun removeSession(message: Message<*>) {
        SimpMessageHeaderAccessor.getSessionId(message.headers)?.let {
            redisTemplate.delete(it.toRedisKey())
        }
    }

    fun deviceBindInterceptor() = object : ChannelInterceptor {
        override fun preSend(message: Message<*>, channel: MessageChannel): Message<*> {
            // 连接时记录deviceId和当前session的关系
            val accessor = MessageHeaderAccessor.getAccessor(message, StompHeaderAccessor::class.java)
            if (accessor != null && StompCommand.CONNECT == accessor.command) {
                val user = accessor.user ?: return message
                val deviceId = accessor.sessionAttributes?.get(DEVICE_ID_ATTRIBUTE)?.toString() ?: return message
                val sessionId = accessor.sessionId!!
                redisTemplate.opsForValue().set(sessionId.toRedisKey(), genDeviceValue(user.name, deviceId))
            }
            return message
        }
    }

    fun deviceIgnoreInterceptor() = object : ChannelInterceptor {
        override fun preSend(message: Message<*>, channel: MessageChannel): Message<*>? {
            // 发送时滤除指定deviceId的sessionID
            val accessor = MessageHeaderAccessor.getAccessor(message, SimpMessageHeaderAccessor::class.java)
            if (accessor != null && SimpMessageType.MESSAGE == accessor.messageType) {
                val username = accessor.removeNativeHeader(USER_ATTRIBUTE)?.singleOrNull() ?: return message
                val ignoreDeviceId = accessor.removeNativeHeader(DEVICE_ID_ATTRIBUTE)?.singleOrNull() ?: return message
                val deviceValueOfMessage = redisTemplate.opsForValue().get(accessor.sessionId!!.toRedisKey()) ?: return message
                if (deviceValueOfMessage == genDeviceValue(username, ignoreDeviceId)) return null
            }
            return message
        }
    }

    private fun genDeviceValue(username: String, deviceId: String): String = "${username}-$deviceId"

    private fun String.toRedisKey() = "MYLOGS_WEBSOCKET_DEVICE_$this"

}
```

### UID解析

握手拦截器中解析UID

```java
private class AuthHandshakeInterceptor(val objectMapper: ObjectMapper) : HandshakeInterceptor {

    override fun beforeHandshake(
        request: ServerHttpRequest,
        response: ServerHttpResponse,
        wsHandler: WebSocketHandler,
        attributes: MutableMap<String, Any>
    ): Boolean {
        val user = request.parseUser(objectMapper)
        val deviceId = request.parseDeviceId()
				... ...
        if (deviceId != null) attributes[DEVICE_ID_ATTRIBUTE] = deviceId

        return true
    }

}

// 扩展方法，从头部或query中取X-GD-UID
fun ServerHttpRequest.parseDeviceId(): String? {
    val deviceIdInHeader = this.headers[DEVICE_UID_HEADER]?.firstOrNull()
    val deviceIdInQuery = lazy { this.uri.query?.split("&")?.find { it.contains(DEVICE_UID_HEADER) }?.split("=")?.last() }
    return deviceIdInHeader ?: deviceIdInQuery.value
}
```

### UID缓存

入方向上的拦截器，取出user、uid、sessionId，放入Redis。参见DeviceHolder.deviceBindInterceptor()。

### 信息拦截

出方向上的拦截器，缓存匹配，则忽略。参见DeviceHolder.deviceIgnoreInterceptor()。

### 连接断开处理

当STOMP连接或WebSocket连接断开时，会发送SessionDisconnectEvent事件，我们监听该事件，在连接断开时主动清理掉内存。

```java
@Component
class DisconnectEventListener(
    private val deviceHolder: DeviceHolder
) : ApplicationListener<SessionDisconnectEvent> {

    override fun onApplicationEvent(event: SessionDisconnectEvent) {
        deviceHolder.removeSession(event.message)
    }

}
```

### 使用方

使用方需传入用户名、目标地址、要忽略的设备ID、要发送的消息等。

```kotlin
fun SimpMessagingTemplate.notifyUserWithoutDevice(userId: Int, deviceId: String?, maxUsn: Long) {
    val user = User.fromId(userId)
    this.convertAndSendToUser(
				// 用户名
        user.name,
				// 用户地址
        STOMP_USER_PULL_NOTIFICATION_TOPIC,
				// 发送的消息体
        PullNotify(maxUsn),
				// 附带的额外属性。很重要，正是它们携带了用户名、设备id到出方向上的拦截器
        mapOf(
            DEVICE_ID_ATTRIBUTE to deviceId,
            USER_ATTRIBUTE to user.name
        )
    )
}
```

## 要点

- Spring WebSocket为我们提供的参与消息收发的方式主要有握手拦截器、握手处理器、STOMP消息入方向上的拦截器、STOMP消息出方向上的拦截器，正是利用这些特性，我们猜完成了设备识别这一需求
- 出方向的拦截器无法获取到消息所属用户，因此这里我们在用SimpMessagingTemplate发送消息时将用户放进头中，再在拦截器中取出。这种方式，并不优雅
- 单实例上的SessionId不会重复，但是多实例之间的SessionId是理论上是可能重复的，此时会存在bug。即一台实例上的session覆盖了另一台实例的缓存，造成有效缓存丢失的情况。有两个解决方案
    - 保证SessionId绝对不同
    - 存储user-deviceId-sessionId三层结构，这样理论上不会出问题，毕竟同一个用户，在同一台机器上出现一样的sessionId的情况，理论上就不可能出现