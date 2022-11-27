---
created_at: 2021-11-30 09:42:23
updated_at: 2021-11-30 09:42:23
slug: spring-source-code-analyze-post-processor
tags:
  - Spring
  - 源码剖析
---

`BeanPostProcessor`是Spring中参与Bean生命周期定制非常重要的一个手段，上文分析过，其执行有两个时机

- 一前：Bean自动注入之后，自定义初始化方法调用前
- 一后：自定义方法调用之后

Spring中很多重要的特性利用了`BeanPostProcessor`达成，毕竟，算来算去，Spring中整个Bean的生命周期已经足够复杂了，如果每加一个功能就要在生命周期上做文章，只会增加复杂度，而`BeanPostProcessor`则是Spring提供的一种扩展方式。与其相对的，一般用户用的可能较少的`BeanFactoryPostProcessor`是针对整个容器初始化完成后提供定制化功能的扩展，我们也要观察一下。观察的主要内容是主要实现类及其作用。

<!-- more -->

## BeanFactoryPostProcessor

它的调用，在`org.springframework.context.support.AbstractApplicationContext#refresh.564行`。

其接口及其简单：一个简单的函数式接口。

```java
@FunctionalInterface
public interface BeanFactoryPostProcessor {
	void postProcessBeanFactory(ConfigurableListableBeanFactory beanFactory) throws BeansException;
}
```

这意味着，在容器创建后，我们能够向其中设置任何内容，也可以利用容器刚刚创建这个时机，来做一些时机上再容器全局的一些事情。

![image-20211122183440854](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211122183440854.png)

具体来说，有这么几类

### 修改现有容器配置

- `AbstractDependsOnBeanFactoryPostProcessor`、`CacheManagerEntityManagerFactoryDependsOnPostProcessor`。强制为某些Bean显式设置依赖关系，使得不满足依赖时容器无法启动。这在自动配时会有用
- `CustomScopeConfigurer`，添加自定义scope，这在`WebSocketMessageBrokerConfigurationSupport`有使用

- `CustomEditorConfigurer`，注册一些自定义的`PropertyEditor`
- `LazyInitializationBeanFactoryPostProcessor`，它将容器中没有指定延迟加载属性的bean定义，除以下条件的bean设置为延迟加载
  - `SmartInitializingSingleton`类型
  - `AopInfrastructureBean`类型
  - `TaskScheduler`类型
  - `ScheduledExecutorService`类型
  - 被`@Scheduled`或`Schedules`注解的类

### 向容器中添加Bean

- `ServletComponentRegisteringPostProcessor`，它创建了一个Servlet环境，注册了必要的Bean
- `EventListenerMethodProcessor`，它配合`SmartInitializingSingleton`，实现了`@EventListener`注解
  - 在容器初始化完成后，获取并持有了容器的`EventListenerFactory`、容器本身
  - 在单例Bean初始化完成后，检测带有`@Component`的Bean内部是否有`@EventListener`注解的方法，如果有，则使用上一步持有的`EventListenerFactory`将该方法创建为一个`ApplicationListener`实例，然后注入容器

### 一些全局开关

- `AspectJWeavingEnabler`，开启AspectJ。

## BeanPostProcessor

它的执行时机，有两个：Bean创建后，实例化前；Bean实例化后。

```java
public interface BeanPostProcessor {

  default Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
    return bean;
  }

  default Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
    return bean;
  }

}
```

下面是主要实现

### xxxAware

- `ApplicationContextAwareProcessor`，在Bean初始化之前，调用了如下接口的setxxx方法
  - `EnvironmentAware`
  - `EmbeddedValueResolverAware`
  - `ResourceLoaderAware`
  - `ApplicationEventPublisherAware`
  - `MessageSourceAware`
  - `ApplicationContextAware`
  - `ApplicationStartupAware`
- `BootstrapContextAwareProcessor`，在Bean初始化之前，调用了如下接口的setxxx方法
  - `BootstrapContextAware`
- `WebApplicationContextServletContextAwareProcessor`，在Bean初始化之前，调用了如下接口的setxxx方法
  - `ServletContextAware`
  - `ServletConfigAware`

### ConfigurationPropertiesBindingPostProcessor

它将环境中的属性绑定到`@ConfigurationProperties`注解到的类上。比如

```kotlin
@ConfigurationProperties(prefix = "aliyun")
class AliyunConfig {
  lateinit var accessKey: String
  lateinit var secretKey: String
}
```

它能够将配置中的如下属性注入对象

```properties
aliyun.access-key=xxxx
aliyun.secret-key=xxx
```

来看看该类的源码

```java
public class ConfigurationPropertiesBindingPostProcessor implements BeanPostProcessor, PriorityOrdered, ApplicationContextAware, InitializingBean {

  private ApplicationContext applicationContext;

  private BeanDefinitionRegistry registry;

  private ConfigurationPropertiesBinder binder;

  @Override
  public void setApplicationContext(ApplicationContext applicationContext) throws BeansException {
    this.applicationContext = applicationContext;
  }

  @Override
  public void afterPropertiesSet() throws Exception {
    this.registry = (BeanDefinitionRegistry) this.applicationContext.getAutowireCapableBeanFactory();
    // 创建ConfigurationPropertiesBinder，这是关键点1
    this.binder = ConfigurationPropertiesBinder.get(this.applicationContext);
  }

  @Override
  public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
    // 关键点2：构建ConfigurationPropertiesBean
    bind(ConfigurationPropertiesBean.get(this.applicationContext, bean, beanName));
    return bean;
  }

  private void bind(ConfigurationPropertiesBean bean) {
    if (bean == null || hasBoundValueObject(bean.getName())) {
      return;
    }
    Assert.state(bean.getBindMethod() == BindMethod.JAVA_BEAN, "错误信息");
    // 关键点3：调用binder.bind方法，完成绑定
    this.binder.bind(bean);
  }

}
```

理解它的关键，在于理解Spring的绑定机制，该机制有点复杂，不是一两句能说清的。简单来说，就是将一堆属性绑定到指定的领域模型。我们只简单地看一下上面涉及到的两个类。具体的，下一篇文章再来看。

