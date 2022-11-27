---
created_at: 2020-10-03 23:43:22.0
updated_at: 2021-02-16 23:43:48.611
slug: vertx-source-code-analyze-code
tags: 
- Vert.x
- 源码剖析
---

> 希望通过本文的解析，让读者了解Vertx的关键部分的实现原理。对诸如如下问题有一个具象的认识。
>
> - Vertx实例的作用？一个应用是否只对应一个Vertx实例？
> - Verticle是一个怎样的存在？
> - 本地模式下消息是如何在EventBus上传输和响应的？
> - EventBus和EventLoop是如何关联起来的？

<!-- more -->

## 概述

Vert.x是一个事件驱动，基于Netty库构建的高性能应用程序框架。实现了所谓的Multi-Reactor模型，能够充分利用多核CPU实现以事件循环为基础的基本编程模型。同时在此基础上构建了Verticle这样类似Actor的概念，以应对并发编程的需求。

Vert.x的核心为EventBus和EventLoop，前者用户消息传输，作为联通各个Handler的神经系统；后者作为任务执行的调度者，保证高性能。任何使用Vert.x构建的应用，都必须围绕这二者作文章。否则就失去了使用它的意义。

## **核心类**

### Vertx

Vertx是最为核心的类，创建任何Vertx组件几乎都需要Vertx类的实例。

创建一个单机实例的方法是`Vertx.vertx()`，然后就可以使用了。以此为入口，我们看看Vertx在创建时都做了什么。

#### 看继承关系

Vertx是一个接口，VertxImpl是最终实现类，也是唯一的实现类。其中包含了单机和集群两种模式的实现。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110710869.png#pic_center)
```java
// 单机实现，创建返回VertxImpl即可
static VertxImpl vertx(VertxOptions options, Transport transport) {
    VertxImpl vertx = new VertxImpl(options, transport);
    vertx.init();
    return vertx;
}
// 集群实现，创建并加入集群
static void clusteredVertx(VertxOptions options, Transport transport, Handler<AsyncResult<Vertx>> resultHandler) {
    VertxImpl vertx = new VertxImpl(options, transport);
    vertx.joinCluster(options, resultHandler);
}
```

#### 看Vertx接口的功能

从Vertx接口，看Vertx能干啥。图太长，不方便放，这里只列举核心部分，也是我们用得最多的。

- 创建单机/集群版的Vertx实例
- 创建或获取上下文Context
- 指定特定的Handler运行在当前上下文中
- 获取EventBus
- 获取共享数据
- 设定定时任务
- 发布Verticle
- 执行阻塞方法

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110732393.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)
如上，Vertx类几乎撑起了所有部分。接着我们看它是如何做到的。

#### 看VertxImpl构造方法

VertxImpl在构造时创建了很多私有对象，具体如下。

