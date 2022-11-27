---
created_at: 2021-10-20 12:04:53.258
updated_at: 2021-10-20 12:07:20.299
slug: jmh-introduction
tags: 
- JMH
---

站在巨人的肩膀上，JMH是一个工具，不打算深入研究它，只求能够正确使用，网上关于它的使用方法讲的还挺全面的，就直接看他们吧。

这篇文章包含基本使用方法、注意事项、IEAD插件、JMH可视化工具的介绍等：[性能调优必备利器之 JMH](https://cloud.tencent.com/developer/article/1644001?from=article.detail.1378150)

这篇文章包含较为深层次的解释：[JAVA拾遗 — JMH与8个代码陷阱](https://cloud.tencent.com/developer/article/1350814?from=article.detail.1378150)

当然最重要的还有官方例程：[JMH给的38个例子](https://github.com/lexburner/JMH-samples)

作为补充，我添加了所有注解的说明，还有自己使用中遇到的问题

<!-- more -->

## 注解解释

- Benchmark：被该注解标记的方法将会编译生成benchmark代码，并添加到Benchmarklist中。

  被它标记的方法有几个限制，如果要打破限制，只能再写一个方法，然后再Benchmark方法中调用他们

  - 必须是public的
  - 方法参数只能是 State、Control、Blackhole三种

- BenchmarkMode：模式多选一

  - 测试吞吐量
  - 测试每次调用的平均时间
  - 基于采样时间，在规定的采样时间内，测试完成的情况
  - 每个方法只执行一次，然后看执行时间

- CompilerControl：编译器控制

  - 为方法添加端点
  - 打印方法的信息
  - 排除某个具体的方法
  - 强制内联
  - 强制不要内联
  - 只编译当前注释的方法，其它的忽略

- Fork：fork的次数，即fork多少个进程来执行方法，放在类上时，对每个方法都有效。

  即，一个方法需要被多少个进程执行，结果取平均

- Group：分组，一个组的方法共享一批线程

  - 一个组内有一个或多个线程
  - 被Group注解注释的多个方法共享一批线程
  - 默认情况下，针对一个Benchmark方法，只会由单个线程执行，除非用GroupThreads进行指定

- GroupThreads：决定有多少个线程参与执行当前的方法

- Measurement：设置做测试时的行为，和Warmup类似，只不过后者是用来热身，前者是用来正式测量的

  能设置的参数如下，

  - iterations：设置测试的迭代数量
  - time：一个迭代执行多长时间
  - timeUnit：时间单位
  - batchSize：每次操作执行方法多少次

  ```kotlin
  @Measurement(iterations = 1, time = 2, timeUnit = TimeUnit.SECONDS, batchSize = 3)
  ```

  这样的配置标识，执行1个迭代，每个迭代时长2秒，每次操作执行3次调用

- OperationsPerInvocation：调用前执行的operation次数，我也不懂啥意思

- OutputTimeUnit：测量结果输出的时间单位

- Param：参数，可以设置参数，在被测试方法中使用，以查看不同参数时的效果

- Setup：设置生命周期方法

  - 每次迭代前调用一次
  - 每次调用前调用一次
  - 测试完成调用一次

  可以理解为JUnit的@Before

- TearDown：等同于Setuo(Level.Trial)

- State：定义了实例的共享范围

  - 全局共享
  - 组内共享
  - 每个线程都会创建一个新的实例

- Threads：指定固定的线程数来跑测试

- Timeout：整个测试的超时时间

- Warmup：类似Measurement，唯一的区别是，这是用来预热的

## 工作机制

JMH由两部分组成

- 代码生成器，根据注解配置，生成我们待测试方法的测试代码
- 库：底层API支持，我们所使用的注解和生成的代码均依赖于它

因此在引入依赖时，一要依赖库，而要以注解处理器的形式引入，对kotlin，注释注解处理器是kapt

```kotlin
dependencies {
  implementation("org.openjdk.jmh:jmh-core:1.28")
  annotationProcessor("org.openjdk.jmh:jmh-generator-annprocess:1.28")
  kapt("org.openjdk.jmh:jmh-generator-annprocess:1.28")
}
```

## 遇到的问题

- ERROR: Unable to find the resource: /META-INF/BenchmarkList

  Benchmarklist是在代码生成阶段生成的，没有说明没有进行生成。这是因为我没有正确配置`jmh-generator-annprocess`，当成普通依赖了，实际上应该如上所述，是注解生成器。

  