#### ConfigurationPropertiesBean

```java
public final class ConfigurationPropertiesBean {

  // 名字，直接就是传入bean的名字
  private final String name;
	// 传入bean的实例
  private final Object instance;
	// 注解在bean实例上的ConfigurationProperties注解实例
  private final ConfigurationProperties annotation;
	// 绑定目标，由传入的bean实例+其它的注解构成
  private final Bindable<?> bindTarget;
	// 绑定方法，枚举，JAVA_BEAN：java bean，使用getter和setter绑定；VALUE_OBJECT：值对象，使用构造方法绑定
  private final BindMethod bindMethod;

  private ConfigurationPropertiesBean(String name, Object instance, ConfigurationProperties annotation, Bindable<?> bindTarget) {
    this.name = name;
    this.instance = instance;
    this.annotation = annotation;
    this.bindTarget = bindTarget;
    this.bindMethod = BindMethod.forType(bindTarget.getType().resolve());
  }

  public static ConfigurationPropertiesBean get(ApplicationContext applicationContext, Object bean, String beanName) {
    // 获取bean的工厂方法，就是我们创建时指定的工厂方法，没有就为null
    Method factoryMethod = findFactoryMethod(applicationContext, beanName);
    return create(beanName, bean, bean.getClass(), factoryMethod);
  }

  private static ConfigurationPropertiesBean create(String name, Object instance, Class<?> type, Method factory) {
    // 获取ConfigurationProperties注解
    ConfigurationProperties annotation = findAnnotation(instance, type, factory, ConfigurationProperties.class);
    if (annotation == null) {
      return null;
    }
    // 获取Validated注解
    Validated validated = findAnnotation(instance, type, factory, Validated.class);
    Annotation[] annotations = (validated != null) ? new Annotation[] { annotation, validated }
    : new Annotation[] { annotation };
    // 解析待绑定类型：工厂方法的返回类型，或者，传入type所指定的类型
    ResolvableType bindType = (factory != null) ? ResolvableType.forMethodReturnType(factory) : ResolvableType.forClass(type);
    Bindable<Object> bindTarget = Bindable.of(bindType).withAnnotations(annotations);
    if (instance != null) {
      bindTarget = bindTarget.withExistingValue(instance);
    }
    return new ConfigurationPropertiesBean(name, instance, annotation, bindTarget);
  }
}
```

- 对`Bindable`和`BindMethod`，可能有一些陌生，暂且不管，后面专门写文章介绍它
- `ConfigurationPropertiesBean`中包含的内容：目标bean实例、`ConfigurationProperties`注解、绑定目标、绑定方式
- 该类为绑定做准备

#### ConfigurationPropertiesBinder

```java
class ConfigurationPropertiesBinder {

  private static final String BEAN_NAME = "org.springframework.boot.context.internalConfigurationPropertiesBinder";
  
  private static final String VALIDATOR_BEAN_NAME = EnableConfigurationProperties.VALIDATOR_BEAN_NAME;

  // 构造方法，初始化了四个属性
  ConfigurationPropertiesBinder(ApplicationContext applicationContext) {
		this.applicationContext = applicationContext;
    // 获取容器的属性源
		this.propertySources = new PropertySourcesDeducer(applicationContext).getPropertySources();
    // 从容器中获取EnableConfigurationProperties.VALIDATOR_BEAN_NAME指定的验证器
		this.configurationPropertiesValidator = getConfigurationPropertiesValidator(applicationContext);
    // 判定是否要遵循jsr303验证规范："javax.validation.Validator", "javax.validation.ValidatorFactory", "javax.validation.bootstrap.GenericBootstrap" 这三个类存在，就需要遵循
		this.jsr303Present = ConfigurationPropertiesJsr303Validator.isJsr303Present(applicationContext);
	}
  
  // 从容器中获取提前初始化OK的binder
  static ConfigurationPropertiesBinder get(BeanFactory beanFactory) {
    return beanFactory.getBean(BEAN_NAME, ConfigurationPropertiesBinder.class);
  }

  // 那个绑定方法
  BindResult<?> bind(ConfigurationPropertiesBean propertiesBean) {
    // 绑定目标
    Bindable<?> target = propertiesBean.asBindTarget();
    // 注解
    ConfigurationProperties annotation = propertiesBean.getAnnotation();
    // 获取处理器
    BindHandler bindHandler = getBindHandler(target, annotation);
    // 调用Binder.bind方法，完成绑定
    return getBinder().bind(annotation.prefix(), target, bindHandler);
  }

  // 获取绑定处理器
  private <T> BindHandler getBindHandler(Bindable<T> target, ConfigurationProperties annotation) {
    // 获取验证器：configurationPropertiesValidator、ConfigurationPropertiesJsr303Validator、自定义验证器
    List<Validator> validators = getValidators(target);
    // 获取处理器：IgnoreTopLevelConverterNotFoundBindHandler
    BindHandler handler = getHandler();
    // 根据不同条件构建不同BindHandler
    handler = new ConfigurationPropertiesBindHander(handler);
    if (annotation.ignoreInvalidFields()) {
      handler = new IgnoreErrorsBindHandler(handler);
    }
    if (!annotation.ignoreUnknownFields()) {
      UnboundElementsSourceFilter filter = new UnboundElementsSourceFilter();
      handler = new NoUnboundElementsBindHandler(handler, filter);
    }
    if (!validators.isEmpty()) {
      handler = new ValidationBindHandler(handler, validators.toArray(new Validator[0]));
    }
    // 一些额外的处理器
    for (ConfigurationPropertiesBindHandlerAdvisor advisor : getBindHandlerAdvisors()) {
      handler = advisor.apply(handler);
    }
    return handler;
  }
  
  // 获取有效的验证器
  private List<Validator> getValidators(Bindable<?> target) {
		List<Validator> validators = new ArrayList<>(3);
		if (this.configurationPropertiesValidator != null) {
      // 容器中的configurationPropertiesValidator
			validators.add(this.configurationPropertiesValidator);
		}
		if (this.jsr303Present && target.getAnnotation(Validated.class) != null) {
      // 新建的ConfigurationPropertiesJsr303Validator
			validators.add(getJsr303Validator());
		}
		if (target.getValue() != null && target.getValue().get() instanceof Validator) {
      // 绑定目标本身也可以是验证器
			validators.add((Validator) target.getValue().get());
		}
		return validators;
	}

  // 创建Binder
  private Binder getBinder() {
    if (this.binder == null) {
      this.binder = new Binder(getConfigurationPropertySources(), getPropertySourcesPlaceholdersResolver(),
                               getConversionServices(), getPropertyEditorInitializer(), null,
                               ConfigurationPropertiesBindConstructorProvider.INSTANCE);
    }
    return this.binder;
  }
}
```

