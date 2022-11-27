---
created_at: 2018-09-08 20:00:00.0
updated_at: 2021-02-16 23:27:11.236
slug: spring-webflow-el-expression
tags: 
- Spring
- Spring Webflow
- Spring Webflow EL
---

> 1. 文章中内容并没有全部验证，仅作为参考
> 2. 上下文一起看，才能明白其中的意思

# Web Flow中EL表达式作用
web-flow使用EL表达式访问flow的model和调用方法。在web-flow中EL表达式主要有如下四种用途

 - 访问客户端(浏览器)数据，比如request的parameter
 - 访问web-flow的RequestContex，比如flowScope和currentEvent等
 - 调用Spring管理的bean的方法
 - 解析表达式(相对于普通表达式)可以解析注入子流程id，view的名称，
##EL表达式分类
web-flow中EL表达式按照按使用形式分为两类

 - 标准表达式
不需要加#{}，直接按照一般程序一样写就行了，如果硬要加#{}，则会报错

```
// 调用searchCriteria对象的nextPage()方法
// searchCriteria对象可以是Spring中的一个bean，也可以是flow上下文中的一个变量
<evaluate expression="searchCriteria.nextPage()" />
```

 - 模板表达式
需要加#{}，这种表达式允许将常量和表达式写在一起，如下这种，最后的view名称是拼出来的

```
<view-state id="error" view="error-#{externalContext.locale}.xhtml" />
```
# Web Flow支持的EL表达式
Web Flow支持spring EL表达式，Unified表达式，以及OGNL表达式

 - Spring EL
从web-flow 2.1开始就使用了Spring EL表达式，该表达式在Spring的全系列产品中都可以使用。使用它只需要在类路径下包含一个单独的jar包`org.springframework.expression`。 并且如果以前使用的EL表达式或者ognl的表达式，还需要将他们的包去除。
 - Unified EL
在we-flow 2.0时期默认使用的是统一EL表达式，`org.jboss.el`提供，该包还需要j2ee提供的`el-api`(一般的容器都会自动提供)。虽然目前版本的Spring EL表达式是默认和推荐使用的，但也可以手动更换为Unified EL表达式。只需加上如下配置即可

```
// 该配置方法在前面讲配置时给过示例
<webflow:flow-builder-services expression-parser="expressionParser"/>
<bean id="expressionParser" class="org.springframework.webflow.expression.el.WebFlowELExpressionParser">
	<constructor-arg>
		  <bean class="org.jboss.el.ExpressionFactoryImpl" />
	</constructor-arg>
</bean>
```

 - OGNL
2.4及以后的版本中，已经非常不推荐使用OGNL表达式了。那还是在web-flow 1.0时代标配的是OGNL表达式，如果硬要使用OGNL表达式，还是可以配置，方法请参考[教程](https://docs.spring.io/spring-webflow/docs/2.4.5.RELEASE/reference/html/el.html#el-ognl)
##EL表达式迁移(Unified EL -> Spring EL)
从Unified EL表达式和OGNL表达式迁移到Spring EL表达式需要注意以下几点

 - EL表达式的符号从${ }变化成了#{ }
 - 针对current Event的比较由`#{currentEvent == 'submit'}` 要换成 `#{currentEvent.id == 'submit'}`
 - 直接解析属性如`#{currentUser.name}` 可能造成空指针异常，以前的检查方式是：`#{currentUser != null ? currentUser.name : null}` ， 目前更好的方式：`#{currentUser?.name}`

更加详细的EL相关内容，看[这里](http://static.springsource.org/spring/docs/3.0.x/spring-framework-reference/html/expressions.html#expressions-language-ref)
# 一些内建的Spring EL变量

内建代表系统自动创建并管理，用户可以直接通过EL表达式访问
## 重要原则

只有当分配一个新的变量时才会用到默认存在的作用域变量(flowScope, viewScope, requestScope, etc), 后面使用时就不需要指定作用域变量了。

```
<!-- 声明modelMap变量，必须显式指定作用域 -->
<evaluate expression="flowController.performSearch(searchForm)" result="flashScope.modelMap"/>
... ...
<!-- 使用modelMap变量不用指定作用域 -->
<evaluate expression="flowController.performResult(modelMap)"/>
```
## 作用域
前面在讲变量时已经讲过作用域(看[这里](https://blog.csdn.net/zou8944/article/details/82502430))，这里提一下，不要忘了。

## 内建变量穷举

 - requestParameters
获取客户端的请求参数
 - currentEvent
可以获取当前的Event对象
 - currentUser
获取当前被授权的用户，即Principal对象
 - messageContext
可以访问当前的上下文，包括错误和成功的信息，详见MessageContext的javaDoc
 - resourceBundle
访问资源文件
 - flowRequestContext
访问当前flow的RequestContext对象 ，它是当前flow的请求信息对象，详见RequestContext的javaDoc
 - flowExecutionContext
访问FlowExecutionContext对象，存储了当前flow的状态
 - flowExecutionUrl
访问当前view的相对路径，可以在view-state中指定的jsp中进行使用
 - externalContext
可以获取客户端的环境信息，包括sessino属性，详见ExternalContext JavaDoc
##Spring EL查找变量的逻辑
当使用flow中声明的变量时，并不需要指定作用域，web flow会自动从各作用域，按照如下顺序进行查找，如果找不到，则报`EvaluationException`异常

```
requestScope -> flashScope -> viewScope -> flowScope -> conversationScope
```