---
created_at: 2022-03-19 17:05:05
updated_at: 2022-03-19 17:05:05
tags:
  - Kotlin
  - Spring
---

Kotlin与Java百分百互操作，顺理成章，Spring开发也可以用Kotlin。可以享受到Kotlin的简洁语法。二者结合的大部分特点，在尝试之后都能体会。本文列举一些实际开发中最容易遇到的问题。

<!--more-->

## 关于POJO

DTO、VO、BO、MyBatis的Entity、Spring配置文件对应的PropertiesBean，各种Bean的组装与传输。直觉告诉我们，最好定义成data class，属性最好是val，最好是不可空，但不可一概而论，需按情况分析。

- 与前端交互的Bean：由于需要在前后端进行传输，需要设置为var的可空类型，且需要有一个不带任何参数的构造方法，有几点原因

  - var：以@RequestBody为例，Spring框架会先创建传输对象，再进行赋值

  - 可空：无法预测前端输入是否为空，且Spring Validate是先构建对象、为属性赋值、再进行验证，即时我们以@NotNull注释了，还是可能在赋值时报不可空的类型赋值错误，而不是@NotNull引起的验证错误

  - 不带参的构造方法：构建空对象 - 属性赋值，是Spring框架内部的常规操作，这也广泛存在于Java的其它三方库，因为Java默认存在无参构造，但Kotlin没有，需要显式构建。这又有两种方法

    - 所有属性写构造方法，但都是可控类型，且赋予了默认值null

      ```kotlin
      data class AppleLoginReq(
          @ApiModelProperty("OICD的idToken", required = true)
          @NotBlank
          var identityToken: String? = null
      )
      ```

    - 真无参构造

      ```kotlin
      class AppleLoginReq {
          @ApiModelProperty("OICD的idToken", required = true)
          @NotBlank
          var identityToken: String? = null
      }
      ```

- 业务内传输Bean：业务内可控，依据实际需要定义为data class + val属性 + 不可空或可空类型，构造方法如实即可
- 配置对应的Bean：Spring[手册](https://docs.spring.io/spring-boot/docs/2.0.x/reference/html/boot-features-kotlin.html#boot-features-kotlin-configuration-properties)中特别提到，可以用data class + lateinit var的形式，不过还是得有无参构造方法
- ORM的Table对应的Bean：虽然数据表是我们定义的，但将ORM对应的Bean属性的可空性和数据表字段的可空性对齐是一件非常繁琐的事。且涉及到日后维护问题，因此建议和前端交互Bean一样，var + 可空类型 + 无参构造方法

## val和var

项目中，纯业务代码能够依照Kotlin建议尽量使用val，但在与框架交互的代码中，使用var经常是唯一选择，主要原因是框架常常采用先创建对象再赋值的形式进行初始化。且赋值可能使用属性字段，也可能使用setter方法，因此，还得是var。常见的注入声明也变成了如下形式

```kotlin
@DisplayName("接口鉴权测试")
class AuthenticationTest {

  // 注意这里是lateinit var
  @Autowired
  private lateinit var mockMvc: MockMvc
```

## 属性复制

字段太多怎么办，属性赋值方法挺不错。考虑到原理，要求源对象的属性必须有getter方法，且，目标对象的属性必须有setter方法，否则复制不会成功

```kotlin
/**
 * 将类S的同名属性填充到D中
 * 要求源对象的属性必须有getter方法，且，目标对象的属性必须有setter方法，否则复制不会成功
 */
@Suppress("NULLABILITY_MISMATCH_BASED_ON_JAVA_ANNOTATIONS")
fun <S, D> D.fillWith(source: S): D = apply {
    BeanUtils.copyProperties(source!!, this!!)
}
```

## 默认final的问题

Spring中用到动态代理或CGLib，要求类可继承，而Kotlin具有默认final的原则，常见方式是手动标注该类为open，使用open关键字。[Kotlin提供了一个插件](https://kotlinlang.org/docs/all-open-plugin.html#gradle)，用注解替代open。我们可以将已有注解放在这里，就啥也不必加了。

```kotlin
allOpen {
    annotation("io.swagger.annotations.ApiModel")
}
```

## Kotlin的Spring插件

针对Spring的特殊要求，Kotlin提供了五个插件：三个已成熟、两个实验中

- [自动生成无参构造方法](https://kotlinlang.org/docs/no-arg-plugin.html)
- [自动为类加上open效果](https://kotlinlang.org/docs/all-open-plugin.html)
- [将SAM当成lambda表达式使用](https://kotlinlang.org/docs/sam-with-receiver-plugin.html)

## MyBatis Plus的Kotlin支持

注意MyBatis Plus支持的kotlin DSL的使用，会简单很多，不要再手动创建QueryWrapper了、不要再手动指定字段名了

```kotlin
@Repository
class BoardDao : ServiceImpl<BoardMapper, BoardModel>() {

    fun getBySn(ownerId: Long, sn: String): BoardModel {
        return ktQuery().eq(BoardModel::ownerId, ownerId).eq(BoardModel::sn, sn).one()
    }

    fun listByOwner(ownerId: Long): List<BoardModel> {
        return ktQuery().eq(BoardModel::ownerId, ownerId).list()
    }

}
```

> 这一点放在这里有点突兀，但体现了其重要性，值得强调

## 总结

Spring切换Kotlin遇到的最大问题还是框架本身大量使用反射、动态代理等技术带来的，究其原因，它是依据Java特性开发的框架。这就导致并不能在Spring中非常完美地使用Kotlin的各种特性，只能发挥Kotlin **90%**的简介特性。不那么Kotlin的点，总结下就是

- 经常使用var
- 经常使用平台类型
- 出于对值的未知不得不使用可空类型
- 必须有的无参构造、class的open关键字

## 参考

- [Spring Kotlin Support](https://docs.spring.io/spring-boot/docs/2.0.x/reference/html/boot-features-kotlin.html)
- [Spring Kotlin Deepdive](https://github.com/sdeleuze/spring-kotlin-deepdive)
- [Spring Boot Kotlin Demo](https://github.com/sdeleuze/spring-boot-kotlin-demo)
- https://spring.io/blog/2016/02/15/developing-spring-boot-applications-with-kotlin
- https://www.baeldung.com/kotlin/spring-boot-kotlin