- 最终还是委托给了`Binder`进行调用，`ConfigurationPropertiesBinder`只能算是一个代理，准备好绑定需要的组件，然后调用`Binder`完成绑定
- 我们看到大量的从容器中获取绑定组件的方式，却没看到什么时候在容器中创建了该bean？实际上`getBean()`方法的首次调用就完成了创建和返回两个操作
- 绑定包含了验证的过程，默认会使用两个验证器
  - `ConfigurationPropertiesValidator`
  - `ConfigurationPropertiesJsr303Validator`
- 支持JSR303验证规范的前提条件：同时存在如下三个类型的Bean
  - `Validator`
  - `ValidatorFactory`
  - `GenericBootstrap`

### ApplicationListenerDetector

`ApplicationListenerDetector`，用于检测实现了`ApplicationListener`的Bean，并将其注入容器和时间广播器。

```java
class ApplicationListenerDetector implements DestructionAwareBeanPostProcessor, MergedBeanDefinitionPostProcessor {

  private final transient AbstractApplicationContext applicationContext;

	private final transient Map<String, Boolean> singletonNames = new ConcurrentHashMap<>(256);
  
  @Override
  public void postProcessMergedBeanDefinition(RootBeanDefinition beanDefinition, Class<?> beanType, String beanName) {
    // 如果Bean类型是ApplicationListener的子类，则加入缓存
    if (ApplicationListener.class.isAssignableFrom(beanType)) {
      this.singletonNames.put(beanName, beanDefinition.isSingleton());
    }
  }

  @Override
  public Object postProcessAfterInitialization(Object bean, String beanName) {
    if (bean instanceof ApplicationListener) {
      // 缓存里有就注册到容器中
      Boolean flag = this.singletonNames.get(beanName);
      if (Boolean.TRUE.equals(flag)) {
        this.applicationContext.addApplicationListener((ApplicationListener<?>) bean);
      } else if (Boolean.FALSE.equals(flag)) {
        this.singletonNames.remove(beanName);
      }
    }
    return bean;
  }

  @Override
  public void postProcessBeforeDestruction(Object bean, String beanName) {
    // 销毁时移除
    if (bean instanceof ApplicationListener) {
      try {
        ApplicationEventMulticaster multicaster = this.applicationContext.getApplicationEventMulticaster();
        multicaster.removeApplicationListener((ApplicationListener<?>) bean);
        multicaster.removeApplicationListenerBean(beanName);
      } catch (IllegalStateException ex) {
        // ApplicationEventMulticaster not initialized yet - no need to remove a listener
      }
    }
  }

}
```

### AutowiredAnnotationBeanPostProcessor

可以以该类为入口，查看整个Spring自动注入的逻辑。首先其继承结构如下。

![image-20211129174225231](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211129174225231.png)

这就意味着有以下几个扩展点可以观察

- 获取到`MergedBeanDefinition`之后的执行点（关于`MergedBeanDefinition`在关于Bean的描述那篇文章讨论过，这里不再看）

  调用点：`AbstractAutowireCapableBeanFactory.java:1116行，applyMergedBeanDefinitionPostProcessors()方法`

- Bean的属性读取完成之后的执行点

  调用点：`AbstractAutowireCapableBeanFactory.java:1436行，polupateBean()方法`

- 构建Bean实例时用于判断构造方法参数的执行点

  调用点：`AbstractAutowireCapableBeanFactory.java:1302行，determineConstructorsFromBeanPostProcessors()方法`

实际上，该processor同时干预了字段注入、方法注入、构造器注入。

首先看其构造方法，可知，适用的注解有三个：`@Autowired、@Value、@Inject`，最后一个是适配JSR330。

```java
public class AutowiredAnnotationBeanPostProcessor implements SmartInstantiationAwareBeanPostProcessor, MergedBeanDefinitionPostProcessor {
  // 适用注解：Autowired、Value、Inject
  public AutowiredAnnotationBeanPostProcessor() {
		this.autowiredAnnotationTypes.add(Autowired.class);
		this.autowiredAnnotationTypes.add(Value.class);
		try {
			this.autowiredAnnotationTypes.add((Class<? extends Annotation>)ClassUtils.forName("javax.inject.Inject", AutowiredAnnotationBeanPostProcessor.class.getClassLoader()));
			logger.trace("JSR-330 'javax.inject.Inject' annotation found and supported for autowiring");
		} catch (ClassNotFoundException ex) {
			// JSR-330 API not available - simply skip.
		}
	}
}
```

然后看第一个扩展点：`postProcessMergedBeanDefinition()`，与他相关的方法全部摆出来。

