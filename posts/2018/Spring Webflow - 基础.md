---
created_at: 2018-09-07 21:33:00.0
updated_at: 2021-02-16 23:27:34.637
slug: spring-webflow-foundation
tags: 
- Spring
- Spring Webflow
---

# 基础

Web Flow将一个流程分为若干个状态(可以理解为步骤)，每个流程由若干个状态组成，通过特性的方式在步骤之间进行跳转，协同完成整个流程。
<!--more-->
常用标签如下

 - `<view-state>` - 视图状态，用于渲染视图
 - `<action-state>` - 动作状态，用于专门执行操作
 - `<transition>` - 转移，用于状态间转移，转移由事件触发
 - `<end-state>` - 结束状态，流程的最后一个状态
 - `<evaluate>` - 执行具体操作，是上述各个标签的子标签，用于所有需要执行操作的位置
####view-state
如下声明了视图状态，在该状态会绘制一个视图，view的解析依赖于具体的视图解析器

```
<view-state id="result" view="flow/view/result"/>
```
可以不指定view属性，此时，会在flow文件同目录下寻找和id相同文件名的视图文件进行渲染

```
<view-state id="enterBookingDetails" />
```
可以在声明同时指定model属性，该属性配合前端spring taglib可将表单数据绑定到model指定的bean中

```
<view-state id="init" view="flow/view/input" model="searchForm">
    <binder>
        <binding property="name"/>
        <binding property="gender"/>
    </binder>
    <transition on="submit" to="validate"/>
</view-state>
...
<!-- 对应的JSP代码 -->
...
<sf:form action="${flowExecutionUrl}&_eventId=submit" commandName="searchForm" method="post">
    Name: <sf:input path="name"/><br/>
    gender:
       <sf:select path="gender">
           <sf:option value="">- Please Select -</sf:option>
       </sf:select>
       <input type="submit" value="Submit">
</sf:form>
...
```

## action-state
action-state将单独一个操作设置为一个状态，除了不能渲染视图外，其它功能和view-state基本一致

```
<action-state id="validate">
    <evaluate  expression="flowController.performValidate(searchForm)"/>
    <transition on="success" to="result"/>
    <transition on="fail" to="input"/>
</action-state>
```

## transition
transaction可以根据事件id从一个state跳转到另一个state，如下，当发生submit时间时，将跳转到id为reviewBooking的state

```
<view-state id="enterBookingDetails">
  		<transition on="submit" to="reviewBooking" />
</view-state>
```
事件id定义的方式比较特殊，最典型的从view中触发事件的方式：

```
<!-- 该超链接被点击时，会触发submit事件 -->
<a href="${flowExecutionUrl}"&_eventId="submit">Submit</a>
```
transition还可以作为<action-state>的子元素，此时on中的内容就是EL表达式，或者执行方法所返回的字符串

```
<action-state id="validate">
    <evaluate  expression="flowController.performValidate(searchForm)" result="flashScope.resultMap"/>
    <!-- EL表达式方式,去resultMap对象中errors值得hasErrors()方法，成立时跳转 -->
    <transition on="resultMap.errors.hasErrors() == true" to="result"/>
</action-state>
... ...
<action-state id="validate">
    <evaluate  expression="flowController.performValidate(searchForm)"/>
    <!-- 方法返回事件id -->
    <transition on="success" to="result"/>
    <transition on="fail" to="input"/>
</action-state>
```

## view中触发事件的几种方式

 - 使用submit按钮

```
<input type="submit" name="_eventId_proceed" value="Proceed" />
```
原理：当web-flow发现请求参数中有以_eventId_字符串开头的参数时，会把该字符串中剩余字符串当做eventId。该方法可用于一次性触发多个事件

 - 使用hidden域

```
<input type="hidden" name="_eventId" value="proceed" />
```
原理：web-flow检测到请求参数中有名为_eventId的参数时，会将其值作为eventId进行触发

 - 使用url参数

```
<a href="${flowExecutionUrl}&_eventId=cancel">Cancel</a>
```
原理同上

 - web-flow检测eventId的逻辑
