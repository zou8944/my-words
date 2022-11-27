---
created_at: 2021-10-18 18:18:56.446
updated_at: 2021-10-18 18:18:56.446
slug: serialization-protobuf
tags: 
- 序列化
- Protobuf
---

# 序列化探索之Protobuf

Protobuf是谷歌提出的一种高压缩比的序列化格式，二进制，不可读，语言无关，平台无关。拥有自己的语法规则，压缩编码算法，并提供主流语言的API生成器（即Protobuf编译器），其序列化结果很小，能够有效节省带宽。

掌握Protobuf，需要比较了解三个方面，其中，如果只是单纯滴使用，前两个方面即可。

- proto语法规则，即proto文件的语法规则
- 具体语言的API生成及使用规则，即通过proto文件生成对应语言的代码
- 序列化和反序列化算法

<!-- more -->

## 语法

截止目前，proto有两个版本，proto2和proto3，我们关注proto3。这里展示一个完整的场景，考虑一个获取资源的rpc协议

```protobuf
syntax = "proto3";

import "resource.proto";

package com.gitee.floyd.serialization.protobuf;

// 一个类一个文件
option java_multiple_files = true;

service ResourceService {
  rpc getResource (GetResourceRequest) returns (GetResourceResponse);
}

message GetResourceRequest {
  int32 resourceId = 1;
}

message GetResourceResponse {
  Resource resource = 1;
}
```

资源定义在这里

```protobuf
syntax = "proto3";

import "google/protobuf/any.proto";

package com.gitee.floyd.serialization.protobuf;

// 定义资源类型
message Resource {

  // 编号1已经被以前使用了
  reserved 1;

  // 类型枚举
  enum Type {
    RECORD = 0;
    TAG = 1;
  }

  // 记录的具体内容
  message RecordData {
    string content = 1;
    repeated string images = 2;
  }

  // 标签的具体内容
  message TagData {
    string title = 1;
  }

  // 资源ID
  int32 id = 2;
  // 资源类型
  Type type = 3;
  // 记录和标签同时只会出现一个
  oneof data {
    RecordData record = 4;
    TagData tag = 5;
  }
  // 还可以塞一些其它的东西
  google.protobuf.Any other = 6;
  // 以map的形式塞一些其它的东西
  map<string, google.protobuf.Any> otherMap = 7;

}
```

就上面用到的进行说明，也就七七八八了，其它的可以参考官方文档自己去补。

### proto结构

- 语法版本声明，如果不声明，默认为proto2
- 导入的proto依赖
- 包声明
- 可选参数设置
- service声明
- 消息声明

其中，除了消息声明，其它都不是必须的，主要的语法内容，也集中在消息声明

### 数据类型

