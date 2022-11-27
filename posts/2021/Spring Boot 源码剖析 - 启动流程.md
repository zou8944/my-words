---
created_at: 2021-12-07 21:48:58
updated_at: 2021-12-07 21:48:58
slug: spring-boot-source-analyse-boot-process
tags:
  - Spring
  - 源码剖析
---


> 在Spring源码剖析的前三篇文章，我们介绍了ApplicationContext、Bean相关内容、BeanPostProcessor的内容；但从普遍反馈和自己事后阅读的体验来看，文章过长，没有重点，条理并不是特别清楚。想必是写作方式出了问题，最突出的莫过于流水账式写法，虽然写作的目的并不一定是写出好的文章，而是主要服务自己，但时间一长，自己也是个普通的读者，同样会看不大懂。
>
> 因此，写作方法是需要变更了：要突出条理和重点，如需大段源码讲解，可在文章最后增加源码解析一节，读者可选读。也就是说，长度还是那么长，但可读性增强了很多。
>

<!-- more -->

本文我们关注SpringBoot启动时做了什么，这是理解自动注解的基础，下一篇文章我们将探索自动注解的实现方式。

一个最简单的SpringBoot应用，可以是这样

```kotlin
@SpringBootApplication
class MyApplication

fun main(args: Array<String>) {
    SpringApplication(MyApplication::class.java).run(*args)
}
```

那么重点落在`SpringApplication`类和其run方法上。

## SpringApplication

SpringApplication是一个大类，包含了所有应用启动流程。包含的主要步骤如下

- 创建`ApplicationContext`
- 注册`CommandLinePropertySource`到`Environment`，用于将命令行参数暴露成容器中的属性值
- 刷新容器，即调用容器的`refresh()`方法
- 创建`CommandLineRunner`并调用其`run()`方法

### 关键点

- SpringApplication能够启动三种类型的应用

  - 普通的Servlet应用
  - 响应式的Reactive应用
  - 普通的非Web应用

  不同的应用，会创建对应的ApplciationContext实现类，在ApplicationContext源码分析那一节有所描述

- SpringApplication引入了一个新的临时容器，`Bootstrapper`、`BootstrapRegistry`，用于在创建出`ApplicationContext`实例之前管理启动阶段的Bean

- SpringApplication提供`ApplicationContextInitializer`接口，用于在`ApplicationContext`刷新前修改它，这为我们提供了一个自定义`ApplicationContext`的扩展点。

  向SpringApplication注册它的方式有两个

  - 调用`SpringApplication.addInitializers()`方法手动注册，手写代码时候可用
  - 放在`META-INF/spring.factories`中，自定义starter时可用

- SpringApplication的核心 —— `META-INF/spring.factories`，启动时，会从所有jar包的该文件中搜寻指定factory类型的实现，SpringBoot的诸多特性，比如自动配置，都是依赖于该机制实现。加载该文件有专门的类——`SpringFactoriesLoader`。在SpringApplication中，加载的类有四种

  - `Bootstrapper`：SpringBoot启动阶段用
  - `ApplicationContextInitializer`：Spring上下文初始化器
  - `SpringApplicationRunListener`：SpringApplication启动时候的监听器
  - `ApplicationListener`：Spring事件监听器

  这其中最重要的当属`ApplicationContextInitializer`，考虑到其能力，SpringBoot的诸多功能应该都是由其子类实现。

  如果我们要查看哪些初始化器生效了，可以去对应jar包的spring.factories下查看。比如要看自动配置，去spring-boot-autoconfigure包下的spring.factories文件下查看（我们将在下一篇文章研究这个）

### SpringApplication提供的自定义点

SpringApplication启动时也支持高级写法，可自定义更多内容，再`run`，比如

```kotlin
fun main(args: Array<String>) {
  // 先创建SpringApplication实例，再设置该实例，自定义一些内容
  springApplicationContext = SpringApplication(MylogApplication::class.java).run {
    addInitializers(MylogApplication())
    run(*args)
  }
}
```