```java
private VertxImpl(VertxOptions options, Transport transport) {
    // 创建closeHooks，CloseHooks维护了一个Closeable的Set，可向其中添加、移除任务，还有执行所有钩子的run方法啦。
    closeHooks = new CloseHooks(log);
    // 创建线程阻塞检查器，它启动一个名为vertx-blocked-thread-checker的定时器，
    checker = new BlockedThreadChecker(options.getBlockedThreadCheckInterval(), options.getBlockedThreadCheckIntervalUnit(), options.getWarningExceptionTime(), options.getWarningExceptionTimeUnit());
    // 指定一个EventLoop最长可以连续执行多久
    maxEventLoopExTime = options.getMaxEventLoopExecuteTime();
    maxEventLoopExecTimeUnit = options.getMaxEventLoopExecuteTimeUnit();
    // 创建EventLoop线程工厂，主要用于指定线程名称和线程阻塞检测器
    eventLoopThreadFactory = new VertxThreadFactory("vert.x-eventloop-thread-", checker, false, maxEventLoopExTime, maxEventLoopExecTimeUnit);
    // 创建EventLoopGroup，它又实际创建了NioEventLoopGroup，它是Netty的组件。一个EventLoopGroup，就是一个EventLoop组。在Netty中，一个EventLoop是线程和IO的结合，一个EventLoop始终绑定在同一个线程上。
    eventLoopGroup = transport.eventLoopGroup(Transport.IO_EVENT_LOOP_GROUP, options.getEventLoopPoolSize(), eventLoopThreadFactory, NETTY_IO_RATIO);
    // 创建一个acceptor EventLoopGroup，创建方式和上面类似。
    ThreadFactory acceptorEventLoopThreadFactory = new VertxThreadFactory("vert.x-acceptor-thread-", checker, false, options.getMaxEventLoopExecuteTime(), options.getMaxEventLoopExecuteTimeUnit());
    acceptorEventLoopGroup = transport.eventLoopGroup(Transport.ACCEPTOR_EVENT_LOOP_GROUP, 1, acceptorEventLoopThreadFactory, 100);
    // 创建worker线程池
    ExecutorService workerExec = new ThreadPoolExecutor(workerPoolSize, workerPoolSize,
                                                        0L, TimeUnit.MILLISECONDS, new LinkedTransferQueue<>(),
                                                        new VertxThreadFactory("vert.x-worker-thread-", checker, true, options.getMaxWorkerExecuteTime(), options.getMaxWorkerExecuteTimeUnit()));
    PoolMetrics workerPoolMetrics = metrics != null ? metrics.createPoolMetrics("worker", "vert.x-worker-thread", 	options.getWorkerPoolSize()) : null;
    workerPool = new WorkerPool(workerExec, workerPoolMetrics);
    // 创建inertnal阻塞线程池
    ExecutorService internalBlockingExec = Executors.newFixedThreadPool(options.getInternalBlockingPoolSize(),
                                                                        new VertxThreadFactory("vert.x-internal-blocking-", checker, true, options.getMaxWorkerExecuteTime(), options.getMaxWorkerExecuteTimeUnit()));
    internalBlockingPool = new WorkerPool(internalBlockingExec, internalBlockingPoolMetrics);
    // 创建文件解析器，在FileSystem中有使用，进行文件操作时使用的是java nio
    this.fileResolver = new FileResolver(options.getFileSystemOptions());
    // 创建地址解析器，在DNS解析时会用到
    this.addressResolver = new AddressResolver(this, options.getAddressResolverOptions());
    // 创建发布管理器，用于发布Verticle
    this.deploymentManager = new DeploymentManager(this);
    if (options.getEventBusOptions().isClustered()) {
        // 创建集群管理器和集群的EventBus
        this.clusterManager = getClusterManager(options);
        this.eventBus = new ClusteredEventBus(this, options, clusterManager);
    } else {
        // 创建本地EventBus
        this.clusterManager = null;
        this.eventBus = new EventBusImpl(this);
    }
    // 创建sharedData，允许你在整个应用中共享你的数据，包括集群范围内
    this.sharedData = new SharedDataImpl(this, clusterManager);
}
```

上面太复杂，整理成思维导图会好看很多。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110752755.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)
EventBus用于进行消息传输；

EventLoopGroup为事件循环组，是Netty库中的类，每当有新的任务都会被提交到该组中执行；

而另一个EventLoopGroup——acceptorEventLoopGroup专用于网络服务的创建，目的是避免上面的eventLoopGroup的阻塞造成服务响应不及时；

WorkerPool为单独开的线程池，负责执行阻塞操作；

FileSystem用于操作文件；

AddressResolver用于进行DNS地址解析；

SharedData用于在整个Vertx应用内部共享数据，包括集群模式；

ClusterManager用于进行集群管理；

DeploymentManager和VerticleManager用于发布Verticle，保证Verticle的特性。

所有上述类你可能都不是很熟悉，没关系，先有个印象，下面分析具体场景时会用到。

### EventBus

EventBus的继承关系也很简单，其单机版实现类为EventBusImpl，ClusteredEventBus继承自它，除了服务监听和远程调用，均使用了EventBusImpl中的方法。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110812514.png#pic_center)

EventBus的能力，以及EventBusImpl持有对象如下：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110827811.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)

出入拦截器自不必说，每次消息进来和出去都会先被拦截器处理；

vertx对象，主要用于获取发送调用代码所处的上线文环境；

handerMap是核心，以地址为key，地址上注册的Handler序列为value，存储了地址-处理器的映射管理；当触发发送动作时，就会到该映射中查找对应的处理器然后执行；对于单机应用，handlerMap就是所有；对于集群应用，则是先找到节点，再在节点中的handlerMap查找对应处理器。

sendNoContext是为了在执行发送的代码块不处于任何上下文时使用的上下文。EventBusImpl创建时使用。

EventBusImpl的构造方法没什么内容，就不提了。

```java
public EventBusImpl(VertxInternal vertx) {
    VertxMetrics metrics = vertx.metricsSPI();
    this.vertx = vertx;
    this.metrics = metrics != null ? metrics.createEventBusMetrics() : null;
    this.sendNoContext = vertx.getOrCreateContext();
}
```

### EventLoop

Vertx中并没有EventLoop这个类，它是Netty中的类。对Vertx的源码，与EventLoop相关的交互只有两处：创建EventLoopGroup；向EventLoopGroup提交任务。

具体内容请查找Netty相关资料进行学习。

### Context

