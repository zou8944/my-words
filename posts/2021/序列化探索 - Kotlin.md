---
created_at: 2021-10-09 17:59:43.418
updated_at: 2021-10-09 18:00:49.384
slug: serialization-kotlin
tags:
- 序列化
- Kotlin
---

> 文章不长，但代码演示居多，可选择性阅读

Kotlin以扩展包的形式提供了序列化能力，使得能够以“Kotlin方式”进行序列化。Kotlin设计目标，是提供一个序列化抽象，具体格式实现可用Json、CBOR、Protobuf、Properties、Yaml等进行替换。但就目前的进度，仅提供了对Json的稳定支持。其它格式都处于试验阶段。

因此，我们看Kotlin的序列化，主要看的就是数据对象与Json之间的序列化和反序列化。

<!-- more -->

## 能力展示

场景假设：需要序列化一个数据类，包含五个字段

- resourceId：资源ID
- resourceType：资源类型
- updatedTime：更新时间
- usn：更新序列号
- data：资源数据

为方便演示，这些字段的类型和组织结构依据场景的不同而不同，下面演示针对这个数据类的对象的序列化。

### 基础能力

开局一段基础代码，下面的使用方式应该是我们能够使用得最多的场景和方式。

```kotlin
@Serializable
class ResourceBasic<T> {

    @SerialName("id")
    var resourceId: String? = null

    @SerialName("type")
    var resourceType: String? = null

    var updatedTime: Long? = null

    var usn: Long? = null

    var data: T? = null

    override fun toString(): String {
        return "ResourceBasic(resourceId=$resourceId, resourceType=$resourceType, updatedTime=$updatedTime, usn=$usn, data=$data)"
    }

}

fun main() {
    val resource = ResourceBasic<JsonElement>().apply {
        this.resourceId = UUID.randomUUID().toString()
        this.resourceType = "record"
        this.updatedTime = LocalDateTime.now().toInstant(ZoneOffset.UTC).toEpochMilli()
        this.usn = null
        this.data = buildJsonObject {
            put("images", buildJsonArray { add("https://www.ppp.com/cdwrgwarhg.png") })
        }
    }

    val jsonFormat = Json {
        prettyPrint = true
        encodeDefaults = true
    }
    // 序列化
    val jsonString = jsonFormat.encodeToString(resource)
    println(jsonString)
    // 反序列化
    val decodedResource = jsonFormat.decodeFromString<ResourceBasic<JsonElement>>(jsonString)
    println(decodedResource)
}
```

输出

```
{
    "id": "74020041-79c4-456c-bd42-c372a4049d61",
    "type": "record",
    "updatedTime": 1633780307486,
    "usn": null,
    "data": {
        "images": [
            "https://www.ppp.com/cdwrgwarhg.png"
        ]
    }
}
ResourceBasic(resourceId=74020041-79c4-456c-bd42-c372a4049d61, resourceType=record, updatedTime=1633780307486, usn=null, data={"images":["https://www.ppp.com/cdwrgwarhg.png"]})
```

上面展示了Kotlin序列化的最基础能力

1. 被序列化的类上必须添加@Serializable注解
2. 被序列化的类可以带泛型
3. 可以通过@SerialName注解修改序列化的键名
4. 序列化时调用Json.encodeToString即可
5. 反序列化时调用Json.decodeFromString即可

更多参考[官方手册](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/basic-serialization.md)

### 自定义序列化逻辑

上例中更新时间为Long，但实际代码编写中使用LocalDateTime更为方便，此时我们需要为LocalDateTime写一个自定义序列化器。