```java
public void postProcessMergedBeanDefinition(RootBeanDefinition beanDefinition, Class<?> beanType, String beanName) {
  // 查找用于自动注入的元数据，InjectionMetadata只是Spring的又一个抽象而已，这里不深究
  InjectionMetadata metadata = findAutowiringMetadata(beanName, beanType, null);
  // 忽略它做了啥
  metadata.checkConfigMembers(beanDefinition);
}

private InjectionMetadata findAutowiringMetadata(String beanName, Class<?> clazz, @Nullable PropertyValues pvs) {
  // 这里是从缓存中取，省略掉了
  InjectionMetadata metadata = ...
    ... ...
    // 真实地去构建
    metadata = buildAutowiringMetadata(clazz);
  ... ...  
    return metadata;
}

private InjectionMetadata buildAutowiringMetadata(final Class<?> clazz) {
  // 目标类上没有前面指定的三个注解之一，则直接忽略
  if (!AnnotationUtils.isCandidateClass(clazz, this.autowiredAnnotationTypes)) {
    return InjectionMetadata.EMPTY;
  }

  List<InjectionMetadata.InjectedElement> elements = new ArrayList<>();
  Class<?> targetClass = clazz;

  do {
    final List<InjectionMetadata.InjectedElement> currElements = new ArrayList<>();

    // 逐个字段扫描
    ReflectionUtils.doWithLocalFields(targetClass, field -> {
      // 在该字段上查找自动注入的注解
      MergedAnnotation<?> ann = findAutowiredAnnotation(field);
      if (ann != null) {
        // 静态字段忽略
        if (Modifier.isStatic(field.getModifiers())) {
          if (logger.isInfoEnabled()) {
            logger.info("Autowired annotation is not supported on static fields: " + field);
          }
          return;
        }
        // 确定是否是必须
        boolean required = determineRequiredStatus(ann);
        currElements.add(new AutowiredFieldElement(field, required));
      }
    });

    // 逐个方法扫描
    ReflectionUtils.doWithLocalMethods(targetClass, method -> {
      // 桥接方法，暂时忽略
      Method bridgedMethod = BridgeMethodResolver.findBridgedMethod(method);
      if (!BridgeMethodResolver.isVisibilityBridgeMethodPair(method, bridgedMethod)) {
        return;
      }
      MergedAnnotation<?> ann = findAutowiredAnnotation(bridgedMethod);
      if (ann != null && method.equals(ClassUtils.getMostSpecificMethod(method, clazz))) {
        // 静态方法忽略
        if (Modifier.isStatic(method.getModifiers())) {
          if (logger.isInfoEnabled()) {
            logger.info("Autowired annotation is not supported on static methods: " + method);
          }
          return;
        }
        // 注入的方法必须要有一个参数
        if (method.getParameterCount() == 0) {
          if (logger.isInfoEnabled()) {
            logger.info("Autowired annotation should only be used on methods with parameters: " +
                        method);
          }
        }
        // 确定是否必须
        boolean required = determineRequiredStatus(ann);
        // 为该方法查找对应的属性描述符
        PropertyDescriptor pd = BeanUtils.findPropertyForMethod(bridgedMethod, clazz);
        currElements.add(new AutowiredMethodElement(method, required, pd));
      }
    });

    elements.addAll(0, currElements);
    targetClass = targetClass.getSuperclass();
  }
  while (targetClass != null && targetClass != Object.class);

  // 搞定收工
  return InjectionMetadata.forElements(elements, clazz);
}

// 从一个字段或方法查找注解
private MergedAnnotation<?> findAutowiredAnnotation(AccessibleObject ao) {
  MergedAnnotations annotations = MergedAnnotations.from(ao);
  // 那三个注解依次检查一遍，有就返回
  for (Class<? extends Annotation> type : this.autowiredAnnotationTypes) {
    MergedAnnotation<?> annotation = annotations.get(type);
    if (annotation.isPresent()) {
      return annotation;
    }
  }
  return null;
}

protected boolean determineRequiredStatus(MergedAnnotation<?> ann) {
  // The following (AnnotationAttributes) cast is required on JDK 9+.
  return determineRequiredStatus((AnnotationAttributes)
                                 ann.asMap(mergedAnnotation -> new AnnotationAttributes(mergedAnnotation.getType())));
}

protected boolean determineRequiredStatus(AnnotationAttributes ann) {
  // this.requiredParameterName写死了是required字符串
  // this.requiredParameterValue写死了是true
  // 如果注解不包含required属性，或者required属性为true，则必须，否则非必须
  return (!ann.containsKey(this.requiredParameterName) ||
          this.requiredParameterValue == ann.getBoolean(this.requiredParameterName));
}
```

- 三个注解`@Autowired、@Value、@Inject`，作用在字段或构造方法上都可以；甚至可以作用在静态字段和方法上，只不过会被忽略而已
- 作用在方法上时，该方法必须拥有参数，方法不应是setter方法
- 决定注入是否必须的条件：未指定required时默认为必须，否则指定什么就是什么

然后我们来看第二个扩展点：`postProcessProperties（）`，它是执行注入的地方

```java
public PropertyValues postProcessProperties(PropertyValues pvs, Object bean, String beanName) {
  // 这和字段扫描时调用的一个方法，不过这里会命中缓存
  InjectionMetadata metadata = findAutowiringMetadata(beanName, bean.getClass(), pvs);
  // 执行注入逻辑
  metadata.inject(bean, beanName, pvs);
  return pvs;
}

public void inject(Object target, @Nullable String beanName, @Nullable PropertyValues pvs) throws Throwable {
  // checkedElements和injectedElements的含义忽略，这里关注注入即可
  Collection<InjectedElement> checkedElements = this.checkedElements;
  Collection<InjectedElement> elementsToIterate = (checkedElements != null ? checkedElements : this.injectedElements);
  if (!elementsToIterate.isEmpty()) {
    for (InjectedElement element : elementsToIterate) {
      // 注入
      element.inject(target, beanName, pvs);
    }
  }
}

protected void inject(Object target, @Nullable String requestingBeanName, @Nullable PropertyValues pvs) throws Throwable {
  if (this.isField) {
    Field field = (Field) this.member;
    ReflectionUtils.makeAccessible(field);
    // 是字段时，按照字段注入，注入的资源来源比较多，这里可以当它是从容器中取的就好
    field.set(target, getResourceToInject(target, requestingBeanName));
  } else {
    ... ...
    try {
      Method method = (Method) this.member;
      ReflectionUtils.makeAccessible(method);
      // 方法注入
      method.invoke(target, getResourceToInject(target, requestingBeanName));
    } catch (InvocationTargetException ex) {
      throw ex.getTargetException();
    }
  }
}
```

- 看起来，自动注入的方法，只允许有一个参数。

最后来看它是如何决定构造方法以干预实例创建的：`determineCandidateConstructors()`

