---
created_at: 2021-10-16 12:42:57.994
updated_at: 2021-10-16 12:42:57.994
slug: serialization-gson
tags: 
- 序列化
- Gson
---

Gson是一个相对简单的库，没有那么多功能，从设计上也并不想让别人去扩展它，它只想安安静静地做一个Json序列化库，简单而实用。

<!-- more -->

## 简单说

Gson提供两种方式创建Gson实例

- `new Gson()`：快速创建，默认配置，快速使用
- `new GsonBuilder().setxxxxx().create()`：完整方式创建，支持一些自定义化的配置

Gson突出一个简单，API如此，功能更是如此，大致列一下其支持的功能

- 基于field的序列化与反序列化：基本特性
- 支持自定义属性名：@SerializedName
- 支持反序列化时指定泛型信息：TypeToken
- 支持排除某个字段：transient关键字排除单个字段、按照可见性修饰符排除、@Expose主动选择
- 支持自定义序列化和反序列化逻辑：JsonSerializer、JsonDeserializer，或者它们的集合体：TypeAdapter

## 基础能力

什么注释也不用加，啥也不用干，直接就能使用

```kotlin
class Resource1<T> {
    var id: Int = -1
    var type: ResourceType? = null

    @Transient
    var secret: String = ""

    @SerializedName("我是实际数据")
    var data: T? = null

    override fun toString(): String {
        return "Resource1(id=$id, type=$type, secret='$secret', data=$data)"
    }

}

fun main() {
    val gson = Gson()
    val resource = Resource1<JsonObject>().apply {
        this.id = 1
        this.type = null
        this.secret = "我是密码"
        this.data = JsonObject().apply {
            addProperty("key", "value")
        }
    }
    val jsonString = gson.toJson(resource)
    println(jsonString)
    println(gson.fromJson<Resource1<JsonObject>>(jsonString, object : TypeToken<Resource1<JsonObject>>() {}.type))
}
```

要点

- 序列化用`gson.toJson(xxx)`，反序列化用`gson.fromJson(jsonString, 类型信息)`
- 忽略字段可以用transient关键字
- 自定义字段名用@SerializedName注解，实际上这是Gson能够个性化配置的唯四之一
- 对于泛型擦除的情况，在反序列化时通过TypeToken指定：`object : TypeToken<Resource1<JsonObject>>() {}.type`。这一点和Jackson和Fastjson的TypeReference类似

## 排除字段

```kotlin
class Resource4 {
    @Expose
    var id: Int = -1
    var type: ResourceType? = null
}

fun main() {
    val gson = GsonBuilder().excludeFieldsWithoutExposeAnnotation().create()
    println(gson.toJson(Resource4().apply { id = 10; type = ResourceType.CHARACTER }))
}
```

- `GsonBuilder().excludeFieldsWithoutExposeAnnotation()`设置只暴露@Expose的数据
- @Expose标记字段

## 自定义实例创建器

Gson反序列化时创建对象的逻辑

- 首先寻找是否存在目标类的无参构造函数，有则用它创建实例
- 其次寻找是否存在用户自定义的实例创建器
- 然后如果目标类是原生类型，则直接查找对应类型的构造器并创建实例
- 都没有，则用sun.misc.Unsafe创建实例

一般不推荐使用Unsafe创建实例，要么提供无参构造方法，要么提供实例创建器，这里有一个后者的例子

```kotlin
class Resource3(var id: Int, var type: ResourceType?) {

    init {
        println("有参构造函数被执行了")
    }

    override fun toString(): String {
        return "Resource3(id=$id, type=$type)"
    }

}

class Resource3Creator : InstanceCreator<Resource3> {

    override fun createInstance(type: Type): Resource3 {
        return Resource3(-1, null)
    }

}

fun main() {
    val gson = GsonBuilder().registerTypeAdapter(Resource3::class.java, Resource3Creator()).create()
    val resource = Resource3(1, null)
    println("序列化")
    val jsonString = gson.toJson(resource)
    println(jsonString)
    println("反序列化")
    println(gson.fromJson(jsonString, Resource3::class.java))
}
```

输出

```bash
有参构造函数被执行了
序列化
{"id":1}
反序列化
有参构造函数被执行了
Resource3(id=1, type=null)
```

> PS：Gson默认忽略掉内部类，因为它没有无参构造函数

## 自定义序列化器

老规矩，自定义LocalDateTime的序列化和反序列化逻辑，为此Gson提供了三种类型可供定义，要么定义序列化器、要么反序列化器，要么同时有。