```kotlin
@Serializable
class ResourceInCustomSerializer {

    var resourceId: String? = null

    var resourceType: String? = null

    @Serializable(with = LocalDateTimeAsLongSerializer::class)
    var updatedTime: LocalDateTime? = null

    var usn: Long? = null

    var data: JsonElement? = null

    override fun toString(): String {
        return "ResourceBasic(resourceId=$resourceId, resourceType=$resourceType, updatedTime=$updatedTime, usn=$usn, data=$data)"
    }

}

object LocalDateTimeAsLongSerializer : KSerializer<LocalDateTime> {

    override val descriptor: SerialDescriptor = buildClassSerialDescriptor("java.util.LocalDateTime")

    override fun serialize(encoder: Encoder, value: LocalDateTime) {
        encoder.encodeLong(value.toInstant(ZoneOffset.UTC).toEpochMilli())
    }

    override fun deserialize(decoder: Decoder): LocalDateTime {
        return LocalDateTime.ofInstant(Instant.ofEpochMilli(decoder.decodeLong()), ZoneOffset.UTC)
    }
}

fun main() {
    val resource = ResourceInCustomSerializer().apply {
        this.resourceId = UUID.randomUUID().toString()
        this.resourceType = "record"
        this.updatedTime = LocalDateTime.now()
        this.usn = null
        this.data = buildJsonObject {
            put("images", buildJsonArray { add("https://www.ppp.com/cdwrgwarhg.png") })
        }
    }
    val jsonFormat = Json {
        prettyPrint = true
        encodeDefaults = true
    }
  	// 序列化
    val jsonString = jsonFormat.encodeToString(resource)
    println(jsonString)
  	// 反序列化
    val decodedResource = jsonFormat.decodeFromString<ResourceInCustomSerializer>(jsonString)
    println(decodedResource)
}
```

要点

- 自定义LocalDateTimeAsLongSerializer，实现KSerializer接口，重写一个属性，两个方法
  - descriptor：类型描述
  - serialize：序列化逻辑
  - deserialize：反序列化逻辑
- @Serializable(with = LocalDateTimeAsLongSerializer::class)标注在目标属性上

### 上下文

上面的例子再变一下，updateTime有时可能想要转换为Long，有时却想要转换为ISO8601格式的字符串。即，要求根据不同**上下文**的变化选择不同的序列化器。

```kotlin
@Serializable
class ResourceInCustomSerializer {

    var resourceId: String? = null

    var resourceType: String? = null

    @Contextual
    var updatedTime: LocalDateTime? = null

    var usn: Long? = null

    var data: JsonElement? = null

    override fun toString(): String {
        return "ResourceBasic(resourceId=$resourceId, resourceType=$resourceType, updatedTime=$updatedTime, usn=$usn, data=$data)"
    }

}

object LocalDateTimeAsLongSerializer : KSerializer<LocalDateTime> {

    override val descriptor: SerialDescriptor = buildClassSerialDescriptor("java.util.LocalDateTime")

    override fun serialize(encoder: Encoder, value: LocalDateTime) {
        encoder.encodeLong(value.toInstant(ZoneOffset.UTC).toEpochMilli())
    }

    override fun deserialize(decoder: Decoder): LocalDateTime {
        return LocalDateTime.ofInstant(Instant.ofEpochMilli(decoder.decodeLong()), ZoneOffset.UTC)
    }
}

object LocalDateTimeAsStringSerializer : KSerializer<LocalDateTime> {

    override val descriptor: SerialDescriptor = buildClassSerialDescriptor("java.util.LocalDateTime")

    override fun serialize(encoder: Encoder, value: LocalDateTime) {
        encoder.encodeString(value.toString())
    }

    override fun deserialize(decoder: Decoder): LocalDateTime {
        return LocalDateTime.parse(decoder.decodeString())
    }

}

fun main() {

    val resource = ResourceInCustomSerializer().apply {
        this.resourceId = UUID.randomUUID().toString()
        this.resourceType = "record"
        this.updatedTime = LocalDateTime.now()
        this.usn = null
        this.data = buildJsonObject {
            put("images", buildJsonArray { add("https://www.ppp.com/cdwrgwarhg.png") })
        }
    }

    var jsonFormat = Json {
        prettyPrint = true
        encodeDefaults = true
        serializersModule = serializersModuleOf(LocalDateTime::class, LocalDateTimeAsLongSerializer)
    }
    // LocalDateTime转换为Long的序列化和反序列化
    var jsonString = jsonFormat.encodeToString(resource)
    println(jsonString)
    var decodedResource = jsonFormat.decodeFromString<ResourceInCustomSerializer>(jsonString)
    println(decodedResource)

    jsonFormat = Json {
        prettyPrint = true
        encodeDefaults = true
        serializersModule = serializersModuleOf(LocalDateTime::class, LocalDateTimeAsStringSerializer)
    }
    // LocalDateTime转换为String的序列化和反序列化
    jsonString = jsonFormat.encodeToString(resource)
    println(jsonString)
    decodedResource = jsonFormat.decodeFromString<ResourceInCustomSerializer>(jsonString)
    println(decodedResource)

}
```

