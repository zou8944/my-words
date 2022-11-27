---
created_at: 2021-12-11 15:59:58
updated_at: 2021-12-11 15:59:58
tags:
  - Spring
  - 源码剖析
---

> 截止目前，我们已经写了四篇关于Spring源码解析的文章，但它们只关注了Spring和SpringBoot的启动流程，并没有回答我们日常使用中的核心问题——自动配置的实现原理，本文进行探索

<!-- more -->

在前文“Spring源码剖析 - BeanDefinition”中扫描Bean定义一节中，我们漏掉了一个关键方法调用，其调用路径如下

```shell
-> org.springframework.context.annotation.AnnotationConfigApplicationContext
   #AnnotationConfigApplicationContext(java.lang.Class<?>...)
-> org.springframework.context.annotation.AnnotationConfigApplicationContext
   #AnnotationConfigApplicationContext()
-> org.springframework.context.annotation.AnnotatedBeanDefinitionReader
   #AnnotatedBeanDefinitionReader(org.springframework.beans.factory.support.BeanDefinitionRegistry)
-> org.springframework.context.annotation.AnnotatedBeanDefinitionReader
   #AnnotatedBeanDefinitionReader(org.springframework.beans.factory.support.BeanDefinitionRegistry, org.springframework.core.env.Environment)
-> org.springframework.context.annotation.AnnotationConfigUtils
   #registerAnnotationConfigProcessors(org.springframework.beans.factory.support.BeanDefinitionRegistry)
-> org.springframework.context.annotation.AnnotationConfigUtils
   #registerAnnotationConfigProcessors(org.springframework.beans.factory.support.BeanDefinitionRegistry, java.lang.Object)
```

即，在`AnnotationConfigApplicationContext`执行构造方法时，调用`AnnotationConfigUtils.registerAnnotationConfigProcessors()`，注册了一系列注解处理器，具体来说，有

- `ConfigurationClassPostProcessor`

  用于处理配置相关的各种注解

- `AutowiredAnnotationBeanPostProcessor`

  用于处理自动注入相关的注解，如`@Autowired`、`@Value`、`@Inject`

- `CommonAnnotationBeanPostProcessor`

  用于处理一些通用注解，比如`@Lazy`、`@Primary`、`PreDestroy`等

- `PersistenceAnnotationBeanPostProcessor`

  用于处理JPA相关注解

- `EventListenerMethodProcessor`

  用于处理`@EventListener`，即把方法注册成监听器

- `DefaultEventListenerFactory`

  结合`EventListenerMethodProcessor`使用，该工厂输入方法，可创建出一个`ApplicationListener`类

本文我们重点关注配置相关的注解

## 概览

![image-20211210152720643](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211210152720643.png)

`ConfigurationClassPostProcessor`继承结构如上，属于容器构建阶段的处理器，我们再复习一下它的两个父接口的作用

- `BeanFactoryPostProcessor`：在容器初始化之后，对容器做一些自定义操作。具体时机是：`BeanDefinition`加载完成之后，`Bean`实例化之前。

- `BeanDefinitionRegistryPostProcessor`：在容器初始化完成之后，`BeanFactoryPostProcessor`执行之前对容器做一些自定义操作。

而`ConfigurationClassPostProcessor`在这两个时机分别做了两件事

- 容器初始化完成后，`BeanFactoryPostProcessor`调用前，从`@Configuration`注解的类中加载Bean定义，然后向容器注册。

  这一点是本文的重点 ，逻辑位于`org.springframework.context.annotation.ConfigurationClassPostProcessor#processConfigBeanDefinitions`，进一步的确切逻辑位于

  - 注解解析：
     -> `org.springframework.context.annotation.ConfigurationClassParser#parse(java.util.Set<org.springframework.beans.factory.config.BeanDefinitionHolder>)`

    -> `org.springframework.context.annotation.ConfigurationClassParser#doProcessConfigurationClass`

  - `BeanDefinition`注册

    -> `org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader#loadBeanDefinitions`。

  - 其它逻辑无助于理解，一概忽略

- 容器初始化完成后，对所有`@Configuration`注解标识的`BeanDefinition`进行增强

  这一点不是重点，大概描述一下：使用的是CGLib的Enhancer API。添加了如下几个增强回调

  - `BeanMethodInterceptor`：拦截所有`@Bean`注解的方法
  - `BeanFactoryAwareMethodInterceptor`：拦截所有实现了`BeanFactoryAware`的`@Configuration`类的`setBeanFactory()`方法，目的是将容器注入