```java
public Constructor<?>[] determineCandidateConstructors(Class<?> beanClass, final String beanName) throws BeanCreationException {
  // 缓存查询
  if (!this.lookupMethodsChecked.contains(beanName)) {
    // 
    if (AnnotationUtils.isCandidateClass(beanClass, Lookup.class)) {
      Class<?> targetClass = beanClass;
      do {
        ReflectionUtils.doWithLocalMethods(targetClass, method -> {
          // 获取Lookup注解
          Lookup lookup = method.getAnnotation(Lookup.class);
          if (lookup != null) {
            LookupOverride override = new LookupOverride(method, lookup.value());
            RootBeanDefinition mbd = (RootBeanDefinition)this.beanFactory.getMergedBeanDefinition(beanName);
            // 将Lookup注解的方法添加到overrides中
            mbd.getMethodOverrides().addOverride(override);
          }
        });
        targetClass = targetClass.getSuperclass();
      }
      while (targetClass != null && targetClass != Object.class);
    }
    this.lookupMethodsChecked.add(beanName);
  }

  candidateConstructors = this.candidateConstructorsCache.get(beanClass);
  if (candidateConstructors == null) {
    Constructor<?>[] rawCandidates;
    // 反射获取所有的构造器
    rawCandidates = beanClass.getDeclaredConstructors();
    List<Constructor<?>> candidates = new ArrayList<>(rawCandidates.length);
    Constructor<?> requiredConstructor = null;
    Constructor<?> defaultConstructor = null;
    // 获取主构造方法，这里主要是考虑Kotlin的主构造方法
    Constructor<?> primaryConstructor = BeanUtils.findPrimaryConstructor(beanClass);
    int nonSyntheticConstructors = 0;
    for (Constructor<?> candidate : rawCandidates) {
      if (!candidate.isSynthetic()) {
        nonSyntheticConstructors++;
      } else if (primaryConstructor != null) {
        continue;
      }
      // 查看构造方法上是否存在Autowired、Value、Inject注解
      MergedAnnotation<?> ann = findAutowiredAnnotation(candidate);
      if (ann == null) {
        // 获取用户的类：这里是考虑代理类，获取被代理的类
        Class<?> userClass = ClassUtils.getUserClass(beanClass);
        if (userClass != beanClass) {
          try {
            Constructor<?> superCtor = userClass.getDeclaredConstructor(candidate.getParameterTypes());
            // 查看该构造方法上是否存在Autowired、Value、Inject注解
            ann = findAutowiredAnnotation(superCtor);
          } catch (NoSuchMethodException ex) {
            // Simply proceed, no equivalent superclass constructor found...
          }
        }
      }
      if (ann != null) {
        // 查看注解是否指定required参数
        boolean required = determineRequiredStatus(ann);
        if (required) {
          requiredConstructor = candidate;
        }
        // 只有有被那三个注解注解的构造器才会被加入candidates
        candidates.add(candidate);
      } else if (candidate.getParameterCount() == 0) {
        // 默认构造器：无参构造器
        defaultConstructor = candidate;
      }
    }
    if (!candidates.isEmpty()) {
      // 有被注解的构造方法，就返回
      ... ...
      candidateConstructors = candidates.toArray(new Constructor<?>[0]);
    } else if (rawCandidates.length == 1 && rawCandidates[0].getParameterCount() > 0) {
      // 就一个有参构造方法时，直接取
      candidateConstructors = new Constructor<?>[] {rawCandidates[0]};
    } else if (nonSyntheticConstructors == 2 && primaryConstructor != null &&
               defaultConstructor != null && !primaryConstructor.equals(defaultConstructor)) {
      // 主构造方法和默认构造方法
      candidateConstructors = new Constructor<?>[] {primaryConstructor, defaultConstructor};
    } else if (nonSyntheticConstructors == 1 && primaryConstructor != null) {
      // 主构造方法
      candidateConstructors = new Constructor<?>[] {primaryConstructor};
    } else {
      // 莫有
      candidateConstructors = new Constructor<?>[0];
    }
    this.candidateConstructorsCache.put(beanClass, candidateConstructors);
  }
  return (candidateConstructors.length > 0 ? candidateConstructors : null);
}
```

- 该方法做了两件事：处理`@Lookup`注解、处理候选构造方法。关于`@Lookup`注解：https://www.baeldung.com/spring-lookup，它注解在方法上，容器会根据其返回值从容器中寻找对应的Bean

总结一下，`AutowiredAnnotationBeanPostProcessor`做了以下事情

1. 被`@Autowired、@Value、@Inject`注解的字段，会注入对应类型的实例；对被注解的方法，会将方法的参数注入对应类型的实例
2. 被`@Lookup`注解的方法，返回值将不会去方法真是返回的，而是返回类型对应的容器内的Bean实例

### RequiredAnnotationBeanPostProcessor

> 先说明：`@Required`注解已经过时了，现在推荐的使用方式是使用构造器注入，或实现自定义的`InitializingBean`。

![image-20211130112452213](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211130112452213.png)

其关键逻辑比较简单：检查被`@Required`注解的字段，是否都已经找到值准备注入，如果这个时候还没有值，就会报违反“必须”的错误。