```kotlin
class Resource5 {
    var id: Int = -1
    var type: ResourceType = ResourceType.CHARACTER

    @JsonAdapter(Resource5TypeAdapter::class)
    var updatedTime: LocalDateTime? = null

    override fun toString(): String {
        return "Resource5(id=$id, type=$type, updatedTime=$updatedTime)"
    }

}

class Resource5TypeAdapter : TypeAdapter<LocalDateTime>() {

    override fun write(out: JsonWriter, value: LocalDateTime?) {
        println("执行了写方法")
        if (value == null) out.nullValue()
        else out.value(value.toInstant(ZoneOffset.UTC).toEpochMilli())
    }

    override fun read(`in`: JsonReader): LocalDateTime {
        println("执行了读方法")
        return LocalDateTime.ofInstant(Instant.ofEpochMilli(`in`.nextLong()), ZoneOffset.UTC)
    }

}

fun main() {
    val resource = Resource5().apply {
        this.id = 1
        this.updatedTime = LocalDateTime.now()
    }
    val gson = Gson()
    val jsonString = gson.toJson(resource)
    println(jsonString)
    println(gson.fromJson(jsonString, Resource5::class.java))
}
```

- 可通过@JsonAdapter局部指定
- 也可通过`GsonBuilder().registerTypeAdapter`全局注册

## 多态

Gson原生不支持多态，但可通过一些其它方式实现，以下是官方推荐的方式（尽管很傻）

```kotlin
fun main() {
    val gson = Gson()
    val list = listOf(
        1,
        "",
        mapOf(
            "key" to "value"
        )
    )
    val jsonString = gson.toJson(list)
    println(jsonString)
    gson.fromJson(jsonString, JsonArray::class.java).mapIndexed { index, jsonElement ->
        when (index) {
            0 -> gson.fromJson(jsonElement, Int::class.java)
            1 -> gson.fromJson(jsonElement, String::class.java)
            2 -> gson.fromJson(jsonElement, object : TypeToken<Map<String, String>>() {}.type)
            else -> throw Exception()
        }
    }.toList().also { println(it) }
}
```

- 如果一个集合中有多重类型，反序列化时，先得到JsonArray，再针对具体元素应用具体类型
- 这就不咋科学，还有一种方式是RuntimeTypeAdapterFactory，这非官方推荐的方式，所以要用多态还是别用Gson了

## 树模型

Gson的树模型还是简单的，只有JsonArray、JsonObject以及JsonElement三个类，但是API不大友好，限制的比较死

- 添加一般属性就要调用addProperty方法，且只支持String、Boolean、Number、Character四种类型
- 添加对象或数组属性就得用add方法
- 不支持fluent API

```kotlin
fun main() {
    val resource = JsonObject().apply {
        addProperty("id", 1)
        addProperty("type", ResourceType.CHARACTER.name)
        addProperty("usn", null as String?)
        add("data", JsonArray().apply {
            add(false)
            add(123)
        })
    }
    println(GsonBuilder().setPrettyPrinting().create().toJson(resource))
}
```

## 支持设置啥能力

穷举一下GsonBuilder，有啥能力，可以看到，其实没啥能力。

![image-20211016115638338](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211016115638338.png)

- 设置序列化和反序列化的排除策略
- 设置各种类型适配器，用于控制类型序列化和反序列化时的行为
- 关闭内部类的序列化
- Html格式转义
- 序列化名称控制
- 输出格式化
- 版本控制（@Since和@Until注解可设置POJO的版本，有点类似@JsonView的功能，但感觉非常鸡肋）
- 设置日期格式
- 设置字段名命名策略

## 基本原理

加上Gson，前前后后看了五个序列化库，除了Java，原理结构上都大同小异，只是在序列化和反序列化的具体算法上有所差别，扣得比较细节，尤其是Fastjson用了很多奇技淫巧，硬是把速度提了上去。

- 对于序列化，首先得到序列化器，再用序列化器将实际对象写入流
- 对反序列化，首先得到反序列化器，再得到目标类的实例，再用反序列化器从流中读取内容塞入目标实例

至于Gson，它比较与众不同的点在于

- 序列化时，直接使用了StringWriter做写操作，而不是自己维护输出流和缓冲区
- Json格式的实际写入在com.google.gson.stream.JsonWriter，内部套StringWriter
  - 写入状态控制与Jackson采用树状结构不同，它采用了栈（一个一维数组，数组的大小即当前层次结构的深度，数组的值即当前所处结构的类型）的方式维护，参见com.google.gson.stream.JsonWriter#stack
- 对未自定义序列化器的类型来说，使用com.google.gson.internal.bind.ReflectiveTypeAdapterFactory.Adapter达成
  - 对于序列化，它直接使用了反射获取符合要求的字段，然后写入writer
  - 对于反序列化，它使用前文"自定义实例创建器"所说的方式创建对象，然后通过反射写入目标对象

## 总结

通篇看起来，Gson定位清晰，目标明确，文档和代码规范，用起来也比较轻松。只是功能简单，原理也简单，直接使用StringWriter和反射，就是一个功能性的Json库，看不大出有什么性能优化，因此可以推测，Gson的性能不会太出色。


