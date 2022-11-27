---
created_at: 2020-05-25 22:57:26.0
updated_at: 2021-02-16 23:21:28.826
slug: kotlin-coroutine-usage
---

> 使用协程已经有较长的时间了，但一直停留在launch、async启动协程，suspend方法挂起的阶段。这段时间系统梳理Kotlin知识时才发现，对协程（仅对Kotlin）还有很多概念不甚了解。例如CoroutineScope对协程生命周期的重要性、协程父子结构的作用、结构化并发、一些Kotlin协程中约定俗称的规定等。

<!-- more -->

# 概述

## 解释协程

解释协程这一概念，是个作死的行为，这里斗胆一试。

我们尝试从几个比较流行的说法来解释协程到底是个什么东西，而不是再增加一种让人猜不透的说法

1. 协程是轻量级线程(官方表述)

   可以换个说法，协程就是方法调用封装成类线程的API。方法调用当然比线程切换轻量；而封装成类线程的API后，它形似线程（可手动启动、有各种运行状态、能够协作工作、能够并发执行）。因此从这个角度说，它是轻量级线程没错。

   当然，协程绝不仅仅是方法调用，因为方法调用不能在一个方法执行到一半时挂起，之后又在原点恢复。这一点可以使用EventLoop之类的方式实现。想象一下在库级别将回调风格或Promise/Future风格的异步代码封装成同步风格，封装的结果就非常接近协程了。

   而协程和线程之间的区别，往大了说，那就是普通函数与线程的区别；往小了说，就是EventLoop和线程的区别。他们之间的唯一的关系，仅仅在于协程的代码是运行在线程中。一个不恰当的类比，人和地球(地球提供生成环境，人在其中生存)

2. 线程运行在内核态，协程运行在用户态

   主要明白什么叫用户态，我们写的几乎所有代码，都执行在用户态，协程对于操作系统来说仅仅是第三方提供的库而已，当然运行在用户态。而线程是操作系统级别的东西，运行在内核态。

3. 协程是一个线程框架(扔物线表述)

   对某些语言，比如Kotlin，这样说是没有问题的，Kotlin的协程库可以指定协程运行的线程池，我们只需要操作协程，必要的线程切换操作交给库，从这个角度来说，协程就是一个线程框架。

   但理论上我们可以在单线程语言如JavaScript、Python上实现协程(事实上他们已经实现了协程)，这时我们再叫它线程框架可能就不合适了。

私以为，协程要从两方面看

- 概念上：coroutine(协程)和subroutine(子程序)是一个级别的(从命名上也类似)。子程序是一段具备一定功能的代码，一个函数、一个方法、一段代码都算是一个子程序。而协程，顾名思义，就是相互协作的子程序，多个子程序之间通过一定的机制相互关联、协作地完成某项任务。比如一个协程在执行上可以被分为多个子程序，每个子程序执行完成后主动挂起，等待合适的时机再恢复；一个协程被挂起时，线程可以执行其它子程序，从而达到线程高利用率的多任务处理目的——协程在一个线程上执行多个任务，而传统线程只能执行一个任务，从多任务执行的角度，协程自然比线程轻量。

  通过提高线程利用率来提高多任务执行效率，这一点和IO多路复用、Reactor模型等基本思想一致，从这个角度看，协程并不是什么新东西。

- 实现上：协程的重点和难点就在于执行到挂起点时挂起和恢复的行为。它在底层技术实现上和我们常用的异步回调没有本质的区别，仅仅是根据不同的编程思想封装成对应的API。

  其具体实现原理我们将在其它文章讨论，这里仅介绍协程概念。

协程解决的问题——以同步的方式写异步代码。如果不使用协程，我们目前能够使用的API形式主要有三种：纯回调风格(如AIO)、RxJava、Promise/Future风格，他们普遍存在回调地狱问题，解回调地狱只能通过行数换层数，且对于不熟悉异步风格的程序员来说，能够看懂较为复杂的异步代码就比较费劲。