要点

- 目标字段使用@Contextual注解，表明该字段的序列化器到上下文中去找
- 定义多个针对LocalDateTime的序列化器
- 在Json实例中，指定当前所用序列化模块，为LocalDateTime注册对应的序列化器，上面，我们用了两个Json实例，分别对应不同的上下文，注册不同的序列化器，对同一个对象的序列化结果有了不同的行为

### 序列化的多态

如果我们的Resource有两个版本，它们拥有共同的三个属性：resourceId、resourceType、data，其中一个版本拥有updatedTime，另一个版本拥有usn，于是有了类型的层次结构。现在假设我有一个列表，该列表同时有两个版本的数据，为了在反序列化时能够恢复出具体元素的类型，在序列化时就需要将元素的类型信息也进行序列化，这就是序列化的多态。如果你觉得对这个概念模式，谷歌一下“jackson @class”，一定是似曾相识。

```kotlin
@Serializable
abstract class ResourceBase {
    var resourceId: String? = null
    var resourceType: String? = null
    var data: String? = null
}

@Serializable
class ResourceWithUsn : ResourceBase() {
    var usn: Long? = null
}

@Serializable
class ResourceWithUpdatedTime : ResourceBase() {
    var updatedTime: Long? = null
}

fun main() {
    val resources = listOf(
        ResourceWithUsn().apply {
            this.resourceId = "1"
            this.resourceType = "record"
            this.data = "这是数据"
            this.usn = 123
        },
        ResourceWithUpdatedTime().apply {
            this.resourceId = "2"
            this.resourceType = "tag"
            this.data = "这是标签"
            this.updatedTime = Instant.now().toEpochMilli()
        }
    )

    val jsonFormat = Json {
        prettyPrint = true
        classDiscriminator = "@class"
        serializersModule = SerializersModule {
            polymorphic(ResourceBase::class) {
                subclass(ResourceWithUpdatedTime::class)
                subclass(ResourceWithUsn::class)
            }
        }
    }

    val jsonString = jsonFormat.encodeToString(resources)
    println(jsonString)
}
```

序列化结果

```bash
[
    {
        "@class": "com.gitee.floyd.serialization.kotlin.ResourceWithUsn",
        "resourceId": "1",
        "resourceType": "record",
        "data": "这是数据",
        "usn": 123
    },
    {
        "@class": "com.gitee.floyd.serialization.kotlin.ResourceWithUpdatedTime",
        "resourceId": "2",
        "resourceType": "tag",
        "data": "这是标签",
        "updatedTime": 1633753842785
    }
]
```

要点

- 父类和子类都要标注@Serializable
- Json实例中，注册多态声明，这里，我们声明ResourceBase的子类包含ResourceWithUpdatedTime、ResourceWithUsn
- 可以通过classDiscriminator自定义类型标记的key，这里写成@class，是为了让读者回想起jackson

Kotlin实际的多态稍有不同，由于Kotlin序列化的大部分工作都是在编译期完成的，因此将一个待序列化的对象声明为其父类型，也能够触发多态。还有接口、密封类在多态中也有不同的特性，具体参见[官方手册](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/polymorphism.md)

> **Java会有多态问题吗？**
>
> 不会，Java序列化结果是二进制流，其中已经包含类型信息，不存在反序列化时候不知道具体类型的情况。也就是说，序列化的多态问题，只是对语言无关的序列化格式如Json有意义。

### Json能力

之前在使用Vertx时，深感其提供的Json库好用至极；Jackson也提供了Tree Mode，让用户能够在不创建类对象的情况下灵活构建Json对象；kotlin也提供了类似的能力——JsonElement，不过它没那么强大：能够凭空构建一个JsonElement，能够遍历其中的数据，却不能修改其中的数据。

