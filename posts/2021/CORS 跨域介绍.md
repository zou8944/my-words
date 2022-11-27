---
created_at: 2021-09-08 22:42:45.383
updated_at: 2021-09-24 17:10:10.681
slug: cors-introduction
tags: 
- CORS
---

## 已知

不得不说，我(们)对跨域可能有些误解。确切地讲，是对跨域的使用有些误解。

我的跨域知识从哪里来？从这里——[跨源资源共享（CORS） - HTTP | MDN](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/CORS)

<!-- more -->

能总结出几点

- 跨域是一种允许服务端对来自浏览器的访问进行控制的机制
- 它涉及到一系列专用的请求头
    - 浏览器端
        - Origin：声明源站
        - Access-Control-Request-Method：声明自己将要使用什么方法
        - Access-Control-Request-Headers：声明自己将要携带哪些自定义头部
    - 服务端
        - Access-Control-Allow-Origin：声明本站允许的源站
        - Access-Control-Allow-Methods：声明本站允许的方法
        - Access-Control-Allow-Headers：声明本真允许的自定义头部
        - Access-Control-Max-Age：声明一个预检请求的有效期，有效期内同一个请求无须再次预检
- 请求被划分为简单请求和复杂请求
    - 复杂请求在请求实际发出之前，会发出OPTIONS预检请求进行跨域询问
    - 简单请求不需要预检

在实际使用中，我们为了方便，尝尝会将服务端的所有响应配置为“*”，即允许所有源站、方法、自定义首部的请求进行访问。

然而，这招在需要传输Cookie的请求中，行不通，浏览器会报如下错误。

```bash
xxx from origin 'xxxx' has been blocked by CORS policy: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute.
```

## 盲区

出现这个问题，是因为漏掉了关键的一点：附带身份凭证的请求。其明确规定一点

- 对于附带身份凭证的请求，服务器不得设置 Access-Control-Allow-Origin 的值为“*”

    相应的，它必须是确切地和请求中的Origin进行匹配，即，如果请求的Origin是http://xyc.com，则响应的Access-Control-Allow-Origin也必须为http://xyc.com

这一点可以验证，并且牵出一个新的响应请求头

- Access-Control-Allow-Credentials: 是否允许跨域携带凭证。为true时，代表允许，相应地Access-Control-Allow-Origin 就一定不会为“*”

出现上面的错误只有一种情况，即响应只有Access-Control-Allow-Origin: *，而没有Access-Control-Allow-Credentials，或者其值为false。

解决办法，加上Access-Control-Allow-Credentials: true，并修改Access-Control-Allow-Origin。

## Spring对跨域的支持

所有Spring Web模块，都支持直接配置跨域。下面是正确且唯一正确的配置

web服务的代码中配置

```kotlin
@Bean
fun corsFilter(): CorsFilter {
    val config = CorsConfiguration()
    // 预检请求有效期
    config.maxAge = 3600
    // 允许跨域发送身份凭证
    config.allowCredentials = true
    // 允许跨域的源为所有，注意与origin:*进行区分
    config.addAllowedOriginPattern("*")
    // 允许所有请求头
    config.addAllowedHeader("*")
    // 允许所有请求方法
    config.addAllowedMethod("*")

    val source = UrlBasedCorsConfigurationSource().apply {
        // 上述配置针对所有请求路径生效
        registerCorsConfiguration("/**", config)
    }

    return CorsFilter(source)
}
```

Spring Gateway中配置文件的配置

```yaml
# /**表示配置针对所有路径
# 允许
spring.cloud.gateway.globalcors.cors-configurations.[/**].allowed-headers=*
spring.cloud.gateway.globalcors.cors-configurations.[/**].allowed-methods=*
spring.cloud.gateway.globalcors.cors-configurations.[/**].allowed-origin-patterns=*
spring.cloud.gateway.globalcors.cors-configurations.[/**].allow-credentials=true
```