这是除了spring.factories外，Spring为我们提供了的额外定义方法，主要可自定义如下内容：

- 主类
- `WebApplicationType`
- 是否允许Bean覆盖
- Bean是否延迟加载
- Banner的模式：不显示、显示在控制台、显示在日志中
- 命令行参数否写入Spring环境
- 是否将`ApplicationConversionService`添加到`ApplicationContext`的转换服务中
- 添加`Bootstrapper`
- 添加`BootstrapRegistryInitializer`
- 设置默认属性，会被添加到环境变量中
- 设置额外的profile
- 设置`BeanNameGenerator`
- 设置`ConfigurableEnvironment`
- 添加其它需要被添加到容器的资源，主要是指Configuration的资源
- 设置`ResourceLoader`
- 设置环境变量前缀，当从系统中获取环境变量时，将会应用该前缀
- 设置`ConfigurableApplicationContext`，相当于手动指定容器的类型了
- 设置`ApplicationContextFactory`
- 设置`ApplicationContextInitializer`，即添加自定义的初始化器
- 添加`ApplicationListener`，即事件监听器
- 设置`ApplicationStartup`，该类并没有什么用，仅日志输出用

### 还缺啥

如上，加上后面的源码分析，我们只看到了`SpringApplication`的启动流程，貌似并没有看到关键之所在

- `application.properties`配置文件的加载原理
- 自动配置加载的原理

这些其实在`spring-boot.jar`和`spring-boot-autoconfigure.jar`中的`META-INF/spring.factories`有指定，出于篇幅，我们下篇文章再讨论。

## 源码分析

这次源码分析我们单独放在一边

### 构造方法

```java
public SpringApplication(Class<?>... primarySources) {
  // 传入的类叫做主要源，这也说明了它的重要性
  this(null, primarySources);
}

public SpringApplication(ResourceLoader resourceLoader, Class<?>... primarySources) {
  this.resourceLoader = resourceLoader;
  Assert.notNull(primarySources, "PrimarySources must not be null");
  this.primarySources = new LinkedHashSet<>(Arrays.asList(primarySources));
  // 检测应用类型”响应式、Servlet、普通应用
  this.webApplicationType = WebApplicationType.deduceFromClasspath();
  // 设置启动器
  this.bootstrappers = new ArrayList<>(getSpringFactoriesInstances(Bootstrapper.class));
  // 设置初始化器
  setInitializers((Collection) getSpringFactoriesInstances(ApplicationContextInitializer.class));
  // 设置监听器
  setListeners((Collection) getSpringFactoriesInstances(ApplicationListener.class));
  // 检测主类
  this.mainApplicationClass = deduceMainApplicationClass();
}
```

#### 新出现的类

- `WebApplicationType`：一个枚举，包含三个值：`SERVLET`、`REACTIVE`、`NONE`。用于决定应用是否需要启动特定类型的web服务器

- `Bootstrapper`：用于初始化`BootstrapRegistry`

  ```java
  public interface Bootstrapper {
  
     /**
      * Initialize the given {@link BootstrapRegistry} with any required registrations.
      * @param registry the registry to initialize
      */
     void intitialize(BootstrapRegistry registry);
  
  }
  ```

- `BootstrapRegistry`：启动注册器，在服务启动阶段到`ApplicationContext`准备好这段时间有效；作用有两个：创建创建过程比较复杂的Bean、创建需要在`ApplicationContext`准备好之前共享的Bean。可以理解为预加载容器，即`SpringBoot`启动阶段使用的容器。

- `ApplicationContextInitializer`：用于初始化`ApplicationContext`，调用时机在`AbstractApplicationContext.refresh()`之前。

  也就是说，在SpringBoot中，可以添加自己的`ApplicationContextInitializer`在容器初始化时修改内容。

  ```java
  public interface ApplicationContextInitializer<C extends ConfigurableApplicationContext> {
  
     /**
      * Initialize the given application context.
      * @param applicationContext the application to configure
      */
     void initialize(C applicationContext);
  
  }
  ```