Context是真正提交任务的地方，凡Vertx中涉及到任务的执行，总是少不了Context的身影。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110844860.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)
其核心能力主要在协调代码的运行，同时也可存储数据。其大部分逻辑都在ContextImpl中。其两个子类，仅在自我裁定、任务提交、上下文复制上有所不同。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110857360.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)
### Verticle

Verticle放在这里有一点另类，因为它并非核心组件。只是Vertx提供的actor模式实现的一个发布单元。它的actor特性由VerticleManager、EventBus、Context等一起保证。就其能力来说，也只有启动和停止两个方法。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003110909141.png#pic_center)
## 从EventBus看Vertx工作原理

一个简单的Vertx应用如下，我们从它开始分析。

```kotlin
fun main() {
  val vertx = Vertx.vertx();
  vertx.eventBus().consumer<String>("helloAddress").handler{
    print(it.body())
  }
  vertx.eventBus().send("helloAddress", "hello world!")
}
```

Vertx.vertx()在上面已经看过了，它创建了一个VertxImpl对象，持有一堆用于组织工作的属性，包括EventBus。

```java
// vertx实例时对eventBus赋值的快照
this.eventBus = new EventBusImpl(this);
```

### consumer做了什么

```java
@Override
public <T> MessageConsumer<T> consumer(String address, Handler<Message<T>> handler) {
    Objects.requireNonNull(handler, "handler");
    MessageConsumer<T> consumer = consumer(address);
    consumer.handler(handler);
    return consumer;
}
// 往里进一步
@Override
public <T> MessageConsumer<T> consumer(String address) {
    checkStarted();
    Objects.requireNonNull(address, "address");
    return new HandlerRegistration<>(vertx, metrics, this, address, null, false, null, -1);
}
// 重点在HandlerRegistration，收集地址后，开启超时回复定时器。
public HandlerRegistration(Vertx vertx, EventBusMetrics metrics, EventBusImpl eventBus, String address,
                               String repliedAddress, boolean localOnly,
                               Handler<AsyncResult<Message<T>>> asyncResultHandler, long timeout) {
    this.vertx = vertx;
    this.metrics = metrics;
    this.eventBus = eventBus;
    this.address = address;
    this.repliedAddress = repliedAddress;
    this.localOnly = localOnly;
    this.asyncResultHandler = asyncResultHandler;
    if (timeout != -1) {
        timeoutID = vertx.setTimer(timeout, tid -> {
            if (metrics != null) {
                metrics.replyFailure(address, ReplyFailure.TIMEOUT);
            }
            sendAsyncResultFailure(new ReplyException(ReplyFailure.TIMEOUT, "Timed out after waiting " + timeout + "(ms) for a reply. address: " + address + ", repliedAddress: " + repliedAddress));
        });
    }
}
// 最上面的consumer.handler(handler);调用了HandlerRegistration的handler方法，如下。可以看到最终是在eventBus上调用了注册方法。
@Override
public synchronized MessageConsumer<T> handler(Handler<Message<T>> h) {
    if (h != null) {
        synchronized (this) {
            handler = h;
            if (registered == null) {
                registered = eventBus.addRegistration(address, this, repliedAddress != null, localOnly);
            }
        }
        return this;
    }
    this.unregister();
    return this;
}
// 最终来到了EventBus的addRegistration方法。在addLocalRegistration中，创建了HandlerHolder，并将其加入EventBus的成员变量handlerMap，然后返回创建的HandlerHolder
protected <T> HandlerHolder<T> addRegistration(String address, HandlerRegistration<T> registration,
                                               boolean replyHandler, boolean localOnly) {
    Objects.requireNonNull(registration.getHandler(), "handler");
    LocalRegistrationResult<T> result = addLocalRegistration(address, registration, replyHandler, localOnly);
    addRegistration(result.newAddress, address, replyHandler, localOnly, registration::setResult);
    return result.holder;
}
```

要点总结

- consumer方法仅仅将给定的handler注册到EventBusImpl持有的handlerMap中，等待被消费。

### send做了什么