## 注解解析

我们从`ConfigurationClassParser.doProcessConfigurationClass`的解析逻辑中，分析如下几个注解的工作原理。

### @Conditional

该注解用于条件配置，即满足条件时才生效，否则被忽略，它的实现由`ConditionEvaluator`完成。使用的地方包括

- `ConfigurationClassParser.processConfigurationClass()`，对配置类有效。
- `ConfigurationClassBeanDefinitionReader#loadBeanDefinitionsForBeanMethod`，加载Bean时有效，即作用在`@Bean`注解的方法上

逻辑落地在`ConditionEvaluator.shouldSkip()`

1. 如果没有被`@Conditional`注解，则不应被跳过
2. 获取`@Conditional`注解的属性值，即其指定的`Condition`类，可能有多个
3. 依次调用这些`Condition`类的`matches()`方法，只要有一个匹配，则判定为应该被跳过，可见，多条件是与的关系

SpringBoot还定义了`ConditionalOnClass`、`ConditionalOnMissingBean`之类的注解，其实看一眼他们的定义就知道。

```java
@Target({ ElementType.TYPE, ElementType.METHOD })
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Conditional(OnClassCondition.class)
public @interface ConditionalOnClass {

	Class<?>[] value() default {};

	String[] name() default {};

}
```

比如上面这个注解，它是`@Conditional`注解加上`OnClassCondition`这个条件构成的。而在`OnClassCondition`的匹配方法的逻辑如下（有继承关系，`matches()`方法在父类，这里只给出核心逻辑）：类加载器能加载出来就匹配，否则就不匹配

```java
public ConditionOutcome getMatchOutcome(ConditionContext context, AnnotatedTypeMetadata metadata) {
  ClassLoader classLoader = context.getClassLoader();
  ConditionMessage matchMessage = ConditionMessage.empty();
  // 获取ConditionalOnClass指定的那些类名
  List<String> onClasses = getCandidates(metadata, ConditionalOnClass.class);
  if (onClasses != null) {
    // 用ClassLoader加载指定的类名，加载不出来则说明缺失
    List<String> missing = filter(onClasses, ClassNameFilter.MISSING, classLoader);
    // 缺失就报不匹配
    if (!missing.isEmpty()) {
      return ConditionOutcome.noMatch(ConditionMessage.forCondition(ConditionalOnClass.class)
                                      .didNotFind("required class", "required classes").items(Style.QUOTE, missing));
    }
  }
  // 否则就是匹配
  return ConditionOutcome.match(matchMessage);
}
```

### @PropertySource