#### 获取工厂对象 - getSpringFactoriesInstances

听这个方法，像是抽象工厂模式，但总体看下来不大像，如果我们只是把它们当成一种插件机制，会更加方便理解。

`getSpringFactoriesInstances()`是贯穿SpringBoot启动的静态方法，用于加载指定类型的实例，来源是所有包下的`META-INF/spring.factories`文件中指定的类型。其作用就是获取指定类型的所有实现类的实例。

我们首先温习一下`spring.factories`文件长啥样

```properties
org.springframework.boot.env.EnvironmentPostProcessor=\
  com.baomidou.mybatisplus.autoconfigure.SafetyEncryptProcessor
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
  com.baomidou.mybatisplus.autoconfigure.MybatisPlusLanguageDriverAutoConfiguration,\
  com.baomidou.mybatisplus.autoconfigure.MybatisPlusAutoConfiguration
```

然后再来看这个方法

```java
private <T> Collection<T> getSpringFactoriesInstances(Class<T> type, Class<?>[] parameterTypes, Object... args) {
  ClassLoader classLoader = getClassLoader();
  // 获取指定类型的完整类名
  Set<String> names = new LinkedHashSet<>(SpringFactoriesLoader.loadFactoryNames(type, classLoader));
  // 创建它们
  List<T> instances = createSpringFactoriesInstances(type, parameterTypes, classLoader, args, names);
  // 按照@Order注解排序
  AnnotationAwareOrderComparator.sort(instances);
  return instances;
}

// 直接调用了反射创建实例
private <T> List<T> createSpringFactoriesInstances(Class<T> type, Class<?>[] parameterTypes, ClassLoader classLoader, Object[] args, Set<String> names) {
  List<T> instances = new ArrayList<>(names.size());
  for (String name : names) {
    try {
      Class<?> instanceClass = ClassUtils.forName(name, classLoader);
      Assert.isAssignable(type, instanceClass);
      Constructor<?> constructor = instanceClass.getDeclaredConstructor(parameterTypes);
      T instance = (T) BeanUtils.instantiateClass(constructor, args);
      instances.add(instance);
    } catch (Throwable ex) {
      throw new IllegalArgumentException("Cannot instantiate " + type + " : " + name, ex);
    }
  }
  return instances;
}
```

理解上面那段代码的重点，又落在了`SpringFactoriesLoader.loadFactoryNames(type, classLoader)`上。