```java
public PropertyValues postProcessPropertyValues(PropertyValues pvs, PropertyDescriptor[] pds, Object bean, String beanName) {
  // 判断是否应该忽略当前bean的处理
  if (!shouldSkip(this.beanFactory, beanName)) {
    List<String> invalidProperties = new ArrayList<>();
    // 遍历pds，pds是当前bean的所有属性的描述符
    for (PropertyDescriptor pd : pds) {
      // 如果属性描述符上存在@Required注解，但pvs中却不包含该属性对应的值，则该属性会报错。
      if (isRequiredProperty(pd) && !pvs.contains(pd.getName())) {
        invalidProperties.add(pd.getName());
      }
    }
    // 存在必须但没有值的字段，报错
    if (!invalidProperties.isEmpty()) {
      throw new BeanInitializationException(buildExceptionMessage(invalidProperties, beanName));
    }
  }
  return pvs;
}

protected boolean shouldSkip(@Nullable ConfigurableListableBeanFactory beanFactory, String beanName) {
  // 容器中没有该bean，忽略
  if (beanFactory == null || !beanFactory.containsBeanDefinition(beanName)) {
    return false;
  }
  BeanDefinition beanDefinition = beanFactory.getBeanDefinition(beanName);
  // 存在该bean的工厂bean，不应该忽略
  if (beanDefinition.getFactoryBeanName() != null) {
    return true;
  }
  // 存在skipRequiredCheck属性，则忽略
  Object value = beanDefinition.getAttribute(SKIP_REQUIRED_CHECK_ATTRIBUTE);
  return (value != null && (Boolean.TRUE.equals(value) || Boolean.parseBoolean(value.toString())));
}

protected boolean isRequiredProperty(PropertyDescriptor propertyDescriptor) {
  Method setter = propertyDescriptor.getWriteMethod();
  // getRequiredAnnotationType()方法获取的就是@Required注解
  return (setter != null && AnnotationUtils.getAnnotation(setter, getRequiredAnnotationType()) != null);
}
```

### InitDestroyAnnotationBeanPostProcessor

它其实和`AutowiredAnnotationBeanPostProcessor`类似，在`BeanDefinition`准备好后查找`@PostConstruct、@PreDestroy`，后在对应的时机调用查找好的方法。

![image-20211130113548755](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211130113548755.png)

首先是查找这些方法的点：`postProcessMergedBeanDefinition()`

```java
public void postProcessMergedBeanDefinition(RootBeanDefinition beanDefinition, Class<?> beanType, String beanName) {
  // 查找生命周期元数据，即那两个注解对应的方法
  LifecycleMetadata metadata = findLifecycleMetadata(beanType);
  // 忽略
  metadata.checkConfigMembers(beanDefinition);
}

private LifecycleMetadata findLifecycleMetadata(Class<?> clazz) {
  ...
  ...
  return buildLifecycleMetadata(clazz);
}

private LifecycleMetadata buildLifecycleMetadata(final Class<?> clazz) {
  // this.initAnnotationType 即 @PostConstruct; this.destroyAnnotationType 即 @PreDestroy
  if (!AnnotationUtils.isCandidateClass(clazz, Arrays.asList(this.initAnnotationType, this.destroyAnnotationType))) {
    return this.emptyLifecycleMetadata;
  }

  List<LifecycleElement> initMethods = new ArrayList<>();
  List<LifecycleElement> destroyMethods = new ArrayList<>();
  Class<?> targetClass = clazz;

  do {
    final List<LifecycleElement> currInitMethods = new ArrayList<>();
    final List<LifecycleElement> currDestroyMethods = new ArrayList<>();

    // 逐个方法遍历
    ReflectionUtils.doWithLocalMethods(targetClass, method -> {
      // 查找所有被@PostConstruct注解的方法
      if (this.initAnnotationType != null && method.isAnnotationPresent(this.initAnnotationType)) {
        LifecycleElement element = new LifecycleElement(method);
        currInitMethods.add(element);
      }
      // 查找素有被@PreDestroy注解的方法
      if (this.destroyAnnotationType != null && method.isAnnotationPresent(this.destroyAnnotationType)) {
        currDestroyMethods.add(new LifecycleElement(method));
      }
    });

    initMethods.addAll(0, currInitMethods);
    destroyMethods.addAll(currDestroyMethods);
    targetClass = targetClass.getSuperclass();
  }
  while (targetClass != null && targetClass != Object.class);

  // 将这些方法组包装成一个LifecycleMetadata予以返回
  return (initMethods.isEmpty() && destroyMethods.isEmpty() ? this.emptyLifecycleMetadata :
          new LifecycleMetadata(clazz, initMethods, destroyMethods));
}
```

然后是`@PostConstruct`的执行点：`postProcessBeforeInitialization()`

```java
public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
  LifecycleMetadata metadata = findLifecycleMetadata(bean.getClass());
  ... ...
  // 调用初始化方法们
  metadata.invokeInitMethods(bean, beanName);
  ... ...
  return bean;
}

public void invokeInitMethods(Object target, String beanName) throws Throwable {
  Collection<LifecycleElement> checkedInitMethods = this.checkedInitMethods;
  Collection<LifecycleElement> initMethodsToIterate =
    (checkedInitMethods != null ? checkedInitMethods : this.initMethods);
  if (!initMethodsToIterate.isEmpty()) {
    // 调用初始化方法们
    for (LifecycleElement element : initMethodsToIterate) {
      element.invoke(target);
    }
  }
}
```

最后是`@PreDestroy`的执行点：`postProcessBeforeDestruction()`

```java
@Override
public void postProcessBeforeDestruction(Object bean, String beanName) throws BeansException {
  LifecycleMetadata metadata = findLifecycleMetadata(bean.getClass());
  ... ...
  // 调用销毁方法们
  metadata.invokeDestroyMethods(bean, beanName);
  ... ...
}

public void invokeDestroyMethods(Object target, String beanName) throws Throwable {
  Collection<LifecycleElement> checkedDestroyMethods = this.checkedDestroyMethods;
  Collection<LifecycleElement> destroyMethodsToUse =
    (checkedDestroyMethods != null ? checkedDestroyMethods : this.destroyMethods);
  if (!destroyMethodsToUse.isEmpty()) {
    for (LifecycleElement element : destroyMethodsToUse) {
      element.invoke(target);
    }
  }
}
```

从这个源码看来

- 被`@PostConstruct、@PreDesctroy`注解的方法可以有多个，他们会依次执行
- 被它们注解的方法需要是无参的，就算有参，也不会给你传值

### ScheduledAnnotationBeanPostProcessor

![image-20211130145022089](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211130145022089.png)

#### 源码分析

大致描述一下它的工作原理：

- 在单例初始化完成后，或收到`ContextRefreshEvent`事件后，该`Processor`需要准备好，准备的内容包括初始化用于指定定时任务的`Scheduler`，持有任务元数据的`ScheduledTaskRegistrar`；
- 在实例初始化完成后，从容器中查找带有`@Scheduled、@Schedules`注解的方法，解析定时参数，构建成任务，然后提交执行；
- 在单个实例销毁前，从缓存中删除该实例对应的定时任务
- 在容器销毁前，清空缓存的定时任务