该注解能够将指定的properties文件加载到容器的Environment中，[使用参考](https://www.baeldung.com/properties-with-spring)。

通过源码解读可以看出它的逻辑

- 读取`@PropertySource`的value值，作为配置文件的位置location
- 解析`location`中的占位符，这意味着location中可以存在动态字段
- 使用`resourceLoader`将location解析成`Resource`对象
- 使用`PropertySourceFactory`创建`PropertySource`对象，并加入`Environment`

这里有一个能够自定义的东西：属性源工厂，如果我们指定自己的属性源工厂，则能够按照自己的需求解析，因此我们能够自定义出解析yaml文件的逻辑。默认是`DefaultPropertySourceFactory`，它创建的是一个`ResourcePropertySource`。

我们大致看一下它的核心逻辑

```java
// 解析注解的属性：name、encoding、value、ignoreResourceNotFound、factory
String name = propertySource.getString("name");
... ...
String encoding = propertySource.getString("encoding");
... ...
String[] locations = propertySource.getStringArray("value");
... ...
boolean ignoreResourceNotFound = propertySource.getBoolean("ignoreResourceNotFound");
Class<? extends PropertySourceFactory> factoryClass = propertySource.getClass("factory");
// 如果有指定factory，构建该工厂对象，否则，使用默认的工厂
PropertySourceFactory factory = (factoryClass == PropertySourceFactory.class ? DEFAULT_PROPERTY_SOURCE_FACTORY : BeanUtils.instantiateClass(factoryClass));

for (String location : locations) {
  ... ...
  // 解析location中的占位符
  String resolvedLocation = this.environment.resolveRequiredPlaceholders(location);
  // 从文件系统中加载出来
  Resource resource = this.resourceLoader.getResource(resolvedLocation);
  // factory创建出属性源，加入environment
  addPropertySource(factory.createPropertySource(name, new EncodedResource(resource, encoding)));
  ... ...
}
```

### @ComponentScan

该注解用于扫描指定包、类所属的包下的Bean定义，其核心逻辑挂在`ComponentScanAnnotationParser.parse()`上，如下

- 构建`ClassPathBeanDefinitionScanner`扫描器，用于执行Bean定义扫描
- 读取`@ComponentScan`的各类属性，写入扫描器，属性包括
  - `nameGenerator`：Bean名生成器
  - `scopedProxy`：scopedProxy的方式：不代理、JDK代理、cglib代理，关于scopedProxy，可以[参考这里](https://stackoverflow.com/questions/14371335/spring-scoped-proxy-bean)。大致来说，就是当scope范围更宽的bean1引用scope范围较小的bean2时，由于他们的作用范围不一致，导致bean1的生存时间大于bean2的生存时间，直接引用会发生问题，此时可以将bean2用一个代理包装起来，由代理负责引用实际的Bean，每当bean2的生命结束时，由代理自动创建新的实例，对bean1做到透明。
  - `scopeResolver`：Scope解析器
  - `resourcePattern`：扫描目标文件的通配符，如`*/**/class`
  - `includeFilters`：过滤器
  - `excludeFilters`：过滤器
  - `lazyInit`：延迟加载
  - `basePackages`：基包
  - `basePackageClasses`：基类

- 调用扫描器的扫描方法，这个在前面介绍扫描BeanDefinition时有描述过，这里不再赘述。

源码也简单，只要注意一点：如果没有指定基包或基类，就是用当前配置类所在的包作为扫描位置

```java
public Set<BeanDefinitionHolder> parse(AnnotationAttributes componentScan, final String declaringClass) {
  ClassPathBeanDefinitionScanner scanner = new ClassPathBeanDefinitionScanner(this.registry, componentScan.getBoolean("useDefaultFilters"), this.environment, this.resourceLoader);

  Class<? extends BeanNameGenerator> generatorClass = componentScan.getClass("nameGenerator");
  boolean useInheritedGenerator = (BeanNameGenerator.class == generatorClass);
  scanner.setBeanNameGenerator(useInheritedGenerator ? this.beanNameGenerator : BeanUtils.instantiateClass(generatorClass));

  ScopedProxyMode scopedProxyMode = componentScan.getEnum("scopedProxy");
  if (scopedProxyMode != ScopedProxyMode.DEFAULT) {
    scanner.setScopedProxyMode(scopedProxyMode);
  } else {
    Class<? extends ScopeMetadataResolver> resolverClass = componentScan.getClass("scopeResolver");
    scanner.setScopeMetadataResolver(BeanUtils.instantiateClass(resolverClass));
  }

  scanner.setResourcePattern(componentScan.getString("resourcePattern"));

  for (AnnotationAttributes filter : componentScan.getAnnotationArray("includeFilters")) {
    for (TypeFilter typeFilter : typeFiltersFor(filter)) {
      scanner.addIncludeFilter(typeFilter);
    }
  }
  for (AnnotationAttributes filter : componentScan.getAnnotationArray("excludeFilters")) {
    for (TypeFilter typeFilter : typeFiltersFor(filter)) {
      scanner.addExcludeFilter(typeFilter);
    }
  }

  boolean lazyInit = componentScan.getBoolean("lazyInit");
  if (lazyInit) {
    scanner.getBeanDefinitionDefaults().setLazyInit(true);
  }

  Set<String> basePackages = new LinkedHashSet<>();
  String[] basePackagesArray = componentScan.getStringArray("basePackages");
  for (String pkg : basePackagesArray) {
    String[] tokenized = StringUtils.tokenizeToStringArray(this.environment.resolvePlaceholders(pkg),
                                                           ConfigurableApplicationContext.CONFIG_LOCATION_DELIMITERS);
    Collections.addAll(basePackages, tokenized);
  }
  for (Class<?> clazz : componentScan.getClassArray("basePackageClasses")) {
    basePackages.add(ClassUtils.getPackageName(clazz));
  }
  // 如果没有指定基包或基类，就是用当前配置类所在的包作为扫描位置
  if (basePackages.isEmpty()) {
    basePackages.add(ClassUtils.getPackageName(declaringClass));
  }

  scanner.addExcludeFilter(new AbstractTypeHierarchyTraversingFilter(false, false) {
    @Override
    protected boolean matchClassName(String className) {
      return declaringClass.equals(className);
    }
  });
  return scanner.doScan(StringUtils.toStringArray(basePackages));
}
```

### @Import

该配置用于导入其它配置，定义如下

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface Import {

  /**
	 * {@link Configuration @Configuration}, {@link ImportSelector},
	 * {@link ImportBeanDefinitionRegistrar}, or regular component classes to import.
	 */
  Class<?>[] value();

}
```

如注释所言，支持导入的对象有四种

- 被`@Configuration`注解的类，即一个普通的配置类，这是最常用的。对它的处理方式就是，再当做配置类执行一遍`processConfigurationClass()`方法逻辑

- `ImportSelector`，顾名思义，导入选择器，这是一个接口，定义了要导入的资源，导入的资源依旧是这四类，但最终会是普通的注解类。

  对于该类对象的处理方式，是找出其选择的导入对象，递归执行导入逻辑

- `ImportBeanDefinitionRegistrar`，顾名思义，用于导入`BeanDefinition`注册器，其逻辑是向`ConfigurationClassBeanDefinitionReader`中注入该注册器，后面在加载`BeanDefinition`时会用到它。

#### 导入选择器

```java
if (candidate.isAssignable(ImportSelector.class)) {
  // Candidate class is an ImportSelector -> delegate to it to determine imports
  Class<?> candidateClass = candidate.loadClass();
  // 初始化选择器
  ImportSelector selector = ParserStrategyUtils.instantiateClass(candidateClass, ImportSelector.class,
                                                                 this.environment, this.resourceLoader, this.registry);
  // 排除过滤器
  Predicate<String> selectorFilter = selector.getExclusionFilter();
  ... ...
  // 调用选择器的关键方法selectImports，实际上就是一个类名数组
  String[] importClassNames = selector.selectImports(currentSourceClass.getMetadata());
  // 类名封装一下
  Collection<SourceClass> importSourceClasses = asSourceClasses(importClassNames, exclusionFilter);
  // 递归执行processImports()
  processImports(configClass, currentSourceClass, importSourceClasses, exclusionFilter, false);
}
```

所以如果导入对象是`ImportSelector`，它所做的工作其实只有选择待导入的配置对象。

#### 导入BeanDefinition集合

```java
else if (candidate.isAssignable(ImportBeanDefinitionRegistrar.class)) {
  // Candidate class is an ImportBeanDefinitionRegistrar ->
  // delegate to it to register additional bean definitions
  Class<?> candidateClass = candidate.loadClass();
  // 构建对象
  ImportBeanDefinitionRegistrar registrar = 
    ParserStrategyUtils.instantiateClass(candidateClass, ImportBeanDefinitionRegistrar.class,
                                         this.environment, this.resourceLoader, this.registry);
  // 将其当做属性加入配置类
  configClass.addImportBeanDefinitionRegistrar(registrar, currentSourceClass.getMetadata());
}
```

在读取Bean定期时是有调用的，在`ConfigurationClassBeanDefinitionReader`中可以看到，它的调用在概览中有描述，在下一节也会描述

```java
// 在类ConfigurationClassBeanDefinitionReader中
private void loadBeanDefinitionsForConfigurationClass(
  ... ...
  loadBeanDefinitionsFromImportedResources(configClass.getImportedResources());
  loadBeanDefinitionsFromRegistrars(configClass.getImportBeanDefinitionRegistrars());
}
```

#### 导入普通配置

```java
else {
  // 递归调用processConfigurationClass()，很好理解
  processConfigurationClass(candidate.asConfigClass(configClass), exclusionFilter);
}
```

#### 小结

总的来说，`@Import`原理上其实非常简单，最终目的是导入其它配置类或`BeanDefinition`集合。

### @ImportResource

该注解用于指定导入源，Spring会将这些源当做配置源进行读取，他们可以是xml、groovy，这是根据资源文件的后缀自动决定的。接口定义如下

```java
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Documented
public @interface ImportResource {

	@AliasFor("locations")
	String[] value() default {};

	@AliasFor("value")
	String[] locations() default {};

	Class<? extends BeanDefinitionReader> reader() default BeanDefinitionReader.class;

}
```

在注解扫描阶段，对它只是进行了读取

```java
AnnotationAttributes importResource = AnnotationConfigUtils.attributesFor(sourceClass.getMetadata(), ImportResource.class);
if (importResource != null) {
  // 获取位置信息
  String[] resources = importResource.getStringArray("locations");
  // 获取读取器
  Class<? extends BeanDefinitionReader> readerClass = importResource.getClass("reader");
  for (String resource : resources) {
    // 解析位置信息中的占位符
    String resolvedResource = this.environment.resolveRequiredPlaceholders(resource);
    // 注册到configClass
    configClass.addImportedResource(resolvedResource, readerClass);
  }
}
```

什么时候执行呢？和前面说的`BeanDefinition`集合一样，都是在加载阶段，后文详述。

### @Bean

该注解用在方法上，将方法的返回值构建成一个新的Bean定义，解析阶段只是向configClass注册了待加载的方法，解析阶段后文详述。

```java
// 从类中加载出所有被Bean注解的方法
Set<MethodMetadata> beanMethods = retrieveBeanMethodMetadata(sourceClass);
for (MethodMetadata methodMetadata : beanMethods) {
  // 把它们加入configClass
  configClass.addBeanMethod(new BeanMethod(methodMetadata, configClass));
}
```

此外，如果配置类实现的接口的方法有被`@Bean`注解，且该配置类实现了该方法，则该方法也会被加载为Bean。

## BeanDefinition注册

我们从`ConfigurationClassBeanDefinitionReader.loadBeanDefinitions`大致看一下加载过程中做了什么事情。

核心逻辑位于：`org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader#loadBeanDefinitionsForConfigurationClass`

```java
private void loadBeanDefinitionsForConfigurationClass(ConfigurationClass configClass, TrackedConditionEvaluator trackedConditionEvaluator) {
	... ...
  if (configClass.isImported()) {
    registerBeanDefinitionForImportedConfigurationClass(configClass);
  }
  for (BeanMethod beanMethod : configClass.getBeanMethods()) {
    loadBeanDefinitionsForBeanMethod(beanMethod);
  }

  loadBeanDefinitionsFromImportedResources(configClass.getImportedResources());
  loadBeanDefinitionsFromRegistrars(configClass.getImportBeanDefinitionRegistrars());
}
```

- 如果配置类是被导入的，则先将该配置类注册成为一个Bean定义
- 将所有被`@Bean`注解的方法构建成Bean定义
- 从`@ImportResource`指定的资源中加载Bean定义
- 从`@Import`导入的`BeanDefinitionRegistrar`中导入Bean定义

### 注册配置类本身

```java
private void registerBeanDefinitionForImportedConfigurationClass(ConfigurationClass configClass) {
  AnnotationMetadata metadata = configClass.getMetadata();
  AnnotatedGenericBeanDefinition configBeanDef = new AnnotatedGenericBeanDefinition(metadata);
	// 解析scope
  ScopeMetadata scopeMetadata = scopeMetadataResolver.resolveScopeMetadata(configBeanDef);
  configBeanDef.setScope(scopeMetadata.getScopeName());
  // 解析beanName
  String configBeanName = this.importBeanNameGenerator.generateBeanName(configBeanDef, this.registry);
  // 处理通用注解
  AnnotationConfigUtils.processCommonDefinitionAnnotations(configBeanDef, metadata);

  // 搞定收工
  BeanDefinitionHolder definitionHolder = new BeanDefinitionHolder(configBeanDef, configBeanName);
  definitionHolder = AnnotationConfigUtils.applyScopedProxyMode(scopeMetadata, definitionHolder, this.registry);
  this.registry.registerBeanDefinition(definitionHolder.getBeanName(), definitionHolder.getBeanDefinition());
  configClass.setBeanName(configBeanName);
}
```

如上，比较简单，不过这里有个值得说的点：处理通用注解`AnnotationConfigUtils.processCommonDefinitionAnnotations()`，它主要用于处理如下注解

- `Lazy`
- `Primary`
- `DependsOn`
- `Role`
- `Description`

都不需要怎么解释，看一下代码就能了解

```java
static void processCommonDefinitionAnnotations(AnnotatedBeanDefinition abd, AnnotatedTypeMetadata metadata) {
  AnnotationAttributes lazy = attributesFor(metadata, Lazy.class);
  if (lazy != null) {
    abd.setLazyInit(lazy.getBoolean("value"));
  } else if (abd.getMetadata() != metadata) {
    lazy = attributesFor(abd.getMetadata(), Lazy.class);
    if (lazy != null) {
      abd.setLazyInit(lazy.getBoolean("value"));
    }
  }

  if (metadata.isAnnotated(Primary.class.getName())) {
    abd.setPrimary(true);
  }
  AnnotationAttributes dependsOn = attributesFor(metadata, DependsOn.class);
  if (dependsOn != null) {
    abd.setDependsOn(dependsOn.getStringArray("value"));
  }

  AnnotationAttributes role = attributesFor(metadata, Role.class);
  if (role != null) {
    abd.setRole(role.getNumber("value").intValue());
  }
  AnnotationAttributes description = attributesFor(metadata, Description.class);
  if (description != null) {
    abd.setDescription(description.getString("value"));
  }
}
```

### @Bean

关于Bean方法的处理，看起来一长串，其实就两个关键的逻辑

- 使用`ConfigurationClassBeanDefinition`作为Bean定义，它将被注解的方法注册成了Bean定义的工厂方法。这样在Bean创建时走的完全是正常的创建流程
- 以代理的方式创建，代理模式为CGLIB

具体参考`ConfigurationClassBeanDefinitionReader#loadBeanDefinitionsForBeanMethod`，这里也没必要列出来源码。

### @ImportResource

创建指定的`BeanDefinitionReader`实例，然后读取指定的location即可。

```java
private void loadBeanDefinitionsFromImportedResources(Map<String, Class<? extends BeanDefinitionReader>> importedResources) {

  Map<Class<?>, BeanDefinitionReader> readerInstanceCache = new HashMap<>();

  importedResources.forEach((resource, readerClass) -> {
    // 决定要使用的BeanDefinitionReader
    // Default reader selection necessary?
    if (BeanDefinitionReader.class == readerClass) {
      if (StringUtils.endsWithIgnoreCase(resource, ".groovy")) {
        // When clearly asking for Groovy, that's what they'll get...
        readerClass = GroovyBeanDefinitionReader.class;
      } else if (shouldIgnoreXml) {
        throw new UnsupportedOperationException("XML support disabled");
      } else {
        // Primarily ".xml" files but for any other extension as well
        readerClass = XmlBeanDefinitionReader.class;
      }
    }

    BeanDefinitionReader reader = readerInstanceCache.get(readerClass);
    // 创建Reader
    if (reader == null) {
      // Instantiate the specified BeanDefinitionReader
      reader = readerClass.getConstructor(BeanDefinitionRegistry.class).newInstance(this.registry);
      // Delegate the current ResourceLoader to it if possible
      if (reader instanceof AbstractBeanDefinitionReader) {
        AbstractBeanDefinitionReader abdr = ((AbstractBeanDefinitionReader) reader);
        abdr.setResourceLoader(this.resourceLoader);
        abdr.setEnvironment(this.environment);
      }
      readerInstanceCache.put(readerClass, reader);
    }

    // reader读，走你
    reader.loadBeanDefinitions(resource);
  });
}
```

### BeanDefinitionRegistrar

更简单，在第一篇Spring源码剖析的文章中我们提到过`Registry`和`Registrar`的区别，前者是注册器，用于接收资源的注册并持有；而后者只是一个资源集合，持有一堆资源，一般调用方式是传入`Registry`，向其中倾泻自己持有的资源。

这里的`BeanDefinitionRegistrar`就是如此，持有一堆`BeanDefinition`集合，在本阶段向注册器中注册

```java
private void loadBeanDefinitionsFromRegistrars(Map<ImportBeanDefinitionRegistrar, AnnotationMetadata> registrars) {
  registrars.forEach((registrar, metadata) ->
                     registrar.registerBeanDefinitions(metadata, this.registry, this.importBeanNameGenerator));
}
```

## 自动配置怎么实现

上一篇介绍SpringBoot启动流程的文章中，我们知道了`SpringApplication`在快速启动中做了什么，这其中，最最重要的是通过`META/spring.factories`加载指定类的实现的机制，即`SpringFactoriesLoader.loadFactory()`方法。但上一篇文章并没有介绍自动配置的原理，因为还缺少`@Import`注解的说明。

本文我们补上了这一点，于是可以探索`@SpringBootApplication`这一SpringBoot的另一核心的原理，其定义如下

```java
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan(excludeFilters = { @Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class),
		@Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) })
public @interface SpringBootApplication {
  ... ...
}
```

层层深入，可以发现它最终落在三个注解上

- `@Configuration`：表明这是一个配置类
- `@Import(AutoConfigurationImportSelector.class)` + `@Import(AutoConfigurationPackages.Registrar.class)`：导入配置
- `@ComponentScan`：表明从当前类的包的子包下扫描

进一步，重点落在`AutoConfigurationImportSelector`和`AutoConfigurationPackages.Registrar`上，重点看前者，后者与自动配置无关，暂且忽略。

### AutoConfigurationImportSelector

该选择器，调用了`SpringFactoriesLoader.loadFactory()`，从spring.factories文件中加载键为`org.springframework.boot.autoconfigure.EnableAutoConfiguration`所对应的值，核心逻辑追踪如下

```shell
-> org.springframework.boot.autoconfigure.AutoConfigurationImportSelector#selectImports
-> org.springframework.boot.autoconfigure.AutoConfigurationImportSelector#getAutoConfigurationEntry
-> org.springframework.boot.autoconfigure.AutoConfigurationImportSelector#getCandidateConfigurations
-> org.springframework.boot.autoconfigure.AutoConfigurationImportSelector#getSpringFactoriesLoaderFactoryClass
```

再看最后这个方法的实现，显而易见了

```java
protected Class<?> getSpringFactoriesLoaderFactoryClass() {
  return EnableAutoConfiguration.class;
}
```

### 看看自动配置

官方的`spring-boot-autoconfigure`下的`META-INF/spring.factories`中，定义了非常多的自动配置类

```java
# Auto Configure
org.springframework.boot.autoconfigure.EnableAutoConfiguration=\
org.springframework.boot.autoconfigure.admin.SpringApplicationAdminJmxAutoConfiguration,\
org.springframework.boot.autoconfigure.aop.AopAutoConfiguration,\
org.springframework.boot.autoconfigure.amqp.RabbitAutoConfiguration,\
org.springframework.boot.autoconfigure.batch.BatchAutoConfiguration,\
org.springframework.boot.autoconfigure.cache.CacheAutoConfiguration,\
org.springframework.boot.autoconfigure.cassandra.CassandraAutoConfiguration,\
... ...
```

我们选取一个比较熟的`org.springframework.boot.autoconfigure.websocket.servlet.WebSocketServletAutoConfiguration`，浏览一下其代码。

```java
@Configuration(proxyBeanMethods = false)
@ConditionalOnClass({ Servlet.class, ServerContainer.class })
@ConditionalOnWebApplication(type = Type.SERVLET)
@AutoConfigureBefore(ServletWebServerFactoryAutoConfiguration.class)
public class WebSocketServletAutoConfiguration {

	@Configuration(proxyBeanMethods = false)
	@ConditionalOnClass({ Tomcat.class, WsSci.class })
	static class TomcatWebSocketConfiguration {

		@Bean
		@ConditionalOnMissingBean(name = "websocketServletWebServerCustomizer")
		TomcatWebSocketServletWebServerCustomizer websocketServletWebServerCustomizer() {
			return new TomcatWebSocketServletWebServerCustomizer();
		}

	}

	@Configuration(proxyBeanMethods = false)
	@ConditionalOnClass(WebSocketServerContainerInitializer.class)
	static class JettyWebSocketConfiguration {

		@Bean
		@ConditionalOnMissingBean(name = "websocketServletWebServerCustomizer")
		JettyWebSocketServletWebServerCustomizer websocketServletWebServerCustomizer() {
			return new JettyWebSocketServletWebServerCustomizer();
		}

	}

	@Configuration(proxyBeanMethods = false)
	@ConditionalOnClass(io.undertow.websockets.jsr.Bootstrap.class)
	static class UndertowWebSocketConfiguration {

		@Bean
		@ConditionalOnMissingBean(name = "websocketServletWebServerCustomizer")
		UndertowWebSocketServletWebServerCustomizer websocketServletWebServerCustomizer() {
			return new UndertowWebSocketServletWebServerCustomizer();
		}

	}

}
```

## 总结

通过`spring.factories`机制和`@Import + ImportSelector`的形式，SpringBoot为实现自动注解提供了最基础的能力，但根据各个具体不同的场景，Spring还在上面提到的基本注解之上构建了非常多具体的注解，比如条件注解就好多。一个个看是不现实的，但我们了解了本文提到的基础知识，再去看就很好理解了。
