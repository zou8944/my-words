---
created_at: 2018-09-08 11:00:00.0
updated_at: 2021-02-16 23:27:25.195
slug: spring-webflow-action
tags: 
- Spring
- Spring Webflow
- Spring Webflow Action
---

# action-state
## 简单使用
该状态只执行操作，然后根据操作的结果转移到其他state。可以有多个操作，他们依次执行

```
<action-state id="moreAnswersNeeded">
	<evaluate expression="interview.moreAnswersNeeded()" />
	<transition on="yes" to="answerQuestions" />
	<transition on="no" to="finish" />
</action-state>
```
## 输出
在action-state中调用普通java对象的方法，这些方法返回的只是一般的值，但是transition标签需要Event来触发，因此web-flow会将这个普通返回值转换为Event对象，具体转换情况如下:

```
方法返回值类型			映射出来的EventId
java.lang.String		直接以字符串的值作为id
java.lang.Boolean		yes (for true), no (for false)
java.lang.Enum			the Enum name
any other type	    	success
```
## action-state的操作
action-state可以有三种方式进行执行操作

 - 调用POJO

```
<evaluate expression="pojoAction.method(flowRequestContext)" />
```

```
public class PojoAction {
	public String method(RequestContext context) {
		...
	}
}
```

 - 实现Action接口，直接调用该action

```
<evaluate expression="customAction" />
```

```
public class CustomAction implements Action {
	public Event execute(RequestContext context) {
		...
	}
}
```

 - 实现MultiAction接口，可以定义多个一连串的方法

```
<evaluate expression="multiAction.actionMethod1" />
```

```
public class CustomMultiAction extends MultiAction {
	public Event actionMethod1(RequestContext context) {
		...
	}

	public Event actionMethod2(RequestContext context) {
		...
	}
	...
}
```
## action的异常处理

 - POJO类action的处理方式
发生异常时，返回相应的字符串，会映射成Event，在transition中响应就可以了，和普通方法正常返回一样
 - MultiAction的处理方式
发生异常时，返回Event对象

```
public class BookingAction extends MultiAction {
	public Event makeBooking(RequestContext context) {
		   try {
			   Booking booking = (Booking) context.getFlowScope().get("booking");
			   BookingConfirmation confirmation = bookingService.make(booking);
			   context.getFlowScope().put("confirmation", confirmation);
			   return success();
		   } catch (RoomNotAvailableException e) {
			   context.getMessageContext().addMessage(new MessageBuilder().error().
				   .defaultText("No room is available at this hotel").build());
			   return error();
		   }
	}
}
```
 - 使用`exception-handler`属性，定义异常处理器

## decision-state
decision-state是action-state的一种简单替代，在if/else情况时比较好用

```
<decision-state id="moreAnswersNeeded">
	<if test="interview.moreAnswersNeeded()" then="answerQuestions" else="finish" />
</decision-state>
```
## action相关标签

1) `<on-start>`	flow开始时执行
2) `<on-entry>`	state进入时执行
3) `<on-exit>`	state退出时执行
4) `<on-end>`	flow结束时执行
5) `<on-render>`view-state中使用，渲染前执行
6) `<transition>`	在转移前执行
## 命名的action
如下展示了一个action-state下多个操作执行，为每个操作命名，第二个操作成功后进行转移操作

```
<action-state id="doTwoThings">
	<evaluate expression="service.thingOne()">
		<attribute name="name" value="thingOne" />
	</evaluate>
	<evaluate expression="service.thingTwo()">
		<attribute name="name" value="thingTwo" />
	</evaluate>
	<transition on="thingTwo.success" to="showResults" />
</action-state>
```
# 向客户端发送流信息
## 应用场景
客户端请求一个图片文件，此时我们需要直接操作httpresponse进行图片的响应，而不是渲染view。
## 解决方案
通过ExternalContext获取HttpResponse，将图片写入，然后操作ExternalContext对象记录response完成，这样web-flow就不会再渲染view，而是直接返回给浏览器

```
public class PrintBoardingPassAction extends AbstractAction {

    @Override
    protected Event doExecute(RequestContext context) throws Exception {
        HttpServletResponse response = (HttpServletResponse)context.getExternalContext().getNativeResponse();
        OutputStream os = response.getOutputStream();
        // 在这里操作os，写入流数据
        os.close();
        context.getExternalContext().recordResponseComplete();
        return success();
    }

}
```