---
created_at: 2021-10-06 19:17:59.175
updated_at: 2021-10-06 19:17:59.175
slug: serialization-java
tags:
- 序列化
- Java
---

序列化和反序列化，渗透在日常开发的方方面面。

所谓的序列化，就是将数据转换为能够在网络上传输、在数据库中存储、在文件中持久化的格式，这类格式很多，可以是字节流（如Java自带的序列化机制）、可以是JSON（系统之间传输用的较多）、可以是Protocol Buffers（压缩率高，GRPC有用）。反序列化，即序列化的反过程。

序列化这件事，不同的语言、库，提供了不同的使用方法，哪怕是对同一种序列化格式的支持也有差别。因此，深入了解常用的序列化技术，很有必要。不要再去记使用方法了，我们来看原理吧。

<!-- more -->

## 序列化探索思路

从序列化格式看，市面上有很多种，我选取最常用的两种：JSON和ProtoBuf。对JSON，协议本身比较简单，主要关注不同库的使用方式和原理、功能和性能差异，重点放在使用最为广泛的Jackson和最快bug也最多的FastJson上；对ProtoBuf，协议本身就具有一定的特点，因此重点放在协议的研究上。

从语言层面看，每种语言一般都会提供序列化的方式，作为对该语言了解的一部分，它提供的序列化也需要研究。这方面的重点我放在Java和Kotlin上。

综上，我们将会分为四个部分学习探索

- Java的序列化支持
- Kotlin的序列化支持
- JSON序列化专题探究
- ProtoBuf序列化专题探究

本文，就是Java。

## Java序列化的使用方法

作为一个Java码农，一定会记得Java序列化的使用方式：目标类实现Serializable接口，给出serialVersionUID常量。然后该类的对象就能够被序列化了。这没错，但不完整，Java序列化能做的，远比这个多。

具体来讲，实现序列化，Java提供了两个接口：Serializable和Externalizable，实现前者的类的序列化逻辑由Java提供，自己能够稍微干涉；实现后者的类的序列化逻辑则完全由该类自己提供。

### Serializable

Java中，一个能够被序列化的类，必须满足如下条件

- 实现Serializable接口
- 指定需要序列化的字段值，两种方法
  - 排除法：默认所有字段都会被序列化，如果某个字段不需要，使用transient关键字排除
  - 显式声明法：声明serialPersistentFields变量，声明需要被序列化的字段

也就是说，下面两种序列化的声明方式，是一样的

```java
// 排除法
public class Video implements Serializable {

    private String id;
    private String title;
    private transient String description;

}

// 显式声明法
public class Video implements Serializable {

    private String id;
    private String title;
    private String description;

    private static final ObjectStreamField[] serialPersistentFields = {
        new ObjectStreamField("id", String.class),
        new ObjectStreamField("title", String.class),
    };

}
```

> One Tip：Kotlin中使用Java序列化时，是没有transient关键字的，此时使用@Transient注解替代

此外，它还能增加一些方法以更加个性化地控制序列化和反序列化

- writeObject()：控制写
- readObject()：控制读
- writeReplace()：指定一个替换对象写进流
- readResolve()：指定一个从流读出来的对象的替换对象

需要注意的是，上述两个write方法互斥，两个read方法互斥，如果同时存在，则只有后面的会生效。writeReplace和readResolve互斥，如果同时存在，只会writeReplace生效。下面演示readResolve()，同时通过注释的方式将其它三个方法签名给出，以供参考。

```java
@Data
@AllArgsConstructor
public class Video implements Serializable {

    private String id;
    private String title;
    private String description;

//    private void writeObject(ObjectOutputStream stream) throws IOException {
//        System.out.println("执行writeObject");
//        stream.writeLong(0xfffffff);
//    }
//
//    private void readObject(ObjectInputStream stream) throws IOException, ClassNotFoundException {
//        System.out.println("执行readObject");
//    }

//    private Object writeReplace() throws ObjectStreamException {
//        System.out.println("执行writeReplace");
//        return "替换成了一个String";
//    }

    public Object readResolve() throws ObjectStreamException {
        System.out.println("执行readResolve");
        return new Video("ID", "标题", "描述");
    }

}

class Main {
    public static void main(String[] args) throws IOException, ClassNotFoundException {
        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);

        Video oldVideo = new Video("旧ID", "旧标题", "旧描述");
        System.out.println("序列化前：" + oldVideo);

        oos.writeObject(oldVideo);
        System.out.println("序列化后：" + bos);

        ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
        ObjectInputStream ois = new ObjectInputStream(bis);
        Video newVideo = (Video) ois.readObject();
        System.out.println("反序列化后：" + newVideo);
    }
}
```

