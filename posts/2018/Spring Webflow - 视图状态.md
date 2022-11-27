---
created_at: 2018-09-09 14:00:00.0
updated_at: 2021-02-16 23:27:30.411
slug: spring-webflow-view-state
tags: 
- Spring
- Spring Webflow
- Spring Webflow View
---

# 基础
## 指定view-state的view属性的几种方式

 - 按照默认名称在相对路径下查找view

```
<!-- 在flow配置文件同目录下查找名为enterBookingDetails的视图 -->
<view-state id="enterBookingDetails">
```

 - 指明view名称，在相对路径下查找view

```
<!-- 在flow配置文件同目录下查找名为bookingDetails.xhtml的视图 -->
<view-state id="enterBookingDetails" view="bookingDetails.xhtml">
```

 - 绝对路径查找view

```
<!-- 直接查找/WEB-INF/hotels/booking/bookingDetails.xhtml的视图 -->
<view-state id="enterBookingDetails" view="/WEB-INF/hotels/booking/bookingDetails.xhtml">
```

 - 按照逻辑ID定位view
这是结合Spring提供的其它viewResolver来定位到其他组件中的view，如Tiles等。在前面 [配置](https://blog.csdn.net/zou8944/article/details/82391712) 一章中有讲

```
<!-- 结合viewResolver共同确定视图位 -->
<view-state id="enterBookingDetails" view="bookingDetails">
```
## 在viewScope中分配变量

 - 直接分配

```
<var name="searchCriteria" class="com.mycompany.myapp.hotels.SearchCriteria" />
```

 - 依靠运算结果分配

```
<on-render>
  	 <evaluate expression="bookingService.findHotels(searchCriteria)" result="viewScope.hotels" />
</on-render>
```
## 在viewScope中操作对象
如下例子展示了如何在同一个view state的不同时机操作一系列对象

```
<view-state id="searchResults">
   	<on-render>
		<evaluate expression="bookingService.findHotels(searchCriteria)"
                 result="viewScope.hotels" />
	</on-render>
	<transition on="next">
		<evaluate expression="searchCriteria.nextPage()" />
		<render fragments="searchResultsFragment" />
	</transition>
	<transition on="previous">
		<evaluate expression="searchCriteria.previousPage()" />
		<render fragments="searchResultsFragment" />
	</transition>
</view-state>
<!-- 渲染view之前，首先执行findHotels方法，将结果放到viewScope的hotels中 -->
<!-- 当返回next事件时，执行nextPage()方法， 然后渲染查找结果部分 -->
<!-- 当返回previous事件时，执行前一页操作，然后渲染查找结果部分 -->
```
## `<on-render>`
在view渲染前可以执行一个或多个action，**这些action将会在视图最开始渲染以及后续的任何刷新，甚至视图局部的重新渲染执行**。以上面的代码为例，在重新渲染结果之前，还会先执行一次findHotels方法。
##数据绑定
## 在view-state上绑定model
使用model属性，可以将一个对象绑定到view中的表单中。web flow可以帮助完成对象属性和表单域的绑定和验证。

```
<view-state id="enterBookingDetails" model="booking">
```
绑定时机是当view的event发生时

 - `view-to-model`绑定：在view完成并回发时，用户的输入域会被绑定到指定对象的属性上
 - `model`验证：绑定后，如果需要验证，验证逻辑会被调用。
 - 需要指出的是：只有当验证成功后才能transition到别的state，验证失败时会重新渲染该view，要求用户重新输入。
##绑定model时的类型转换
####基础
由于客户端上传的表单数据都是字符串类型的， 因此需要进行类型转换

 - Web Flow类型转换和Spring MVC的类型转换的关系
在web-flow 2.1以前，Sprign MVC和web-flow使用不同的类型转换机制，但是2.1以后，二者使用相同的类型转换
**以前**，Web Flow使用`spring-binding-2.4.6.RELEASE.jar`包提供的API进行类型转换，相关的类有`org.springframework.binding.convert.service.DefaultConversionService`， `org.springframework.binding.convert.converters.Converter`等，通过实现`Converter`接口完成自定义转换器，再通过`DefaultConversionService`进行注册，就像如下所示的方式1那样；而且这样还能够注册带命名ID的转换器，可以结合`<bingding>`的`converter`属性进行使用，但这种方式已经非常不建议了。
**目前**， Web Flow在执行conversionService时依然使用`org.springframework.binding.convert.service.DefaultConversionService`，但该服务已经不会去注册任何默认的转换器和格式化器了，而是将转换和格式任务全部委托给来自`spring-core-4.3.7.RELEASE.jar`包的`org.springframework.core.convert.ConversionService`完成。`DefaultConversionService`内部维护一个`ConversionService`对象，对`DefaultConversionService`中进行的大多数操作都被转变成对`ConversionService`的操作(对带命名ID转换器的管理除外)。值得一提的是，命名ID的转换器非常没有必要，因为在检测到相应类型后，系统会自动调用合适的转换器。

 - 方式一 传统方式添加Converter(不建议使用)

```
import org.springframework.binding.convert.converters.Converter;
// 定义自己的转换器
public class DateConverter implements Converter {

    public Class<?> getSourceClass() {
        return String.class;
    }

    public Class<?> getTargetClass() {
        return java.util.Date.class;
    }

    public Object convertSourceToTargetClass(Object source, Class<?> targetClass) throws Exception {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
        
        return sdf.parse(source.toString());
    }

}
```

```
// 注册自己的转换器
public class ApplicationConversionService extends DefaultConversionService {
	public ApplicationConversionService() {
   		addConverter(new DateConverter());
	}
}
```

```
<!-- 使用转换器，什么都不用指定，当检测到model中的checkinDate属性为Date类型时，DateConverter会自动被调用 -->
<view-state id="enterBookingDetails" model="booking">
   	<binder>
       	<binding property="checkinDate"/>
   	</binder>
</view-state>
```

 - 方式二 添加带ID的Converter(已过时，不推荐使用)

```
DateConverter的定义不变
```

```
// 注册时指定id
public class ApplicationConversionService extends DefaultConversionService {
	public ApplicationConversionService() {
		// 该方法已被标为deprecated
   		addConverter("dateConverter", new DateConverter());
	}
}
```

```
<!-- 使用时指定id -->
<view-state id="enterBookingDetails" model="booking">
   	<binder>
       	<binding property="checkinDate" converter="dateConverter"/>
   	</binder>
</view-state>
```
 - 方式三 - 配置通用的Converter和Formatter(推荐使用，当前版本鼓励的方式)

```
// 首先实现FormattingConversionServiceFactoryBean，添加自定义格式化器和转换器
public class ApplicationConversionServiceFactoryBean extends FormattingConversionServiceFactoryBean {

    @Override
    public void setConverters(Set<?> converters) {
        Converter<String, Date> converter = new Converter<String, Date>() {
            public Date convert(String source) {
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
                return sdf.parse(source);
            }
        };
        
        Set<Converter<String, Date>> set = new HashSet<Converter<String,Date>>();
        set.add(converter);
        super.setConverters(set);
    }

    @Override
    public void setFormatters(Set<?> formatters) {
        Set<Formatter<Date>> set= new HashSet<Formatter<Date>>();
        set.add(new Formatter<Date>() {

            public String print(Date object, Locale locale) {
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
                return sdf.format(object);
            }

            public Date parse(String text, Locale locale) throws ParseException {
                SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd");
                return sdf.parse(text);
            }
            
        });
        
        super.setFormatters(set);
    }

}
```

```
// 创建由ApplicationConversionServiceFactoryBean产生的ConversionService
// 该ConversionService是Spring MVC中类型转换的核心，可以同时配置给Spring MVC和Web Flow
@Bean("applicationConversionService")
public ConversionService applicationConversionService() {
    FormattingConversionServiceFactoryBean factory = new ApplicationConversionServiceFactoryBean();
    // 添加自定义格式化器
    factory.setFormatters(null);
    // 添加自定义格式转换器
    factory.setConverters(null);
    // 生成ConversionService 
    factory.afterPropertiesSet();
    // 返回ConversionService 
    return factory.getObject();
}
```

```
// 下面三个步骤用于配置给Web Flow

@Bean("defaultConversionService")
public DefaultConversionService conversionService(@Autowired ConversionService applicationConversionService) {
    return new DefaultConversionService(applicationConversionService);
}

@Bean
public FlowBuilderServices flowBuilderServices(@Autowired MvcViewFactoryCreator mvcViewFactoryCreator, @Autowired DefaultConversionService defaultConversionService) {
    return getFlowBuilderServicesBuilder()
            .setConversionService(defaultConversionService)
            .build();
}

// 注册flow
@Bean("flowRegistry")
public FlowDefinitionRegistry flowRegistry(@Autowired FlowBuilderServices flowBuilderServices) {
    
    return getFlowDefinitionRegistryBuilder()
            .setBasePath("/WEB-INF/jsp/flow")
            .addFlowLocation("/config/search-flow.xml")
            .setFlowBuilderServices(flowBuilderServices)
            .build();
}
```

```
<!-- 下面的步骤用于注册给Spring MVC -->
<mvc:annotation-driven conversion-service="applicationConversionService" />
```
 - 针对上述三种方式的说明
  - 方式一表面上使用的是旧的转换器添加方式，但内部实现还是按照新的方式进行，在添加Converter时，会通过一个适配器类转换将`org.springframework.binding.convert.converters.Converter`转换为`org.springframework.core.convert.converter.GenericConverter`

```
// 源码片段
public void addConverter(Converter converter) {
	((ConverterRegistry) delegate).addConverter(new SpringBindingConverterAdapter(converter));
	if (converter instanceof TwoWayConverter) {
		TwoWayConverter twoWayConverter = (TwoWayConverter) converter;
		((ConverterRegistry) delegate).addConverter(new SpringBindingConverterAdapter(new ReverseConverter(
				twoWayConverter)));
	}
}
```

  - 方式二已过时，这里仅展示
  - 方式三推荐使用，但这里仅展示了我自己实验成功的java config配置方式，xml配置方式可以参见[官网](https://docs.spring.io/spring-webflow/docs/2.4.5.RELEASE/reference/html/views.html#converter-configuration)。
  - 实际使用时，会发现方式一从视图提交到model时类型转换能够正常进行，但是从model回填到视图时并非自己最开始输入的数值，那是因为我们只设置了Converter，没有设置Formatter。
  - 关于转换器的配置，只要认识到ConversionService是类型转换的核心，就会省事很多

## Converter和Formatter的区别

 - `Converter`: 是`spring-core-4.3.7.RELEASE.jar`包提供的，用于`Object to Object`的转换
 - `Formatter`: 是`spring-context-4.3.7.RELEASE.jar`包提供的，用于`Object to String`的转换。

## 格式化注解
新的类型转换提供两个有用的注解，可以放在model类的属性上，和被@Controller类的方法参数中。

 - `NumberFormat`
 - `DateTimeFormat`： 该注解默认使用[`Joda Time`](http://www.joda.org/joda-time/)，需要在类路径中包含Joda Time的包。默认情况下Spring MVC和web flow都没有其他的日期相关的转换器和格式化器。因此定义我们自己的日期相关转换器和格式化器非常重要。
 - 此外，我们还可以参照上述两个注解定义自己的注解.

## 关于绑定的另外两点

 - 取消绑定
可以使用bind属性在特定情况下取消绑定。如下当触发cancel事件时不会执行绑定操作

```
<view-state id="enterBookingDetails" model="booking">
    <transition on="proceed" to="reviewBooking">
    <transition on="cancel" to="bookingCancelled" bind="false" />
</view-state>
```

 - 显式地指明绑定的字段
使用<binder>标签可以显式指明需要绑定的字段，同时可以指明需要使用到的转换器，和是否允许为空。

```
<view-state id="enterBookingDetails" model="booking">
    <binder>
        <binding property="checkinDate" converter="shortDate" required="true" />
        <binding property="checkoutDate" converter="shortDate" required="true" />
        <binding property="creditCard" required="true" />
        <binding property="creditCardName" required="true" />
        <binding property="creditCardExpiryMonth" required="true" />
        <binding property="creditCardExpiryYear" required="true" />
    </binder>
    <transition on="proceed" to="reviewBooking">
    <transition on="cancel" to="bookingCancelled" bind="false" />
</view-state>
```

> 注意事项
> 1. 没有显式指定绑定字段时，所有model对象的公共属性都会被绑定；指定绑定字段时，则只有显式指定的字段会被绑定
> 2. 没有显式声明转换器时，会使用自动检测的转换器
> 3. 声明不允许为空时，若出现空，则会产生验证错误，并会重新绘制视图并报错。
> ##绑定数据的验证
> Web Flow支持自定义验证条件和JSR-303 Bean验证框架
> ####JSR-303 Bean Validation
>  -  基础配置
> 首先类路径中需要有一个validator的jar包，然后按照如下配置后，validator会应用到所有的添加了条件注解的model属性中
```
<webflow:flow-registry flow-builder-services="flowBuilderServices" />
<webflow:flow-builder-services id="flowBuilderServices" validator="validator" />
<bean id="validator" class="org.springframework.validation.beanvalidation.LocalValidatorFactoryBean" />
```
&emsp;&emsp;form中按如下方式配置

```
@NotNull
@Size(min = 2, max = 30, message="at least 3 chars" )
private String name;
```
&emsp;&emsp;前端按如下配置，使用`<sf:errors>`可将name属性的错误信息显示出来

```
<sf:form action="${flowExecutionUrl}&_eventId=submit" commandName="searchForm" method="post">
    Name: <sf:input path="name"/> <sf:errors path="name"></sf:errors><br/>
       <input type="submit" value="Submit">
</sf:form>
```
&emsp;&emsp;效果如下
![这里写图片描述](https://img-blog.csdn.net/20180909184901856?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3pvdTg5NDQ=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

 - 部分验证
JSR-303支持部分验证，通过验证组的方式，使用如下(我在验证该方式时是不行的，提示viwe-state标签不允许出现validation-hints属性)

```
@NotNull
@Size(min = 2, max = 30, groups = State1.class)
private String name;
```

```
<view-state id="state1" model="myModel" validation-hints="'group1,group2'">
```
&emsp;&emsp;对该方法不做详细解释，最好还是参考一下JSR-303再来看
## 自定义验证
JSR-303仅支持对Bean的验证，如非空，字符串长度等。我们经常需要自定义验证逻辑，有如下两种方式进行自定义

 - 一是在model类内部定义一个以`validate${stateId}(ValidationContext)`为签名的方法，在view提交时会自动调用该验证方法。stateId是view-state的id

```
// 官方示例
public class Booking {
    private Date checkinDate;
    private Date checkoutDate;
    ...

    public void validateEnterBookingDetails(ValidationContext context) {
        MessageContext messages = context.getMessageContext();
        if (checkinDate.before(today())) {
            messages.addMessage(new MessageBuilder().error().source("checkinDate").
                defaultText("Check in date must be a future date").build());
        } else if (!checkinDate.before(checkoutDate)) {
            messages.addMessage(new MessageBuilder().error().source("checkoutDate").
                defaultText("Check out date must be later than check in date").build());
        }
    }
}
```

 - 二是单独定义一个类，类名为`${model}Validator`，在其内部定义一个以`validate${stateId}(${model}, ValidationContext)`为签名的方法，然后将该类装载到Spring中。

```
// 官方示例
@Component
public class BookingValidator {
    public void validateEnterBookingDetails(Booking booking, ValidationContext context) {
        MessageContext messages = context.getMessageContext();
        if (booking.getCheckinDate().before(today())) {
            messages.addMessage(new MessageBuilder().error().source("checkinDate").
                defaultText("Check in date must be a future date").build());
        } else if (!booking.getCheckinDate().before(booking.getCheckoutDate())) {
            messages.addMessage(new MessageBuilder().error().source("checkoutDate").
                defaultText("Check out date must be later than check in date").build());
        }
    }
}
```
&emsp;&emsp;针对第二种情况也可以定义一个`validate(${model}, ValidationContext)`方法，这样无论在哪个view-state的view返回时，只要绑定了该moel，都会调用该验证方法。
&emsp;&emsp;当`validate(${model}, ValidationContext)`和validate`${stateId}(${model}, ValidationContext)`都存在时，会先调用后者，再调用前者。

## 多说两点

 - 失能验证
通过如下方式可以在局部使得验证失效

```
<view-state id="chooseAmenities" model="booking">
    <transition on="proceed" to="reviewBooking">
    <transition on="back" to="enterBookingDetails" validate="false" />
</view-state>
```
# 转移
在一个view-state中，可能发生各种转移

 -  转移之前执行操作
可以在转移之前执行特定的操作，如一个方法， 当方法返回false或者发生错误时，转移不会继续进行下去。而是重新渲染相应的部分

```
<transition on="submit" to="bookingConfirmed">
    <evaluate expression="bookingAction.makeBooking(booking, messageContext)" />
</transition>
```

 - 全局转移
定义全局有效的转移操作

```
<global-transitions>
    <transition on="login" to="login" />
    <transition on="logout" to="logout" />
</global-transitions>
```

 - 事件处理器
可以利用transition标签只响应事件，而不做任何跳转操作，从而作为事件处理器

```
<transition on="event">
    <!-- Handle event -->
</transition>
```

 - 局部渲染
利用`<render>`标签可以进行局部渲染，一般用于Ajax的局部刷新操作

```
<transition on="next">
    <evaluate expression="searchCriteria.nextPage()" />
    <render fragments="searchResultsFragment" />
</transition>
```
&emsp;&emsp;如上，当发生next事件时，首先执行翻页操作，然后重新刷新查询结果区域。fragment属性应该引用想要刷新的view的id,当刷新多个区域时，使用逗号隔开。
# view的回退控制
当我们从一个view跳转到另一个view时，通过浏览器的回退按钮，可以返回上一个view，我们可以对这个功能进行配置

 - 失能一个回退view，即当前view不能再下一个view上回退，回退到的是前一个view

```
<transition on="cancel" to="bookingCancelled" history="discard">
```

 - 失能所有回退view，即当前及之前所有view都是不能够被回退的。

```
<transition on="confirm" to="bookingConfirmed" history="invalidate">
```
##MessageContext
Spring web flow的MessageContext是用来记录在flow执行期间的信息的。而其中包含的信息都由MessageBuilder产生，可以手动添加，也可以由系统自动产生。

## 手动添加信息

 - 手动添加普通文本

```
MessageContext context = ...（这里一般是从上一级获取到context对象）
MessageBuilder builder = new MessageBuilder();
context.addMessage(builder.error().source("checkinDate")
    .defaultText("Check in date must be a future date").build());
context.addMessage(builder.warn().source("smoking")
    .defaultText("Smoking is bad for your health").build());
context.addMessage(builder.info()
    .defaultText("We have processed your reservation - thank you and enjoy your stay").build());
```

 - 添加Spring MessageSource得到的信息

```
MessageContext context = ...
MessageBuilder builder = new MessageBuilder();
context.addMessage(builder.error().source("checkinDate").code("checkinDate.notFuture").build());
context.addMessage(builder.warn().source("smoking").code("notHealthy")
    .resolvableArg("smoking").build());
context.addMessage(builder.info().code("reservationConfirmation").build());
```

 - 添加message bundle获取的信息
可以直接在view或flow中使用`resourceBundle`这个EL变量来获取资源文件中的内容。(这个需要在web-flow同目录下放置一个`message.properties`文件)

```
<input value="#{resourceBundle.reservationConfirmation}" />
```
## 系统自动产生信息
&emsp;&emsp;有多重情况下web-flow会自动生成message,其中一种重要的情况是当view-to-model验证失败时，生成规则是，首先到资源文件中查找key为`${model}l.${property}.${errCode}`的资源，如果找不到，则直接查找key为`${errCode}`的资源。
&emsp;&emsp; 举例：有model名为booking，验证其中的checkDate属性，当出现类型不匹配时，系统给出的错误代码为`typeMismatch`，则会在资源文件中查找如下key的资源
 `booking.checkDate.typeMismatch`  或 `typeMismatch`

# 附
下面大致列举一下Spring MVC会自动注册的转换器和格式化器(调用`ConversionService`的`toString()`方法)

```
@org.springframework.format.annotation.DateTimeFormat java.lang.Long -> java.lang.String: org.springframework.format.datetime.DateTimeFormatAnnotationFormatterFactory@3de4aaed,@org.springframework.format.annotation.NumberFormat java.lang.Long -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.DateTimeFormat java.time.LocalDate -> java.lang.String: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.time.LocalDate -> java.lang.String : org.springframework.format.datetime.standard.TemporalAccessorPrinter@1cb91eff
@org.springframework.format.annotation.DateTimeFormat java.time.LocalDateTime -> java.lang.String: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.time.LocalDateTime -> java.lang.String : org.springframework.format.datetime.standard.TemporalAccessorPrinter@2918eadb
@org.springframework.format.annotation.DateTimeFormat java.time.LocalTime -> java.lang.String: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.time.LocalTime -> java.lang.String : org.springframework.format.datetime.standard.TemporalAccessorPrinter@6d563cf9
@org.springframework.format.annotation.DateTimeFormat java.time.OffsetDateTime -> java.lang.String: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.time.OffsetDateTime -> java.lang.String : org.springframework.format.datetime.standard.TemporalAccessorPrinter@2f20d514
@org.springframework.format.annotation.DateTimeFormat java.time.OffsetTime -> java.lang.String: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.time.OffsetTime -> java.lang.String : org.springframework.format.datetime.standard.TemporalAccessorPrinter@19212c1c
@org.springframework.format.annotation.DateTimeFormat java.time.ZonedDateTime -> java.lang.String: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.time.ZonedDateTime -> java.lang.String : org.springframework.format.datetime.standard.TemporalAccessorPrinter@2e061032
@org.springframework.format.annotation.DateTimeFormat java.util.Calendar -> java.lang.String: org.springframework.format.datetime.DateTimeFormatAnnotationFormatterFactory@3de4aaed
@org.springframework.format.annotation.NumberFormat java.lang.Byte -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.NumberFormat java.lang.Double -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.NumberFormat java.lang.Float -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.NumberFormat java.lang.Integer -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.NumberFormat java.lang.Short -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.NumberFormat java.math.BigDecimal -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
@org.springframework.format.annotation.NumberFormat java.math.BigInteger -> java.lang.String: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.Boolean -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@839fe61
java.lang.Character -> java.lang.Number : org.springframework.core.convert.support.CharacterToNumberFactory@30f9d9cf
java.lang.Character -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@2062b73e
java.lang.Enum -> java.lang.Integer : org.springframework.core.convert.support.EnumToIntegerConverter@65bd69cd
java.lang.Enum -> java.lang.String : org.springframework.core.convert.support.EnumToStringConverter@24ccca42
java.lang.Integer -> java.lang.Enum : org.springframework.core.convert.support.IntegerToEnumConverterFactory@22b0410c
java.lang.Long -> java.time.Instant : org.springframework.format.datetime.standard.DateTimeConverters$LongToInstantConverter@36c61628
java.lang.Long -> java.util.Calendar : org.springframework.format.datetime.DateFormatterRegistrar$LongToCalendarConverter@7a56bca3,java.lang.Long -> java.util.Calendar : org.springframework.format.datetime.DateFormatterRegistrar$LongToCalendarConverter@32680fd1
java.lang.Long -> java.util.Date : org.springframework.format.datetime.DateFormatterRegistrar$LongToDateConverter@21f63842,java.lang.Long -> java.util.Date : org.springframework.format.datetime.DateFormatterRegistrar$LongToDateConverter@3ae27639
java.lang.Number -> java.lang.Character : org.springframework.core.convert.support.NumberToCharacterConverter@37dca65c
java.lang.Number -> java.lang.Number : org.springframework.core.convert.support.NumberToNumberConverterFactory@5ad62efe
java.lang.Number -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@5dbb5323
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.lang.Long: org.springframework.format.datetime.DateTimeFormatAnnotationFormatterFactory@3de4aaed,java.lang.String -> @org.springframework.format.annotation.NumberFormat java.lang.Long: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.time.LocalDate: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.lang.String -> java.time.LocalDate: org.springframework.format.datetime.standard.TemporalAccessorParser@1a482c16
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.time.LocalDateTime: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.lang.String -> java.time.LocalDateTime: org.springframework.format.datetime.standard.TemporalAccessorParser@726b4b72
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.time.LocalTime: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.lang.String -> java.time.LocalTime: org.springframework.format.datetime.standard.TemporalAccessorParser@7d025d62
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.time.OffsetDateTime: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.lang.String -> java.time.OffsetDateTime: org.springframework.format.datetime.standard.TemporalAccessorParser@7b82b59
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.time.OffsetTime: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.lang.String -> java.time.OffsetTime: org.springframework.format.datetime.standard.TemporalAccessorParser@5d6bf8bc
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.time.ZonedDateTime: org.springframework.format.datetime.standard.Jsr310DateTimeFormatAnnotationFormatterFactory@13c06099,java.lang.String -> java.time.ZonedDateTime: org.springframework.format.datetime.standard.TemporalAccessorParser@4100b1dd
java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.util.Calendar: org.springframework.format.datetime.DateTimeFormatAnnotationFormatterFactory@3de4aaed
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.lang.Byte: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.lang.Double: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.lang.Float: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.lang.Integer: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.lang.Short: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.math.BigDecimal: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> @org.springframework.format.annotation.NumberFormat java.math.BigInteger: org.springframework.format.number.NumberFormatAnnotationFormatterFactory@806d8b
java.lang.String -> java.lang.Boolean : org.springframework.core.convert.support.StringToBooleanConverter@3dd765a2
java.lang.String -> java.lang.Character : org.springframework.core.convert.support.StringToCharacterConverter@4b28d17b
java.lang.String -> java.lang.Enum : org.springframework.core.convert.support.StringToEnumConverterFactory@5a85577c
java.lang.String -> java.lang.Number : org.springframework.core.convert.support.StringToNumberConverterFactory@4a4bac52
java.lang.String -> java.nio.charset.Charset : org.springframework.core.convert.support.StringToCharsetConverter@77b7395f
java.lang.String -> java.time.Duration: org.springframework.format.datetime.standard.DurationFormatter@223f8ade
java.lang.String -> java.time.Instant: org.springframework.format.datetime.standard.InstantFormatter@744a1e70
java.lang.String -> java.time.MonthDay: org.springframework.format.datetime.standard.MonthDayFormatter@48e0bd1
java.lang.String -> java.time.Period: org.springframework.format.datetime.standard.PeriodFormatter@326e1143
java.lang.String -> java.time.YearMonth: org.springframework.format.datetime.standard.YearMonthFormatter@2013283d
java.lang.String -> java.util.Currency : org.springframework.core.convert.support.StringToCurrencyConverter@73d62889
java.lang.String -> java.util.Date: cn.floyd.pw.flow.converter.ApplicationConversionServiceFactoryBean$2@c01b01e,java.lang.String -> java.util.Date : cn.floyd.pw.flow.converter.ApplicationConversionServiceFactoryBean$1@bda7edf,java.lang.String -> @org.springframework.format.annotation.DateTimeFormat java.util.Date: org.springframework.format.datetime.DateTimeFormatAnnotationFormatterFactory@3de4aaed
java.lang.String -> java.util.Locale : org.springframework.core.convert.support.StringToLocaleConverter@15f3ecb1
java.lang.String -> java.util.Properties : org.springframework.core.convert.support.StringToPropertiesConverter@1734f8d8
java.lang.String -> java.util.TimeZone : org.springframework.core.convert.support.StringToTimeZoneConverter@219e655b
java.lang.String -> java.util.UUID : org.springframework.core.convert.support.StringToUUIDConverter@7a2a1350
java.nio.charset.Charset -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@79cac565
java.time.Duration -> java.lang.String : org.springframework.format.datetime.standard.DurationFormatter@223f8ade
java.time.Instant -> java.lang.Long : org.springframework.format.datetime.standard.DateTimeConverters$InstantToLongConverter@bbf9adc
java.time.Instant -> java.lang.String : org.springframework.format.datetime.standard.InstantFormatter@744a1e70
java.time.LocalDateTime -> java.time.LocalDate : org.springframework.format.datetime.standard.DateTimeConverters$LocalDateTimeToLocalDateConverter@224c05f6
java.time.LocalDateTime -> java.time.LocalTime : org.springframework.format.datetime.standard.DateTimeConverters$LocalDateTimeToLocalTimeConverter@bb6fc38
java.time.MonthDay -> java.lang.String : org.springframework.format.datetime.standard.MonthDayFormatter@48e0bd1
java.time.OffsetDateTime -> java.time.Instant : org.springframework.format.datetime.standard.DateTimeConverters$OffsetDateTimeToInstantConverter@7e4083f
java.time.OffsetDateTime -> java.time.LocalDate : org.springframework.format.datetime.standard.DateTimeConverters$OffsetDateTimeToLocalDateConverter@1e188fca
java.time.OffsetDateTime -> java.time.LocalDateTime : org.springframework.format.datetime.standard.DateTimeConverters$OffsetDateTimeToLocalDateTimeConverter@79b804b1
java.time.OffsetDateTime -> java.time.LocalTime : org.springframework.format.datetime.standard.DateTimeConverters$OffsetDateTimeToLocalTimeConverter@178638ba
java.time.OffsetDateTime -> java.time.ZonedDateTime : org.springframework.format.datetime.standard.DateTimeConverters$OffsetDateTimeToZonedDateTimeConverter@5dd8aa91
java.time.Period -> java.lang.String : org.springframework.format.datetime.standard.PeriodFormatter@326e1143
java.time.YearMonth -> java.lang.String : org.springframework.format.datetime.standard.YearMonthFormatter@2013283d
java.time.ZoneId -> java.util.TimeZone : org.springframework.core.convert.support.ZoneIdToTimeZoneConverter@375fe360
java.time.ZonedDateTime -> java.time.Instant : org.springframework.format.datetime.standard.DateTimeConverters$ZonedDateTimeToInstantConverter@5b6ff572
java.time.ZonedDateTime -> java.time.LocalDate : org.springframework.format.datetime.standard.DateTimeConverters$ZonedDateTimeToLocalDateConverter@44caea49
java.time.ZonedDateTime -> java.time.LocalDateTime : org.springframework.format.datetime.standard.DateTimeConverters$ZonedDateTimeToLocalDateTimeConverter@748fb300
java.time.ZonedDateTime -> java.time.LocalTime : org.springframework.format.datetime.standard.DateTimeConverters$ZonedDateTimeToLocalTimeConverter@362e6386
java.time.ZonedDateTime -> java.time.OffsetDateTime : org.springframework.format.datetime.standard.DateTimeConverters$ZonedDateTimeToOffsetDateTimeConverter@4864c695
java.time.ZonedDateTime -> java.util.Calendar : org.springframework.core.convert.support.ZonedDateTimeToCalendarConverter@53757723
java.util.Calendar -> java.lang.Long : org.springframework.format.datetime.DateFormatterRegistrar$CalendarToLongConverter@3effd16f,java.util.Calendar -> java.lang.Long : org.springframework.format.datetime.DateFormatterRegistrar$CalendarToLongConverter@6625da72
java.util.Calendar -> java.time.Instant : org.springframework.format.datetime.standard.DateTimeConverters$CalendarToInstantConverter@3ea63a04
java.util.Calendar -> java.time.LocalDate : org.springframework.format.datetime.standard.DateTimeConverters$CalendarToLocalDateConverter@311b3b
java.util.Calendar -> java.time.LocalDateTime : org.springframework.format.datetime.standard.DateTimeConverters$CalendarToLocalDateTimeConverter@b827cbe
java.util.Calendar -> java.time.LocalTime : org.springframework.format.datetime.standard.DateTimeConverters$CalendarToLocalTimeConverter@27334ef2
java.util.Calendar -> java.time.OffsetDateTime : org.springframework.format.datetime.standard.DateTimeConverters$CalendarToOffsetDateTimeConverter@18a5b69c
java.util.Calendar -> java.time.ZonedDateTime : org.springframework.format.datetime.standard.DateTimeConverters$CalendarToZonedDateTimeConverter@2181b391
java.util.Calendar -> java.util.Date : org.springframework.format.datetime.DateFormatterRegistrar$CalendarToDateConverter@43409a9e,java.util.Calendar -> java.util.Date : org.springframework.format.datetime.DateFormatterRegistrar$CalendarToDateConverter@25a7d510
java.util.Currency -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@59874f76
java.util.Date -> java.lang.Long : org.springframework.format.datetime.DateFormatterRegistrar$DateToLongConverter@2d72afcb,java.util.Date -> java.lang.Long : org.springframework.format.datetime.DateFormatterRegistrar$DateToLongConverter@60b0c620
java.util.Date -> java.lang.String : cn.floyd.pw.flow.converter.ApplicationConversionServiceFactoryBean$2@c01b01e,@org.springframework.format.annotation.DateTimeFormat java.util.Date -> java.lang.String: org.springframework.format.datetime.DateTimeFormatAnnotationFormatterFactory@3de4aaed
java.util.Date -> java.util.Calendar : org.springframework.format.datetime.DateFormatterRegistrar$DateToCalendarConverter@635f0388,java.util.Date -> java.util.Calendar : org.springframework.format.datetime.DateFormatterRegistrar$DateToCalendarConverter@7b746ecc
java.util.Locale -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@572faa97
java.util.Properties -> java.lang.String : org.springframework.core.convert.support.PropertiesToStringConverter@387ae6b6
java.util.UUID -> java.lang.String : org.springframework.core.convert.support.ObjectToStringConverter@19b50f9c
```