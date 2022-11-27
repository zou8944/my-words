---
created_at: 2019-09-08 11:00:21.0
updated_at: 2021-02-16 23:26:30.182
slug: rxjava-introduction
tags: 
- RxJava
---

## Observable

 ReactiveX中, 应用的是观察者模式, 一个观察者订阅一个被观察者. 然后该观察者根据被观察者释放的任何信息进行反应. 这样能够使得并发称为可能, 观察者不必阻塞等待被观察者的响应内容, 而是创建一个哨兵, 并随时准备在未来的任何时候响应被观察者释放出的内容
 <!-- more -->
Observable通过调用Observer的方法向其发送通知
如下图片能够展示一个被观察者释放的一系列数据, 以及对这些数据进行转换的操作

![1564802038820](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564802038820.png)

本文中称的观察者, 在别的文档中有时也被称为订阅者, 也叫作反应器. 该模型对应于 反应式模型

### 建立一个Observable

- 定义一个结果处理的方法, 该方法是观察者的一部分
- 将异步调用本身定义为被观察者
- 通过订阅的方式, 将观察者附加到被观察者身上. 

### OnNext, OnCompleted, OnError

这些是观察者的一部分. 三个方法被调用的时机不同

- OnNext
  被观察者每次释放一个数据都会调用它

- OnError
  当被观察者发生错误时会调用, 调用该方法后, OnNext和OnCompleted方法都不会再被调用

- OnCompleted
  在调用最后一次OnNext时会调用OnCompleted

我们管OnNext叫做释放数据, 管OnError和OnCompleted叫通知.

### 观察者约定(The Observable Contract)

该约定尝试对被观察者做一个正式的定义, 他会出现在Rx文档的很多地方

#### 通知

一个被观察者通过如下方式和它的观察者们交流

- OnNext: 从被观察者向观察者传送一个item
- OnCompleted: 表明被观察者已经成功地完成, 并且不会再释放数据
- OnError: 表明被观察者已经被某个原因中止, 并且不会再释放数据
- OnSubscribe(背压): 表明被观察者已经准备好接收来自观察者的请求通知

一个观察者通过如下方式和它的被观察者交流

- Subscribe: 表明观察者已经准备好接收来自被观察者的通知
- UnSubscribe: 表明观察者已经不想要再接收到被观察者的通知了
- Request(背压): 表明观察者只希望接收到不超过特定数量的来自被观察者的通知(通过OnNext发送过来的)

#### 约定

一个被观察者可能调用0次或多次OnNext, OnCompleted和OnError只会且一定会调用其一, 且其后不得再发送任何通知

一个被观察者可能根本不会释放任何数据, 也可能因为永远不停止而不会发出OnCompleted和OnError. 即: 观察者可能不发出任何通知, 可能发出OnCompleted和OnError通知, 也可能仅发出OnNext通知

一个被观察者发送给观察者的通知必须是串行的, 他们可以在不同的线程发出, 但必须有一个先行发生原则确保其顺序

#### 被观察者的中止

如果被观察者没有发出完成或错误通知, 观察者会认为它仍然是活动的, 并且可能会给他发送通知(如unsubscribe和request通知等).
如果被观察者发出了完成或错误通知, 该被观察者会释放其资源, 其观察者不应试图与其有进一步的沟通
一个OnError通知必须包含错误原因, 就是说传入一个null的OnError是无效的
被观察者停止自己之前, 必须先向它的所有订阅者发出OnCompleted或OnError消息

#### 订阅和取消订阅

被观察者可以在收到观察者发出的Subscribe通知后马上开始向其发送通知
当观察者发送UnSubscribe通知给被观察者时, 被观察者会试图停止向其发送通知, 但这是不被保证的, 
被观察者发送OnCompleted或OnError通知给观察者时, 它们的订阅关系将会自动结束. 不需要再由观察者发送UnSubscribe消息给被观察者

#### 多个订阅者

如果第二个观察者订阅了一个已经向第一个观察者释放了一些数据的被观察者, 那么第二个观察者收到的消息可能如下