当然，Json能力并非本文的重点，我们的重点在于探究Kotlin序列化的使用方式和原理，因此有关Json能力，参考[官方手册](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/json.md#json-elements)。

## 原理解析

Kotlin序列化几乎所有逻辑都在编译期生成。因此，配置Kotlin序列化时，需要同时引入序列化插件和序列化包

```kotlin
plugins {
    kotlin("plugin.serialization") version "1.5.31"
}
dependencies {
  implementation("org.jetbrains.kotlinx:kotlinx-serialization-json:1.3.0")
}
```

### 从@Serializable讲起

为目标类添加@serializable注解，编译器会自动生成序列化逻辑，以一个最简单的类进行展示

```kotlin
@Serializable
class SimpleData {
    val id: Long? = null
}
```

其字节码反编译结果整理之后如下（去除了多余的噪声）

```java
public final class SimpleData {

	private final Long id;
  
  public static final SimpleData.Companion Companion = ... ...

  public final Long getId() {
    return this.id;
  }
  
  ... ...

  @JvmStatic
  public static final void write$Self(SimpleData self, CompositeEncoder output, SerialDescriptor serialDesc) {
    if (Intrinsics.areEqual(self.id, (Object)null) ^ true || output.shouldEncodeElementDefault(serialDesc, 0)) {
      output.encodeNullableSerializableElement(serialDesc, 0, (KSerializer)LongSerializer.INSTANCE, self.id);
    }
  }

  public static final class Companion {
    
    ... ...
    
    public final KSerializer serializer() {
      return (KSerializer)SimpleData.$serializer.INSTANCE;
    }
  }

  public static final class $serializer implements GeneratedSerializer {
    
    public static final SimpleData.$serializer INSTANCE;
    
    private static final SerialDescriptor $$serialDesc;

    private $serializer() {
    }

    static {
      SimpleData.$serializer var0 = new SimpleData.$serializer();
      INSTANCE = var0;
      PluginGeneratedSerialDescriptor var1 = new PluginGeneratedSerialDescriptor("com.gitee.floyd.serialization.kotlin.SimpleData", (GeneratedSerializer)INSTANCE, 1);
      var1.addElement("id", true);
      $$serialDesc = var1;
    }

    @NotNull
    public KSerializer[] typeParametersSerializers() {
      return DefaultImpls.typeParametersSerializers(this);
    }

    @NotNull
    public SerialDescriptor getDescriptor() {
      return $$serialDesc;
    }

    public void serialize(Encoder encoder, SimpleData value) {
      SerialDescriptor var3 = $$serialDesc;
      Encoder encoder = encoder.beginStructure(var3);
      SimpleData.write$Self(value, encoder, var3);
      encoder.endStructure(var3);
    }
    
    public void serialize(Encoder var1, Object var2) {
      this.serialize(var1, (SimpleData)var2);
    }

    public SimpleData deserialize(Decoder decoder) {
      SerialDescriptor var2 = $$serialDesc;
      int var4 = 0;
      Long var5 = null;
      Decoder decoder = decoder.beginStructure(var2);
      if (decoder.decodeSequentially()) {
        var5 = (Long)decoder.decodeNullableSerializableElement(var2, 0, (KSerializer)LongSerializer.INSTANCE, var5);
        var4 = Integer.MAX_VALUE;
      } else {
        while(true) {
          int var3 = decoder.decodeElementIndex(var2);
          switch(var3) {
            case 0:
              var5 = (Long)decoder.decodeNullableSerializableElement(var2, 0, (KSerializer)LongSerializer.INSTANCE, var5);
              var4 |= 1;
              break;
            default:
              throw (Throwable)(new UnknownFieldException(var3));
          }
        }
      }

      decoder.endStructure(var2);
      return new SimpleData(var4, var5, (SerializationConstructorMarker)null);
    }

    public Object deserialize(Decoder var1) {
      return this.deserialize(var1);
    }
  }
}
```

解读一下生成的这个类

- 编译器生成了伴生类Companion，同时附带serializer()方法，返回一个KSerializer对象
- 类本身新增静态方法`write$Self(SimpleData self, CompositeEncoder output, SerialDescriptor serialDesc)`，在生成的序列化器中有被调用
- 看生成的序列化器内部——getDescriptor方法，返回一个SerialDescriptor对象
- 看生成的序列化器内部——serialize方法
  - 传入Encoder对象、数据类对象
  - 调用Encoder的方法，将数据类型写入
- 看生成的序列化器内部——deserialize方法
  - 传入Decoder
  - 从decoder中解析出字段，构建新的SimpleData对象并传入
- 看生成的序列化器，跟上面我们自己写的序列化器，像不像，其实它们就是一样的。

要点

- 添加了@Serializable的类，会自动生成属于自己类的序列化器

- 实际上随着Kotlin序列化库的引入，你会发现，所有Kotlin原生类型也都被添加了一个扩展方法，serializer()

  ![image-20211009145331561](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211009145331561.png)

  点进去看看他们的逻辑，依然是内置实现了KSerializer

  ```kotlin
  public fun String.Companion.serializer(): KSerializer<String> = StringSerializer
  
  internal object StringSerializer : KSerializer<String> {
      override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor("kotlin.String", PrimitiveKind.STRING)
      override fun serialize(encoder: Encoder, value: String): Unit = encoder.encodeString(value)
      override fun deserialize(decoder: Decoder): String = decoder.decodeString()
  }
  ```

- 我们会发现几个关键定义：KSerializer、SerialDescriptor、Encoder、Decoder、SerialKind，搞清楚它们之间的联系，就基本清楚了Kotlin的序列化原理。

### Kotlin序列化的设计思路

```
+---------+  Serialization  +------------+  Encoding  +---------------+
| Objects | --------------> | Primitives | ---------> | Output format |
+---------+                 +------------+            +---------------+
```

这张图取自[官方手册](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/basic-serialization.md#basics)，对于理解至关重要。Kotlin将序列化分为两个阶段

- 阶段一（序列化）：将目标对象序列化成基础类型，如Long、Char、String等，这一步是通用的，与最终序列化格式无关。这一步对应KSerializer
- 阶段二（编码）：基础类型编码为最终格式，如Json、Protobuf。这一步对应Encoder、Decoder

### 核心类解析

现在我们可以来看那几个关键定义

- KSerializer

  它定义了Encoder和目标对象value的关系，即控制了编码器编码和解码目标对象的逻辑。编码时，需要用到类描述信息SerialDescriptor

  ```kotlin
  public interface KSerializer<T> : SerializationStrategy<T>, DeserializationStrategy<T> {
      override val descriptor: SerialDescriptor
  }
  public interface SerializationStrategy<in T> {
    
      public val descriptor: SerialDescriptor
  
      public fun serialize(encoder: Encoder, value: T)
  }
  public interface DeserializationStrategy<T> {
    
      public val descriptor: SerialDescriptor
  
      public fun deserialize(decoder: Decoder): T
  }
  ```

- SerialDescriptor

  从名称就可得知，它定义了目标类型的描述信息，它的常规实现是SerialDescriptorImpl

  - serialName：序列化名称，一般是类名
  - kind：目标类型，下文会讲
  - elements：当为类类型时，会包含多个属性，它们是以元素集合的形式提供的，具体可以看SerialDescriptorImpl实现

  ```kotlin
  public interface SerialDescriptor {
  
      public val serialName: String
      
      public val kind: SerialKind
      
      public val isNullable: Boolean get() = false
      
      public val isInline: Boolean get() = false
      
      public val elementsCount: Int
      
      public val annotations: List<Annotation> get() = emptyList()
      
      public fun getElementName(index: Int): String
      
      public fun getElementIndex(name: String): Int
      
      public fun getElementAnnotations(index: Int): List<Annotation>
      
      public fun isElementOptional(index: Int): Boolean
  }
  ```

- Encoder/Decoder

  上面说了，Encoder负责从原始类型向最终类型的转换，从接口定义就能看出

  - serializersModule：这是一个专门为上下文和多态准备的类，下面会讲到
  - encodeXXX：写入各种类型的数据，其中枚举和内联类一般会特殊处理
  - beginStructure：当要编码的是一个复杂对象时，就需要用到CompositeEncoder，具体参见其源码，不过原理和Encoder差不多，套娃而已
  - 最后两个方法只是快捷方法，用户自定义序列化器的情况：其实也只是套娃而已。

  ```kotlin
  public interface Encoder {
  
      public val serializersModule: SerializersModule
  
      public fun encodeNotNullMark() {}
  
      public fun encodeNull()
  
      public fun encodeBoolean(value: Boolean)
  
      ... ... //所有原始类型的编码方法
  
      public fun encodeString(value: String)
  
      public fun encodeEnum(enumDescriptor: SerialDescriptor, index: Int)
  
      public fun encodeInline(inlineDescriptor: SerialDescriptor): Encoder
  
      public fun beginStructure(descriptor: SerialDescriptor): CompositeEncoder
  
      public fun <T : Any?> encodeSerializableValue(serializer: SerializationStrategy<T>, value: T) {
          serializer.serialize(this, value)
      }
    
      public fun <T : Any> encodeNullableSerializableValue(serializer: SerializationStrategy<T>, value: T?) {
          val isNullabilitySupported = serializer.descriptor.isNullable
          if (isNullabilitySupported) {
              return encodeSerializableValue(serializer as SerializationStrategy<T?>, value)
          }
  
          if (value == null) {
              encodeNull()
          } else {
              encodeNotNullMark()
              encodeSerializableValue(serializer, value)
          }
      }
  }
  ```

- SerialKind

  枚举了所有类型，其中CONTEXTUAL（上下文）和PolymorphicKind（多态）下文有详细讲解

  ```kotlin
  public sealed class SerialKind {
      public object ENUM : SerialKind()
      public object CONTEXTUAL : SerialKind()
  }
  
  public sealed class PrimitiveKind : SerialKind() {
      public object BOOLEAN : PrimitiveKind()
      public object BYTE : PrimitiveKind()
      public object CHAR : PrimitiveKind()
      public object SHORT : PrimitiveKind()
      public object INT : PrimitiveKind()
      public object LONG : PrimitiveKind()
      public object FLOAT : PrimitiveKind()
      public object DOUBLE : PrimitiveKind()
      public object STRING : PrimitiveKind()
  }
  
  public sealed class StructureKind : SerialKind() {
      public object CLASS : StructureKind()
      public object LIST : StructureKind()
      public object MAP : StructureKind()
      public object OBJECT : StructureKind()
  }
  
  public sealed class PolymorphicKind : SerialKind() {
      public object SEALED : PolymorphicKind()
      public object OPEN : PolymorphicKind()
  }
  ```

### 看看Json序列化的实现

先引入一个定义：SerialFormat，它是专门定义用来作为序列化入口的接口，我们的实现类都使用它，包括Json类（这里的serializersModule暂且忽略）

```kotlin
public interface SerialFormat {
    public val serializersModule: SerializersModule
}
```

最常用的它的子类：StringFormat，定义了针对字符串的操作方式，及其快捷方式

```kotlin
public interface StringFormat : SerialFormat {

    public fun <T> encodeToString(serializer: SerializationStrategy<T>, value: T): String

    public fun <T> decodeFromString(deserializer: DeserializationStrategy<T>, string: String): T
}

public inline fun <reified T> StringFormat.encodeToString(value: T): String =
    encodeToString(serializersModule.serializer(), value)

public inline fun <reified T> StringFormat.decodeFromString(string: String): T =
    decodeFromString(serializersModule.serializer(), string)
```

最常用的序列化方法是`StringFormat.encodeToString(value: T)`，实际调用`Json.encodeToString`，它的逻辑：创建StreamingJsonEncoder（Encoder的实现类），将数据写入JsonStringBuilder，完成后转换为字符串进行返回。进入StreamingJsonEncoder查看，可以看到它定义了Composer类，控制Json格式的组合

```kotlin
public final override fun <T> encodeToString(serializer: SerializationStrategy<T>, value: T): String {
  val result = JsonStringBuilder()
  try {
    val encoder = StreamingJsonEncoder(
      result, this,
      WriteMode.OBJ,
      arrayOfNulls(WriteMode.values().size)
    )
    encoder.encodeSerializableValue(serializer, value)
    return result.toString()
  } finally {
    result.release()
  }
}
```

如果我们去AbstractJsonLexer.kt下面看，还可以看到预定义的各种Json元字符。

<img src="https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211009154534756.png" alt="image-20211009154534756" style="zoom:80%;" />

### 实现上下文和多态

前文我们能够看到，在使用上下文和多态功能时，会创建SerializersModule，事实上，SerializersModule就是专门为上下文和多态设计的，因此首先要拆解SerializersModule，可以看到，它只包含了两类方法，上下文和多态，其中上下文返回的是KSerializer，多态在序列化和反序列化各自定义了一个方法。

```kotlin
public sealed class SerializersModule {

    public fun <T : Any> getContextual(kclass: KClass<T>): KSerializer<T>? =
        getContextual(kclass, emptyList())

    public abstract fun <T : Any> getContextual(
        kClass: KClass<T>,
        typeArgumentsSerializers: List<KSerializer<*>> = emptyList()
    ): KSerializer<T>?
  
    public abstract fun <T : Any> getPolymorphic(baseClass: KClass<in T>, value: T): SerializationStrategy<T>?

    public abstract fun <T : Any> getPolymorphic(baseClass: KClass<in T>, serializedClassName: String?): DeserializationStrategy<out T>?
}
```

其唯一的实现类SerialModuleImpl如下，它维护了四个map

- class2ContextualFactory：存储类型和上下文Provider的映射，上下文Provider根据类型参数得到最终的序列化器
- polyBase2Serializers：存储了基类和具体值的真实类型的序列化器的映射关系，用于多态序列化
- polyBase2NamedSerializers：存储了基类和序列化后的类名的反序列化器的映射关系，用于多态反序列化
- polyBase2DefaultProvider：存储了针对基类的默认反序列化器

```kotlin
internal class SerialModuleImpl(
  private val class2ContextualFactory: Map<KClass<*>, ContextualProvider>,
  @JvmField val polyBase2Serializers: Map<KClass<*>, Map<KClass<*>, KSerializer<*>>>,
  private val polyBase2NamedSerializers: Map<KClass<*>, Map<String, KSerializer<*>>>,
  private val polyBase2DefaultProvider: Map<KClass<*>, PolymorphicProvider<*>>
) : SerializersModule() {

  override fun <T : Any> getPolymorphic(baseClass: KClass<in T>, value: T): SerializationStrategy<T>? {
    if (!value.isInstanceOf(baseClass)) return null
    return polyBase2Serializers[baseClass]?.get(value::class) as? SerializationStrategy<T>
  }

  override fun <T : Any> getPolymorphic(baseClass: KClass<in T>, serializedClassName: String?): DeserializationStrategy<out T>? {
    // Registered
    val registered = polyBase2NamedSerializers[baseClass]?.get(serializedClassName) as? KSerializer<out T>
    if (registered != null) return registered
    // Default
    return (polyBase2DefaultProvider[baseClass] as? PolymorphicProvider<T>)?.invoke(serializedClassName)
  }

  override fun <T : Any> getContextual(kClass: KClass<T>, typeArgumentsSerializers: List<KSerializer<*>>): KSerializer<T>? {
    return (class2ContextualFactory[kClass]?.invoke(typeArgumentsSerializers)) as? KSerializer<T>?
  }
}
```

现在我们可以按照步骤来看上下文和多态的实现方方法了

1. 注册类和对应的序列化器，实际上就是创建SerialModuleImpl对象，并赋值给SerialFormat的serializersModule属性。

   实际写入的是SerialModuleImpl.class2ContextualFactory属性

   ```kotlin
   Json {
     serializersModule = serializersModuleOf(LocalDateTime::class, LocalDateTimeAsLongSerializer)
   }
   ```

2. 调用StringFormat.encodeToString()，它调用serializersModule.serializer()方法获取对应的序列化器

   ```kotlin
   public inline fun <reified T> StringFormat.encodeToString(value: T): String =
       encodeToString(serializersModule.serializer(), value)
   
   public inline fun <reified T> SerializersModule.serializer(): KSerializer<T> {
       return serializer(typeOf<T>()).cast()
   }
   ```

   重点就在`serializer(typeOf<T>())`了，根据类型确定序列化器（走反射），源码过长过碎，这里就不展示了，只说大致逻辑

   - 如果类型是枚举，则创建枚举序列化器
   - 如果是接口，则创建PolymorphicSerializer，即多态序列化器，
   - 如果伴生对象中存在序列化器，则直接使用（@Serializable自动生成的那个）
   - 如果有Polymorphic注解，或者Serializable直接中明确指明使用PolymorphicSerializer，则返回多态序列化器
   - 否则，调用SerialModuleImpl.getContextual()方法，根据类获取之前注册到上下文中的序列化器。

   可以看到，在不同的情况下，会返回不同的序列化器，所谓上下文和多态，都是通过序列化器实现的。这里要多提的一点是，多态一定是通过PolymorphicSerializer实现的，因为它需要添加一个type字段。

#### 总结

可以看到，上下文和多态，实际上都只是根据类型确定序列化器和反序列化器的过程，而这些序列化器默认来自SerializersModule。

当然，我们最终也可以显式地指定序列化器，跳过这个决定的过程，毕竟，StringFormat的方法都可以接收序列化器。

## 开发属于自己的序列化格式

这里做一个小演示，如果我想要实现自己的序列化格式，只需要三步

1. 实现Encoder
2. 实现SerialFormat
3. 使用

```kotlin
// 实现Encoder
class FloydEncoder(
    private val sb: StringBuilder,
    override val serializersModule: SerializersModule
) : AbstractEncoder() {

    override fun encodeValue(value: Any) {
        sb.append("$value}")
    }

    override fun encodeElement(descriptor: SerialDescriptor, index: Int): Boolean {
        sb.append("{${descriptor.getElementName(index)}=")
        return true
    }
}
// 实现SerialFormat
object Floyd : StringFormat {
    override val serializersModule: SerializersModule = EmptySerializersModule

    override fun <T> decodeFromString(deserializer: DeserializationStrategy<T>, string: String): T {
        TODO("Not yet implemented")
    }

    override fun <T> encodeToString(serializer: SerializationStrategy<T>, value: T): String {
        val sb = StringBuilder()
        FloydEncoder(sb, serializersModule).encodeNullableSerializableValue(serializer, value).toString()
        return sb.toString()
    }

}
// 使用
@Serializable
data class Resource(
    val id: String,
    val desc: String
)

fun main() {
    val resource = Resource("1", "用于测试自定义Encoder的资源")
    val encodeString = Floyd.encodeToString(resource)
    println(encodeString)
}
```

输出

```bash
{id=1}{desc=用于测试自定义Encoder的资源}
```

## 哪些文档能看

这里只讲了主要部分，具体细节还有更多，目前网络上系统介绍Kotlin序列化的文章不多，还是以官方文档为主

- 首推[官方文档](https://github.com/Kotlin/kotlinx.serialization/blob/master/docs/serialization-guide.md)
- 然后[Kotlin 序列化Api doc](https://kotlin.github.io/kotlinx.serialization/kotlinx-serialization-core/kotlinx-serialization-core/index.html)
- 然后是源码

不过看源码有一个很重的感受：Kotlin库总是将抽象本身定义得比较抽象，然后大量使用扩展方法来为这些抽象增加能力，这会导致代码片段比较碎。如果用IDEA查看源码，会出现库的索引页全是类型，极不方便查找，但事实上可能只有少数几个kt源文件，所以需要探寻更加时刻Kotlin库的源码查看方式。

## 总结

优点

- Kotlin原生，使用起来相对优雅
- 其抽象逻辑具有很强的扩展性，要基于此实现自己的序列化格式也比较容易
- 序列化逻辑编译期生成，可能会比较快，这点尚未验证

缺点

- 太新，不够成熟，尽管Json版本已经稳定了，但其中很多API还是被标注为“实验性”的。如果线上要使用，我可能还是会选择Jackson吧。
- 不能很好滴和第三方库如Spring等很好地融合。

此外，本文所有代码，都能在[这里](https://gitee.com/zou8944/play-floyd/tree/master/serialization/src/main/kotlin/com/gitee/floyd/serialization/kotlin)找到。