```java
//通过跟踪，最终会来到sendOrPubInternal，首先创建一个用于回复的HandlerRegistration，然后创建OutboundDeliveryContext，调用其next方法
public <T> void sendOrPubInternal(MessageImpl message, DeliveryOptions options,
                                  Handler<AsyncResult<Message<T>>> replyHandler) {
    checkStarted();
    HandlerRegistration<T> replyHandlerRegistration = createReplyHandlerRegistration(message, options, replyHandler);
    OutboundDeliveryContext<T> sendContext = new OutboundDeliveryContext<>(message, options, replyHandlerRegistration);
    sendContext.next();
}
// createReplyHandlerRegistration方法创建了__vertx.reply.xxx地址的响应HandlerRegistration
private <T> HandlerRegistration<T> createReplyHandlerRegistration(MessageImpl message,
                                                                  DeliveryOptions options,
                                                                  Handler<AsyncResult<Message<T>>> replyHandler) {
    if (replyHandler != null) {
        long timeout = options.getSendTimeout();
        String replyAddress = generateReplyAddress();
        message.setReplyAddress(replyAddress);
        Handler<Message<T>> simpleReplyHandler = convertHandler(replyHandler);
        HandlerRegistration<T> registration =
            new HandlerRegistration<>(vertx, metrics, this, replyAddress, message.address, true, replyHandler, timeout);
        registration.handler(simpleReplyHandler);
        return registration;
    } else {
        return null;
    }
}
protected String generateReplyAddress() {
    return "__vertx.reply." + Long.toString(replySequence.incrementAndGet());
}
// OutboundDeliveryContext类接收了消息和响应HandlerRegistration，调用next，如下。其中的iter多半是拦截器，暂时不用管。核心在sendOrPub(this)和sendReply(this, replierMessage)
@Override
public void next() {
    if (iter.hasNext()) {
        Handler<DeliveryContext> handler = iter.next();
        try {
            if (handler != null) {
                handler.handle(this);
            } else {
                next();
            }
        } catch (Throwable t) {
            log.error("Failure in interceptor", t);
        }
    } else {
        if (replierMessage == null) {
            sendOrPub(this);
        } else {
            sendReply(this, replierMessage);
        }
    }
}
// 定义io.vertx.core.eventbus.impl.EventBusImpl#sendOrPub，再定位到io.vertx.core.eventbus.impl.EventBusImpl#deliverMessageLocally,最终来到io.vertx.core.eventbus.impl.EventBusImpl#deliverMessageLocally
// 这里的关键由两个地方：一是点对点的实现——再handlerMap中找到指定地址的handlers，只取第一个进行处理；还有发布订阅的实现——对在一个地址注册的handlers全部处理；第二个关键点是消息发送的方法deliverToHandler(msg, holder)
protected ReplyException deliverMessageLocally(MessageImpl msg) {
    msg.setBus(this);
    ConcurrentCyclicSequence<HandlerHolder> handlers = handlerMap.get(msg.address());
    if (handlers != null) {
        if (msg.isSend()) {
            //Choose one
            HandlerHolder holder = handlers.next();
            if (metrics != null) {
                metrics.messageReceived(msg.address(), !msg.isSend(), isMessageLocal(msg), holder != null ? 1 : 0);
            }
            if (holder != null) {
                deliverToHandler(msg, holder);
                Handler<AsyncResult<Void>> handler = msg.writeHandler;
                if (handler != null) {
                    handler.handle(Future.succeededFuture());
                }
            }
        } else {
            // Publish
            if (metrics != null) {
                metrics.messageReceived(msg.address(), !msg.isSend(), isMessageLocal(msg), handlers.size());
            }
            for (HandlerHolder holder: handlers) {
                deliverToHandler(msg, holder);
            }
            Handler<AsyncResult<Void>> handler = msg.writeHandler;
            if (handler != null) {
                handler.handle(Future.succeededFuture());
            }
        }
        return null;
    } else {
        ... ...
    }
}
// 最终的处理函数如下：创建InboundDeliveryContext，在HandlerHolder的context环境下运行其next方法：
private <T> void deliverToHandler(MessageImpl msg, HandlerHolder<T> holder) {
    // Each handler gets a fresh copy
    MessageImpl copied = msg.copyBeforeReceive();
    DeliveryContext<T> receiveContext = new InboundDeliveryContext<>(copied, holder);

    if (metrics != null) {
        metrics.scheduleMessage(holder.getHandler().getMetric(), msg.isLocal());
    }

    holder.getContext().runOnContext((v) -> {
        try {
            receiveContext.next();
        } finally {
            if (holder.isReplyHandler()) {
                holder.getHandler().unregister();
            }
        }
    });
}
// next方法啥也没干，直接将message传入目标handler
@Override
public void next() {
    if (iter.hasNext()) {
        // ... 拦截器迭代，忽略
    } else {
        holder.getHandler().handle(message);
    }
}
```

要点总结

- send分为两步
  - 查询handler，调用send时马上执行，是同步的。
  - 执行handler，通过handler注册时的context执行，是异步的。