## Kotlin的协程

根据[Kotlin协程设计提案](https://github.com/Kotlin-zh/KEEP/blob/master/proposals/coroutines.md)，Kotlin协程的设计目标有如下三点

- 不依赖 Future 之类复杂的库提供的特定实现
- 同时涵盖 “async/await” 用例以及“生成器代码块”
- 使 Kotlin 协程能包装各种现有的异步 API （如 Java NIO、各种 Future 的实现等）

可以认为，Kotlin是想在自己的代码环境中用协程消除传统的异步API，以原语的方式提供。

## 本文介绍

上面介绍了协程的基本概念和Kotlin协程的设计目的，接下来介绍Kotlin中协程的使用方法、核心组件、核心概念以及常见使用约定。有关实现原理，尚未探索，计划另开文章详述。

# 使用协程

## 启动

协程需要运行在协程上下文环境，在非协程环境中凭空启动协程，有三种方式

- runBlocking{}

  启动一个新协程，并阻塞当前线程，直到其内部所有逻辑及子协程逻辑全部执行完成。

  该方法的设计目的是让suspend风格编写的库能够在常规阻塞代码中使用，常在main方法和测试中使用。

- GlobalScope.launch{}

  在应用范围内启动一个新协程，协程的生命周期与应用程序一致。这样启动的协程并不能使线程保活，就像守护线程。

  由于这样启动的协程存在启动协程的组件已被销毁但协程还存在的情况，极限情况下可能导致资源耗尽，因此并不推荐这样启动，尤其是在客户端这种需要频繁创建销毁组件的场景。

- 实现CoroutineScope + launch{}

  这是在应用中最推荐使用的协程使用方式——为自己的组件实现CoroutieScope接口，在需要的地方使用launch{}方法启动协程。使得协程和该组件生命周期绑定，组件销毁时，协程一并销毁。从而实现安全可靠地协程调用。

在一个协程中启动子协程，一般来说有两种方式

- launch{}

  异步启动一个子协程

- async{}

  异步启动一个子协程，并返回Deffer对象，可通过调用Deffer.await()方法等待该子协程执行完成并获取结果，常用于并发执行-同步等待的情况

一个合适的例子

```kotlin
class TtpServiceImpl(val vertx: Vertx): TtpService, CoroutineScope {
    override val coroutineContext: CoroutineContext by lazy { vertx.dispatcher() }
    
    override fun getContentList(resultHandler: Handler<AsyncResult<OperationResponse>>){
        launch{
            val deffer1 = async{ awaitResult<List<JsonObject>>{ dbService.getContentList(it) } }
            val deffer2 = async{ awaitResult<List<JsonObject>>{ dbService.getAuthorList(it) } }
            val contents = deffer1.await()
            val authors = deffer2.await()
            val reuslt = contents.map{ content -> 
                content.put("author", authors.filter{ ... }.first())
            }
            resultHandler.succeed(reuslt)
        }
    }
}
```

## 取消

launch{}返回Job，async{}返回Deffer，Job和Deffer都有cancel()方法，用于取消协程。

**从协程内部看取消的效果**

- 标准库的挂起方法会抛出CancellationException异常。
- 用户自定义的常规逻辑并不会收到影响，除非我们手动检测isActive标志。

上面两个特性和线程的interrupt机制非常类似，理解起来并不难。

```kotlin
val job = launch {
    // 如果这里不检测isActive标记，协程就不会被正常cancel，而是执行直到正常结束
    while (isActive) { 
        ......
    }
}
job.cancelAndJoin() // 取消该作业并等待它结束
```

了解协程的启动和取消，对于最基本的使用已经足够了。不过为了更加安全放心地使用，需要更加深入地了解，我们从核心组件说起。

## 异常

Kotlin协程的异常有两种

- 因协程取消，协程内部suspend方法抛出的CancellationException
- 常规异常，这类异常，有两种异常传播机制
  - launch：将异常自动向父协程抛出，将会导致父协程退出
  - async: 将异常暴露给用户(通过捕获deffer.await()抛出的异常)

这里借用官方例子讲解

```kotlin
fun main() = runBlocking {
    val job = GlobalScope.launch { // root coroutine with launch
        println("Throwing exception from launch")
        throw IndexOutOfBoundsException() // 我们将在控制台打印 Thread.defaultUncaughtExceptionHandler
    }
    job.join()
    println("Joined failed job")
    val deferred = GlobalScope.async { // root coroutine with async
        println("Throwing exception from async")
        throw ArithmeticException() // 没有打印任何东西，依赖用户去调用等待
    }
    try {
        deferred.await()
        println("Unreached")
    } catch (e: ArithmeticException) {
        println("Caught ArithmeticException")
    }
}
```

输出结果

```kotlin
Throwing exception from launch
Exception in thread "DefaultDispatcher-worker-2 @coroutine#2" java.lang.IndexOutOfBoundsException
Joined failed job
Throwing exception from async
Caught ArithmeticException
```

注意，例子是在GlobalScope.launch{}中抛异常，不会导致父协程退出。

**全局异常处理**

指定全局异常处理器，省时省力。

```kotlin
  override fun getContentList(resultHandler: Handler<AsyncResult<OperationResponse>>) {
    launch(CoroutineExceptionHandler { _, e ->
      logger.error("Exception when get content list.", e)
      resultHandler.fail()
    }) {
            val deffer1 = async{ awaitResult<List<JsonObject>>{ dbService.getContentList(it) } }
            val deffer2 = async{ awaitResult<List<JsonObject>>{ dbService.getAuthorList(it) } }
            val contents = deffer1.await()
            val authors = deffer2.await()
            val reuslt = contents.map{ content -> 
                content.put("author", authors.filter{ ... }.first())
            }
            resultHandler.succeed(reuslt)
    }
}
```

# 核心组件

Kotlin的协程实现是以附加库kotlinx-coroutines-core的形式提供的，但其实协程的接口定义在核心库kotlin-stdlib-common的kotlin.coroutines中。

## 协程上下文

顾名思义，协程上下文表示协程的运行环境，包括协程调度器、代表协程本身的Job、协程名称、协程ID等。通过CoroutineContext定义，CoroutineContext被定义为一个带索引的集合，集合的元素为Element，上面所提到调度器、Job等都实现了Eelement接口。

由于CoroutineContext被定义为集合，因此在实际使用时可以自由组合加减各种上下文元素。

启动子协程时，子协程默认会继承除Job外的所有父协程上下文元素，创建新的Job，并将父Job设置为当前Job的父亲。

启动子协程时，可以指定协程上下文元素，如果父上下文中存在该元素则覆盖，不存在则添加。

```kotlin
    override fun getContentList(resultHandler: Handler<AsyncResult<OperationResponse>>){
        // 自定义新协程名称
        launch(CoroutineName("customName")){
            ... ...
        }
    }
```

### 调度器

调度器是协程上下文中众多元素中最重要的一个，通过CoroutineDispatcher定义，它控制了协程以何种策略分配到哪些线程上运行。这里介绍几种常见的调度器

- Dispatcher.Default

  默认调度器。它使用JVM的共享线程池，该调度器的最大并发度是CPU的核心数，默认为2

- Dispatcher.Unconfined

  非受限调度器，它不会将操作限制在任何线程上执行——在发起协程的线程上执行第一个挂起点之前的操作，在挂起点恢复后由对应的挂起函数决定接下来在哪个线程上执行。

- Dispathcer.IO

  IO调度器，他将阻塞的IO任务分流到一个共享的线程池中，使得不阻塞当前线程。该线程池大小为环境变量kotlinx.coroutines.io.parallelism的值，默认是64或核心数的较大者。

  该调度器和Dispatchers.Default共享线程，因此使用withContext(Dispatchers.IO)创建新的协程不一定会导致线程的切换。

- Dispathcer.Main

  该调度器限制所有执行都在UI主线程，它是专门用于UI的，并且会随着平台的不同而不同

  - 对于JS或Native，其效果等同于Dispatchers.Default
  - 对于JVM，它是Android的主线程、JavaFx或者Swing EDT的dispatcher之一。

  并且为了使用该调度器，还必须增加对应的组件

  - kotlinx-coroutines-android
  - kotlinx-coroutines-javafx
  - kotlinx-coroutines-swing

- 其它

  在其它支持协程的第三方库中，也存在对应的调度器，如Vertx的vertx.dispatcher()，它将协程分配到vertx的EventLoop线程池执行。

注意，由于上下文具有继承关系，因此启动子协程时不显式指定调度器时，子协程和父协程是使用相同调度器的。

### Job

Job也是上下文元素，它代表协程本身。Job能够被组织成父子层次结构，并具有如下重要特性。

- 父Job退出，所有子job会马上退出
- 子job抛出除CancellationException(意味着正常取消)意外的异常会导致父Job马上退出

类似Thread，一个Job可能存在多种状态

| **State**                        | [isActive] | [isCompleted] | [isCancelled] |
| -------------------------------- | ---------- | ------------- | ------------- |
| _New_ (optional initial state)   | `false`    | `false`       | `false`       |
| _Active_ (default initial state) | `true`     | `false`       | `false`       |
| _Completing_ (transient state)   | `true`     | `false`       | `false`       |
| _Cancelling_ (transient state)   | `false`    | `false`       | `true`        |
| _Cancelled_ (final state)        | `false`    | `true`        | `true`        |
| _Completed_ (final state)        | `false`    | `true`        | `false`       |

我们直接使用launch获取到的job已经处于Active装填，启动时加上LAZY参数时则得到New状态的Active。

各状态转换关系如下，注意，Completing只是一个内部状态，外部观察还是Active状态。

![image-20200530154420916](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kotlin协程-使用篇/image-20200530154420916.png)

要区分是主动取消还是异常导致一个协程退出，可以getCancellationException()查看退出原因。

## 作用域

协程作用域——CoroutineScope，用于管理协程，管理的内容有

- 启动协程的方式 - 它定义了launch、async、withContext等协程启动方法(以extention的方式)，并在这些方法内定义了启动子协程时上下文的继承方式。
- 管理协程生命周期 - 它定义了cancel()方法，用于取消当前作用域，同时取消作用域内所有协程。

## 区分作用域和上下文

从类定义看，CoroutineScope和CoroutineContext非常类似，最终目的都是协程上下文，但正如Kotlin协程负责人Roman Elizarov在[Coroutine Context and Scope](https://medium.com/@elizarov/coroutine-context-and-scope-c8b255d59055)中所说，二者的区别只在于使用目的的不同——**作用域用于管理协程；而上下文只是一个记录协程运行环境的集合**。他们的关系如下。

![image-20200530153221730](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kotlin协程-使用篇/image-20200530153221730.png)

Roman Elizarov的文章说得可能不是很明晰，我认为比较容易理解的说法是

- CoroutineScope规范了CoroutineContext的继承和管理方式。

# 约定和经验

## 避免使用GlobalScope.launch

GlobalScope是实现了CoroutineScope的单例对象，含有一个空的上下文对象

```kotlin
// GlobalScope的定义
public object GlobalScope : CoroutineScope {
    override val coroutineContext: CoroutineContext
        get() = EmptyCoroutineContext
}
```

这意味着它的生命周期与整个应用绑定，并且永远不会被主动取消。这样启动的协程只有两个归宿:

- 协程正常执行完成
- 协程内部发生错误，导致协程因异常自动取消

这是危险的。考虑极端情况:

1. 在一个实例方法中使用GlobalScope.launch启动了一个CPU密集型协程，且执行时间较长
2. 在启动协程后，该实例方法因异常退出，所属对象也被销毁
3. 反复多次出现步骤1\2

这样导致的结果是启动了超多CPU密集型任务，最终导致应用卡顿，甚至资源耗尽。

解决方案是避免使用GlobalScope。正确的做法是将自己的组件实现CoroutineScope，并在组件销毁时调用作用域的cancel()方法。实现方式多使用委托。

```kotlin
// 官方例子
class MyActivity : AppCompatActivity(), CoroutineScope by MainScope() {
    override fun onDestroy() {
         cancel() // cancel is extension on CoroutineScope
    }
    ... ...
}
// vertx例子
abstract class CoroutineVerticle : Verticle, CoroutineScope {
  // 默认上下文使用context.dispatcher()
  override val coroutineContext: CoroutineContext by lazy { context.dispatcher() }
  ... ...
}
```

## 结构化并发

首先从结构化并发这一概念说起(参考[这篇文章](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/))。

**非结构化并发**

与结构化并发相对的是非结构化并发，即传统的异步框架和异步库。这种异步框架在工作时，可能会在函数中启动一个新的协程，或新注册一个回调函数，当函数调用返回时，从语义上，函数貌似返回了，但实际上它仍然在后台运行(对于启动的协程，他会运行直到结束；对于注册的回调函数，仍然属于原函数的一部分，会在将来执行)，如果不了解其中的因果关系，就不知道它什么时候结束，**这违反了因果关系**。

正是由于异步框架的非结构化并发的缺点，导致出现背压这样更加复杂的副产物。尽管它们能够使程序正常工作，但会很麻烦，违反编程直觉——你不是在编程，而是在使用一种工具。

一个非结构化并发的逻辑流如同go语句产生的效果。

![image-20200530165158464](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kotlin协程-使用篇/image-20200530165158464.png)

**结构化并发**

结构化并发，就是将多个分开的并发路径最终再次连接起来，使得符合因果关系，在意义上类比将面条代码始作俑者go语句从编程语言中剔除。

![image-20200530165243662](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/Kotlin协程-使用篇/image-20200530165243662.png)

实现结构化并发需要运行环境，用于包装真正的异步操作，并暴露取消机制、异常传播机制等API。

**Kotlin如何实现结构化并发**

Kotlin协程通过CoroutineScope实现结构化并发。因为作用域具有如下特性

- 能够控制内部协程的生命周期
- 可以取消内部所有协程
- 所有子协程完成后作用域才结束

为了让我们能够对一部分代码块实现结构化并发，Kotlin提供了coroutineScope{}方法(官方声称其目的在于并行分解，即将一个长耗时任务分解成多个并发的短耗时任务，并在最终组装，正是利用了作用域的结构化并发特性，才能够实现并行分解)

```kotlin
// 常用的示意例子，这里用的是async，实际上用launch时，coroutineScope也会等待其结束后再返回。
suspend fun loadAndCombine(name1: String, name2: String): Image = coroutineScope {
    val deferred1 = async { loadImage(name1) }
    val deferred2 = async { loadImage(name2) }
    combineImages(deferred1.await(), deferred2.await())
}
```

此外，从结构化并发的概念上看，runBlocking{}也能够结构化并发。

## suspend方法和CoroutineScope扩展方法的取舍

Kotlin中，有两个约定俗成的东西

1. 每一个声明为CoroutineScope的扩展方法的方法，都会马上返回，但是会并发地执行扩展方法指定的内容

   这也是runBlocking不是CoroutineScope的扩展方法的原因之一

2. 每一个仅声明为suspend的方法，会等待其内部逻辑完成后再返回给调用者

但如果拥有如下签名的方法会怎么样呢？它是suspend方法，同时也是CoroutineScope的扩展方法。调用者并不知道在方法内是否会启动新的协程，凭空给代码增加了复杂度，因此不推荐使用。

```kotlin
suspend fun CoroutineScope.obfuscate(data: Data)
```

suspend方法就应该在所有任务都完成后再返回。如果在suspend方法内部有需要并发执行的内容，那就应该等待他们都完成后再返回，此时可以使用coroutineScope{}，而不是在方法签名上加上CoroutineScope扩展。

# 区分与对比

Kotlin中，有几种方式能够启动协程，或者看似能够启动协程，这里列举

- launch{}

  CoroutineScope的扩展方法，**启动一个协程**，不阻塞当前协程，并返回新协程的Job。

- async{}

  CoroutineScope的扩展方法，**启动一个协程**，不阻塞当前协程，返回一个Deffer，除包装了未来的结果外，其余特性与launch{}一致

- withContext(){}

  一个suspend方法，在给定的上下文执行给定挂起块并返回结果，**它并不启动协程**，只会(可能会)导致线程的切换。用它执行的挂起块中的上下文是当前协程的上下文和由它执行的上下文的合并结果。

  withContext的目的不在于启动子协程，它最初用于将长耗时操作从UI线程切走，完事再切回来。

  前面我们说过，协程取消后，位于协程中的标准库的suspend函数会抛出CancellationException，withContext也不例外。

- coroutineScope{}

  一个suspend方法，创建一个新的作用域，并在该作用域内执行指定代码块，**它并不启动协程**。其存在的目的是进行符合结构化并发的并行分解（即，将长耗时任务拆分为并发的多个短耗时任务，并等待所有并发任务完成后再返回）。

- runBlocking{}

  是一个裸方法，**创建一个协程，并阻塞当前线程**，直到协程执行完毕。前面说过，这里不再赘述。

# Kotlin协程的其它功能

## 异步流

首先说，Kotlin中的异步流和RxJava中的流在概念上非常类似，可以被归为响应式流。并且Kotlin也提供响应的库将它转换为其它响应式流

- kotlinx-coroutines-reactive 用于Reactive Streams
- kotlinx-coroutines-reactor  用于Project Reactor
- kotlinx-coroutines-rx2      用于RxJava2

### 为什么需要异步流

一个挂起函数能够异步地返回单一的值，如果我们要异步返回多个值并针对每个都做处理呢？这也是一般响应式流遇到的场景，在Kotlin中，异步流用来解决它。

**已有现成的响应式流，为啥还有异步流？**

从功能上说，现有的响应式流库能够解决问题，但在Kotlin中不够优雅。Flow的设计目标是拥有尽可能精简的设计，能够完美融合到Kotlin的协程API中。

### 使用异步流

```kotlin
  val flow = flow {
    // 耗时操作1
    delay(1000)
    emit(12)
    // 耗时操作2
    delay(1000)
    emit(13)
  }

  runBlocking {
    flow.collect { println(it) }
  }
```

- flow接收的lambda表达式是一个协程环境，里面的操作实在一个协程中执行
- collect是收集操作，**只有收集时才会真的去执行流中定义的逻辑**
- flow也可以被取消

更多详情，移步[官方手册](https://www.kotlincn.net/docs/reference/coroutines/flow.html)

## 通道

通道(Channel)用于在多个协程之间传输数据。Channel是和BlockingQueue非常相似的概念。不同的是写入和读取数据用的是异步的send和recieve

这里展示简单的使用

- 直接通过Channel构造函数

  ```kotlin
  val channel = Channel<Int>()
  launch {
      for (x in 1..5) channel.send(x * x)
      channel.close()
  }
  for (y in channel) println(y)
  println("Done!")
  ```

- 使用produce构建器

  ```kotlin
  val channel = produce {
      send(12)
      send(13)
  }
  
  for (value in channel) {
      println(value)
  }
  ```

在通道没有数据时，调用recieve会导致协程挂起；在通道缓冲满时，调用send会导致协程挂起。

通道遵循FIFO原则，先发出的消息会先被获取。

## 监督

常规的Job当子协程抛异常时，父协程也会被退出。有时不想要这种情况发生，可以使用监督。使用方式是将SupervisorJob在协程启动时当上下文元素传入。

## 协程+通道实现actor

Kotlin的协程本质上说是更好用的线程的封装，因此还是会有共享的可变状态的并发问题。解决方式无非几种

- 共享变量使用并发数据结构，如Atomic数据类
- 限制访问共享变量的协程在单线程上执行
- 对共享变量的访问加锁
- 使用actor模式，将共享变量封装在actor中，通过actor的消息邮箱将并发变串行

Kotlin的actor是由一个**协程**、协程封装的**状态**、一个它与其它协程通信的**通道**组成。

和scala一样，正确使用actor的方式是先创建消息类，然后定义actor，然后发送消息

```kotlin
// 计数器 Actor 的各种类型
sealed class CounterMsg
object IncCounter : CounterMsg() // 递增计数器的单向消息
class GetCounter(val response: CompletableDeferred<Int>) : CounterMsg() // 携带回复的请求

fun main() = runBlocking<Unit> {
  val counter = actor<CounterMsg> {
    var counter = 0 // actor 状态
    for (msg in channel) { // 即将到来消息的迭代器
      when (msg) {
        is IncCounter -> counter++
        is GetCounter -> msg.response.complete(counter)
      }
    }
  }
  withContext(Dispatchers.Default) {
    counter.send(IncCounter)
  }
  // 发送一条消息以用来从一个 actor 中获取计数值
  val response = CompletableDeferred<Int>()
  counter.send(GetCounter(response))
  println("Counter = ${response.await()}")
  counter.close() // 关闭该actor
}
```

actor能够并发安全的原因是它将并发过来的请求存储在通道中，再一个一个地处理。达到了不需要加锁的串行调用。比直接并发安全，比加锁高效。

# 总结

本文详述了Kotlin协程的基本用法及重要组件的运行机制，对它们有了足够详细的了解和清晰的认识有助于我们写出正确的Kotlin协程代码。当然实际使用还需要根据具体情况选择恰当的API。文章的最后大致介绍了Kotlin协程中的其它功能，虽然不常用到，但了解总是没错的，万一有用呢。

文章中偏重讲解，示例代码较少，且部分实例代码来自官方，部分来自自己，并不一定能够直接运行，重在展示用法，阅读时注意区分。

写本文前打了很多草稿，如有兴趣翻阅，可以看[这里]()。

# 参考资料

1. [协程 - 维基百科]([https://zh.wikipedia.org/wiki/%E5%8D%8F%E7%A8%8B](https://zh.wikipedia.org/wiki/协程))
2. [[码上开学]协程系列视频(扔物线，共3集)](https://www.bilibili.com/video/BV164411C7FK?from=search&seid=6066955533575291649)
3. [Kotlin协程设计提案(翻译版)](https://github.com/Kotlin-zh/KEEP/blob/master/proposals/coroutines.md)
4. [Kotlin协程官方手册](https://www.kotlincn.net/docs/reference/coroutines/coroutines-guide.html)
5. Kotlin核心组件Javadoc
6. [Coroutine Context and Scope - Roman Elizarov](https://medium.com/@elizarov/coroutine-context-and-scope-c8b255d59055)
7. [The reason to avoid GlobalScope - Roman Elizarov](https://medium.com/@elizarov/the-reason-to-avoid-globalscope-835337445abc)
8. [Structed concurrency - Roman Elizarov](https://medium.com/@elizarov/structured-concurrency-722d765aa952)
9. [Structed concurrency - Somebody](https://vorpus.org/blog/notes-on-structured-concurrency-or-go-statement-considered-harmful/)
10. [Explicit Concurrency - Roman Elizarov](https://medium.com/@elizarov/explicit-concurrency-67a8e8fd9b25)