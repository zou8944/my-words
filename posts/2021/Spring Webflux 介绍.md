---
created_at: 2021-03-15 23:41:04.013
updated_at: 2021-03-20 20:24:34.764
slug: spring-webflux-introduction
tags: 
- Spring
- Spring Webflux
---

> 说明：文章中代码参考使用方式即可，请忽略其代表的逻辑部分

## 为何想要用Spring Webflux?

《每记》是一款新产品。一开始想用webflux，为什么呢？这里给出自己的几点理由

- Spring生态加持，想必会很好用
- 一直只闻其声不见其人，很想用用
- 原计划中的vertx-spring项目，想要做成的结果，和webflux很像；因此希望从webflux中找到一些发现

<!-- more -->

### 《每记》技术构成

《每记》的主要业务逻辑都在客户端，后端只需要负责用户接口和数据备份。需要用到的技术只有两个

- grpc —— 用于grpc服务，如user-service，media-service
- 数据库 —— 用于数据存取

grpc的官方库实现基于Netty，天然响应式，能够和webflux结合得比较好；

数据库方面，Spring官方提供R2DBC，但它所处的技术层级和JDBC类似，且尚不成熟，从官方手册的描述就不是很敢用于生产。

> Spring Data R2DBC aims at being conceptually easy. In order to achieve this it does NOT offer caching, lazy loading, write behind or many other features of ORM frameworks. This makes Spring Data R2DBC a simple, limited, opinionated object mapper.

至于其他的异步数据库链接库，不成体系，使用不便。因此还是使用JDBC。

至于ORM框架，考虑了MyBatis plus、jooq、korm几种，还是认为MyBatis plus相对方便。

于是技术组成就是：

Spring Webflux + GRPC + MyBatis plus

Spring WebMVC + GRPC + Myabtis plus （作为对比）

## Webflux简介

横向看，WebFlux组成大致如下

![tapd_61207716_1615454473_19](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/tapd_61207716_1615454473_19_1616242796287.png)

这和WebMVC的结构图很像，解释一下各部分工作。

- 容器reactor-netty：即基于netty实现的符合reactor标准的容器，Spring Boot默认使用它。其对应的关键核心接口是HttpHandler，webflux中对应的重要实现类是：WebHttpHandlerBuilder，它是整个webflux程序的入口。
- Webfilter：过滤器
- DispatcherHandler：核心处理器，协调如下三个核心组件工作
  - HandleMapping：存储请求URI和处理器的对应关系
  - HandlerAdapter：封装了主要处理逻辑，处理结果封装成HandlerResult
  - HandlerResultHandler：针对上一步结果的处理器
- WebExceptionHandler：整个流程中抛出的任何异常，都会被它捕获，“真”全局异常处理

如想了解进一步内容，请从源码挖掘。

## 使用

本节介绍Webflux的使用方式。Webflux有两种使用方式

- 注解式
- 编程式

我们选择注解式，更为方便。至于API风格，选择kotlin协程。

具体使用方式参见mylog的spring-webflux分支，这里列出几个关键点。

### 路由

使用方式和一般的MVC程序没有什么区别，除了一点

- 方法需要是suspend方法或返回Mono/Flux

```kotlin
@RestController
class ResourceController(
    private val resourceService: ResourceService
) {

    @PostMapping("resources/:push")
    suspend fun push(
        @RequestBody pushRequest: PushRequest
    ): PushResponse {
        val result = resourceService.validateAndSave(pushRequest.resources)
        return PushResponse(result.map { it.data as Map<String, Any> })
    }
}
```

### 过滤器

Webflux中没有拦截器这个概念，要做类似的工作需要在过滤器中完成，项目中我们用到Token验证，使用方法是注册过滤器。