```java
// 注意这个spring.factories的位置
public static final String FACTORIES_RESOURCE_LOCATION = "META-INF/spring.factories";

public static <T> List<T> loadFactories(Class<T> factoryType, @Nullable ClassLoader classLoader) {
  Assert.notNull(factoryType, "'factoryType' must not be null");
  ClassLoader classLoaderToUse = classLoader;
  if (classLoaderToUse == null) {
    classLoaderToUse = SpringFactoriesLoader.class.getClassLoader();
  }
  // 关键方法，根据指定的工厂类型，获取其实现类们的名字
  List<String> factoryImplementationNames = loadFactoryNames(factoryType, classLoaderToUse);
  if (logger.isTraceEnabled()) {
    logger.trace("Loaded [" + factoryType.getName() + "] names: " + factoryImplementationNames);
  }
  List<T> result = new ArrayList<>(factoryImplementationNames.size());
  for (String factoryImplementationName : factoryImplementationNames) {
    // 反射实例化这些工厂实现类
    result.add(instantiateFactory(factoryImplementationName, factoryType, classLoaderToUse));
  }
  // 按照Order和Priority注解排序
  AnnotationAwareOrderComparator.sort(result);
  return result;
}

/**
 * Load the fully qualified class names of factory implementations of the
 * given type from {@value #FACTORIES_RESOURCE_LOCATION}, using the given
 * class loader.
 * <p>As of Spring Framework 5.3, if a particular implementation class name
 * is discovered more than once for the given factory type, duplicates will
 * be ignored.
 * @param factoryType the interface or abstract class representing the factory
 * @param classLoader the ClassLoader to use for loading resources; can be
 * {@code null} to use the default
 * @throws IllegalArgumentException if an error occurs while loading factory names
 * @see #loadFactories
 */
public static List<String> loadFactoryNames(Class<?> factoryType, @Nullable ClassLoader classLoader) {
  ClassLoader classLoaderToUse = classLoader;
  if (classLoaderToUse == null) {
    classLoaderToUse = SpringFactoriesLoader.class.getClassLoader();
  }
  String factoryTypeName = factoryType.getName();
  return loadSpringFactories(classLoaderToUse).getOrDefault(factoryTypeName, Collections.emptyList());
}

private static Map<String, List<String>> loadSpringFactories(ClassLoader classLoader) {
  Map<String, List<String>> result = cache.get(classLoader);
  if (result != null) {
    return result;
  }

  result = new HashMap<>();
  try {
    // 获取所有包下的 META-INF/spring.factories 文件
    Enumeration<URL> urls = classLoader.getResources(FACTORIES_RESOURCE_LOCATION);
    while (urls.hasMoreElements()) {
      URL url = urls.nextElement();
      UrlResource resource = new UrlResource(url);
      // 将spring.factories文件的内容加载成属性
      Properties properties = PropertiesLoaderUtils.loadProperties(resource);
      for (Map.Entry<?, ?> entry : properties.entrySet()) {
        String factoryTypeName = ((String) entry.getKey()).trim();
        // 值按逗号拆分
        String[] factoryImplementationNames = StringUtils.commaDelimitedListToStringArray((String) entry.getValue());
        // 组装成key-list的形式
        for (String factoryImplementationName : factoryImplementationNames) {
          result.computeIfAbsent(factoryTypeName, key -> new ArrayList<>())
            .add(factoryImplementationName.trim());
        }
      }
    }

    // Replace all lists with unmodifiable lists containing unique elements
    result.replaceAll((factoryType, implementations) -> implementations.stream().distinct()
                      .collect(Collectors.collectingAndThen(Collectors.toList(), Collections::unmodifiableList)));
    cache.put(classLoader, result);
  }
  catch (IOException ex) {
    ... ...
  }
  return result;
}

private static <T> T instantiateFactory(String factoryImplementationName, Class<T> factoryType, ClassLoader classLoader) {
  try {
    Class<?> factoryImplementationClass = ClassUtils.forName(factoryImplementationName, classLoader);
    // 反射实例化
    return (T) ReflectionUtils.accessibleConstructor(factoryImplementationClass).newInstance();
  } catch (Throwable ex) {
    ... ...
  }
}
```

#### 检测WebApplicationType

```java
private static final String[] SERVLET_INDICATOR_CLASSES = { "javax.servlet.Servlet", "org.springframework.web.context.ConfigurableWebApplicationContext" };

private static final String WEBMVC_INDICATOR_CLASS = "org.springframework.web.servlet.DispatcherServlet";

private static final String WEBFLUX_INDICATOR_CLASS = "org.springframework.web.reactive.DispatcherHandler";

private static final String JERSEY_INDICATOR_CLASS = "org.glassfish.jersey.servlet.ServletContainer";

// 要么是响应式应用、要么是Servlet应用、要么是普通应用
static WebApplicationType deduceFromClasspath() {
  if (ClassUtils.isPresent(WEBFLUX_INDICATOR_CLASS, null) && !ClassUtils.isPresent(WEBMVC_INDICATOR_CLASS, null) && !ClassUtils.isPresent(JERSEY_INDICATOR_CLASS, null)) {
    return WebApplicationType.REACTIVE;
  }
  for (String className : SERVLET_INDICATOR_CLASSES) {
    if (!ClassUtils.isPresent(className, null)) {
      return WebApplicationType.NONE;
    }
  }
  return WebApplicationType.SERVLET;
}
```