- 消息响应的实现方式是注册一个响应handler到EventBus中，名为__vertx.reply.xxx，其中xxx为单调递增数字。
- 如果同一地址注册了多个handler，则点对点传输模式下只会取第一个handler进行处理；发布模式下才会执行所有。
- 在一个上下文中注册的handler，不管被执行时机如何，最终都会在该上下文中执行。参见：`holder.getContext().runOnContext(...`，hodler为HandlerHolder对象，在调用consumer注册时保存了注册上下文。

### 和EventLoop的关系在哪？

通过consumer和send看到了EventBus是如何协调接收和发送的，但并没有看到EventLoop是如何参与的。其实它是有参与的，在`holder.getContext().runOnContext(...`是进行了参与。

于是我们看看EventLoopContext.runOnContext()，如下。就是向Context保存的EventLoop对象提交一个任务即可。调度的事，交给Netty来做

```java
// 看到只调用了一个executeAsync()
@Override
public void runOnContext(Handler<Void> task) {
    try {
        executeAsync(task);
    } catch (RejectedExecutionException ignore) {
        // Pool is already shut down
    }
}
// 这里就能看到Vertx的底了，它直接将任务提交给了netty的eventLoop
void executeAsync(Handler<Void> task) {
    nettyEventLoop().execute(() -> executeTask(null, task));
}
```

## Verticle工作机制

Vert.x推荐使用Verticle进行开发，它是一个类Actor的模型，具有如下特点。

- 同一Verticle下的所有操作均在一个EventLoop线程上执行。以此避免了线程安全问题。
- Verticle之间通过EventBus进行消息传递
- Verticle具有父子层级关系

一个典型的代码结构如下（官方starter使用Launcher启动的应用，本质上也是通过这种方式启动的）

```kotlin
class Verticle1 : AbstractVerticle() {
    override fun start() {
        println("Verticle 1 started")
    }
}

class Verticle2 : AbstractVerticle() {
    override fun start() {
        println("Verticle 2 started")
    }
}

fun main() {
    val vertx = Vertx.vertx();
    vertx.deployVerticle(Verticle1::class.java.canonicalName)
    vertx.deployVerticle(Verticle2::class.java.canonicalName)
}
```

我们需要探究的问题是

- deployVerticle时发生了什么？
- start()和stop()方法什么时候被调用？
- 如何保证一个Verticle下的所有操作都在一个EventLoop线程上执行？
- 父子层级关系如何维持？有什么作用？

要搞清楚这些问题，我们先看几个与此相关的类

### Deployment

维护一个发布状态，父子状态也是由它维护的。其唯一实现类DeploymentImpl是作为DeploymentManager的私有内部类存在的。这意味着Verticle发布的所有操作都在DeploymentManager内完成。

其中可能需要解释的点是getVerticles()，这意味着一个Deployment可以有多个Verticle吗？一定程度上是，但仅当一个Verticle需要发布多个实例时，才会存在多个Verticle对象。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003111022872.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)
其中需要重点关注的方法是`io.vertx.core.impl.DeploymentManager.DeploymentImpl#doUndeploy`和`io.vertx.core.impl.DeploymentManager.DeploymentImpl#doUndeployChildren`，两个方法递归调用，完成了指定Verticle及其子Verticle的取消。

```java
public synchronized Future<Void> doUndeploy(ContextInternal undeployingContext) {
    if (status == ST_UNDEPLOYED) {
        return Future.failedFuture(new IllegalStateException("Already undeployed"));
    }
    // 子发布不为空，则先取消子发布，成功后再取消当前发布。
    if (!children.isEmpty()) {
        status = ST_UNDEPLOYING;
        return doUndeployChildren(undeployingContext).compose(v -> doUndeploy(undeployingContext));
    } else {
        // 子发布为空、或取消子发布完成，现在来取消当前发布
        status = ST_UNDEPLOYED;
        List<Future> undeployFutures = new ArrayList<>();
        if (parent != null) {
            parent.removeChild(this);
        }
        // 为当前发布的每个Verticle实例执行此操作
        for (VerticleHolder verticleHolder: verticles) {
            ContextImpl context = verticleHolder.context;
            Promise p = Promise.promise();
            undeployFutures.add(p.future());
            // 该context是Verticle发布时就存好的，调用它保证了Verticle的stop和start方法在同一个线程运行。
            context.runOnContext(v -> {
                Promise<Void> stopPromise = Promise.promise();
                Future<Void> stopFuture = stopPromise.future();
                stopFuture.setHandler(ar -> {
                    // 从deployments映射中移除
                    deployments.remove(deploymentID);
                    VertxMetrics metrics = vertx.metricsSPI();
                    if (metrics != null) {
                        metrics.verticleUndeployed(verticleHolder.verticle);
                    }
                    context.runCloseHooks(ar2 -> {
                        if (ar2.failed()) {
                            // Log error but we report success anyway
                            log.error("Failed to run close hook", ar2.cause());
                        }
                        if (ar.succeeded()) {
                            p.complete();
                        } else if (ar.failed()) {
                            p.fail(ar.cause());
                        }
                    });
                });
                try {
                    // 执行Verticle的stop方法
                    verticleHolder.verticle.stop(stopPromise);
                } catch (Throwable t) {
                    if (!stopPromise.tryFail(t)) {
                        undeployingContext.reportException(t);
                    }
                }
            });
        }
        Promise<Void> resolvingPromise = undeployingContext.promise();
        CompositeFuture.all(undeployFutures).<Void>mapEmpty().setHandler(resolvingPromise);
        return resolvingPromise.future();
    }
}

private synchronized Future<Void> doUndeployChildren(ContextInternal undeployingContext) {
    if (!children.isEmpty()) {
        List<Future> childFuts = new ArrayList<>();
        // 对每个子发布执行doUndeploy方法
        for (Deployment childDeployment: new HashSet<>(children)) {
            Promise<Void> p = Promise.promise();
            childFuts.add(p.future());
            childDeployment.doUndeploy(undeployingContext, ar -> {
                children.remove(childDeployment);
                p.handle(ar);
            });
        }
        return CompositeFuture.all(childFuts).mapEmpty();
    } else {
        return Future.succeededFuture();
    }
}
```