这里尤其注意区分

`addAllowedOriginPattern("*")`和`addOrigins("*")`的区别

- 前者的*表示通配符，用来匹配请求的Origin，如果匹配成功，响应的Access-Control-Allow-Origin就直接被设置为请求的Origin
- 后者表示直接将所有的Access-Control-Allow-Origin值都设置为”*“。这个在和allowCredentials=true一起使用的情况下要注意
- 如果两个都设置，将会是`addOrigins("*")`生效。这一点可以去翻源码

    位置：org.springframework.web.cors.CorsConfiguration#checkOrigin

## 请求头冲突的问题

如果使用Spring Gateway作为网关，后面再挂着Spring Web作为服务，并且它们都正确配置了跨域。那么正常情况下，响应的请求头就会出现两份完全一样的跨域头部，像下面这样

```yaml
vary: Origin
access-control-allow-credentials: true
access-control-allow-origin: xxxx
vary: Origin
access-control-allow-credentials: true
access-control-allow-origin: xxxx
```

这似乎不违反HTTP关于请求头重复的规定，但在跨域的机制中，却是不可接收的，可能出现这种错误

```bash
Access to XMLHttpRequest at 'xxxxx' from origin 'http://localhost:3200' has been blocked by CORS policy: 
The 'Access-Control-Allow-Origin' header contains multiple values '*, http://localhost:3200', but only one is allowed.
```

解决办法就是在网关对重复的头部进行处理，我们可以用过滤器：DedupeResponseHeader

```yaml
spring.cloud.gateway.default-filters[0]=DedupeResponseHeader=Vary Access-Control-Allow-Origin Access-Control-Allow-Credentials
```