检测逻辑

- 类路径中只有`org.springframework.web.reactive.DispatcherHandler`时，是响应式应用
- 类路径中同时存在`javax.servlet.Servlet`、`org.springframework.web.context.ConfigurableWebApplicationContext`时，是Servlet应用
- 否则，是普通应用

> WebApplicationType有什么用
>
> - 创建environment时决定创建什么类型的Environment：`private ConfigurableEnvironment getOrCreateEnvironment()`
> - 创建ApplicationContext时指定具体类型

#### 检测主类

```java
private Class<?> deduceMainApplicationClass() {
  try {
    StackTraceElement[] stackTrace = new RuntimeException().getStackTrace();
    for (StackTraceElement stackTraceElement : stackTrace) {
      if ("main".equals(stackTraceElement.getMethodName())) {
        return Class.forName(stackTraceElement.getClassName());
      }
    }
  } catch (ClassNotFoundException ex) {
    // Swallow and continue
  }
  return null;
}
```

检测逻辑：从当前调用栈中，寻找main方法那一层，其所属类就是主类

### run方法

这是应用启动的主要逻辑之所在

```java
public ConfigurableApplicationContext run(String... args) {
  // 秒表，仅作为启动时间记录用
  StopWatch stopWatch = new StopWatch();
  stopWatch.start();
  // 创建默认的BootstrapContext，前面说了它是启动阶段的临时容器
  DefaultBootstrapContext bootstrapContext = createBootstrapContext();
  ConfigurableApplicationContext context = null;
  // SpringApplicationRunListener，专为SpringApplication启动的各个阶段准备的监听器
  // 其实只有一个实现类EventPublishingRunListener，用于创建启动中的事件并广播出去
  SpringApplicationRunListeners listeners = getRunListeners(args);
  listeners.starting(bootstrapContext, this.mainApplicationClass);
  try {
    // 命令行参数封装起来
    ApplicationArguments applicationArguments = new DefaultApplicationArguments(args);
    // 准备环境
    ConfigurableEnvironment environment = prepareEnvironment(listeners, bootstrapContext, applicationArguments);
    // 打印banner
    Banner printedBanner = printBanner(environment);
    // 创建容器
    context = createApplicationContext();
    context.setApplicationStartup(this.applicationStartup);
    // 准备容器
    prepareContext(bootstrapContext, context, environment, listeners, applicationArguments, printedBanner);
    // 刷新容器
    refreshContext(context);
    // 刷新容器的善后处理：默认为空
    afterRefresh(context, applicationArguments);
    stopWatch.stop();
    if (this.logStartupInfo) {
      new StartupInfoLogger(this.mainApplicationClass).logStarted(getApplicationLog(), stopWatch);
    }
    // 广播已开始事件
    listeners.started(context);
    callRunners(context, applicationArguments);
  }
  catch (Throwable ex) {
    handleRunFailure(context, ex, listeners);
    throw new IllegalStateException(ex);
  }

  try {
    // 广播运行中事件
    listeners.running(context);
  }
  catch (Throwable ex) {
    handleRunFailure(context, ex, null);
    throw new IllegalStateException(ex);
  }
  return context;
}
```

#### 获取SpringApplicationRunListener

```java
private SpringApplicationRunListeners getRunListeners(String[] args) {
  Class<?>[] types = new Class<?>[] { SpringApplication.class, String[].class };
  // 从sprin.factories中获取SpringApplicationRunListener子类
  return new SpringApplicationRunListeners(logger,getSpringFactoriesInstances(SpringApplicationRunListener.class, types, this, args), this.applicationStartup);
}
```

