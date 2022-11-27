---
created_at: 2019-09-25 22:33:16.0
updated_at: 2021-02-16 23:25:55.071
slug: akka-and-lightend-introduction
tags:
- Akka
- Lightend
---

> akka这个技术一致都在听人弹起，只知道它与后端有关，是一个牛B的框架，别的么。。。并不知道。那么，我觉得现在是时候了解一下了。

<!-- more -->

# akka

akka是一个基于actor模式的消息驱动的开源框架，用于解决并发和可伸缩性问题。支持scala和java两种语言，运行于JVM。

在akka中，所有每个功能模块被抽象成一个actor，actor之间没有api可相互调用，他们之间通过message进行异步交流，message可以是任意类型，这样保证了actor之间高度去耦合。这使得代码执行效率得到了很大提升，并且actor降低了各模块之间的耦合，从而能够方便地增减功能。

这里是akka的[官方例程](https://developer.lightbend.com/guides/akka-quickstart-java/)

这里是akka的[github地址](https://developer.lightbend.com/guides/akka-quickstart-java/)

# Lightend

这是akka背后的公司，除akka外，该公司还有另一个非常著名的产品：Scala编程语言。同时，基于akka，他们还构建了Web服务框架Play，和微服务框架Lagom。从[Lightend的简介](https://www.lightbend.com/about-lightbend)上看，该公司致力于构建一个实时的企业级软件平台，并且在响应式开发做出了很多贡献。

Scala自不必说，这是目前非常流行的语言。另外两个框架，由于是基于akka得来，因此性能上也是差不多的。

# actor设计模式

 Actors属于并发组件模型 ，通过组件方式定义并发编程范式的高级阶段，避免使用者直接接触多线程并发或线程池等基础概念。

传统多数流行的语言并发是基于多线程之间的共享内存，使用同步方法防止写争夺，Actors使用消息模型，每个Actors在同一时间处理最多一个消息，可以发送消息给其他Actors，保证了[单独写原则 ](https://www.jdon.com/performance/singlewriter.html)。从而巧妙避免了多线程写争夺。

Actors模型的特点是：

  - 隔离计算实体
  - "Share nothing"
  - 没有任何地方同步
  - 异步消息传递
  - 不可变的消息 消息模型类似mailbox / queue

Actor使用的一个关键是构建出层级关系的Actor树，树中父节点负责监督子节点的运行，使得子节点出错时能够被捕获并恢复，这就是监督机制，它使得Actor模型具有很高的可靠性。

![](https://yqfile.alicdn.com/img_1aeb3f16f0f7045930299c586806561a.png)

在Akka的Actor模型使用中，只要遵循如下使用原则，就能够得到高并发和高可靠性。

- 所有的计算都是在actor中执行的
- actor之间只能通过消息进行通信交流
- 为了响应消息，actor可以进行下列操作
  -  更改状态或行为
  -  发消息给其他actor
  -  创建有限数量的子actor

# akka VS vertx

其实vertx也是Actor模式的一种实现，其verticle对应actor，所有Actor要求满足的条件，使用上的限制，vertx同样都有满足，但相比akka会包得更深一些，暴露给用户的部分更加简单易于理解，使用时完全感觉不到他在使用Actor模型。

akka则不一样，它基本上是比较直接地将Actor模型应用起来，熟练使用Akka需要熟练掌握Actor模型的各种概念和使用原则。

此外，在使用场景上我认为二者也略有不同，akka仅仅是一个解决并发的框架，是Actor模式的直接实现。而vertx是一个完整的平台，仅仅是并发部分使用了Actor模式实现，此外它还包括数据库、web服务、微服务、网络等应有尽有的模块。相比而言Lightend公司也仅有akka+play+Lagom这样的基本产品可供选择。

总的来说：

akka和vertx的共同点在于其都使用Actor模式解决并发和伸缩性问题。不同点在于akka专注于Actor模式的实现，提供更加丰富的选择，但同时要求使用者对Actor模式非常熟悉；而vertx在Actor模式部分封装得比较深，对使用者比较友好，更重要的是vertx提供一整套完整的方案，成为了一个工具集或平台级别的框架。