它默认保留重复头中的第一个，具体参见[手册]([https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#the-deduperesponseheader-gatewayfilter-factory](https://docs.spring.io/spring-cloud-gateway/docs/current/reference/html/#the-deduperesponseheader-gatewayfilter-factory))

## Vary怎么说

我们总是能看到响应中有Vary头部，它有什么用？服务端是如何生成的？

根据[标准]([https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Vary](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Headers/Vary))，它是被服务器用来声明一个请求的响应的变化依据，浏览器可用它来控制缓存。比如对`Vary: Origin`，它表示，对同一个请求，服务器针对不同的源站有不同的响应。

服务端是如何生成的呢？确切地讲，不同场景下有不同的生成方式，比如Spring Web中如果开启了跨域，默认会在响应上添加Vary请求头，写死的，其值包含

- Origin
- Access-Control-Request-Method
- Access-Control-Request-Headers

源码参见：org.springframework.web.cors.reactive.DefaultCorsProcessor#VARY_HEADERS

```java
private static final List<String> VARY_HEADERS = Arrays.asList(
			HttpHeaders.ORIGIN, HttpHeaders.ACCESS_CONTROL_REQUEST_METHOD, HttpHeaders.ACCESS_CONTROL_REQUEST_HEADERS);

@Override
public boolean process(@Nullable CorsConfiguration config, ServerWebExchange exchange) {

	ServerHttpRequest request = exchange.getRequest();
	ServerHttpResponse response = exchange.getResponse();
	HttpHeaders responseHeaders = response.getHeaders();

	List<String> varyHeaders = responseHeaders.get(HttpHeaders.VARY);
        // 如果当前响应没有包含Vary，则加上
	if (varyHeaders == null) {
		responseHeaders.addAll(HttpHeaders.VARY, VARY_HEADERS);
	}
	... ...
}
```
## Spring Cloud同时使用DedupeResponseHeader和WebSocket

Spring Cloud中同时使用DedupeResponseHeader和WebSocket会报错。如下，这是握手成功后抛出的异常。

```bash
java.lang.UnsupportedOperationException
	at org.springframework.http.ReadOnlyHttpHeaders.set(ReadOnlyHttpHeaders.java:106)
```

**原因**

Spring Cloud对WebSocket有特殊处理，位于过滤器WebsocketRoutingFilter中，与这部分相关的逻辑位于：org.springframework.web.reactive.socket.server.upgrade.ReactorNettyRequestUpgradeStrategy#upgrade

```kotlin
@Override
public Mono<Void> upgrade(ServerWebExchange exchange, WebSocketHandler handler,
		@Nullable String subProtocol, Supplier<HandshakeInfo> handshakeInfoFactory) {

	ServerHttpResponse response = exchange.getResponse();
	HttpServerResponse reactorResponse = ServerHttpResponseDecorator.getNativeResponse(response);
	HandshakeInfo handshakeInfo = handshakeInfoFactory.get();
	NettyDataBufferFactory bufferFactory = (NettyDataBufferFactory) response.bufferFactory();
	URI uri = exchange.getRequest().getURI();

	// Trigger WebFlux preCommit actions and upgrade
	return response.setComplete()
			.then(Mono.defer(() -> {
				WebsocketServerSpec spec = buildSpec(subProtocol);
				return reactorResponse.sendWebsocket((in, out) -> {
					ReactorNettyWebSocketSession session =
							new ReactorNettyWebSocketSession(
									in, out, handshakeInfo, bufferFactory, spec.maxFramePayloadLength());
					return handler.handle(session).checkpoint(uri + " [ReactorNettyRequestUpgradeStrategy]");
				}, spec);
			}));
}
```

其中的关键点是，response.setComplete()，这里已经将response设置为完成状态，后续过滤器就无法再操作其内容，而我们设置的DedupeResponseHeader过滤器就在它的后面，因此报错。

**解决**

这里，要明白两个点

- WebSocket握手成功后的响应头，不会存在重复的情况，这一点由WebSocket相关的Filter自己去保证
- DedupeResponseHeader，不会去判断response是否已经完成

为此，可以自定义DedupeResponseHeader，加上对response的完成状态进行判断的逻辑。如下，整个逻辑完全照抄DedupeResponseHeaderGatewayFilterFactory，连Config和Strategy都沿用，这样能够使得对它的使用上完全和DedupeResponseHeader一致。

```kotlin
@Component
class CustomDedupeResponseHeaderGatewayFilterFactory : AbstractGatewayFilterFactory<Config>(Config::class.java) {

    init {
        log.info("Loaded GatewayFilterFactory [CustomDedupeResponseHeader]")
    }

    override fun shortcutFieldOrder(): List<String> {
        return listOf(NAME_KEY, "strategy")
    }

    override fun apply(config: Config) = GatewayFilter { exchange, chain ->
        chain.filter(exchange).then(Mono.fromRunnable {
            if (!exchange.response.isCommitted) {
                dedupe(exchange.response.headers, config)
            }
        })
    }

    private fun dedupe(headers: HttpHeaders?, config: Config) {
        val names = config.name
        val strategy = config.strategy
        if (headers == null || names == null || strategy == null) {
            return
        }
        for (name in names.split(" ".toRegex()).toTypedArray()) {
            dedupe(headers, name.trim { it <= ' ' }, strategy)
        }
    }

    private fun dedupe(headers: HttpHeaders, name: String, strategy: Strategy) {
        val values = headers[name]
        if (values == null || values.size <= 1) {
            return
        }
        when (strategy) {
            Strategy.RETAIN_FIRST -> headers[name] = values[0]
            Strategy.RETAIN_LAST -> headers[name] = values[values.size - 1]
            Strategy.RETAIN_UNIQUE -> headers[name] = values.stream().distinct().collect(Collectors.toList())
            else -> Unit
        }
    }

}
```

配置

```kotlin
spring.cloud.gateway.default-filters[0]=CustomDedupeResponseHeader=Vary Access-Control-Allow-Origin Access-Control-Allow-Credentials
```