- 从订阅开始, 所有订阅者将收到一样的消息,(即新的订阅者会收不到已经释放原来订阅者的消息)
- 重新向新的订阅者发送完全相同的数据
- 新的订阅者将会收到顺序完全不同的数据

上面这些都是可能的, 具体哪一种取决于被观察者的实现. 

没有一个通用的约定说两个多个观察者能够得到一样顺序的消息

#### 背压

背压是可选的, 并非所有ReactiveX实现都包括背压.而且在哪些包括了背压的实现中, 也并非所有被观察者都支持背压.
如果一个被观察者实现了背压，并且它的观察者使用了背压，那么该被观察者不会在订阅后立即向观察者发出项目。相反，它将向观察者发出一个onsubscribe通知。
观察者收到onsubscribe消息后, 会发送一个请求通知给被观察者, 指定需要数据的数量, 被观察者就会释放不多于该数量的数据. 当然, 被观察者也可以主动发出OnCompleted和OnError通知, 甚至在观察者发送请求通知前发出以结束订阅.

对于没有实现背压的被观察者, 当它收到来自观察者的请求通知时, 应该回敬一个OnError通知, 说明自己并不支持背压

请求是累积的: 如果一个观察者发出了三个请求通知, 分别请求3,5,10条数据, 则被观察者将会至多发送18条数据, 不会因为说刚发了两条时马上来了一个5条的请求就把原本剩下的那一条忽略掉.
如果被观察者产生了多余请求数量的数据, 多出来的数据的处理方式完全看被观察者自己.

### 热 , 冷 的被观察者

- 热: 指的是被观察者从一开始就释放数据, 这样观察者从订阅开始就只能从中途获取数据
- 冷: 指的是被观察者在被定于后才开始释放数据, 这样就能保证获取完整的数据
- connectable: 这是在部分ReactiveX实现中的被观察者, 只有当connect方法被调用时才会释放数据, 而不管有没有观察者订阅他

### 被观察者操作符的组合

被观察者和观察者仅仅是ReactiveX的开始, 他们本身只是标准的观察者模式的轻量级扩展, 更适合处理一连串事件, 而不是单个回调
其真正厉害的地方在于通过操作符转换, 组合, 运算由被观察者释放出来的一系列数据

## Operators

### 操作分类

#### 创建被观察者

- create: 通知显式调用订阅者方法来创建Observable
- defer: 观察者订阅时才创建, 不订阅就不创建, 且为每个新的观察者创建一个新的被观察者
- interval: 创建一个每隔一段时间释放一个数据的被观察者

#### 处理操作

- buffer: 被观察者一个一个地发送数据, 该操作设定缓存个数, 缓存满了之后将整个缓存一起释放
- flatMap: 将多个被观察者释放的数据合并到一个被观察者中
- groupBy: 将单个被观察者切分成多个被观察者, 每次只从原被观察者处释放一组
- scan: 对每个释放的数据应用一个函数, 将结果释放出去, 一次运算释放的值会作为下一次运算的输入

#### 过滤操作

- debounce: 只释放这样的数据, 该数据被释放之后, 指定的一段时间内没有新数据的出现, 则释放该数据.否则对新释放的数据继续做此判断
- elementAt: 只获取释放的第n个元素
- first: 只释放第一个数据, 或满足条件的数据
- last: 只释放最后一个数据
- sample: 获取一段时间内被观察者释放的最后一个数据
- take: 只获取头几个释放的数据
- takeLast: 只获取最后几个释放的数据

#### 组合操作

将多个被观察者合并为一个被观察者

- combineLatest: 将一个被观察者释放的数据和另一个被观察者释放的最近的一个数据组合起来

![1564822583394](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564822583394.png)

- join: 将两个被观察者释放的在一个时间窗中的数据进行合并

![1564823248295](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564823248295.png)

- merge: 直接将两个释放合并

![1564823342178](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564823342178.png)

- startWith: 在释放常规数据前, 先释放指定的数据

![1564823975876](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564823975876.png)

- switch: 将释放数据为Observable的几个被观察者转换成一个释放所有这些数据的被观察者

![Switch](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/switch.c.png)