总结如下

- 一个Verticle被取消，则其所有子Verticle都会被取消
- VerticleHolder中存储了Verticle对应的Context，因此能够保证Verticle的所有生命周期方法都在同一个Context中执行。

### DeploymentManager

DeploymentManager专门用于Verticle发布。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003111046409.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)

重点方法在如下几个

- `DeploymentManager#doDeploy(DeploymentOptions, Function<Verticle,String>, ContextInternal, ContextInternal,ClassLoader, Callable<io.vertx.core.Verticle>)`
- `DeploymentManager#undeployVerticle(String)`

#### 发布

发布代码如下

```java
private Future<Deployment> doDeploy(String identifier,
                                    DeploymentOptions options,
                                    ContextInternal parentContext,
                                    ContextInternal callingContext,
                                    ClassLoader tccl, Verticle... verticles) {
    Promise<Deployment> promise = callingContext.promise();
    String poolName = options.getWorkerPoolName();

    Deployment parent = parentContext.getDeployment();
    // 生成发布ID
    String deploymentID = generateDeploymentID();
    // 创建Deployment对象，上面有说过它是干啥的
    DeploymentImpl deployment = new DeploymentImpl(parent, deploymentID, identifier, options);

    // 发布计数
    AtomicInteger deployCount = new AtomicInteger();
    // 失败标示
    AtomicBoolean failureReported = new AtomicBoolean();
    // 如果一个Verticle发布多个实例，则会有多个verticle对象
    for (Verticle verticle: verticles) {
        // Verticle可以被要求发布到Worker线程池还是EventLoop线程池，在这里做区分
        WorkerExecutorInternal workerExec = poolName != null ? vertx.createSharedWorkerExecutor(poolName, options.getWorkerPoolSize(), options.getMaxWorkerExecuteTime(), options.getMaxWorkerExecuteTimeUnit()) : null;
        WorkerPool pool = workerExec != null ? workerExec.getPool() : null;
        // 为每个Verticle都创建一个新的Context
        ContextImpl context = (ContextImpl) (options.isWorker() ? vertx.createWorkerContext(deployment, pool, tccl) :
                                             vertx.createEventLoopContext(deployment, pool, tccl));
        if (workerExec != null) {
            context.addCloseHook(workerExec);
        }
        // 向Deployment加入Verticle对象
        deployment.addVerticle(new VerticleHolder(verticle, context));
        // 在新创建的Context上执行Verticle生命周期
        context.runOnContext(v -> {
            try {
                // 执行init方法
                verticle.init(vertx, context);
                Promise<Void> startPromise = context.promise();
                Future<Void> startFuture = startPromise.future();
                // 执行start方法
                verticle.start(startPromise);
                startFuture.setHandler(ar -> {
                    if (ar.succeeded()) {
                        if (parent != null) {
                            // 发布成功，加入父节点
                            if (parent.addChild(deployment)) {
                                deployment.child = true;
                            } else {
                                // Orphan
                                deployment.undeploy(event -> promise.fail("Verticle deployment failed.Could not be added as child of parent verticle"));
                                return;
                            }
                        }
                        // 加入发布完成的map
                        deployments.put(deploymentID, deployment);
                        // 发布的数量和待发布的数量匹配，说明发布完成，成功结束
                        if (deployCount.incrementAndGet() == verticles.length) {
                            promise.complete(deployment);
                        }
                    } else if (failureReported.compareAndSet(false, true)) {
                        // 发布失败的回滚
                        deployment.rollback(callingContext, promise, context, ar.cause());
                    }
                });
            } catch (Throwable t) {
                if (failureReported.compareAndSet(false, true))
                    deployment.rollback(callingContext, promise, context, t);
            }
        });
    }

    return promise.future();
}
```