运行main方法，能够输出如下。

```bash
序列化前：Video(id=旧ID, title=旧标题, description=旧描述)
序列化后：��sr#com.gitee.floyd.serialization.Video����.@LdescriptiontLjava/lang/String;Lidq~Ltitleq~xpt	旧描述t旧IDt	旧标题
执行readResolve
反序列化后：Video(id=ID, title=标题, description=描述)
```

从输出我们看出几点

- 序列化后的字节流其实有一定规律，将其转换为字符串后还有一定可读性。其规律遵循Java序列化流语法规范，稍后讨论。
- 执行了readResolve，并且其返回值替换了我们原先的对象。

> 为了更直观地观察序列化后的内容，我们可以通过[IDEA二进制插件](https://bined.exbin.org/intellij-plugin/)查看，对上面的内容，我们能够得到如下。脱离IDEA的单独软件，也可以使用[HexEdit](https://hexed.it/)（亲测好用）
>
> ![image-20211006160453425](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211006160453425.png)

### Externalizable

首先要理解这个接口，所谓“外部”序列化，重点在理解这个“外部”，它不是代码的外部，而是Java自身序列化逻辑的外部，相当于一方和二方的差别。具体来说，对Serializable的支持，Java提供完整的序列化规范，用户可以完全撒手不管；而Externalizable，Java除了将类ID写入，整个序列化和反序列化逻辑是完全由用户控制。

选用时，如果自定义序列化程度非常高，可以使用Externalizable，如果依旧需要Java的序列化逻辑，使用Serializable，具体方式可参考[这篇文章](https://www.baeldung.com/java-externalizable)。

同样，对于支持外部序列化的类，必须满足如下条件

- 实现Externalizable接口
- 实现接口的writeExternal和readExternal方法

也可以实现下面两个方法，其作用和前文所述完全一样

- writeReplace：指定一个替换对象写进流
- readResolve：指定一个从流读出来的对象的替换对象

### serialVersionUID

提出问题：

- serialVersionID有什么用？如果没有行不行？

- 不同的类具有相同的serialVersionID，会有什么影响？
- 同一个类的serialVersionID不同时，会有什么影响？
- 同一个类演变多次，实际不兼容，却还有一个serialVersionID时，会有什么影响？

serialVersionUID用于做序列化的版本控制：在反序列化时，反序列化器会检测输入流中的serialVersionUID和目标类的serialVersionUID是否一致，如果一致则继续反序列化流程，否则抛出异常。但这个行为，是果不是因。具体怎么说，参考下文的“版本控制”。这里我们先看它的生成方式。

上面的例子，我们并没有提供serialVersionUID常量。事实上，如果不提供，Java会按照默认算法提供一个。计算方式如下

1. 使用DataOutputStream构建一个字节流，其输入组成由
   - 类名
   - 类修饰符标记
   - 类的接口的名字排序后组成的字符串
   - 类中所有的字段，除static和transient的：字段名、修饰符标记、描述符
   - 类的初始化器：方法名(\<cinit>)、修饰符标记(java.lang.reflect.Modifier.STATIC)、描述符(()v)
   - 类的所有非私有构造方法：方法名(\<init>)、修饰符标记、描述符
   - 类的所有非私有方法：方法名、修饰符标记、描述符
2. 对上述字节流进行SHA-1摘要计算，生成5个32bit值
3. 取摘要计算的最高两个32位构成serialVersionUID

虽然这个生成逻辑看起来比较周到，但它有可能随着编译器的变化而变化，对同一个类，不同的编译器可能生成不同的serialVersionUID，因此，最好的方式还是我们自己指定serialVersionUID。

> One Tip：IDEA中创建类时，没有生成serialVersionUID的固定快捷键可用，可安装GenerateSerialVersionUID插件，在generate菜单中增加一个自动生成serialVersionUID的功能。看了一下[它生成serialVersionUID的逻辑](https://github.com/jbellassai/idea-GenerateSerialVersionUID/blob/master/src/org/intellij/plugins/serial/siyeh_ig/fixes/SerialVersionUIDBuilder.java)，也是根据类的完整特征生成的，包括了类名、描述符、方法签名等。

### 注意事项

1. 对一个类序列化，会递归序列化器所有属性，这就要求与其关联的所有属性的类都可被序列化
2. 枚举的序列化与常规对象不同，只会序列化其name，读取时读取name，然后调用该枚举类型的valueof方法获取原枚举
3. 不建议对内部类进行序列化，因为
   - 内部类引用外部类，会连同外部类一起序列化
   - 不同的java编译器实现针对内部类的实现有所差别，这些差别可能导致序列化后不兼容，还可能导致serialVersionUID冲突
   - 内部类是没有无参构造函数的（它有一个默认参数，就是外部类的引用），不能实现Externalizable

## Java序列化原理

了解Java序列化，回答两个问题即可：一是怎么用？二是序列化的结果是个啥？第一个问题上面已经回答了，这里回答第二个问题。

Java序列化结果是具有一定格式的二进制流，即协议。ObjectOutputStream和ObjectInputStream就是该协议的实现。

### 序列化流协议

一手资料在[这里](https://docs.oracle.com/javase/7/docs/platform/serialization/spec/protocol.html)，仔细看的话，还挺复杂的，这里简单总结留个印象就好。

序列化后的流组成：

- 魔数
- 序列化协议版本号
- 内容正文
  - 序列化的对象，包含很多种类，包括实例对象、类对象、数组、空引用、对已经在流中的序列化对应的应用
    - 起始标记，可查看ObjectStreamConstants
    - 类名
    - serialVersionUID
    - 类描述
    - 所有字段
    - 注解
    - 父类描述等
    - 结束标记
  - 块数据
    - 起始标记
    - 真实数据
    - 结束标记

当然实际组成要复杂得多，具体查看原文档的6.4节

**为原始文档做的说明**

- New Class指的是用户自定义的类，New Object同理
- block data，原生类型值会以块模式写入，这叫做block data，是ObjectStreamConstants.PROTOCOL_VERSION_2之后引入的。
- 所有需要用到的常量，都定义在ObjectStreamConstants中

### 序列化结果解读

我们将上面例子的serialVersionID转成0XFFFFFFFFFFFFFFFFL，以便区分，然后来大致解读序列化结果（为什么不详细解读？尝试过，花费太多时间，都绕晕了，最后放弃，一个字——没必要）。

![image-20211006175542457](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211006175542457.png)

来个表格

| 二进制值                                                     | 含义                                           |
| ------------------------------------------------------------ | ---------------------------------------------- |
| AC ED                                                        | 魔数，ObjectStreamConstants.STREAM_MAGIC       |
| 00 05                                                        | 版本号，ObjectStreamConstants.STREAM_VERSION   |
| 73                                                           | 新对象                                         |
| 72                                                           | 新的类型描述符                                 |
| 00                                                           | classDescFlags                                 |
| 23 63 6F 6D 2E 67 69 74 65 65 2E 66 6C 6F 79 64 2E 73 65 72 69 61 6C 69 7A 61 74 69 6F 6E 2E 56 69 64 65 6F | 类名：#com.gitee.floyd.serialization.Video     |
| FF FF FF FF FF FF FF FF                                      | serialVersionID                                |
| 02 00 03 4C                                                  | newHandle                                      |
| 00                                                           | classDescFlags                                 |
| 0B                                                           | count                                          |
| 64 65 73 63 72 69 70 74 69 6F 6E                             | description                                    |
| 4C 6A 61 76 61 2F 6C 61 6E 67 2F 53 74 72 69 6E 67           | Ljava/lang/String                              |
| 。。。。。。                                                 | 后面反正就是一堆，有兴趣自己对着规范一个一个找 |

## 其它

### 版本控制

序列化流的版本控制是什么：控制的是新旧版本的类序列化的结果，让对方进行反序列化时，应该做出什么样的反应。

这里的主要问题是：类的演进，如何算兼容，如何算不兼容呢？

**兼容的标准**

- 旧版本的类序列化后，能够被新版本的类正常反序列化，并且反序列化的结果在数据完整性上不会造成破坏
- 反之亦然

**不兼容的演进**

- 删除字段：旧版本的类在反序列化时会因为缺少对应字段的值，被设置为默认值，默认值可能对业务产生负面影响
- 非静态字段改为静态字段、给已有字段添加transient关键字：等效于删除
- 在层次结构中上下移动类：流中的数据会以错误的形式出现
- 修改字段类型：反序列化时将无法正确进行类型转换
- 更改writeObject和readObject，使其发生了重大变化：将导致反序列化失败
- 将Serializable改为Externalizable或者删除Serializable：将直接导致不可序列化
- 从非枚举改为枚举：枚举的序列化方式是不一样的

**兼容的演进**

- 增加字段：对原始类不会产生影响，在新的类中应该设定对新增字段默认值的处理
- 增加类：增加的类也能够被检测出来，新增的类将被初始化为零值
- 删除类：删除类是能够检测出来的
- 添加writeObject/readObject：新添加逻辑
- 其它。。。

可以看到，这里说的兼容演进是非常主观的，是说可以在新类中做添加兼容逻辑，如果逻辑添加错误，还是可能发生不兼容的情况。上面的不兼容演进，是没有机会添加兼容逻辑了，所以才叫”不兼容“。

**serialVersionID扮演的作用**

如果我们认为新类和原始类是能够兼容的，那么他们就应该具有相同的serialVersionID；反之，如果认为不兼容，他们就应该具有不同的serialVersionID。

声明和维护serialVersionID是必要的

- serialVersionID是Java提供的强制不兼容机制，必须要有，如果我们不声明，它也会自动生成，而自动生成的可能不稳定，有隐患。
- 如果实际演进不兼容，却具有相同的serialVersionID，而当不兼容的修改项运行时并不会报错，却影响到业务逻辑（如删除字段）时，是非常危险的，及时修改serialVersionID，相当于将兼容性问题显式暴露出来。

**现在来回答那四个问题**

- serialVersionID有什么用？如果没有行不行？

  上面回答过了，忽略

- 不同的类具有相同的serialVersionID，会有什么影响？

  不会有什么一项，serialVersionID只在类内部起作用，类之间互不干扰。

- 同一个类的serialVersionID不同时，会有什么影响？

  反序列化时会报错

- 同一个类演变多次，实际不兼容，却还有一个serialVersionID时，会有什么影响？

  可能反序列化时候会报错，也可能不报错，从而产生bug

### 安全考量

有时会涉及到敏感信息的序列化和反序列化，可以通过以下方式进行数据保护：

- 可以通过transient忽略敏感字段

- 如果一个类敏感，它就不应该能够被序列化。IDEA还提供了这方面的警告，当在一个安全上下文中使用序列化时报警

  ![image-20211006184408647](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211006184408647.png)

- 如果实在要序列化，则应该在writeObject()时控制它，在readObject()时候验证它

> PS：敏感数据，压根儿就不应该被序列化

## 总结

Java自带的序列化，现在其实很少使用，学习它，一方面是作为Java程序员的职责，一方面也是消散心中的执念。

总体来看，我们要关注几个方面

- Java序列化的使用方式，不只是Serializable那么简单
- serialVersionID的正确理解
- 序列化流协议，可以了解一下，我们要知道一个对象被序列化后长什么样子

同时也可以看出它的缺点

- 不能跨平台，自己定义的二进制协议，其它语言不能使用，除非人家实现这个协议，不过别人也没必要去实现这个协议吧
- 实现中大量使用反射，效率可能会比较低

## 参考

- [Java序列化规范](https://docs.oracle.com/javase/7/docs/platform/serialization/spec/serialTOC.html)
- ObjectOutputStream、ObjectInputStream源码

- 一些网络文档