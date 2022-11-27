---
created_at: 2020-11-03 23:44:18.0
updated_at: 2021-02-16 23:44:32.966
slug: vertx-source-code-analyze-web
tags: 
- Vert.x
- 源码剖析
---

我们在前面的文章分析了Vertx核心单机部分的源码。今天轮到[Vert.x-Web](https://vertx-web-site.github.io/docs/vertx-web/java/)，由于Web的内容比较多，因此分为上下两部分。

- 上：分析Vert.x-Web核心类及其主要能力。
- 下：分析HttpServer的线程调度以及Web OpenAPI的工作原理

<!-- more -->

一个基本的VertxWeb代码片段如下：

```kotlin
fun main() {
    val vertx = Vertx.vertx()
    val router = Router.router(vertx)
    router.get("/hello")
        .handler { ctx ->
                  println("哈哈哈，我好开心")
                  ctx.next()
                 }
    .failureHandler(ErrorHandler.create())
    val server = vertx.createHttpServer().requestHandler(router)
    server.listen(8080)
}
```

上面创建了一个Http服务，暴露8080端口，并注册了一个path为hello，方法为GET的接口。上面涉及到Vert.x-Web的类有：Router、Route、RoutingContext、HttpServer。我们介绍前三个。

## Router

### Router

首先是Router接口，它主要有以下几个方面组成。

- Router.router(vertx) 创建一个Router对象

- routeXXX() 各种路由方法，可以根据路径、方法、媒体类型、正则表达式等各种方式路由，返回一个Route对象，用于指定处理器。

- getRoutes() 获取所有route

- clear() 清除所有Route

- mountSubRouter() 挂载子router

- exceptionHandler() 指定一个router级别的异常处理器，当handler中抛出异常时，它会捕获。但它不会影响正常业务逻辑。

  但它目前已被废弃，应该使用errorHandler()，它对应的是500的错误

- errorHandler(code, handler)  当发生特定错误码时会调用它。当RoutingContext失败(fail) 或 一些handler失败但没有写响应 或 handler中抛出了异常，都会调用它。需要注意的是它的500有特殊的意义，代表通用错误。

- handleContext(context) 将一个RoutingContext传进来，当一个Router被挂载到某个route时会用：将该route的RoutingContext传入本router进行处理。

- handleFailure(RoutingContext) 使用场景同上，处理失败

- modifiedHandler(handler) 当本Router的Route发生变化时该方法会被触发。

首先说，Router只是Handler的子类，因此本质上还只是一个处理器，是被动调用的。

```java
@VertxGen
public interface Router extends Handler<HttpServerRequest> {
... ...
```

### RouterImpl

众多route生成方法的实现都大同小异，都是创建RouteImpl

```kotlin
public synchronized Route route(String path) {
  state = state.incrementOrderSequence();
  return new RouteImpl(this, state.getOrderSequence(), path);
}
```

另外一个重点是handle，既然Router是Handler的子类，因此本类最初被调用的一定是handle方法（**在请求进来时调用**）

```kotlin
@Override
public void handle(HttpServerRequest request) {
    // 注意后面的next()调用，这很容易被看漏掉。
    new RoutingContextImpl(null, this, request, state.getRoutes()).next();
}
```

啥也没干，就**创建了一个RoutingContextImpl，并调用了next()，开启处理逻辑**。

### RouterState

一个RouterImpl包含一个RouterState，在初始化时创建，用于管理Router的状态

```kotlin
public RouterImpl(Vertx vertx) {
    this.vertx = vertx;
    this.state = new RouterState(this);
}
```

共有如下几种状态

- Route集合：Router内注册的Route全在这里
- errorHandler映射：失败的处理器，其中key对应的错误码，如400
- modifiedHandler：用于在Router发生变化时做出响应的处理器

```kotlin
private final Set<RouteImpl> routes;
private final Map<Integer, Handler<RoutingContext>> errorHandlers;
private final Handler<Router> modifiedHandler;
```

## Route

### Route

一个接口，对路由信息的描述，包含如下几种信息，见名思义。

- method
- path
- regex
- consumes
- produces

同时包含了对匹配到的请求的处理方式

- handler()：为Route添加一个处理器，多个handler之间会连缀调用。
- failureHandler()：为Route添加一个失败处理器，多个handler之间会连缀调用。
- blockingHandler()：为Route添加一个能够执行阻塞操作的处理器。
- subRouter()：为Route添加一个子Router，符合要求的请求都会被转发给该Router。

### RouteImpl

就是对上面各个方法的实现，这里不赘述。

### RouteState

对一个路由状态的持有，相对RouterState而言，它持有的状态复杂得多。

```kotlin
// 路径
private final String path;
// 顺序
private final int order;
// 是否开启
private final boolean enabled;
// 方法
private final Set<HttpMethod> methods;
// 消费的多媒体类型
private final Set<MIMEHeader> consumes;
// 是否允许body为空
private final boolean emptyBodyPermittedWithConsumes;
// 产生的多媒体类型
private final Set<MIMEHeader> produces;
// 常规处理器集合
private final List<Handler<RoutingContext>> contextHandlers;
// 失败处理器集合
private final List<Handler<RoutingContext>> failureHandlers;
// 不知道干嘛的
private final boolean added;
// 用于匹配的正则
private final Pattern pattern;
// 也属于正则表达式的一部分
private final List<String> groups;
// 是否使用归一化路径
private final boolean useNormalisedPath;
// 还是正则表达式
private final Set<String> namedGroupsInRegex;
// 主机匹配
private final Pattern virtualHostPattern;
// 路径是否以斜杠结尾
private final boolean pathEndsWithSlash;
// 是否被排除
private final boolean exclusive;
// 是否精确匹配
private final boolean exactPath;
```

对Route最重要的方法当然是判断是否匹配，该方法也是在RouteState中给出

io.vertx.ext.web.impl.RouteState#matches，逻辑比较复杂，有兴趣可以去看看

## RoutingContext

RoutingContext是Router上下文的抽象，代表一个请求从进入到响应全阶段的状态。由于在Router.handle()中，直接创建了RoutingContextImpl对象，并调用了RoutingContext.next()，因此我们重点关注它。

```kotlin
// RoutingContext的实现类RoutingContextImpl的构造方法
public RoutingContextImpl(String mountPoint, RouterImpl router, HttpServerRequest request, Set<RouteImpl> routes) {
    super(mountPoint, request, routes);
    this.router = router;
    this.fillParsedHeaders(request);
    if (request.path().length() == 0) {
        this.fail(400);
    } else if (request.path().charAt(0) != '/') {
        this.fail(404);
    }
}
// RoutingContextImpl的父类RoutingContextImplBase的构造方法
RoutingContextImplBase(String mountPoint, HttpServerRequest request, Set<RouteImpl> routes) {
    this.mountPoint = mountPoint;
    this.request = new HttpServerRequestWrapper(request);
    this.routes = routes;
    this.iter = routes.iterator();
    this.currentRouteNextHandlerIndex = new AtomicInteger(0);
    this.currentRouteNextFailureHandlerIndex = new AtomicInteger(0);
    this.resetMatchFailure();
}

// next方法
public void next() {
    if (!this.iterateNext()) {
        this.checkHandleNoMatch();
    }
}
```

仔细看iterateNext()

```kotlin
boolean iterateNext() {
    boolean failed = this.failed();
    // 在route的第二个handler调用next时，走的是这段逻辑。
    if (this.currentRoute != null) {
        try {
            if (!failed && this.currentRoute.hasNextContextHandler(this)) {
                this.currentRouteNextHandlerIndex.incrementAndGet();
                this.resetMatchFailure();
                this.currentRoute.handleContext(this);
                return true;
            }

            if (failed && this.currentRoute.hasNextFailureHandler(this)) {
                this.currentRouteNextFailureHandlerIndex.incrementAndGet();
                this.currentRoute.handleFailure(this);
                return true;
            }
        } catch (Throwable var5) {
            this.handleInHandlerRuntimeFailure(this.currentRoute.getRouter(), failed, var5);
            return true;
        }
    }

    // 死循环迭代所有route
    while(true) {
        // this.iter是Router.getRoutes().iterator()得到的，即迭代所有routes
        if (this.iter.hasNext()) {
            // RouteState包含了所有Route的状态和内容，因此要操作Route就一定要获取它啦
            RouteState routeState = ((RouteImpl)this.iter.next()).state();
            this.currentRouteNextHandlerIndex.set(0);
            this.currentRouteNextFailureHandlerIndex.set(0);

            try {
                // 匹配结果是0或4开头的状态码，如果是0则表示成功。这意味着每个route都会匹配一次，也一定会有一个结果。
                int matchResult = routeState.matches(this, this.mountPoint(), failed);
                // 匹配失败的情况
                if (matchResult != 0) {
                    if (matchResult == 405) {
                        if (this.matchFailure == 404) {
                            this.matchFailure = matchResult;
                        }
                    } else if (matchResult != 404) {
                        this.matchFailure = matchResult;
                    }
                    continue;
                }

                // 匹配成功的情况
                this.resetMatchFailure();

                try {
                    this.currentRoute = routeState;、

                    if (failed && this.currentRoute.hasNextFailureHandler(this)) {
	                    // 如果有失败，则调用route原先保存的failureHandler
                        this.currentRouteNextFailureHandlerIndex.incrementAndGet();
                        routeState.handleFailure(this);
                    } else {
                        // 如果成功，则调用route原先保存的contextHandler
                        if (!this.currentRoute.hasNextContextHandler(this)) {
                            continue;
                        }

                        this.currentRouteNextHandlerIndex.incrementAndGet();
                        routeState.handleContext(this);
                    }
                } catch (Throwable var6) {
                    this.handleInHandlerRuntimeFailure(routeState.getRouter(), failed, var6);
                }

                return true;
            } catch (Throwable var7) {
                if (LOG.isTraceEnabled()) {
                    LOG.trace("IllegalArgumentException thrown during iteration", var7);
                }

                if (!this.response().ended()) {
                    this.unhandledFailure(var7 instanceof IllegalArgumentException ? 400 : -1, var7, routeState.getRouter());
                }

                return true;
            }
        }

        return false;
    }
}
```

再来仔细看

```kotlin
private void checkHandleNoMatch() {
    if (this.failed()) {
	    // 如果失败了，则按照未处理的异常处理，即从router的errorHandler中获取对应code的handler并给出结果
        this.unhandledFailure(this.statusCode, this.failure, this.router);
    } else {
        // 没有失败时也获取以下，有说明是预期的失败，还是要处理。
        Handler<RoutingContext> handler = this.router.getErrorHandlerByStatusCode(this.matchFailure);
        this.statusCode = this.matchFailure;
        if (handler == null) {
            this.response().setStatusCode(this.matchFailure);
            // 404的情况
            if (this.request().method() != HttpMethod.HEAD && this.matchFailure == 404) {
                this.response().putHeader(HttpHeaderNames.CONTENT_TYPE, "text/html; charset=utf-8").end("<html><body><h1>Resource not found</h1></body></html>");
            } else {
                // 常规情况，直接结束
                this.response().end();
            }
        } else {
            handler.handle(this);
        }
    }

}
```

## 总结

到现在，抛开Router是被谁调用这问题。我们知道**整个RoutingContext的执行起始是Router的handle方法：它创建RoutingContextImpl对象，并调用next()启动route的匹配操作，并在匹配后调用对应route的正常handler链或失败handler链。**

这里掌握三个关键点

- **RoutingContext对象是在Router的handle中创建的，并在匹配到的route的handler中流转。**
- **遍历所有route的过程会在每次请求进来被处理。逻辑在iterateNext()方法的下半部分。**
- **route的handler链调用比较特殊，需要开发者手动调用RoutingContext的next()方法处理。逻辑在iterateNext()方法的上半部分。**
- **在从Router的handle开始，都是在当前线程不阻塞地执行，可以一镜到底。**

对于Web的整个处理链，我们弄得差不多了。现在还存在如下问题，我们留待下篇再来看。

- 谁构建HttpServerRequest并调用了Router的handler？
- 调用Router时线程分配是如何的？

