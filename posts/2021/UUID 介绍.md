---
created_at: 2021-09-30 16:43:00.093
updated_at: 2021-09-30 16:43:00.093
slug: uuid-introduction
tags: 
- UUID
---

UUID，Universal Unique Identifier，全局唯一标识符。也叫做GUID，Global Unique Identifier。

概念都了解，全局唯一嘛，但怎么实现的？多大概率重复？JDK的UUID和PostgreSQL的UUID一样吗？带着这些问题，我们从RFC，到JDK源码、PG手册，一点点看。

本文包含以下内容：

- UUID实现原理
- 自己实现一个UUID
- JDK的实现方式
- PG的实现方式
- 其它全局唯一ID

## 实现原理

老样子，要想了解一项基础技术，最好的方式是阅读一手资料。于UUID，它是[RFC4122](https://www.rfc-editor.org/rfc/pdfrfc/rfc4122.txt.pdf)。

这一节，更莫如说是对RFC的总结，毕竟规范这东西，写得太啰嗦了，全文字不说，还没有示意图。

### 基本特性

- 长度128个bit位。一般通过16位十六进制字符表示，如：4cc9de16-414b-4f68-9b7e-6feeb8f629b0
- 不需要中心管理，具有跨越时间和空间的唯一性
- 按照本标准中的算法，支持每台机器每秒高达1000万次高分配速率

### 组成

理解UUID有两个重点：一是理解其组成部分；二是理解各版本对各部分的填充方式。我们先看最重要的——组成部分。

为了较为形象地展示，我画了张图。第一行是结果，第二行是十六进制说明，第三行是二进制说明。

![image-20210930084244949](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210930084244949.png)

- time-low：时间戳低位，占用32个bit
- time-mid：时间戳中位，占用16个bit
- time-high-and-version：时间戳高位+版本号，前者占12个bit，后者占4个bit，注意区分版本号是在前的
- clock-seq-high-and-reserved：时钟序列高位+预留位。前者占6个bit，后者占2个bit，也注意他们的前后顺序
- clock-seq-low：时间序列低位，占8个bit
- node：节点，占用48个bit

引出新概念，time、clock-seq、node

- time：即时间戳
- clock-seq：当时间戳或node重复时，使用clock-seq作为附加保证唯一性
- node：机器的节点，一般是机器的MAC地址

### 区分版本

注意到上面说组成时，有一个version字段。UUID是有多个版本的，目前总计5个。

版本规定了各字段的填充方式，版本2比较特殊这里忽略，其它版本如下

| 版本 | Timestamp                                   | Clock sequence                                               | node                           |
| ---- | ------------------------------------------- | ------------------------------------------------------------ | ------------------------------ |
| 1    | 从UTC时间1582-10-15 00:00:00起，100ns的个数 | 第一个clock sequence应该是随机产生的<br />如果知道本机上一次生成UUID的clock sequence，则此次只需要在其基础上加一<br /> 如果不知道，该字段需要设置成一个随机数 | MAC地址 如果没有，则使用随机数 |
| 3    | 命名空间+名称的MD5只的一部分                | 命名空间+名称的MD5只的一部分                                 | 命名空间+名称的MD5只的一部分   |
| 4    | 随机数的一部分                              | 随机数的一部分                                               | 随机数的一部分                 |
| 5    | 命名空间+名称的SHA1只的一部分               | 命名空间+名称的SHA1只的一部分                                | 命名空间+名称的SHA1只的一部分  |

可以看到，所谓的时间戳、时钟序列、node这些字段，仅对版本1有效，其它版本填充进去的值并无逻辑意义。

### 如何保证唯一性

- 对Version 1：它通过MAC地址保证空间唯一性，时间戳+序列号保证时间唯一性
- 对Version 2：和Version 1类似，只不过会把时间戳的前4位置换为POSIX的UID或GID
- 对Version 3、5：它纯依赖于名字保证唯一性，这就需要一个规整的命名系统：命名空间+名称
- 对Version 4：它纯通过随机数保证唯一性，此时一个高质量的随机数发生器就显得尤为重要

### Version 1生成逻辑

1. 获取一个系统级别的全局时钟

2. 从一个系统全局共享的的存储位置，读取上一个UUID的状态：时间戳、始终序列、node等

3. 获取当前时间戳：从UTC时间1582-10-15 00:00:00起，100ns的个数

4. 获取nodeid，即MAC地址

5. 如果上一个UUID状态不稳定（不存在、nodeid与新获取的nodeid不一样），生成一个随机clock value

6. 如果状态存在，但时间戳比当前时间戳还晚，则clock sequence自增

7. 将新的状态保存

8. 将上面的三个部分按照格式组成UUID

**有一个bug**

MAC地址直接放在nodeid中，就是一个bug，这会暴露用户的MAC地址：梅丽莎病毒制作者的位置就是这么暴露的

### Version 4生成逻辑

1. 获取一个随机数
2. 将预留位、版本位之外的位，使用该随机数填充，填充位对应方式，参考RFC

### Version 3、5生成逻辑

1. 命名空间+名字组成字符串，使用MD5或者SHA1计算摘要
2. 将预留位、版本位之外的位，使用该摘要填充，填充位对应方式，参考RFC

### 为什么时间戳从1582-10-15开始

这是公历改革到基督教日历的日期，说来话长，我也没啥兴趣去详细了解，如果需要，[看看知乎吧](https://www.zhihu.com/question/300868434)

## 自己写一个UUID吧

尝试着实现了一下抽象定义和基于时间戳的版本，发现主要有几个难点：kotlin的进制转换、二进制操作等。

这是一个不能实际使用的UUID版本（实现它也不是本文的目的），仅作演示。

先是UUID的抽象定义，我们使用两个Long作为底层bit持有对象，定义各字段的set方法，主要是二进制操作。

```kotlin
abstract class UUID {

    companion object {

        const val TIME_LOW_MASK = (0xFFFFFFFFL).shl(32)
        const val TIME_MID_MASK = (0xFFFFFFFFL).shl(16)
        const val VERSION_MASK = (0xFFL).shl(12)
        const val TIME_HIGH_MASK = 0xFFFFFFL

        const val RESERVED_MASK = (0xFL).shl(62)
        const val CLOCK_SEQ_HIGH_MASK = (0xFFFL).shl(56)
        const val CLOCK_SEQ_LOW_MASK = (0xFFFFL).shl(48)
        const val NODE_MASK = 0xFFFFFFFFFFFFL

        fun timeBasedUUID(): UUID = UUIDVersion1()

    }

    /**
     * 高有效位们：靠右
     */
    private var mostSignificantBits = 0L

    /**
     * 低有效位：靠左
     */
    private var leastSignificantBits = 0L

    fun setTimeLow(timeLow: Int) {
        leastSignificantBits = leastSignificantBits.or(timeLow.toLong().shl(32).and(TIME_LOW_MASK))
    }

    fun setTimeMid(timeMid: Int) {
        leastSignificantBits = leastSignificantBits.or(timeMid.toLong().shl(16).and(TIME_MID_MASK))
    }

    fun setVersion(version: Int) {
        leastSignificantBits = leastSignificantBits.or(version.toLong().shl(12).and(VERSION_MASK))
    }

    fun setTimeHigh(timeHigh: Int) {
        leastSignificantBits = leastSignificantBits.or(timeHigh.toLong().and(TIME_HIGH_MASK))
    }

    fun setReserved(reserved: Int) {
        mostSignificantBits = mostSignificantBits.or(reserved.toLong().shl(62).and(RESERVED_MASK))

    }

    fun setClockSeqHigh(clockSeqHigh: Int) {
        mostSignificantBits = mostSignificantBits.or(clockSeqHigh.toLong().shl(56).and(CLOCK_SEQ_HIGH_MASK))
    }

    fun setClockSeqLow(clockSeqLow: Int) {
        mostSignificantBits = mostSignificantBits.or(clockSeqLow.toLong().shl(48).and(CLOCK_SEQ_LOW_MASK))

    }

    fun setNode(nodeId: Int) {
        mostSignificantBits = mostSignificantBits.or(nodeId.toLong().and(NODE_MASK))

    }

    override fun toString(): String {
        val lsbString = leastSignificantBits.toHexString()
        val msgString = mostSignificantBits.toHexString()

        val seg1 = lsbString.substring(0, 8)
        val seg2 = lsbString.substring(8, 12)
        val seg3 = lsbString.substring(12, 16)
        val seg4 = msgString.substring(0, 4)
        val seg5 = msgString.substring(4, 16)

        return "$seg1-$seg2-$seg3-$seg4-$seg5"
    }

}
```

然后是一个粗糙的实现类，实现Version 1

```kotlin
class UUIDVersion1 : UUID() {

    init {
        // 计算time
        val start = LocalDateTime.of(1582, 10, 15, 0, 0, 0, 0)
        val end = LocalDateTime.now(ZoneId.of("UTC"))
        val duration = Duration.between(start, end)
        val time = duration.toMillis() * 10
        // 计算clock seq
        val clock = 0
        // 获取node，我们用随机数替换
        val node = Random.nextInt()

        this.setTimeLow(time.toInt())
        this.setTimeMid(time.shr(32).toInt())
        this.setTimeHigh(time.shr(48).toInt())

        this.setClockSeqHigh(clock.shr(8))
        this.setClockSeqLow(clock)

        this.setNode(node)

        this.setVersion(0b001)
        this.setReserved(0b10)
    }

}
```

我们还可以将生成的UUID转换为JDK的UUID进行验证。

```kotlin
fun main() {
    val uuidString = UUID.timeBasedUUID().toString()
    println(uuidString)
    val uuid = java.util.UUID.fromString(uuidString)
    println(uuid.version())
    println(uuid.variant())
    println(uuid.timestamp())
    println(uuid.clockSequence())
    println(uuid.node())
}
```

能够得到如下输出

```bash
51d8c022-7dfc-1000-8000-ffffd963e9ed
1
2
138522658390050
0
281474328947181
```

> 仔细想想，这个时间戳也不一定要从1580年开始，也可以换成自定义的时间戳，完全看需求。

## JDK UUID

JDK只提供Version 3和Version 4两种UUID，实现上也超级简单。

类似地，它也用两个long来组成128位，构建时直接分配位即可

```java
/*
  * The most significant 64 bits of this UUID.
  *
  * @serial
  */
private final long mostSigBits;

/*
  * The least significant 64 bits of this UUID.
  *
  * @serial
  */
private final long leastSigBits;

private UUID(byte[] data) {
  long msb = 0;
  long lsb = 0;
  assert data.length == 16 : "data must be 16 bytes in length";
  for (int i=0; i<8; i++)
    msb = (msb << 8) | (data[i] & 0xff);
  for (int i=8; i<16; i++)
    lsb = (lsb << 8) | (data[i] & 0xff);
  this.mostSigBits = msb;
  this.leastSigBits = lsb;
}
```

### Version 4

```java
public static UUID randomUUID() {
  SecureRandom ng = Holder.numberGenerator;

  byte[] randomBytes = new byte[16];
  ng.nextBytes(randomBytes);
  randomBytes[6]  &= 0x0f;  /* clear version        */
  randomBytes[6]  |= 0x40;  /* set to version 4     */
  randomBytes[8]  &= 0x3f;  /* clear variant        */
  randomBytes[8]  |= 0x80;  /* set to IETF variant  */
  return new UUID(randomBytes);
}
```

可以看到，重点其实在Holder.numberGenerator，它的随机性决定了UUID的重复概率。而其实现SecureRandom，则涉及到另一个知识点——随机数，我们这里挖个坑，后面再探究随机数生成器到底有多随机。

```java
private static class Holder {
  static final SecureRandom numberGenerator = new SecureRandom();
}
```

### Version 3

```kotlin
public static UUID nameUUIDFromBytes(byte[] name) {
  MessageDigest md;
  try {
    md = MessageDigest.getInstance("MD5");
  } catch (NoSuchAlgorithmException nsae) {
    throw new InternalError("MD5 not supported", nsae);
  }
  byte[] md5Bytes = md.digest(name);
  md5Bytes[6]  &= 0x0f;  /* clear version        */
  md5Bytes[6]  |= 0x30;  /* set to version 3     */
  md5Bytes[8]  &= 0x3f;  /* clear variant        */
  md5Bytes[8]  |= 0x80;  /* set to IETF variant  */
  return new UUID(md5Bytes);
}
```

这个更简单，做一下MD5，修改相应的bit填入即可，它的唯一性就完全依赖于传入的name了。

## PostgreSQL的UUID

根据[手册](https://www.postgresql.org/docs/current/functions-uuid.html)描述，PG的UUID也是Version 4，即基于随机数生成。

## UUID重复的概率

就是个好奇，我们能够大致算一算，UUID重复的概率有多大，其实可以归结如下。

- 对基于时间戳的情况，node稳定时，多个节点不可能重复，而单个节点，由于有记录上一个UUID的状态，因此也不会重复。只不过有生成速率限制，以RFC的方式来说，每个节点每100ns，最多能够生成2^14=16384个UUID，换算成秒，即每秒1.6亿个。

- 基于随机数的情况，取决于随机数生成器的质量
- 基于名字的情况，取决于命名系统，这种情况UUID只是命名系统的延伸，应该说不会考虑UUID重复的情况，而是命名系统本身的性能
- 128bit空间本身是否可能重复呢？用尽了就会，不过这个概率，类似流星撞地球吧。

## 其它全局唯一ID

最为大家熟知的恐怕就是雪花算法了吧，此外号段模式也算一个。

### 雪花算法（SnkwFlake）

了解了UUID Version 1的生成方式后，雪花算法就很容易理解，也是由时间戳-机器id-序列号组成，不同的是其只需要64个bit。且各字段可以根据实际需求调整bit的个数。雪花算法只是一种思想：将各位打散，再赋予不同的用途。UUID Version 1也是这种思想。



![image-20210930142313559](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210930142313559.png)

**几个需要考虑的问题**

- 时钟回拨问题：常见的方式是容忍小范围回拨，即如果当前时间戳比上一个生成的时间戳早，且在一定范围内，则依旧使用上一次的时间戳。这算一种校准方式，即回拨的这个时间差会被算到上一个时间戳的序列中，随着时间的推移，时间回拨问题会被抹平，但这段期间的生成效率会降低。
- 机器ID的生成方式：机器ID必须是稳定的，常见的解决方式是融合MAC地址。

**雪花算法和UUID差别**

雪花算法得到的id依旧是64位，就是一个long，且时间戳在高位，是有序递增的。有序性，往往很重要。

**一些雪花算法的实现**

- 百度UidGenerator

  它解决时钟回拨的方式，是不容忍任何回拨，直接报错

- 美团Leaf

  可选基于雪花算法或基于号段模式两种方案。其中使用雪花算法时，依赖于Zookeeper来分配WorkerID

  它解决时钟回拨问题，和上面我们说的类似

### 号段模式

这并不是什么算法，而是一种数据库自增ID的用法，一次取一批ID，用完了再取，保证了唯一性，降低了数据库的访问频率。

## 分布式ID的选择

你看，我们已经了解了最重要的全局唯一ID生成方式，那就可以讨论这个问题：分布式ID应该用哪种呢？

UUID优点在于生成简单，唯一性好，几乎所有语言都有标准实现。缺点在于长度过长、不具有单调性，且无意义。

雪花算法优点在于具有单调性，长度适中。缺点在于需要自己实现或引入第三方库。（一说雪花算法缺点在于依赖时间，但要在跨时间上保证唯一性，除了依赖时间，就是依赖随机数，所以我认为也算不上缺点，且时间回拨不是已经有解决方式了嘛）

如果ID需要存入数据库，由于UUID的无序性，可能会使得索引重建花费较长时间，当然使用**雪花算法比较好**。

### 每记选择UUID作为key，合理吗？

作为一个离线客户端软件，我们面临以下问题

- 客户端环境千奇百怪，多平台（PC、网页、安卓、IOS等），多版本，总之，就很难信任客户端环境
- 离线时也要能正常使用

如果使用雪花算法，会有几个问题

- 首先，工作机器ID的确定，需要考虑的情况就会比较多，即生成算法需要调试。客户端的时间回拨，那可不就是修正就能够完事的。
- 其次，即使有序性有了，但多个设备上传的顺序依旧无法保证，受网络、环境影响较大，依旧会造成索引重建时候较多数据的移动

如果使用UUID，其实就只有一个问题

- 数据库存储的效率：索引重建。如果是聚簇索引，索引重建时移动的数据会很多，这对MySQL的innodb这类引擎来说可能是灾难。但是PgstgreSQL并非以B+树存储数据，所以性能损失并非想象的那么严重。具体如何，待后面详细研究一波PG的各种原理（完蛋，又挖了一个坑）

  且，即使是MySQL，依然可以解决：主键设为单调自增的number，来自客户端的UUID仅作为普通字段，在该字段创建索引，会好很多。

综上所述，使用UUID对客户端更方便，在服务端性能也算可以接受，所以说**是合理的**。

作为佐证，我抓了一个印象笔记下类每记产品”印象清单“，它就更加直白了，id字段名为”taskGuid“，值就是UUID。

```json
[
  {
    "syncDataObject":{
      "tasks":[
        {
          "state":1,
          "ruleId":"",
          "description":"",
          "clientUpdatedTime":1632988316566,
          "sortIndex":0,
          "dueTime":1632988311635,
          "operation":0,
          "title":"æµè¯",
          "finishedTime":-1,
          "taskGuid":"a1e4836c-4d59-409d-bf00-864d6d31cba0",
          "createTime":1632988316566,
          "taskListId":"default",
          "reminderTime":-1,
          "reminderType":0,
          "taskRelatedNote":[
            
          ]
        }
      ],
      "rules":[
        
      ],
      "taskLists":[
        
      ]
    }
  }
]
```

## 好文推荐

这篇UUID的文章写的不错，如果结合起来看，可以增进理解：[冷饭新炒：理解JDK中UUID的底层实现](https://www.cnblogs.com/throwable/p/14343086.html#namespace-name-based-md5%E7%89%88%E6%9C%AC%E5%AE%9E%E7%8E%B0)

雪花算法呢，这篇文章看起来还行：[SnowFlake](https://zhuanlan.zhihu.com/p/402822041)

美团的Leaf，美团技术团队博客有进行说明：[Leaf——美团点评分布式ID生成系统](https://tech.meituan.com/2017/04/21/mt-leaf.html)

## 总结

研究UUID的出发点，只是其RFC很短，仅三十多页，有效内容不到二十页。过程中却有几点意外之喜：

- 顺着UUID的实现原理，了解到JDK的实现方式，自此，UUID于我，成了白盒；
- 能够体会JDK不提供Version1的原因（它太依赖具体系统，而语言级别的实现，一定是要所有情况通用的，显然Version 1的通用实现，不大好办）；
- 思路发散到分布式ID，详细了解了雪花算法，它和Version 1是如此接近，却只因为将node和seq换了个位置就能够单调递增，如此相似，结果却如此不同；
- 离线客户端用SnowFlake如何？它们看起来是大型分布式系统，实则与我们后端常说的分布式系统很不一样，这其中最大的不同是客户端环境不可控。
- 同时，还挖了两个坑：深入研究随机数、深入研究PostgreSQL

本着输出驱动输入的方法完成本文，预期一两天，实则因思路发散花了更多时间，结果是令人满意的，因为它让我对技术，又少了一个模糊地带。

也应验了那句话：持续不断地学习，一定会给你带来惊喜。关键词是：**持续不断**