完整的类型声明参考[官方文档](https://developers.google.com/protocol-buffers/docs/proto3#scalar)，总结如下

- int32：占用字节数是变化的；能表示负数，但效率不是很高
- uint32：占用字节数是变化的；无符号
- sint32：占用字节数是变化的；能表示负数，效率较高
- fixed32：定长，当数字真的非常大时，它比uint32更有效率
- sfixed32：同上，只不过是有符号的
- string：UTF8编码，最长2^32个字节
- bytes：最长2^32个字节

### 枚举

枚举定义参考上面的Resource.Type，要点

- 必须有一个的编号是0，以便设置默认值；且必须是第一个元素，以便于proto2兼容
- 由于其实际上是使用变长编码，因此编号尽量不好是负数

### 修饰

**repeated**

字段只有单数和复数，复数用repeated修饰符，对应的Java中的集合。

**oneof**

- 可使用oneof设置字段多选一，但是使用之前需要使用hasxxx()方法查看是否有值。

- oneof里面不能使用repeated

- 序列化时，如果为多个字段都设置值，只有最后一个设定的值会被保留，其它会被清除，反序列化同理

- 针对oneof的版本升级问题一般不建议做，会有丢失数据的问题

  比如新版本将其中一个元素移出去了，那么新的协议得到的序列化结果用旧的协议来解析，则移出去那个元素有值，oneof本身内部有一个有效值，由于旧版本都在oneof内部，因此会丢失一个对新版本来说有效的值。

**map**

- key可以是除了浮点数、bytes和枚举之外的任意值
- value可以是除了map之外的任意值
- map不能是repeated
- map内顺序不被保证

**Any**

- 能够包含任意被序列化为bytes的类型
- 有专门的方法去包装和拆解它：pack()和unpack()

### 注意事项

- 一旦一个编号被使用，在之后的升级中，它将不能再被使用，否则会导致反序列化出错
- 字段编号并非无穷，在1到2^29次方之间；但19000到19999之间的是Protocol Buffers预留的，不能使用
- 如果不给字段赋值，将会设置为默认值，各种类型默认值如下
  - 字符串：空串
  - 字节数组：空数组
  - bool：false
  - 数字：0
  - 枚举：编号是0的那个值
  - 消息字段：取决于具体语言，Kotlin和Java中
- proto的导入不可跨层传递，除非用`import public`，但这在Java中是不支持的
- protobuf可以和Json之间直接映射，有兴趣可以去研究一下

## 序列化算法

Protobuf序列化的目标单位是一条消息（message），其算法，就是一个压缩算法，总体要点有几个

- 以序号替代字段名
- 对一般的数字类型和布尔采用变长表示法，这样一个int32类型的字段最低只要一个字节即可表示完成
- 将所有字段类型分为几类，分别有不同的表示方法
- 对string或自定义的结构化类型，只是多了一个长度标识

### 一个例子

下面以一个序列化说明

```protobuf
message Resource {

	message Data {
		string content = 1;
	}

	int32 id = 1;
	string type = 2;
	Data data = 3;
	
}
```

我们按照如下设置值

```bash
id = 2
type = "R" # UTF8编码为：
data.content = "我" # UTF8编码为
```

其对应的代码为

```kotlin
fun main() {
    val resourceBuilder = Resource.newBuilder()
    val data = resourceBuilder.dataBuilder.setContent("我").build()
    val resource = Resource.newBuilder()
        .setId(2)
        .setType("R")
        .setData(data)
        .build()
    val buffer = ByteArrayOutputStream()
    resource.writeTo(buffer)
    println(buffer.toByteArray().toHexString())
}
```

它的序列化结果将是

```bash
08021201521a050a03e68891
```

### 前置知识

二进制流组成：字段编号<<3 + 编码类型 + 字段值

字段值为复杂类型时，将会递归使用上述编码方式

编码类型如下

| Type | Meaning          | Used For                                                 |
| :--- | :--------------- | :------------------------------------------------------- |
| 0    | Varint           | int32, int64, uint32, uint64, sint32, sint64, bool, enum |
| 1    | 64-bit           | fixed64, sfixed64, double                                |
| 2    | Length-delimited | string, bytes, embedded messages, packed repeated fields |
| 3    | Start group      | groups (deprecated)                                      |
| 4    | End group        | groups (deprecated)                                      |
| 5    | 32-bit           | fixed32, sfixed32, float                                 |

### 例子分析

现在我们再来看上面的输出：

08 -> 00001 000 ：字段编号为1，类型为0

02 -> 0000 0010 ：字段值为2

12 -> 00010 010 ：字段编号为2，类型为2，即复杂字段，这个类型的下一个字节标识了长度

01 -> 0000 0001 ：字段编号为2的字段值长度为1

52 -> 0101 0010 ：字段编号为2的字段值的UTF8编码，即”R“

1a -> 00011 010 ：字段编号为3，类型为2

05 -> 0000 0101 ：字段编号为3的字段值长度为5，对应我们的嵌套类型Data

​	0a -> 00001 010 ：字段编号为1，类型为2

​	03 -> 0000 0011 ：字段编号为1的字段值长度为3

​	e68891 -> 字段编号为1的字段值的UTF8编码，即”我“

结束

### 如何做到版本兼容

由于它是根据字段编号标识字段，反序列化时，遇到不认识的字段编号会直接忽略。因此版本兼容的方式就是，字段编号只增不减，不可与之前的编号复用。复用在protobuf里是绝对不允许的。

## API生成规则

使用protobuf编译器，能够生成对应语言的代码，我们主要看Java和Kotlin，由于Kotlin是在Java生成的基础上生成的，因此一起讲了。

其主要能力，是对proto中定义的消息进行构建，然后提供转换为流的方式；如果加上特定RPC插件，还可以生成Service的代码。

### Java文件生成

- 文件拆分：如果设置了`option java_multiple_files = true;`，则会按照顶层的Service和Message分别生成多个Java源文件
- 包名：如果设置了`option java_package = "xx.xx.xx.xxx";`，则以它为准；否则以proto文件定义的package为准
- 字段名：proto中为小写+下划线，Java文件中转换为小驼峰命名

### 关键字段类型

- repeated：转换为ProtocolStringList类型，其直接继承了java.util.List
- 枚举：转换为普通枚举类型，但是会多一个UNRECOGNIZE，表示未知参数
- oneof：多选一的字段，每个字段都会生成一个`hasXXX()`方法，用以判断是否有值；也有提供`hasOneof()`，判断这几个字段是否有存在一个
- map：转换为`java.util.Map`类型
- Any：转换为`com.google.protobuf.Any`，它提供pack和unpack，用于将其它任意消息类型进行封装和解封

### 消息类型的构建

- 消息是不可变的，一旦构建不可更改
- 消息构建采用建造器模式，典型地如`Resource.newBuilder().setType(Resource.Type.RECORD).build()`
- 嵌套消息，其建造器也是嵌套的，嵌套在父建造器上：`Resource.newBuilder().recordBuilder.addImages("").build()`

### Service

尽管我们在proto文件中定义了Service，但是脱离具体的RPC实现（比如gRPC），这个Service就没有意义。且一般的RPC实现会作为插件的形式载入（所以你看很多gradle中配置grpc是以插件的形式声明在protobuf块中的），生成两个部分

- 服务抽象类：定义服务端，用户通过它实现自己的服务端逻辑
- 客户端Stub：定义客户端，用户通过它连接远端服务

proto文件中存在`option java_generic_services = true;`时，会生成一个通用的Service实现。有兴趣可以看一下。

### 其它

- 每个消息，还提供了Descriptor，用以描述其proto信息，类似反射，可以获取元信息，如果我们写自己的RPC插件，可以使用
- 每个消息，都提供`getDefaultInstance()`，返回一个空对象

### 来个例子（Java）

这里仅展示将上面定义的Resource消息设置值，并将序列化结果以流的形式输出。

```kotlin
fun main() {
    val resourceBuilder = Resource.newBuilder()
    val record = resourceBuilder.recordBuilder
        .addImages("https://hello.png")
        .addAllImages(listOf("https://key.png", "https://key2.png"))
        .setContent("这是记录")

    val resource1 = resourceBuilder
        .setId(1)
        .setType(Resource.Type.RECORD)
        .setRecord(record)
        .build()

    val resource2 = resourceBuilder
        .setId(2)
        .setType(Resource.Type.RECORD)
        .setOther(Any.pack(resource1))
        .putOtherMap("key", Any.pack(resource1))
        .build()

    ByteArrayOutputStream().run {
        resource2.writeTo(this)
        println(this.toByteArray().toHexString())
    }
}
```

### 来个例子（Kotlin）

Kotlin生成在Java之上，为我们提供了DSL，上面的代码，用DSL再写一遍，看起来明显好很多。

```kotlin
fun main() {
    val resource1 = resource {
        this.id = 1
        this.type = Resource.Type.RECORD
        this.record = ResourceKt.recordData {
            this.images.add("https://hello.png")
            this.images.addAll(listOf("https://key.png", "https://key2.png"))
            this.content = "这是记录"
        }
    }

    val resource2 = resource {
        this.id = 2
        this.type = Resource.Type.RECORD
        this.other = Any.pack(resource1)
        this.otherMap.put("key", Any.pack(resource1))
    }

    ByteArrayOutputStream().run {
        resource2.writeTo(this)
        println(this.toByteArray().toHexString())
    }
}
```

## 环境问题

API生成，可以有两种方式

- protoc命令行生成API，gradle只引入相关依赖。好处是简单；缺点是一次性，每次修改协议都要生成一次。
- 直接使用gradle插件，将protoc生成命令嵌入gradle生命周期。好处是一旦配置完成就一劳永逸；坏处是配置麻烦。

protobuf简单是简单，但配置起来还是有几个问题的。问题主要在于kotlin代码的生成，gradle插件的配置

### 关于protoc的安装

需要在[项目发布](https://github.com/protocolbuffers/protobuf/releases/tag/v3.18.1)页下载压缩包进行安装，macos直接选择对应的编译好的二进制包，有先尝试过直接`brew install protobuf`，结果它不包含protoc-kotlin-gen插件。

![image-20211018112756901](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211018112756901.png)

### 包的引入

协议相关包，在[这里](https://search.maven.org/search?q=g:com.google.protobuf)才是最完整的，无论java也好，kotlin也好。

![image-20211018112836558](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211018112836558.png)

### Kotlin的生成

kotlin API需要依赖java代码，因此要同时生成java

```bash
$ protoc --java_out=xxxxxx --kotlin_out=xxxxxx resource_service.proto
```

生成的Java代码

![截屏2021-10-18 上午11.40.08](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-10-18%20%E4%B8%8A%E5%8D%8811.40.08.png)

生成的Kotlin代码

![截屏2021-10-18 上午11.40.49](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-10-18%20%E4%B8%8A%E5%8D%8811.40.49.png)

### Gradle插件

插件的项目地址：[我是插件的项目地址](https://github.com/google/protobuf-gradle-plugin)

配置要点

- 添加protobuf插件的依赖
- 通过sourceSets指定proto文件位置
- protobuf.generatedFilesBaseDir指定代码生成位置
- protobuf.protoc指定protoc的版本
- protobuf.generateProtoTasks定制

```kotlin
buildscript {
    repositories {
        mavenCentral()
    }
    dependencies {
        classpath("com.google.protobuf:protobuf-gradle-plugin:0.8.17")
    }
}

plugins {
    id("java")
    id("com.google.protobuf") version "0.8.17"
}

sourceSets {
    main {
        proto {
            srcDir("src/main/resources/proto")
        }
    }
}

protobuf {
    generatedFilesBaseDir = "$projectDir/src/generated"

    protoc {
        artifact = "com.google.protobuf:protoc:3.18.1"
    }

    generateProtoTasks {
        all().forEach { task ->
            task.builtins {
                java { }
            }
        }
    }
}
```

> kotlin代码的插件配置方式，暂时还没找到

## 总结

Protobuf优点众多：语法简单；编码算法使得结果非常小巧；编码算法也不难理解；对主流语言提供了API生成支持。但代码生成这种方式增加了构建时间，实际体验并不是很好。

有关更多内容，请需要参考官方文档

[语法说明](https://developers.google.com/protocol-buffers/docs/proto3)

[编码方式](https://developers.google.com/protocol-buffers/docs/encoding)

[Java API生成说明](https://developers.google.com/protocol-buffers/docs/reference/java-generated)

[Kotlin API生成说明](https://developers.google.com/protocol-buffers/docs/reference/kotlin-generated#nested-types)

[gradle插件](https://github.com/google/protobuf-gradle-plugin)