- zip: 将多个被观察者释放的数据以一定的方法合并到一个被观察者上

![1564824218864](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564824218864.png)

#### 错误处理操作

- catch: 从错误中恢复出来, 使原被观察者继续执行
- retry: 被观察者抛出错误时, 重新订阅它

#### 被观察者的工具操作

- delay: 每个元素都延迟释放
- doOnEach: 为每个元素执行一个操作
- materialize: 将释放的消息和发送的通知都当做释放的消息
- observeOn: 指定观察者将会在哪个schedudler上对被观察者进行观察
- subscribe: 将被观察者绑定到观察者
- timeInterval: 将一个释放普通元素的被观察者转换为释放元素之间的时间间隔的被观察者
- timeout: 一个元素释放后的指定时间内不再释放新的元素时, 停止该被观察者
- timestamp: 为每一个释放的元素绑定一个时间戳

#### 条件和布尔操作

- all: 判断是否释放的所有元素都满足给定条件
- amb: 给定多个被观察者, 只获取最先释放数据的被观察者的所有数据
- contains: 判断释放的元素是否包含指定元素
- sequenceEqual: 判断两个被观察者是否释放了一样的数据流

#### 数学和聚集操作

- concat:  将两个被观察者连接起来, 一个被观察者释放完所有数据后, 另一个被观察者才继续释放它的所有数据
- reduce: 对每个释放的数据应用某个函数, 并输出最终结果

![1564825542157](https://gdz.oss-cn-shenzhen.aliyuncs.com/hexo/%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%20-%20RxJava/1564825542157.png)

#### 背压操作

这是用来应对生产数据快过消费数据的情况

#### Connectable Observable的操作

- connect: 开始释放数据
- publish: 将原本的observable转换成一个Connectable Observable
- refcount: 使Connectable Observable向一个原始Observable一样工作
- replay: 确保所有观察者都能够看到相同顺序的数据, 即使他们在不同时刻订阅

#### Observable转换操作

- to:  将一个Observable转换成其它对象或数据结构

## Single

Single是Observable的一个变体, 不同于Observable是释放一系列数据, Single仅释放一个数据, 或触发一次错误.因此, Single中, 仅能使用OnSuccess与OnError同观察者交流. 当上述两个方法中任意一个被调用了, 另一个都不会再被调用, Single也停止了, 订阅关系也自动解除了.
也就是说, Single没有结束一说, 只有成功和错误两个时机, 因此调用doOnCompleted是不会被触发的

### Single中值得记住的方法

- doOnSuccess/doOnError: 在调用OnSuccess和OnError方法时, 会同时触发该方法

## Subject

Subject在某些实现中有做, 它可以看做是一个桥梁或是一个代理, 能够同时充当订阅者, 获取其它被观察者的消息, 也能够充当被观察者, 向其它观察者发送消息.

Subject有四种变形, 分别用在不同的场景下

### AsyncSubject

AsyncSubject在源Observable结束时, 释放源Observable的最后一个元素, 如果源Observable一个元素都没有释放, 则AsyncSubject也会什么都不释放, 然后结束. 如果源Observable发生错误, 则AsyncSubject会直接将该错误释放, 不会释放其它数据

### BehaviorSubject

BehaviorSubject会释放源Observable最近释放过的数据, 如果没有最近释放过的数据, 则返回指定的默认值.

当源Observable发生错误时, BehaviorSubject不会释放任何数据. 而是直接释放该数据

### PublishSubject

PublishSubject直接将源Observable的数据进行原样释放, 源Observable来一个它就释放一个, 这意味着较晚订阅它的订阅者会丢失订阅之前的消息

### ReplaySubject

ReplaySubject会将源Observable所释放的数据全部再次释放一遍.

## Scheduler

Scheduler用于做线程调度.

默认情况下, Observable及其操作链将会工作在subscribe调用时的线程上. 可以通过ObserveOn操作符改变该行为. 该方法指定一个线程调度器, Observable会在其上运行.

SubscribeOn指定了Observable将会在哪个调度器上进行操作, 即观察者所在的线程.