首先检查有没有_eventId的参数，如果没有，检查有没有以_eventId_开头的参数名，都没有时，则没有事件会被触发。
####end-tate
定义流程结束状态

 - 当该流程是子流程时，会接着下面的流程继续进行，<end-state>的id属性将会作为event id
 - 当该流程添加了view时，该view会被渲染。还可以添加属性，使得进行重定向之类的
 - 当不是子流程也没有指定view，则该流程结束，并且重新开启一个新的流程实例
####evaluate
Web Flow允许我们在如下几个切入点执行我们自己的业务逻辑，而执行业务逻辑使用`<evaluate>`标签。**该标签可以调用所用Spring中管理的bean和flow中声明的变量的方法**。

 - flow开始 - 对应`<on-start>`标签，定义在根标签`<flow>`下

```
<on-start>
	<!-- 仅调用方法 -->
    <evaluate expression="flowController.performInit()"/>
</on-start>
```

 - state进入时 - 对应`<on-entry>`标签，可定义在所有`state`标签下

```
<view-state id="init" view="flow/view/input">
	<on-entry>
		<!-- 调用方法，并将方法返回的对象存在flow变量modelMap中 -->
		<evaluate expression="flowController.performInit()" result="flashScope.modelMap"/>
	</on-entry>
    ... ...
</view-state>
```

 - view渲染时 - 对应`<on-render>`标签，定义在`<view-state>`下

```
<view-state id="init" view="flow/view/input">
	<on-render>
		<!-- 调用方法，并将方法返回的对象转型成目标类型，然后存储在flow变量modelMap中 -->
		<evaluate expression="flowController.performInit()" result="flashScope.modelMap" resultType="java.util.Map"/>
	</on-render>
    ... ...
</view-state>
```

 - transition执行时 - 对应`<transition>`标签

```
<view-state id="init" view="flow/view/input">
	<transition on="submit" to"validate">
		<evaluate expression="flowController.performTransition()"/>
	</transition>
</view-state>
```

 - state退出时 - 对应`<on-entry>`标签，可定义在所有state标签下

```
<action-state id="validate">
    ... ...
    <on-exit>
		<evaluate expression="flowController.performExit()"/>
	</on-exit>
</action-state>
```

 - flow结束时 - 对应`<on-start>`标签，定义在根标签`<flow>`下

```
<on-end>
    <evaluate expression="flowController.performEnd()"/>
</on-end>
```
# 进阶
## 变量

可以在流程中定义多个变量，这些变量将在流程开始被分配。被声明变量的类必须实现serializable，因为在两个state之间，变量需要被保存。

```
<var name="searchCriteria" class="com.mycompany.myapp.hotels.search.SearchCriteria"/>
```
####变量的分配方式
 - 直接分配

```
<var name="searchCriteria" class="com.mycompany.myapp.hotels.search.SearchCriteria"/>
```

 - 赋值的时候分配

```
<!-- 创建InitMap对象，并将方法返回的对象赋值给InitMap -->
<evaluate expression="flowController.performInit()" result="flowScope.InitMap" />
```

## 变量的使用方法

 - jsp中使用
使用jsp中的el表达式访问flow中声明的变量，如`${modelMap.name}`，访问了flow变量modelMap的name属性
 - flow文件中使用
直接使用Spring EL表达式进行访问

```
<transition on="modelMap.name == null" to="result"/>
```

 - 方法中使用
将变量传给调用方法，即可在方法中使用

```
<evaluate expression="flowController.performSearch(modelMap)"/>
```

## 变量作用域
 - `flowScope`：流程开始时分配，流程结束时销毁
 - `viewScope`：在`<view-state>`进入时创建，退出时销毁
 - `requestScope`：当流程被调用时分配，流程返回时销毁。比flowScope作用域稍微大一点
 - `flashScope`：在流程开始时分配，流程结束时销毁，但是在每一个view渲染后都会被清零
 - `conversation Scope`：最顶层的流程开始时分配，最顶层的流程结束时销毁。该作用域的变量是存储在Session中的。