```kotlin
@Component
class AuthFilter(applicationContext: ApplicationContext) : AbstractAuthFilter(applicationContext) {

    @Value("\${authentication.token.name}")
    lateinit var tokenName: String

    // 注意这里使用了协程的grpc stub
    @GrpcClient("user-service")
    lateinit var userStub: UsersServiceGrpcKt.UsersServiceCoroutineStub

    override fun filter(exchange: ServerWebExchange, chain: WebFilterChain): Mono<Void> = mono {
        val request = exchange.request

        if (request.needAuth()) {
            val token = request.headers[tokenName]?.first() 
            val result = userStub.verify(Token.newBuilder().setToken(token).build())
            ... ...
        }

        // chain.filter返回的是Mono，需要调用await方法转换为协程
        chain.filter(exchange).awaitSingleOrNull()
    }

}
```

### 全局异常处理

Webflux中可以使用@ControllerAdvice注册全局异常处理器，但它仅Controller中抛出的异常生效，无法顾及到过滤器。对异常，推荐的方式是注册WebExceptionHandler。

```kotlin
@Component
@Order(Ordered.HIGHEST_PRECEDENCE)
class ExceptionHandler : ErrorWebExceptionHandler {

    private val objectMapper = ObjectMapper()

    // 对协程的支持
    override fun handle(exchange: ServerWebExchange, ex: Throwable): Mono<Void> {

        val errResponse = objectMapper.writeValueAsBytes("error message")

        response.headers.contentType = MediaType.APPLICATION_PROBLEM_JSON
        response.statusCode = code.httpStatus

        return response.writeWith(Mono.just(response.bufferFactory().wrap(errResponse)))
    }
}
```

### 同步DAO的调用

JDBC是同步的，基于它的MyBatis也是同步的，为了不阻塞DIspatcher-Worker线程，需要将其手动调度到其他线程池。当然如下步骤也可以使用AOP实现，这样就不用为每个方法手动调mono方法。

```kotlin
// 注入Scheduler
@Autowired
private lateinit var scheduler: Scheduler
// 讲同步代码注册到该scheduler
protected fun <T> mono(block: () -> T): Mono<T> {
    return Mono.defer { Mono.just(block()) }.subscribeOn(scheduler)
}

// 调用方式
fun save(modifications: List<Resource>): Mono<List<Resource>> = mono {
    modifications.mapNotNull {
        resourceMapper.save(it)
    }
}
```

### Swagger

Knife4j的增强功能无法在Webflux下使用，且当controller为suspend方法时无法正常读取到返回值，需要打如下补丁。

```kotlin
/**
 *  修复controller方法为suspend方法时，springfox无法获取返回值类型的情况
 *  因为suspend方法转换为字节码后返回值为null
 *  #issue: https://github.com/springfox/springfox/issues/3241
 */
@Component
@Primary
class CustomRequestHandler(
    private val resolver: TypeResolver
) : HandlerMethodResolver(resolver) {

    override fun methodReturnType(handlerMethod: HandlerMethod): ResolvedType {
        val func = handlerMethod.beanType.kotlin.declaredFunctions.first { it.javaMethod == handlerMethod.method }
        if (func.returnType == Unit::class.starProjectedType) resolver.resolve(Void.TYPE)
        return resolver.resolve(func.returnType.javaType)
    }

}
```
## 测试

以一个最典型的接口resources/:pull进行压力测试，该接口逻辑如下

- 访问user-service验证token
- 访问数据库读取数据

测试工具为apache-utils，ab。

测试结果总结就是：相同条件下，webflux的性能表现相比webmvc并没有什么变化。

## 初步结论 —— 不选择

### 优点

- 本身的异步模型
- Spring生态支持，依赖注入，注解，协程

### 缺点

- 整体生态的缺乏，首要的是异步ORM
- 响应式的固有问题，学习曲线

## 不选择的原因

- 实际测试下来，性能并没有实质性的提升，反而增加了开发难度
  - 需要桥接阻塞的ORM库存
  - Springfox打补丁
  - 没有拦截器，只有过滤器，做权限验证时不方便
  - 其它未知的点
- 上手成本，从近期招聘简历上看，熟悉响应式的人少之又少，我们有极大可能招聘到一个对此不熟悉的人，技术墙还是有的。

综上，如果引入webflux，并没有带来好处，反而有诸多不便。因此最终决定使用webmvc。