#### 准备环境

```java
private ConfigurableEnvironment prepareEnvironment(SpringApplicationRunListeners listeners, DefaultBootstrapContext bootstrapContext, ApplicationArguments applicationArguments) {
  // 创建environment对象
  ConfigurableEnvironment environment = getOrCreateEnvironment();
  // 配置环境对象：添加conversionService和命令行参数
  configureEnvironment(environment, applicationArguments.getSourceArgs());
  // 向环境中添加属性源：ConfigurationPropertySource
  ConfigurationPropertySources.attach(environment);
  // 广播环境准备好的消息
  listeners.environmentPrepared(bootstrapContext, environment);
  // 将默认属性移到属性源的最末尾，属性源的顺序很重要
  DefaultPropertiesPropertySource.moveToEnd(environment);
  // 将类中的profile加入environment的activeProfiles中，使得该profile生效
  configureAdditionalProfiles(environment);
  ... ...
  return environment;
}

// 不同的应用类型，需要创建不同的环境对象，前面分析ApplicationContext时说过不同环境对象的区别
private ConfigurableEnvironment getOrCreateEnvironment() {
  if (this.environment != null) {
    return this.environment;
  }
  switch (this.webApplicationType) {
    case SERVLET:
      return new StandardServletEnvironment();
    case REACTIVE:
      return new StandardReactiveWebEnvironment();
    default:
      return new StandardEnvironment();
  }
}

protected void configureEnvironment(ConfigurableEnvironment environment, String[] args) {
  // 处理ConversionService，前面分析ApplicationContext时说过该对象的作用，用于类型转换
  if (this.addConversionService) {
    ConversionService conversionService = ApplicationConversionService.getSharedInstance();
    environment.setConversionService((ConfigurableConversionService) conversionService);
  }
  // 配置属性源：将命令行参数加入属性源
  configurePropertySources(environment, args);
  // 没用
  configureProfiles(environment, args);
}
```

#### 创建ApplicationContext

```java
protected ConfigurableApplicationContext createApplicationContext() {
  return this.applicationContextFactory.create(this.webApplicationType);
}

// 不言自明
ApplicationContextFactory DEFAULT = (webApplicationType) -> {
  try {
    switch (webApplicationType) {
      case SERVLET:
        return new AnnotationConfigServletWebServerApplicationContext();
      case REACTIVE:
        return new AnnotationConfigReactiveWebServerApplicationContext();
      default:
        return new AnnotationConfigApplicationContext();
    }
  } catch (Exception ex) {
    ... ...
  }
};
```

#### 准备容器

```java
private void prepareContext(DefaultBootstrapContext bootstrapContext, ConfigurableApplicationContext context,
                            ConfigurableEnvironment environment, SpringApplicationRunListeners listeners,
                            ApplicationArguments applicationArguments, Banner printedBanner) {
  // 注入environment
  context.setEnvironment(environment);
  // 注入resourceLoader、classLoader、beanNameGenerator、conversionService
  postProcessApplicationContext(context);
  // 应用所有在构造方法中和set注入的ApplicationContextInitializer
  applyInitializers(context);
  // 广播事件
  listeners.contextPrepared(context);
  // 临时容器工作完成，关闭
  bootstrapContext.close(context);
  // 下面添加一些与SpringBoot相关的一些Bean
  ConfigurableListableBeanFactory beanFactory = context.getBeanFactory();
  beanFactory.registerSingleton("springApplicationArguments", applicationArguments);
  if (printedBanner != null) {
    beanFactory.registerSingleton("springBootBanner", printedBanner);
  }
  if (beanFactory instanceof DefaultListableBeanFactory) {
    ((DefaultListableBeanFactory) beanFactory).setAllowBeanDefinitionOverriding(this.allowBeanDefinitionOverriding);
  }
  if (this.lazyInitialization) {
    context.addBeanFactoryPostProcessor(new LazyInitializationBeanFactoryPostProcessor());
  }
  // 获取加载源，即配置类所在源
  Set<Object> sources = getAllSources();
  Assert.notEmpty(sources, "Sources must not be empty");
  // 从源加载Bean定义到容器中
  load(context, sources.toArray(new Object[0]));
  // 广播事件：Bean定义加载完成
  listeners.contextLoaded(context);
}
```

