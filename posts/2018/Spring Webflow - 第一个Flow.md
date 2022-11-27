---
created_at: 2018-09-06 23:00:00.0
updated_at: 2021-02-16 23:27:41.378
slug: spring-webflow-example
tags: 
- Spring
- Spring Webflow
---

> 在学习每一门新语言时，第一个程序往往是Hello World。这里我们写一个非常简单的flow，使用常用标签，在深入讲解之前有一个感官上的认识

# 需求说明
假设有如下简单流程：要求程序启动，显式输入界面，用户输入信息后，点击提交按钮，后台查询数据库，然后显式查询结果界面，中间任何步骤出错，都重新返回输入界面，并显示错误信息。流程大体如下。
<!-- more -->
![需求流程图](20180906212548121.png)
# 需求分析
将上述需求分解：流程启动时，初始化输入界面的信息，渲染输入页面，用户点击提交按钮，后台验证输入信息的格式是否正确，验证失败则返回输入界面，验证成功则进行下一步查询数据库操作，查询完成后跳转到结果页面进行显示，流程结束。(请忽略如下流程中判断图示不标准的错误)
![逻辑流程图](20180906213226568.png)
# 运行前的基本配置
首先需要将FlowRegistry，FlowExecutor，FlowHandlerAdapter，FlowHandlerMapping等项配置好。本文的采用了[Spring Web Flow 学习 —— 配置 - 001](https://www.zouguodong.top/2018/09/05/Spring%20Webflow%20-%20%E9%85%8D%E7%BD%AE/)的配置。
# Flow文件
如下配置文件讲解: 

 - 流程启动时指定flowController的performInit()方法，并返回一个ModelMap类型的对象，分配flowScope作用域下的InitMap变量，将返回的对象赋予该变量；
 - 渲染/WEB-INF/jsp/flow/view/input.jsp，并将input界面中上传的参数与searchForm进行绑定，当触发submit事件时，跳转到validate状态
 - validate状态中，执行flowController的performValidate(searchForm)方法，返回success时跳转到result状态，返回fail时跳转到init状态，重新渲染input.jsp。
 - result状态，渲染result.jsp，渲染前，首先指定flowController的performSearch(searchForm)方法，该方法返回一个modelMap并分配给flashScope范围内的modelMap变量。在result界面，无论点击任何按键，只要是向flow在此提交请求，都会跳转到end状态，
 - end状态, 重定向到spring首页
 至此，流程结束。

```
<?xml version="1.0" encoding="UTF-8"?>
<!-- 这是web flow 2.4.5的根标签形式，2.5.0并不一样 -->
<flow xmlns="http://www.springframework.org/schema/webflow"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.springframework.org/schema/webflow
                          http://www.springframework.org/schema/webflow/spring-webflow-2.0.xsd">
    
    <var name="searchForm" class="cn.floyd.pw.flow.SearchForm"/>
    
    <on-start>
        <evaluate expression="flowController.performInit()" 
                result="flowScope.InitMap" 
                result-type="org.springframework.ui.ModelMap"/>
    </on-start>
    
    <view-state id="init" view="flow/view/input" model="searchForm">
        <binder>
            <binding property="name"/>
            <binding property="gender"/>
        </binder>
        <transition on="submit" to="validate"/>
    </view-state>

    <action-state id="validate">
        <evaluate  expression="flowController.performValidate(searchForm)"/>
        <transition on="success" to="result"/>
        <transition on="fail" to="input"/>
    </action-state>

    <view-state id="result" view="flow/view/result">
        <on-render>
            <evaluate expression="flowController.performSearch(searchForm)" result="flashScope.modelMap"/>
        </on-render>
        <transition to="end"/>
    </view-state>
    
    <end-state id="end" view="externalRedirect:http://springframework.org"/>
</flow>
```
看完上面的描述，想必刚接触web flow的人是一脸懵逼
![这里写图片描述](20180906215538433.jpeg)
解释几个概念就好了。

 - 状态：web flow将一个步骤称作一个状态(state)，有专门渲染view的view-state，也有只执行操作的action-state
 - 变量：web flow是以xml的形式进行编程的，可以在该xml上下文中定义变量，该变量可以在flow上下文以及flow渲染的jsp文件(使用EL表达式调用)，调用的方法中(作为参数传入)使用。定义变量的方式主要有两种，一是通过`<var>`标签显式定义，二是在`<evaluate>`标签的`result`属性中定义(此时同时完成了分配变量和变量赋值两个操作)
 - 变量作用域：规定了变量的作用范围，常见的有flashScope(当前状态有效)，flowScope(当前flow有效)等
 - 事件：从一个状态到另一个状态，一般需要进行触发，而进行触发的就是事件。事件可能由view触发，也可能由方法触发，我们不用真的去定义一个事件对象。当view-state中的view返回的请求中带有_eventId的参数时，其值会被自动转换成Event，当action-state中调用的方法返回字符串时，该字符串也会被自动转换成Event
 - 模型绑定：当view需要提交参数时，可以采用模型绑定的形式，web flow会自动将对应参数绑定到我们的model中，并且还可以自定义验证和转换规则。

# 相关其它文件
## FlowController
按照顺序列出相关文件，`<evaluate>`标签的`expression`属性可以通过Spring EL表达式的形式直接访问Spring管理的bean的方法或属性，也可以访问flow上下文环境中的对象的方法或属性。其中主要方法讲解如下：

 - `performInit()`初始化下拉选中的初始值，返回modelMap对象，该对象被赋值给flow中的InitMap变量
 - `performValidate(SearchForm form)`将SearchForm对象传入，用于验证输入的值，这里假设全都验证通过，返回的"success"会被映射成Event
 - `performSearch(SearchForm form)`根据传入form中的参数进行数据查找，这里假设已经查找完毕，并将数据放入一个ModelMap，赋值给flow中的modelMap变量

该类是Spring管理的一个bean，
```
@Controller("flowController")
public class FlowController implements Serializable{
    
    private static final long serialVersionUID = -4439633424434338888L;

    public ModelMap performInit() {
        ModelMap model = new ModelMap();
        model.addAttribute("gender", new String[] {"Man", "Woman"});
        return model;
    }
    
    public String performValidate(SearchForm form) {
        // assume we have pass the validation
        return "success";
    }
    
    public ModelMap performSearch(SearchForm form) {
        // assume we have finished the search process, and got the search result
        ModelMap model = new ModelMap();
        model.addAttribute("name", form.getName());
        model.addAttribute("gender", form.getGender());
        model.addAttribute("age", 25);
        model.addAttribute("profession", "Programmer");
        model.addAttribute("hobbies", new String[] {"Basktball", "Football"});
        
        return model;
    }
}
```
## input.jsp
输入界面，将`InitMap`中的值通过EL表达式渲染到下拉选中。通过`_eventId=submit`的GET参数方式触发submit事件。`${flowExecutionUrl}`是flow中自管理变量，访问它才能使得流程继续下去

 - 尤其需要注意的一个点是，在声明form时，一定要使用spring提供的taglib，否则会出现无法跳转到下一个state，无限回到第一个state的情况。
```
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="sf" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Input page</title>
	</head>
	<body>
		<!-- commandName 声明该form需要绑定的model，与flow.xml中<view-state>声明的model是一个东西 -->
	   <sf:form action="${flowExecutionUrl}&_eventId=submit" commandName="searchForm" method="post">
	       Name: <sf:input path="name"/><br/>
           gender:
           <sf:select path="gender">
               <sf:option value="">- Please Select -</sf:option>
               <c:forEach items="${InitMap.gender }" var="gender">
                   <sf:option value="${gender }">${gender }</sf:option>
               </c:forEach>
           </sf:select>
           <input type="submit" value="Submit">
	   </sf:form>
	</body>
</html>
```

## SearchForm
form，与input.jsp中的form参数对应，注意必须要实现序列化接口。
```
public class SearchForm implements Serializable {

    private String name;
    private String gender;

    ... ...
}

```

## result.jsp
将flow中的`modelMap`变量渲染到页面中
```
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
		<title>Result Page</title>
	</head>
	<body>
	    Name: ${modelMap.name } <br/>
	    Gender: ${modelMap.gender } <br/>
	    Age: ${modelMap.age } <br/>
	    profession: ${modelMap.profession } <br/>
	    hobbies: 
        <c:forEach items="${modelMap.hobbies }" var="hobby">
            ${hobby } &ensp;
        </c:forEach>
        <br/>
	</body>
</html>
```

# 调试中遇到的坑

 - 现象
点击form的submit按钮，无法跳转到下一个state，始终重新渲染input界面；定义一个`<a href="${flowExecutionUrl}&_eventId=submit">`标签，能够正常跳转到下一个state
 - 原因
使用了原生的html标签`<form>`进行表单的声明，导致web flow无法继续工作，改用Spring标签即可。
Web Flow无法工作的具体原理尚不明晰，我是在参考公司已有项目时发现这个问题的。
 - 解决方案
使用Spring官方提供的taglib进行form及其属性的声明。