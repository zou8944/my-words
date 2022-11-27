---
created_at: 2021-10-15 17:11:21.211
updated_at: 2021-10-15 17:11:39.595
slug: serialization-fastjson
tags: 
- 序列化
- Fastjson
---

开局一吐槽，Fastjson的文档，比Jackson还差。Jackson只是位置不明确，如果安下心来看看，还是能够理清楚的。而Fastjson是位置不明确，如果安下心来看看，还会发现，它的文档零零散散，中英文混杂，找不准主线在哪儿。我记得知乎上有个问题，[fastjson这么快老外为啥还是热衷 jackson?](https://www.zhihu.com/question/44199956)，就这文档，让老外用个啥。

不过看还是要看的，毕竟它是目前主流序列化框架之一。老样子，我们还是从基本使用方法和原理分析两部分着手。

<!-- more -->

## 能力

Fastjson仅仅针对json，尚不支持其它任何格式，也没有看到谁为它进行格式扩展。因为这并不是它的目的，库如其名，它是为了更快地序列化Json而存在。因此，使用上来，会简单许多。具体分为几个部分

- 常规使用
- 注解
- 自定义序列化器
- 自定义过滤器
- 树模型

### 基础能力

```kotlin
fun testBase() {

    data class Resource(
        var id: String,
        var type: Type
    )

    val jsonString = JSON.toJSONString(Resource("1", Type.RECORD))
    println(jsonString)
    val resource = JSON.parseObject(jsonString, Resource::class.java)
    println(resource)
}
```

- 序列化：`JSON.toJSONString(对象)`

- 反序列化：`JSON.parseObject(jsonString, 对象class)`

- 注意

  - 默认情况下，是根据getter和setter方法取得和设置字段的，如果没有，将得不到输出

  - 也可以基于属性获取和设置字段，考虑下面的例子

    ```kotlin
    fun testBasedOnFields() {
    
        data class Resource(
            private var id: String,
            private var type: Type
        )
    	
      	// 设置基于字段的序列化
        val serializeConfig = SerializeConfig(true)
      	// 设置基于字段反序列化
        val parserConfig = ParserConfig(true)
        val jsonString = JSON.toJSONString(Resource("1", Type.RECORD), serializeConfig)
        println(jsonString)
        val resource = JSON.parseObject<Resource>(jsonString, Resource::class.java, parserConfig)
        println(resource)
    }
    ```

### 注解

注解方面它采取了另一种思路，它只有两个注解，但将功能放在注解的属性中

- @JSONType：放在类上的注解 ，可设置
  - alphabetic：字段按照字母顺序排序
  - asm：反序列化时是否使用asm
  - orders：字段之间的顺序
  - includes：需要包含哪些字段
  - excludes：需要排除哪些字段
  - serializeFeatures：需要包含的序列化功能
  - parseFeatures：需要包含的反序列化功能
  - mappingTo：映射成某个类
  - builder：指定反序列化的构建器
  - serializer：指定序列化器
  - deserializer：指定反序列化器
  - naming：指定命名策略
  - serialzeFilters：指定过滤器
- @JSONField：放在属性上的注解 ，可设置
  - ordinal：序列化后字段的位置
  - name：序列化后的名字
  - format：指定日期的格式
  - serialize：是否参与序列化
  - deserialize：是否参与反序列化
  - serializeFeatures：需要包含的序列化功能
  - parseFeatures：需要包含的反序列化功能
  - label：标签，这是内部功能，结合过滤器可实现类似分组的功能
  - serializeUsing：指定序列化器
  - deseializeUsing：指定反序列化器
  - alternateNames：指定别名，反序列化时可用
  - unwrapped：将带有结构的对象的属性提取到顶层
  - defaultValue：反序列化时的默认值

```kotlin
// 一个简单的修改属性名字献给大家
fun testAnnotations() {

    @JSONType(alphabetic = false, ignores = ["id"])
    data class Resource(
        val id: String,
        @JSONField(name = "resourceType")
        val type: Type,
        val updatedTime: Date
    )

    println(JSON.toJSONString(Resource("1", Type.RECORD, Date()), SerializerFeature.PrettyFormat))
}
```

仔细想想，从注解能力上来说，还是有所差别的

- @JsonRawValue，将字段作为原生json看待
- @JsonAutoDetect，自定义属性检测的可见性修饰符
- @JsonView，同一个POJO的多种序列化结果，可通过label实现
- @JsonAnyGetter、@JsonAnySetter，多余的字段塞到map，以及反过程
- @JsonValue，将POJO的某个字段作为整个POJO的序列化结果
- @JsonInclude，根据情况决定是否将字段加入序列化
- @JsonEnumDefaultValue，给枚举设置默认值
- @JsonInject，给某个字段强行注入
- 多态，不过可以通过其它方式变相达成：SerializeFeature.WriteClassName
- @JsonManagedReference等循环引用的解决方式，Fastjson也有解决，不过它是采用$ref的方式，而非jackson的去除或使用某个字段替代。
- @JsonRootName，将对象序列化到一个指定名称的属性下

### 自定义序列化器

不多解释，传统技能：为LocalDateTime自定义序列化器

```kotlin
fun testCustomSerializer() {
    data class Resource(
        val id: String,
        val type: Type,
        val updatedTime: LocalDateTime
    )

    class LocalDateTimeSerializer : ObjectSerializer {
        override fun write(
            serializer: JSONSerializer,
            `object`: Any?,
            fieldName: Any?,
            fieldType: java.lang.reflect.Type?,
            features: Int
        ) {
            val out = serializer.out
            if (`object` == null) {
                out.writeNull()
            } else {
                out.writeLong((`object` as LocalDateTime).toInstant(ZoneOffset.UTC).toEpochMilli())
            }
        }
    }

    SerializeConfig.globalInstance.put(LocalDateTime::class.java, LocalDateTimeSerializer())
    println(JSON.toJSONString(Resource("1", Type.RECORD, LocalDateTime.now())))
}
```

不过这序列化器注册的方式嘛，是不是不大友好呀。要么全局注册，要么序列化时传参进去，并不能持有多套配置JSON对象。

### 自定义过滤器

过滤器是Fastjson比较独有的概念，也比较好理解：在序列化的多个阶段提供给用户参与调整的机会。

![image-20211015152451901](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211015152451901.png)

具体怎么用，只能靠猜，源码也没有注释，文档也不好找，需要的时候再去找吧。这里就展示怎么注册：把所有名称都设置为大写

```kotlin
fun testCustomFilter() {

    data class Resource(
        val id: String,
        val type: Type,
        val updatedTime: LocalDateTime
    )

    class IdFilter : NameFilter {
        override fun process(`object`: Any?, name: String, value: Any): String? {
            return name.uppercase(Locale.getDefault())
        }

    }
    SerializeConfig.globalInstance.addFilter(Resource::class.java, IdFilter())
    println(JSON.toJSONString(Resource("1", Type.RECORD, LocalDateTime.now())))
}
```

### 树模型的使用

没错，它也有树模型，只是功能没那么强大而已，它也只有两个对象

- JSONObject：可直接理解为Map，事实上它也是继承了Map
- JSONArray：理解为List

```kotlin
fun testTreeModel() {
    val resource = JSONObject()
        .fluentPut("ID", 1)
        .fluentPut(
            "data", JSONArray()
                .fluentAdd(
                    JSONObject()
                        .fluentPut("images", "[]")
                )
        )
    println(JSON.toJSONString(resource, SerializerFeature.PrettyFormat, SerializerFeature.SortField))
}
```

输出如下，这里可以看到一个问题：Fastjson默认序列化后所有的字段都是排序的，这就很不好。

```bash
{
	"data":[
		{
			"images":"[]"
		}
	],
	"ID":1
}
```

### 其它功能

其它功能，主要就是在Feature中指定的内容了，基本都是置顶序列化和反序列化时遵循的特性。

```java
// 序列化相关的功能
public enum SerializerFeature {
  	// 字段名用引号引起来
    QuoteFieldNames,
    // 使用单引号
    UseSingleQuotes,
    WriteMapNullValue,
    // 枚举调用toString()输出
    WriteEnumUsingToString,
    // 枚举调用name()输出
    WriteEnumUsingName,
    // 日期使用ISO8601格式
    UseISO8601DateFormat,
    // 列表的null输出为[]
    WriteNullListAsEmpty,
    // 字符串的null输出为空串
    WriteNullStringAsEmpty,
    // 数字的null输出为0
    WriteNullNumberAsZero,
    // 布尔的null输出为false
    WriteNullBooleanAsFalse,
    // 忽略被transient标记的字段
    SkipTransientField,
    // 为字段排序
    SortField,
    // 格式化输出
    PrettyFormat,
    // 输出结果添加类名，可用来实现多态
    WriteClassName,
		// 关闭循环引用检测
    DisableCircularReferenceDetect,
		// 将斜线当做特殊符号
    WriteSlashAsSpecial,
		// 浏览器兼容
    BrowserCompatible,
		// Date使用日期格式输出
    WriteDateUseDateFormat,
		// 不写根类的名字
    NotWriteRootClassName,
    // 将java bean的字段以数组的形式输出，而不是对象
    BeanToArray,
		// 将非字符串的key当做字符串输出
    WriteNonStringKeyAsString,
    // 不为没有值的属性写默认值
    NotWriteDefaultValue,
    // 浏览器安全
    BrowserSecure,
    // 忽略没有幕后字段的getter
    IgnoreNonFieldGetter,
    // 将非字符串的值当做字符串输出
    WriteNonStringValueAsString,
    // getter报错时忽略
    IgnoreErrorGetter,
		// 将bigdecimal当做字符串输出
    WriteBigDecimalAsPlain,
		// map输出时也要将字段排序
    MapSortField;
}

// 反序列化相关的功能
public enum Feature {
    // 读取完后自动关闭读取源
    AutoCloseSource,
    // 允许注释出现
    AllowComment,
    // 允许未被引号包含的字段名
    AllowUnQuotedFieldNames,
   	// 允许单引号
    AllowSingleQuotes,
    // 字段名intern化，主要用于节省空间
    InternFieldNames,
    // 允许ISO8601格式的日期格式
    AllowISO8601DateFormat,
		// 允许任意数量的逗号间隔
    AllowArbitraryCommas,
		// 数字使用BigDecinal接收
    UseBigDecimal,
    // 字段不匹配时忽略，不报错
    IgnoreNotMatch,
		// 启用有序字段的匹配算法，会更快
    SortFeidFastMatch,
    // 不启用ASM
    DisableASM,
    // 关闭循环引用的检测
    DisableCircularReferenceDetect,
    // 字符串类型的字段初始化为空串
    InitStringFieldAsEmpty,
    // 支持将数组转换为bean
    SupportArrayToBean,
    // 字段排序
    OrderedField,
    // 关闭特殊字符检测
    DisableSpecialKeyDetect,
    // 使用对象数组
    UseObjectArray,
		// 支持非public的字段写入
    SupportNonPublicField,
		// 忽略autotype，即多态的功能
    IgnoreAutoType,
		// disable field smart match, improve performance in some scenarios.
    DisableFieldSmartMatch,
		// 开启自动类型转换
    SupportAutoType,
		// 非字符串的key转化为string
    NonStringKeyAsString,
		// 使用自定义的Map的反序列化器
    CustomMapDeserializer,
		// 枚举不匹配时报错
    ErrorOnEnumNotMatch,
		// 安全模式
    SafeMode,
		// 字符串字段去除两头空字符
    TrimStringFieldValue
}
```

## 原理

看了kotlinx.serialization、Jackson，再看Fastjson，发现它们的组成基本一致，无非三个部分，可能根据情况其命名和具体实现方式会有所不同。这部分没啥新意，自己追一下方法就OK了。

- 门面：JSON
- 将原始对象写入流：SerializeWriter、JSONReaderScanner
- 将自定义对象转换为原始对象：ObjectSerializer、ObjectDeserializer

Fastjson的特点在于快，为什么这么快呢？据说是算法，[作者自己的博客——Fastjson技术内幕](https://www.iteye.com/blog/wenshao-1142031)有所描述，归结起来大概就是

- 自定义SerializeWriter，提供两部并做一步走之类的方法writeIntAndChar，减少越界检查
- 使用ASM避免反射
- 自定义IdentityHashMap，避免equals操作
- 默认字段有序，以便为反序列化性能提升做准备
- balabalabalabalabala

所以Fastjson的原理，重点是算法，而不在结构上。而这些算法，是不是有点奇技淫巧了🤔。

## 总结

看了官方手册、网上相关文章，翻阅了源码，试用了基本功能，Fastjson给人最大的感觉——偏科生。

偏在哪里？速度，大家都在强调快快快，一切以快为目标。作者告诉我们Fastjson是目前已知的最快的Json序列化库，给出benchmark，晒出获奖记录，好像要脚踩Jackson，拳打Gson，唯我独尊，甚至和Protobuf进行了对比（这个对比我觉得就很扯）；网文介绍Fastjson的功能时，快是一定要强调的。大家好像陷入一种狂热状态，好像Json序列化最主要的功能就是为了快，这明显是不正常的。

典型的Web场景，数据库读取几十ms，序列化几ms，如果序列化不是以指数形式加速，快个小几倍个人认为意义不大，可能对于京东淘宝这种超大吞吐量有意义，对一般的网站，Jackson已经足够快速。

作为一个序列化库，更重要的是稳定性、安全性、可用性。这几方面FastJson做的貌似都不大好，文档混乱、代码没有注释、类命名还是有奇怪的地方，当然作为一个人撸出来的代码，也不能苛求太多。

对此，我个人的观点是，Fastjson只适合少数特定场景下的使用，并不能作为一个通用的Json序列化框架。目前看起来，我用Jackson。