总结如下

- 对每个verticle，vertx都会创建一个新的Context，因此每个verticle之间是相互独立的(一个Context代表了一个EventLoop线程。)
- 传入init和start方法的vertx实例，是DeploymentManager中维护的，它是在Vertx.vertx()创建时赋予的，整个应用一个。
- 整个verticle的内容都通过Context.runOnContext注册运行，所以它们才会始终都在一个线程上执行，并且执行顺序从上到下，不存在多线程竞争问题。
- 发布完成的Deployment会被加入DeploymentManager维护的deployments映射中，方便进行查找和之后的使用。

#### 取消发布

```java
public Future<Void> undeployVerticle(String deploymentID) {
    // 从deployments中获取Deployment对象
    Deployment deployment = deployments.get(deploymentID);
    // 获取当前上下文
    Context currentContext = vertx.getOrCreateContext();
    if (deployment == null) {
        return ((ContextInternal) currentContext).failedFuture(new IllegalStateException("Unknown deployment"));
    } else {
        // 调用deployment的undeploy()
        return deployment.undeploy();
    }
}
```

Deployment.undeploy()在上面介绍Deployment时已介绍。

### VerticleManager

DeploymentManager专注于发布，VerticleManager则主要专注于Verticle的创建。其内部持有一个DeploymentManager对象，用于执行实际的发布操作。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201003111106890.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=,size_16,color_FFFFFF,t_70#pic_center)
该类中有两个主要逻辑

- VerticleFactory的注册、取消、查找等。可以实现自定义的VerticleFactory，这里不深入。
- Verticle的发布和创建的逻辑：调用VerticleFactory创建Verticle实例，在调用DeploymentManager.deploy()发布，代码过长，不给出。

### 所以Verticle是如何工作的？

这里回答最初提出的四个问题，就能解释Verticle是如何工作的。

- deployVerticle时发生了什么？

  创建Verticle对象 -> 创建Context并和Verticle对象绑定 -> 构建Deployment并存起来 -> 执行init() -> 执行start() -> 完成

- start()和stop()方法什么时候被调用？

  start(): 发布时，在新创建的Context上执行。

  stop(): 取消发布时，在与该Verticle绑定的Context上执行。

- 如何保证一个Verticle下的所有操作都在一个EventLoop线程上执行？

  通过将Context和Verticle绑定，调用start()和stop()时均在该Context下执行；而在start()和stop()中调用vertx的大多数操作，均是在调用代码块的当前Context下执行，而一个Context始终对应同一个EventLoop线程，如此即能保证一个Verticle下的所有操作都在同一个EventLoop线程上执行。

- 父子层级关系如何维持？有什么作用？

  通过Deployment对象记录并维持。作用在于关闭一个Verticle时，其子Verticle也会被依次关闭。

如此一来，Verticle几乎有了除容错机制外的所有的Actor模型的特性。

## **数据共享机制**

Vertx提供了SharedData组件，用于为整个应用范围内提供共享组件，一个共享Map的使用大概如下

```kotlin
class Verticle1 : AbstractVerticle() {
    override fun start() {
        println("Verticle 1 started")
        vertx.sharedData().getLocalAsyncMap<String, String>("myMap").setHandler { ar ->
                                                                                 ar.result().put("你好", "我是Verticle1")
                                                                                }
    }
}

class Verticle2 : AbstractVerticle() {
    override fun start() {
        println("Verticle 2 started")
        vertx.sharedData().getLocalAsyncMap<String, String>("myMap").setHandler { ar ->
                                                                                 val value = ar.result().get("你好").result()
                                                                                 println(value)
                                                                                }
    }
}

fun main() {
    val vertx = Vertx.vertx();
    vertx.deployVerticle(Verticle1::class.java.canonicalName)
    Thread.sleep(1000)
    vertx.deployVerticle(Verticle2::class.java.canonicalName)
}
```

所有关于共享数据的内容都在io.vertx.core.shareddata包下，核心类是SharedDataImpl。

提供如下三种数据结构

