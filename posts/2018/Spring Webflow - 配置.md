---
created_at: 2018-09-05 22:33:00.0
updated_at: 2021-02-16 23:27:46.205
slug: spring-webflow-configuration
tags: 
- Spring
- Spring Webflow
- Spring Webflow Configuration
---

>  1. 本文基于Spring Web Flow 2.4.5，其它版本配置方式可能略有不同，请参考相应版本的[官方文档](https://projects.spring.io/spring-webflow/)
>  2. Maven依赖
maven库查询推荐地址：http://mvnrepository.com/
```
<dependency>
    <groupId>org.springframework.webflow</groupId>
    <artifactId>spring-webflow</artifactId>
    <version>2.4.5.RELEASE</version>
</dependency>
```
# Web Flow嵌入到Spring MVC工作流简介
请求被DispatcherServlet拦截 -> 分发flow进行处理，返回view -> viewResolver解析 -> 返回请求

---
# 配置项预览
<ul>
	<li>FlowRegistry：必须，注册流程，指明流程配置文件所在位置；指定流程id(用于请求访问标识)；指定流程属性；此外还可以传入FlowBuilderServices进行更多个性化配置</li>
	<li>FlowBuilderServices：必须，用于设定流程配置文件中EL表达式的解析器、form属性绑定时的转换器、view-state的view解析器等，很重要</li>
	<li>FlowExecutor：必须，用于执行流程，可指定执行监听器(可选，常用于流程安全和持久化)</li>
	<li>FlowHandlerAdapter：必须，用于适配Spring MVC，配置时传入FlowExecutor</li>
	<li>FlowHandlerMapping：必须，用于将请求映射到对应的flow，配置时传入FlowRegistry</li>
</ul>

---
# 配置I - 注册流程 - FlowRegistry
FlowRegistry用于注册流程实例，指定流程位置和流程id，并可自定义流程创建相关内容

## 注册flow的各种方式

- 直接指定流程位置
默认情况下，web-flow的id为其文件名减去后缀名，如下配置的id为booking。指定了基地址或使用了通配符时除外。
```
<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
// 注册了一个路径为/WEB-INF/flows/booking/booking.xml的流程，其余为默认配置。
```
- 自定义id

```
<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" id="bookHotel" />
```

-  定义流程属性
如下定义了一个带有属性caption，其值为"Books a hotel"的流程。属性的使用方法暂时不了解
```
<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml">
    <webflow:flow-definition-attributes>
        <webflow:attribute name="caption" value="Books a hotel" />
    </webflow:flow-definition-attributes>
</webflow:flow-location>
```

 - 使用通配定义流程位置
**使用该方法并没有正确实验出id**，这点作为参考
```
<webflow:flow-location-pattern value="/WEB-INF/flows/**/*-flow.xml" />
```

- 使用基地址
使用基地址的flow的id为其path属性减去文件名，如下配置的id为/hotels/booking；如果path中没有路径信息，只有文件名，则id为文件名减去后缀。
```
<webflow:flow-registry id="flowRegistry" base-path="/WEB-INF">
    <webflow:flow-location path="/hotels/booking/booking.xml" />
</webflow:flow-registry>
```
## flow id属性总结
1.  id的作用
id用于请求定位到某个确切的flow，如当请求路径为http://localhost:8090/Floyd/search-flow，其中Floyd是项目名，如果有id为search-flow的flow存在，则会访问该flow
2. id的定义
 - 没有基地址或通配符时，flow的id为文件名减去后缀，如`<webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />`这里的id为booking
 - 有基地址时，id为path的值减去文件名，如基地址为`/WEB-INF`， path=`/flows/booking/booking.xml`时，id被确定为`flows/booking`
 - 有通配符时，该情况比较特殊，按照[官方说明](https://docs.spring.io/spring-webflow/docs/2.4.5.RELEASE/reference/html/system-setup.html#flow-registry-base-path)并没有验证通过，这里略过。
当显式指定了id属性时，则使用指定的id。<b>推荐自定义id</b>
## FlowRegistry继承
FlowRegistry是可以继承的，可以定义一个公用的注册器，在多个子注册器中继承该注册器

```
<!-- my-system-config.xml -->
<webflow:flow-registry id="flowRegistry" parent="sharedFlowRegistry">
    <webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
</webflow:flow-registry>

<!-- shared-config.xml -->
<webflow:flow-registry id="sharedFlowRegistry">
    <!-- Global flows shared by several applications -->
</webflow:flow-registry>
```

---
# 配置II - 使用FlowBuilder services
使用FlowBuilder Services可以在build流程时自定义服务，比如视图解析器、EL表达式解析器、类型格式化和转换服务等。如无显式设定FlowBuilder Services，系统将使用默认实现。

```
<webflow:flow-registry id="flowRegistry" flow-builder-services="flowBuilderServices">
    <webflow:flow-location path="/WEB-INF/flows/booking/booking.xml" />
</webflow:flow-registry>

<webflow:flow-builder-services id="flowBuilderServices"
    conversion-service="conversionService"
    expression-parser="expressionParser"
    view-factory-creator="viewFactoryCreator" />

<bean id="conversionService" class="..." />
<bean id="expressionParser" class="..." />
<bean id="viewFactoryCreator" class="..." />
```
## 自定义视图解析器 view-factory-creator
view-factory-creator用于视图解析工作，默认的creator可以支持Spring MVC支持的几种视图类型：JSP, Velocity，FreeMarker等。
```
<webflow:flow-registry id="flowRegistry" flow-builder-services="flowBuilderServices">
	<webflow:location path="/WEB-INF/hotels/booking/booking.xml" />
</webflow:flow-registry>

<!-- 尤其注意这里的development，设置为true时表示开启开发模式，该模式下会在flow定义改变时自动re-load，甚至flow中引用的resource bundle发生了变化都会热重载 -->
<webflow:flow-builder-services id="flowBuilderServices" view-factory-creator="mvcViewFactoryCreator" development="true"/>

<bean id="mvcViewFactoryCreator" class="org.springframework.webflow.mvc.builder.MvcViewFactoryCreator">
	<!-- myExistingViewResolverToUseForFlows就是我们常用的视图解析器，注意这里引用的是一个列表 -->
	<property name="viewResolvers" ref="myExistingViewResolverToUseForFlows"/>
</bean>

... ... 
... ...
<!-- 做验证时使用的是javaconfig的形式，这种形式并没有验证过 -->
<property name="myExistingViewResolverToUseForFlows">
    <list>
        <ref bean="viewResolver" />
    </list>
</property>

<bean id="viewResolver" class="org.springframework.web.servlet.view.InternalResourceViewResolver">
   <property name="prefix" value="/WEB-INF/"/>
   <property name="suffix" value=".jsp"/>
</bean>

```

## 自定义表达式解析器 expression-parser
expression-parser用于定义表达式解析器，默认的解析器使用逻辑：当类路径下有Unified EL解析器时，则使用；没有时，则使用OGNL表达式解析器(官方文档在[EL表达式](https://docs.spring.io/spring-webflow/docs/2.4.5.RELEASE/reference/html/el.html#el-unified-el)一章和[系统设置](https://docs.spring.io/spring-webflow/docs/2.4.5.RELEASE/reference/html/system-setup.html#builder-service-expression-parser)一章关于默认表达式解析说法有出入，自己认为比较可信的是Spring Web Flow 2.1以后，默认使用Spring EL表达式解析器)。
下面是手动配置成Unified EL解析器的方式：

```
<webflow:flow-builder-services expression-parser="expressionParser"/>

<bean id="expressionParser" class="org.springframework.webflow.expression.el.WebFlowELExpressionParser">
    <constructor-arg>
        <bean class="org.jboss.el.ExpressionFactoryImpl" />
    </constructor-arg>
</bean>
```

## 自定义类型转换器 conversion-service
 详细内容参见本系列视图渲染相关章节或[官方文档](https://docs.spring.io/spring-webflow/docs/2.4.5.RELEASE/reference/html/views.html#converter-configuration)

```
<webflow:flow-registry id="flowRegistry" flow-builder-services="flowBuilderServices" ... />

<webflow:flow-builder-services id="flowBuilderServices" conversion-service="defaultConversionService" ... />

<bean id="defaultConversionService" class="org.springframework.binding.convert.service.DefaultConversionService">
	<constructor-arg ref="applicationConversionSevice"/>
</bean>

<bean id="applicationConversionService" class="somepackage.ApplicationConversionServiceFactoryBean">
```

```
public class ApplicationConversionServiceFactoryBean extends FormattingConversionServiceFactoryBean {
    @Override
    protected void installFormatters(FormatterRegistry registry) {
        // ...
    }
}
```

---
# 配置III - 发布流程执行器 - FlowExecutor
FlowExecutor用于执行flow并管理flow执行过程，常见的自定义项有：设置监听器，监听流程执行过程并作出相应，如security监听器，用于监听并控制流程的访问权限；调整flow的部分持久化选项等。

 - 注册监听器

```
<!-- 这里是为特定的flow应用该监听器，当不设criteria属性时，将对所有flow应用 -->
<webflow:flow-execution-listeners>
    <webflow:listener ref="securityListener" criteria="securedFlow1,securedFlow2"/>
</webflow:flow-execution-listeners>
```

 - 调整持久化参数
- max-executions： 设定为每个用户保留的执行数(没错，就是执行数)，当超过该数量时，最先的那个执行会被清除。(这里的执行，我认为是一个新开的且处于激活状态下的flow实例)
- max-execution-snapshots： 设定每个执行保留的最大快照数。不允许保留时，设为0。允许无线保留时，设为-1。(快照用于浏览器的返回按钮)
```
<webflow:flow-executor id="flowExecutor" flow-registry="flowRegistry">
    <webflow:flow-execution-repository max-executions="5" max-execution-snapshots="30" />
</webflow:flow-executor>

```

---
# 配置IV - Spring MVC集成
## 基础配置（将请求转发给flow）

 - Spring MVC基础配置

```
<servlet>
	<servlet-name>Spring MVC Dispatcher Servlet</servlet-name>
	<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
	<init-param>
		<param-name>contextConfigLocation</param-name>
		<param-value>/WEB-INF/web-application-config.xml</param-value>
	</init-param>
</servlet>

<servlet-mapping>
	<servlet-name>Spring MVC Dispatcher Servlet</servlet-name>
	<!-- 不能使用类型/*的通配符进行匹配，否则会出现jsp不解析直接回发给浏览器的情况 -->
	<url-pattern>/</url-pattern>
</servlet-mapping>
```

***
## FlowHandlerAdapter
该步骤是使得Web Flow能够适配Spring MVC
当一个对flow的请求被接收到时，FlowHandlerAdapter会决定是启动一个全新的flow还是继续之前的流程(如从一个view-state跳转到下一个state就属于继续之前的流程)，继续之前的flow是需要在请求有相关信息才行。有关这一方面，web flow默认有如下设定：
&emsp;&emsp;1.Http请求参数在任何情况下都是可以使用的
&emsp;&emsp;2.当一个flow执行结束，且结束时没有想浏览器发送最后的响应时，默认的handler会尝试在同一个request中启动一个新的flow执行
&emsp;&emsp;3.除了NoSuchFlowExecutionException异常外，所有其它异常都会以冒泡的方式抛到Dispatcher中。这是因为默认的handler会尝试自动从该异常中恢复过来，恢复的方式是新开一个全新的flow执行
针对大多数设定，都可以通过实现FlowHandlerAdapter类的子类进行自定义。

```
<!-- Enables FlowHandler URL mapping -->
<bean class="org.springframework.webflow.mvc.servlet.FlowHandlerAdapter">
	<!-- flowExecutor就是前文声明的执行器 -->
	<property name="flowExecutor" ref="flowExecutor" />
</bean>
```

---
# 配置V - FlowHandlerMapping

```
<!-- Maps request paths to flows in the flowRegistry;
	e.g. a path of /hotels/booking looks for a flow with id "hotels/booking" -->
<bean class="org.springframework.webflow.mvc.servlet.FlowHandlerMapping">
	<!-- flowRegistry就是前文声明的注册器 -->
	<property name="flowRegistry" ref="flowRegistry"/>
	<property name="order" value="0"/>
</bean>
```
有了Flow的基本配置和这里的两个Spring MVC的集成配置，请求就能够映射到flow中了。接下来就是写Flow了。想要快速上手的可忽略本文后面的内容，转而直接看本系列其它文章。

---
# 配置VI - 实现自定义的FlowHandler

  - FlowHandler讲解
 FlowHandler可用于自定义flow在HTTP Servlert环境中执行的方式，FlowHandler在FlowHandlerAdapter中被使用，主要负责如下内容：

 &emsp;&emsp;- 返回flow的id以用于执行该flow
 &emsp;&emsp;- 在新流程开始时创建输入
 &emsp;&emsp;- 在流程结束时处理流程的输出
 &emsp;&emsp;- 在流程发生异常时，处理这些异常

 其主要方法如下：


```
public interface FlowHandler {

	public String getFlowId();

	public MutableAttributeMap createExecutionInputMap(HttpServletRequest request);

	public String handleExecutionOutcome(FlowExecutionOutcome outcome,
		HttpServletRequest request, HttpServletResponse response);

	public String handleException(FlowException e,
		HttpServletRequest request, HttpServletResponse response);
}
```
 &emsp;&emsp;该接口的直接实现为AbstractFlowHandler，当我们想要自定义某个设定时，继承该抽象类并重写其中的方法即可。

 - 发布一个FlowHandler
 一个FlowHandler负责一个flow，发布方式是在Spring环境中声明一个bean，该bean的name必须和我们想要处理的flow的id一致，配置好后，当方位该flow的id，则会定位到新发布的FlowHandler中，我们自定义的方法也就生效了。


```
<!-- 这里的BookingHandler只是一个例子，实际用时替换成我们自己的Handler -->
<bean name="hotels/booking" class="org.springframework.webflow.samples.booking.BookingFlowHandler" />
```
 - 着重讲一下FlowHandler中handleExecutionOutcome(...)方法
 该方法用于处理flow结束时产生的FlowExecutionOutcome(系统自动产生)，我们常用它来在流程结束后进行重定向，比如


```
public class BookingFlowHandler extends AbstractFlowHandler {
	// handlExecutionOutcome()方法返回的String代表的是重定向的地址
	public String handleExecutionOutcome(FlowExecutionOutcome outcome,
										HttpServletRequest request, HttpServletResponse response) {
		if (outcome.getId().equals("bookingConfirmed")) {
			return "/booking/show";
		} else {
			return "/hotels/index";
		}
	}
}
// 当flow id为bookinConfirmed时，重定向到/booking/show，否则重定向到/hotels/index
```

&emsp;&emsp;默认情况下，该方法返回的地址是相关于当前Servlet的。但是我们也可以显式地指定一些前缀来扩展重定向的范围

 &emsp;&emsp; -- `servletRelative`: - 相对于当前Servlet重定向
&emsp;&emsp; -- `contextRelative`: - 相对于当前应用重定向
&emsp;&emsp; -- `serverRelative`: - 相对于当前服务器的基地址重定向
&emsp;&emsp; -- `http:// or https://` - 重定向到一个完整的URI地址

&emsp;&emsp;相同的前缀同样适用于声明state时的view属性配上`externalRedirect`的情况

```
<end-state view="externalRedirect:http://springframework.org"/>
<!-- 在流程结束时，跳转到spring首页 -->
```

-----------------------------------------------------手动分割线------------------------------------------------------------------------------------------

# 一个能用的配置(采用Java config的方式配置)
## WebInitializer（与web.xml作用类似）

```
public class WebInitializer extends AbstractAnnotationConfigDispatcherServletInitializer {

	@Override
	protected Class<?>[] getRootConfigClasses() {
		return null;
	}

	@Override
	protected Class<?>[] getServletConfigClasses() {
		return new Class<?>[] {MainConfig.class, RegisterConfig.class};
	}

	@Override
	protected String[] getServletMappings() {
		return new String[] {"/"};
	}

}
```

## MainConfig（Spring的主要配置文件）

```
@Configuration
@EnableWebMvc
@ComponentScan("cn.floyd.pw")
public class MainConfig extends WebMvcConfigurerAdapter{

	@Bean(name="viewResolver")
	public ViewResolver getViewResolver() {
		InternalResourceViewResolver resolver = new InternalResourceViewResolver();
		resolver.setPrefix("/WEB-INF/jsp/");
		resolver.setSuffix(".jsp");
		return resolver;
	}
	
	@Bean
	public MultipartResolver multipartResolver() throws IOException {
	    CommonsMultipartResolver resolver = new CommonsMultipartResolver();
	    return resolver;
	}

	// enable the static resource
	@Override
	public void configureDefaultServletHandling(DefaultServletHandlerConfigurer configurer) {
		configurer.enable();
	}
	
	@Bean
    public FlowHandlerAdapter flowHandlerAdapter(@Autowired FlowExecutor flowExecutor) {
	    System.out.println("init flowHandlerAdapter");
        FlowHandlerAdapter adapter = new FlowHandlerAdapter();
        adapter.setFlowExecutor(flowExecutor);
        
        return adapter;
    }
    
    @Bean
    public FlowHandlerMapping flowHandlerMapping(@Autowired FlowDefinitionRegistry flowRegistry) {
        System.out.println("init flowHandlerMapping");
        FlowHandlerMapping mapping = new FlowHandlerMapping();
        mapping.setOrder(0);
        mapping.setFlowRegistry(flowRegistry);
        
        return mapping;
    }
	
}
```

## RegisterConfig（配置FlowRegister和flowExecutor）

```
@Configuration
public class RegisterConfig extends AbstractFlowConfiguration {

    // 用于注册flow
    @Bean("flowRegistry")
    public FlowDefinitionRegistry flowRegistry(@Autowired FlowBuilderServices flowBuilderServices) {
        
        return getFlowDefinitionRegistryBuilder()
                .setBasePath("/WEB-INF/jsp/flow")
                .addFlowLocation("/config/search-flow.xml")
                .setFlowBuilderServices(flowBuilderServices)
                .build();
    }
    
    @Bean
    public FlowBuilderServices flowBuilderServices(@Autowired MvcViewFactoryCreator mvcViewFactoryCreator) {
        return getFlowBuilderServicesBuilder()
                .setViewFactoryCreator(mvcViewFactoryCreator)
                .build();
    }
    
    @Bean
    public MvcViewFactoryCreator mvcViewFactoryCreator(@Autowired ViewResolver viewResolver) {
        MvcViewFactoryCreator creator = new MvcViewFactoryCreator();
        List<ViewResolver> list = new ArrayList<ViewResolver>();
        list.add(viewResolver);
        creator.setViewResolvers(list);
        
        return creator;
    }
    
    @Bean
    public FlowExecutor flowExecutor(@Autowired FlowDefinitionRegistry flowRegistry) {
        return getFlowExecutorBuilder(flowRegistry).build();
    }
    
}
```

---
# 配置时踩过的坑

## flow id的坑
> 最开始对flow id的认识不够，导致不知道到底该如何定位到flow，其实访问方式就是  .../appName/flowId
> #### Web MVC Environment null not supported
> 启动时正常，访问flow时报异常java.lang.IllegalStateException: Web MVC Environment null not supported
>  是在创建viewFactory时出错，由于我没有采用在config中声明bean的方式创建MvcViewFactoryCreator，因此出现找不到mvc环境的问题，原来是spring在自动检测并创建bean时，会同时设置该bean的环境，因此不能自己随意采用new的方式创建这些配置类
> #### JSP文件不解析
> 出现JSP文件不经过解析就直接传送给了浏览器的问题(对如下阐述的原理并不是很清楚)
> url-pattern为"/*"时，能够匹配到任何路径，因此当controller返回.jsp文件时，也会被拦截，从而返回jsp源码(这里不是很理解，主要是跟自己认识的spring mvc处理流程有差别)。
> url-pattern为"/"时，只能够匹配不带后缀的路径，因此jsp就不会被dispatcherServlet拦截，而是会被jspServlet拦截并处理。但是"/"在配置使能的情况下也能够拦截并允许静态资源的访问