### 其它 - 注解排序

为组件排序的方法，我们发现哪儿都有它，这里关照一下：`AnnotationAwareOrderComparator.sort()`。

```java
public class AnnotationAwareOrderComparator extends OrderComparator {

  public static final AnnotationAwareOrderComparator INSTANCE = new AnnotationAwareOrderComparator();

  public static void sort(List<?> list) {
    if (list.size() > 1) {
      // 将当前单例当做比较器传入
      list.sort(INSTANCE);
    }
  }

  // 这个在OrderComparator会调用到
  protected Integer findOrder(Object obj) {
    // 调用父类的方法获取order：实现Ordered接口就给出值
    Integer order = super.findOrder(obj);
    if (order != null) {
      return order;
    }
    // 否则从注解中找
    return findOrderFromAnnotation(obj);
  }

  @Nullable
  private Integer findOrderFromAnnotation(Object obj) {
    // 从@Order注解中取得排序值
    AnnotatedElement element = (obj instanceof AnnotatedElement ? (AnnotatedElement) obj : obj.getClass());
    MergedAnnotations annotations = MergedAnnotations.from(element, SearchStrategy.TYPE_HIERARCHY);
    Integer order = OrderUtils.getOrderFromAnnotations(element, annotations);
    if (order == null && obj instanceof DecoratingProxy) {
      return findOrderFromAnnotation(((DecoratingProxy) obj).getDecoratedClass());
    }
    return order;
  }

}
```

所以，重点肯定在`OrderComparator`的`compare()`方法上。

```java
public int compare(@Nullable Object o1, @Nullable Object o2) {
  return doCompare(o1, o2);
}

private int doCompare(@Nullable Object o1, @Nullable Object o2) {
  boolean p1 = (o1 instanceof PriorityOrdered);
  boolean p2 = (o2 instanceof PriorityOrdered);
  // PriorityOrdered有短路作用，有实现PriorityOrdered的比没有实现的优先级低
  if (p1 && !p2) {
    return -1;
  } else if (p2 && !p1) {
    return 1;
  }

  // 二者都没有实现PriorityOrdered，则根据Ordered接口或@Order注解来
  int i1 = getOrder(o1);
  int i2 = getOrder(o2);
  return Integer.compare(i1, i2);
}

protected int getOrder(@Nullable Object obj) {
  if (obj != null) {
    Integer order = findOrder(obj);
    if (order != null) {
      return order;
    }
  }
  // 没有实现任何顺序的优先级最低
  return Ordered.LOWEST_PRECEDENCE;
}

protected Integer findOrder(Object obj) {
  return (obj instanceof Ordered ? ((Ordered) obj).getOrder() : null);
}
```

可以总结出优先级顺序，两个组件

- 如果一个实现了`PriorityOrdered`接口，一个没有实现`PriorityOrdered`接口，则实现了这个优先级更高

  `PriorityOrdered`是`Order`的子接口，没有任何附加实现

  也就是说，`PriorityOrdered`就是想实现一点：它比普通`Ordered`接口具有更高的优先级

- 如果都实现了`PriorityOrdered`，则根据其order值排序

- 如果实现了`Ordered`或被`@Order`注解，则根据其order值排序

- 没有任何排序接口或注解的组件之间相互对比，永远是相等的

- 没有任何排序接口或注解的组件，和，有任意一个排序接口或注解的组件，后者优先级更高，除非后者主动指定order为`Ordered.LOWEST_PRECEDENCE`