- io.vertx.core.shareddata.impl.LocalAsyncLocks

  异步排他锁，在集群内部有效的锁。其实现的思路如下

  - 维护一个ConcurrentMap，存储锁名和等待该锁的Handler列表
  - 每次新来一个获取锁的请求，向等待列表中加入。并启动定时器开始计算超时，超时后直接回调锁等待超时。

  至此加入等待列表的逻辑完成。然后是锁流转逻辑。采用被动的逻辑，非常节省复杂度。

  - 当等待列表为空时，来一个请求就将锁给它；列表不为空时，仅加入等待列表，不做尝试获取锁的操作。
  - 当一个锁被释放时，再主动将锁给等待列表的下一个请求。这样几乎从来不会出现竞争的情况。

- io.vertx.core.shareddata.impl.AsynchronousCounter

  计数器，增减都是原子操作

- io.vertx.core.shareddata.impl.LocalMapImpl

  本地Map，用于单个实例中共享数据。仅是对ConcurrentMap的包装，没有其它特别之处。他的所有操作都是同步的。

- io.vertx.core.shareddata.impl.LocalAsyncMapImpl

  异步Map，同样是对ConcurrentMap的包装。不同之处在于其value是Holder类，它封装了TTL，实现原理是调用vertx.setTimer设置一个TTL长度的定时器，过期移除。

  ```java
  @Override
  public void put(K k, V v, long timeout, Handler<AsyncResult<Void>> completionHandler) {
      long timestamp = System.nanoTime();
      long timerId = vertx.setTimer(timeout, l -> removeIfExpired(k));
      Holder<V> previous = map.put(k, new Holder<>(v, timerId, timeout, timestamp));
      if (previous != null && previous.expires()) {
          vertx.cancelTimer(previous.timerId);
      }
      completionHandler.handle(Future.succeededFuture());
  }
  ```

  可能有顾虑设置太多定时器不好，但vertx其实是将定时任务加入eventLoop线程去执行，因此并不会增加额外成本

  ```java
  public long setTimer(long delay, Handler<Long> handler) {
      return scheduleTimeout(getOrCreateContext(), handler, delay, false);
  }
  private long scheduleTimeout(ContextImpl context, Handler<Long> handler, long delay, boolean periodic) {
      if (delay < 1) {
          throw new IllegalArgumentException("Cannot schedule a timer with delay < 1 ms");
      }
      long timerId = timeoutCounter.getAndIncrement();
      InternalTimerHandler task = new InternalTimerHandler(timerId, handler, periodic, delay, context);
      timeouts.put(timerId, task);
      context.addCloseHook(task);
      return timerId;
  }
  InternalTimerHandler(long timerID, Handler<Long> runnable, boolean periodic, long delay, ContextImpl context) {
      this.context = context;
      this.timerID = timerID;
      this.handler = runnable;
      this.periodic = periodic;
      EventLoop el = context.nettyEventLoop();
      if (periodic) {
          future = el.scheduleAtFixedRate(this, delay, delay, TimeUnit.MILLISECONDS);
      } else {
          future = el.schedule(this, delay, TimeUnit.MILLISECONDS);
      }
      if (metrics != null) {
          metrics.timerCreated(timerID);
      }
  }
  ```


## **框图**

有待为每个工作原理都加上框图

## **总结**

Vertx核心为EventBus、EventLoop，以及Verticle。这里通过先展示核心类的能力和实现原理，让读者有一个具象的认识，了解每个核心类大概有能干什么。然后通过EventBus的简单收发分析，展示了EventBus的工作原理及EventLoop参与代码执行的方式；通过Verticle的发布，展示了Verticle是如何运转的，以及Verticle的线程安全特性得到保障的原因；最后展示了SharedData进行应用范围内数据共享的实现原理。让读者对Vert.x核心部分有了较为深入的认识。

当然，Vert.x的能力远不止于此，这里仅介绍了单机版运行原理，它还支持集群和高可用特性，都是本文没有覆盖到的；此外，核心部分的文件系统、网络编程相关内容也均未介绍，这些留待之后再说。

最后，总结一波一些核心组件相互之间的关系。

- 一般来说，一个应用只有一个Vertx，在整个应用中传来传去的vertx实例，都是一个，除非我们想要拥有完全隔离的EventBus。
- 一个Vertx实例只持有一个EventBus和一个用于日常调度的EventLoopGroup(用于网络服务监听的不算)。
- 一个Vertx实例持有多个线程池，我们最常解除的只有EventLoopGroup和WorkerPool。
- 一个Context只持有一个EventLoop，即只对应一个线程。通过runOnContext()将任务调度到该EventLoop上执行。
- 一个VerticleManager持有多个VerticleFactory。
- 一个DeployManager持有多个Deployment，Deployment之间的父子关系由Deployment自己维护。
- 一个Deployment可以持有多个Verticle实例，但仅能持有一个Verticle类型