然后，我们来看准备阶段和检测阶段的代码，结束阶段就忽略掉了。先是准备阶段

```java
public ScheduledAnnotationBeanPostProcessor() {
  // ScheduledTaskRegistrar是实例初始化时创建的
  this.registrar = new ScheduledTaskRegistrar();
}

public void onApplicationEvent(ContextRefreshedEvent event) {
  if (event.getApplicationContext() == this.applicationContext) {
    // 先完成定时器和定时注册器的准备工作
    finishRegistration();
  }
}

private void finishRegistration() {
  if (this.scheduler != null) {
    this.registrar.setScheduler(this.scheduler);
  }

  if (this.beanFactory instanceof ListableBeanFactory) {
    // 从容器中查找SchedulingConfigurer实例，用来配置任务注册器
    Map<String, SchedulingConfigurer> beans = ((ListableBeanFactory) this.beanFactory).getBeansOfType(SchedulingConfigurer.class);
    List<SchedulingConfigurer> configurers = new ArrayList<>(beans.values());
    AnnotationAwareOrderComparator.sort(configurers);
    for (SchedulingConfigurer configurer : configurers) {
      configurer.configureTasks(this.registrar);
    }
  }

  if (this.registrar.hasTasks() && this.registrar.getScheduler() == null) {
    Assert.state(this.beanFactory != null, "BeanFactory must be set to find scheduler by type");
    try {
      // 从容器中查找TaskScheduler，按类型查找
      this.registrar.setTaskScheduler(resolveSchedulerBean(this.beanFactory, TaskScheduler.class, false));
    } catch (NoUniqueBeanDefinitionException ex) {
      try {
        // 如果不止一个，则按照名称taskScheduler来找
        this.registrar.setTaskScheduler(resolveSchedulerBean(this.beanFactory, TaskScheduler.class, true));
      } catch (NoSuchBeanDefinitionException ex2) {
      }
    } catch (NoSuchBeanDefinitionException ex) {
      try {
        // 如果找不到，则查找ScheduledExecutorService类型的Bean
        this.registrar.setScheduler(resolveSchedulerBean(this.beanFactory, ScheduledExecutorService.class, false));
      } catch (NoUniqueBeanDefinitionException ex2) {
        try {
          // 如果不止一个，则按照名称taskScheduler来找
          this.registrar.setScheduler(resolveSchedulerBean(this.beanFactory, ScheduledExecutorService.class, true));
        } catch (NoSuchBeanDefinitionException ex3) {
        }
      } catch (NoSuchBeanDefinitionException ex2) {
        // 实在找不到，就算了，也不报错
      }
    }
  }

  this.registrar.afterPropertiesSet();
}
```

然后来看检测阶段

```java
public Object postProcessAfterInitialization(Object bean, String beanName) {
  // 获取最终的类（如果是代理类，则获取被代理类）
  Class<?> targetClass = AopProxyUtils.ultimateTargetClass(bean);
  // this.nonAnnotatedClasses是个缓存
  // 判断目标类是否被Scheduled或Schedules注解
  if (!this.nonAnnotatedClasses.contains(targetClass) &&
      AnnotationUtils.isCandidateClass(targetClass, Arrays.asList(Scheduled.class, Schedules.class))) {
    // 获取所有被Scheduled注解的方法
    Map<Method, Set<Scheduled>> annotatedMethods = MethodIntrospector.selectMethods(targetClass, (MethodIntrospector.MetadataLookup<Set<Scheduled>>) method -> {
      Set<Scheduled> scheduledMethods = AnnotatedElementUtils.getMergedRepeatableAnnotations(method, Scheduled.class, Schedules.class);
      return (!scheduledMethods.isEmpty() ? scheduledMethods : null);
    });
    if (annotatedMethods.isEmpty()) {
      // 缓存填充，为的是下次遇到该类时可以快速略过，提升性能
      this.nonAnnotatedClasses.add(targetClass);
    } else {
      // 处理哪些定时方法
      annotatedMethods.forEach((method, scheduledMethods) -> scheduledMethods.forEach(scheduled -> processScheduled(scheduled, method, bean)));
    }
  }
  return bean;
}

protected void processScheduled(Scheduled scheduled, Method method, Object bean) {
  try {
    // 创建Runnable任务
    Runnable runnable = createRunnable(bean, method);
    boolean processedSchedule = false;

    Set<ScheduledTask> tasks = new LinkedHashSet<>(4);

    // Determine initial delay：解析出首次执行的延迟时间
    long initialDelay = scheduled.initialDelay();
    String initialDelayString = scheduled.initialDelayString();
    if (StringUtils.hasText(initialDelayString)) {
      Assert.isTrue(initialDelay < 0, "Specify 'initialDelay' or 'initialDelayString', not both");
      if (this.embeddedValueResolver != null) {
        initialDelayString = this.embeddedValueResolver.resolveStringValue(initialDelayString);
      }
      if (StringUtils.hasLength(initialDelayString)) {
        try {
          initialDelay = parseDelayAsLong(initialDelayString);
        } catch (RuntimeException ex) {
        }
      }
    }

    // 解析cron表达式
    String cron = scheduled.cron();
    if (StringUtils.hasText(cron)) {
      String zone = scheduled.zone();
      if (this.embeddedValueResolver != null) {
        cron = this.embeddedValueResolver.resolveStringValue(cron);
        zone = this.embeddedValueResolver.resolveStringValue(zone);
      }
      if (StringUtils.hasLength(cron)) {
        Assert.isTrue(initialDelay == -1, "'initialDelay' not supported for cron triggers");
        processedSchedule = true;
        if (!Scheduled.CRON_DISABLED.equals(cron)) {
          TimeZone timeZone;
          if (StringUtils.hasText(zone)) {
            timeZone = StringUtils.parseTimeZoneString(zone);
          } else {
            timeZone = TimeZone.getDefault();
          }
          // 注册Cron任务
          tasks.add(this.registrar.scheduleCronTask(new CronTask(runnable, new CronTrigger(cron, timeZone))));
        }
      }
    }

    // At this point we don't need to differentiate between initial delay set or not anymore
    if (initialDelay < 0) {
      initialDelay = 0;
    }

    // 解析fixdelay的情况，即一次性任务
    long fixedDelay = scheduled.fixedDelay();
    if (fixedDelay >= 0) {
      Assert.isTrue(!processedSchedule, errorMessage);
      processedSchedule = true;
      // 添加FixedDelay任务
      tasks.add(this.registrar.scheduleFixedDelayTask(new FixedDelayTask(runnable, fixedDelay, initialDelay)));
    }
    String fixedDelayString = scheduled.fixedDelayString();
    if (StringUtils.hasText(fixedDelayString)) {
      if (this.embeddedValueResolver != null) {
        fixedDelayString = this.embeddedValueResolver.resolveStringValue(fixedDelayString);
      }
      if (StringUtils.hasLength(fixedDelayString)) {
        Assert.isTrue(!processedSchedule, errorMessage);
        processedSchedule = true;
        try {
          fixedDelay = parseDelayAsLong(fixedDelayString);
        } catch (RuntimeException ex) {
        }
        // 添加FixedDelay任务
        tasks.add(this.registrar.scheduleFixedDelayTask(new FixedDelayTask(runnable, fixedDelay, initialDelay)));
      }
    }

    // 解析固定间隔执行的情况
    long fixedRate = scheduled.fixedRate();
    if (fixedRate >= 0) {
      Assert.isTrue(!processedSchedule, errorMessage);
      processedSchedule = true;
      // 添加FixedRate任务
      tasks.add(this.registrar.scheduleFixedRateTask(new FixedRateTask(runnable, fixedRate, initialDelay)));
    }
    String fixedRateString = scheduled.fixedRateString();
    if (StringUtils.hasText(fixedRateString)) {
      if (this.embeddedValueResolver != null) {
        fixedRateString = this.embeddedValueResolver.resolveStringValue(fixedRateString);
      }
      if (StringUtils.hasLength(fixedRateString)) {
        Assert.isTrue(!processedSchedule, errorMessage);
        processedSchedule = true;
        try {
          fixedRate = parseDelayAsLong(fixedRateString);
        } catch (RuntimeException ex) {
        }
        // 添加FixedRate任务
        tasks.add(this.registrar.scheduleFixedRateTask(new FixedRateTask(runnable, fixedRate, initialDelay)));
      }
    }

    // Finally register the scheduled tasks
    synchronized (this.scheduledTasks) {
      Set<ScheduledTask> regTasks = this.scheduledTasks.computeIfAbsent(bean, key -> new LinkedHashSet<>(4));
      regTasks.addAll(tasks);
    }
  } catch (IllegalArgumentException ex) {
    ... ...
  }
}
```

至此，`Processor`的任务结束了，我们来看看这些任务的执行逻辑，以`ScheduledTaskRegistrar.scheduleFixedRateTask()`为例：

```java
public ScheduledTask scheduleFixedRateTask(FixedRateTask task) {
  ScheduledTask scheduledTask = this.unresolvedTasks.remove(task);
  boolean newTask = false;
  if (scheduledTask == null) {
    scheduledTask = new ScheduledTask(task);
    newTask = true;
  }
  if (this.taskScheduler != null) {
    if (task.getInitialDelay() > 0) {
      Date startTime = new Date(this.taskScheduler.getClock().millis() + task.getInitialDelay());
      // 调用的是taskScheduler的scheduleAtFixedRate
      scheduledTask.future = this.taskScheduler.scheduleAtFixedRate(task.getRunnable(), startTime, task.getInterval());
    } else {
      scheduledTask.future = this.taskScheduler.scheduleAtFixedRate(task.getRunnable(), task.getInterval());
    }
  } else {
    addFixedRateTask(task);
    this.unresolvedTasks.put(task, scheduledTask);
  }
  return (newTask ? scheduledTask : null);
}

public ScheduledFuture<?> scheduleAtFixedRate(Runnable task, Date startTime, long period) {
  // 获取ScheduledExecutorService
  ScheduledExecutorService executor = getScheduledExecutor();
  long initialDelay = startTime.getTime() - this.clock.millis();
  try {
    // 提交固定速率的任务
    return executor.scheduleAtFixedRate(errorHandlingTask(task, true), initialDelay, period, TimeUnit.MILLISECONDS);
  } catch (RejectedExecutionException ex) {
    throw new TaskRejectedException("Executor [" + executor + "] did not accept task: " + task, ex);
  }
}
```

#### 定时器如何生效

定时器默认不生效，当需要使用时，通过`@EnableScheduling`引入，其最终结果是向容器中声明了`ScheduledAnnotationBeanPostProcessor`实例。

```java
// EnableScheduling注解引入了SchedulingConfiguration配置类
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Import(SchedulingConfiguration.class)
@Documented
public @interface EnableScheduling {

}

// SchedulingConfiguration配置类创建了ScheduledAnnotationBeanPostProcessor实例Bean，而它，我们上面已经分析过了
@Configuration(proxyBeanMethods = false)
@Role(BeanDefinition.ROLE_INFRASTRUCTURE)
public class SchedulingConfiguration {

  @Bean(name = TaskManagementConfigUtils.SCHEDULED_ANNOTATION_PROCESSOR_BEAN_NAME)
  @Role(BeanDefinition.ROLE_INFRASTRUCTURE)
  public ScheduledAnnotationBeanPostProcessor scheduledAnnotationProcessor() {
    return new ScheduledAnnotationBeanPostProcessor();
  }

}
```

### 其它

还有两个非常重要的内容：`BeanValidationPostProcessor`、AOP相关处理器，涉及内容较多，将单独来看，这里忽略。

## 总结

本文介绍了通过`BeanPostProcessor`实现的几个关键内容：配置绑定类、事件监听器的侦测、自动注入的实现、初始化和销毁注解的实现、定时任务的实现等。
