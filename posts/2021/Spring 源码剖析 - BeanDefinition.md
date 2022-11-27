---
created_at: 2021-11-17 18:09:43
updated_at: 2021-11-17 18:09:43
slug: spring-source-code-analyze-bean-definition
tags:
  - Spring
  - 源码剖析
---

> 阅读提示：TL;DR。文章包含大量源码，阅读时长较长，认真阅读可能超过20分钟。

回想一下，Spring最最核心的功能，终究是一个容器，用于提供所谓的”`Bean`“，并负责`Bean`之间的联结。而我们又知道，`Bean`有不同的`Scope`，即作用范围，单例的、原型的、`Session`的，或自定义的。`Bean`还能够懒加载。因此，创建`Bean`的时机可能是运行时的任何时候。Spring使用`BeanDefinition`描述一个`Bean`的name、类、scope等元数据，并在需要时候创建。创建过程自然也包括了自动注入的过程。

<!-- more -->

本文我们重点关注Spring中对`Bean`的管理。

## 如何描述Bean

![截屏2021-11-17 下午7.52.20](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-11-17%20%E4%B8%8B%E5%8D%887.52.20.png)

Spring使用`BeanDefinition`来描述`Bean`，其继承拓扑图如上，我们只选取了几个具有代表性的来看。根绝`BeanDefinition`接口的定义，能够知道，Spring中的`Bean`具有如下特性：

- 基本信息
  - 名字
  - 描述
  - 用于创建该Bean的Class对象
- 具有作用范围Scope
  - singleton：全局唯一实例
  - prototype：每次获取都创建新的实例
- 可以有父子关系
- 可以有依赖关系，即一个Bean的创建依赖于另一个Bean的存在
- 可延迟加载
- 可自动装配
  - 设置是否参与自动装配（基于类型）
  - 如果有多个类型符合要求，可设置主要的
- 可自定义Bean实例创建方式
  - 设置工厂Bean，用另一个Bean来创建该Bean
  - 设置工厂方法，用该方法创建实例
- 生命周期管理
  - 可指定初始化方法 `initMethod`
  - 可指定销毁方法 `destroyMethod`
- 具有角色，目前定义了三种角色，但暂未看到如何使用
  - `ROLE_APPLICATION`：该Bean是应用的主体，默认值
  - `ROLE_SUPPORT`：标识该Bean是其它更大部分的支持部分
  - `ROLE_INFRASTRUCTURE`：该Bean作为纯基础设施的支持，用户接触不到它
- 获取构造方法的参数的值
- 获取`MutablePropertyValues`，这对应的是Bean的属性键值对，自动注入时会使用。
- `BeanDefinition`可包装另一个`BeanDefinition`，通过`BeanDefinition getOriginatingBeanDefinition()`获取被包装的定义。

至于继承树中其它类，各自有所区别，我们依次看

### AbstractBeanDefinition

`BeanDefinition`的直接实现，从中也可以看到一些特性的默认值

- `scope`默认为单例
- 延迟加载默认关闭
- 自动注入默认关闭
- 角色默认为`ROLE_APPLICATION`

### RootBeanDefinition

说实话直接看这个类时，有点懵，原注释这么说。

> A root bean definition represents the merged bean definition that backs a specific bean in a Spring BeanFactory at runtime. It might have been created from multiple original bean definitions that inherit from each other, typically registered as GenericBeanDefinitions. A root bean definition is essentially the 'unified' bean definition view at runtime.
> Root bean definitions may also be used for registering individual bean definitions in the configuration phase. However, since Spring 2.5, the preferred way to register bean definitions programmatically is the GenericBeanDefinition class. GenericBeanDefinition has the advantage that it allows to dynamically define parent dependencies, not 'hard-coding' the role as a root bean definition.

我看懂了字面意思，却没看懂这串英文背后的含义。什么是`MergedBean`，关于这点，可以参考[这篇文章](https://blog.csdn.net/andy_zhang2007/article/details/86514320)，所谓合并，就是将具有父子关系的`BeanDefinition`合并为一个`BeanDefinition`。”合并“的具体过程，下文”如何创建Bean“将会分析。

### GenericBeanDefinition

`BeanDefinition`的标准实现，相较于`AbstractBeanDefinition`，它多了对父子关系的实现。我们是可以直接用该类创建自己的`BeanDefinition`的。如果我们要凭空创建一个`BeanDefinition`注入容器，可以用它。

### AnnotatedBeanDefinition

`BeanDefinition`的直接扩展接口，向调用者暴露了`AnnotationMetadata`。那么问题来了，什么是`AnnotationMetadata`呢？它是Spring为指定类的注解所定义的抽象，通过它可以不加载目标类即可获取到注解信息。类似的还有`ClassMetadata`。看来，Spring是将Bean定义的方方面面都进行了抽象。

![截屏2021-11-17 下午9.45.35](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-11-17%20%E4%B8%8B%E5%8D%889.45.35.png)

### AnnotatedGenericBeanDefinition

同时实现了`GenericBeanDefinition`和`AnnotatedBeanDefinition`，表明它既具有一个完整`BeanDefinition`的能力，又持有Bean原类上的注解信息。持有注解信息有什么用呢？当然有用，运行时可以直接获取Bean定义的注解而不加载原类呀，提升性能。

### ScannedGenericBeanDefinition

和`AnnotatedGenericBeanDefinition`一样，可以说是一模一样。

### 小结

Spring关于Bean的描述，其实不止这几个类，但我认为其它都是干扰，因此去掉了。我们的重点，是要通过这些定义看到Spring是如何进行抽象的，以及各级抽象的作用。写代码时不会用到，但它可保看源码时不会懵逼。

## Bean定义从何而来

还是上一篇文章那个例子，一个最最简单的应用方式。

```java
fun main() {
    val context = AnnotationConfigApplicationContext("com.gitee.floyd.springme.core")
    println(context.getBean(Bean1::class.java))
}
```

我们以`org.springframework.context.annotation.AnnotationConfigApplicationContext`构造方法为入口，分析Bean定义加载的过程。

```java
public AnnotationConfigApplicationContext(String... basePackages) {
  this();
  scan(basePackages);
  ... ...
}

public AnnotationConfigApplicationContext() {
  this.reader = new AnnotatedBeanDefinitionReader(this);
  this.scanner = new ClassPathBeanDefinitionScanner(this);
}


public void scan(String... basePackages) {
  ... ... 
    this.scanner.scan(basePackages);
  ... ...
}
```

这里引入两个新的类：`AnnotatedBeanDefinitionReader`和`ClassPathBeanDefinitionScanner`，我们先看它们的能力，再看这个扫描的过程

### AnnotatedBeanDefinitionReader

```java
public class AnnotatedBeanDefinitionReader {
  // Bean定义注册器，一个注册接口，其实现类一般会持有所有这些注册的BeanDefinition，典型的实现类就是具体的ApplicationContext
  private final BeanDefinitionRegistry registry;
  // Bean名称生成器，AnnotationBeanNameGenerator是按照@Component注解或其子注解生成名字
  private BeanNameGenerator beanNameGenerator = AnnotationBeanNameGenerator.INSTANCE;
  // Scope元信息解析器，AnnotationScopeMetadataResolver解析的是@Scope注解
  private ScopeMetadataResolver scopeMetadataResolver = new AnnotationScopeMetadataResolver();
  // 条件计算器，用于解析@Conditional注解
  private ConditionEvaluator conditionEvaluator;

  ... ...
  // 注册Bean
  public void registerBean(Class<?> beanClass) {
    doRegisterBean(beanClass, null, null, null, null);
  }
  ... ...
  // 实际注册Bean，传入bean的类型、名字等
  private <T> void doRegisterBean(Class<T> beanClass, @Nullable String name,
                                    @Nullable Class<? extends Annotation>[] qualifiers, @Nullable Supplier<T> supplier,
                                    @Nullable BeanDefinitionCustomizer[] customizers) {
		// 根据类对象创建AnnotatedGenericBeanDefinition
    AnnotatedGenericBeanDefinition abd = new AnnotatedGenericBeanDefinition(beanClass);
    // 判断是否需要忽略该Bean定义
    if (this.conditionEvaluator.shouldSkip(abd.getMetadata())) {
      return;
    }
		// 设置一个实例创建时的回调函数，它作为一种工厂方法的替换
    abd.setInstanceSupplier(supplier);
    ScopeMetadata scopeMetadata = this.scopeMetadataResolver.resolveScopeMetadata(abd);
    // 为Bean定义加上Scope
    abd.setScope(scopeMetadata.getScopeName());
    // 生成bean名字
    String beanName = (name != null ? name : this.beanNameGenerator.generateBeanName(abd, this.registry));
		// 处理通用注解：@Lazy、@Primary、@DependsOn、@Role、@Description
    AnnotationConfigUtils.processCommonDefinitionAnnotations(abd);
    // 根据传入的修饰注解决定
    if (qualifiers != null) {
      for (Class<? extends Annotation> qualifier : qualifiers) {
        if (Primary.class == qualifier) {
          abd.setPrimary(true);
        }
        else if (Lazy.class == qualifier) {
          abd.setLazyInit(true);
        }
        else {
          abd.addQualifier(new AutowireCandidateQualifier(qualifier));
        }
      }
    }
    // 应用传入的BeanDefinition定制器
    if (customizers != null) {
      for (BeanDefinitionCustomizer customizer : customizers) {
        customizer.customize(abd);
      }
    }
		
    // 包装成BeanDefinitionHolder
    BeanDefinitionHolder definitionHolder = new BeanDefinitionHolder(abd, beanName);
    // Bean的scope代理模式是封装在BeanDefinitionHolder中的，这里进行设置
    definitionHolder = AnnotationConfigUtils.applyScopedProxyMode(scopeMetadata, definitionHolder, this.registry);
    // 将处理完的BeanDefinitionHolder注入registry
    BeanDefinitionReaderUtils.registerBeanDefinition(definitionHolder, this.registry);
  }
}

// AnnotationConfigUtils.processCommonDefinitionAnnotations方法
static void processCommonDefinitionAnnotations(AnnotatedBeanDefinition abd, AnnotatedTypeMetadata metadata) {
  // 延迟加载的处理
  AnnotationAttributes lazy = attributesFor(metadata, Lazy.class);
  if (lazy != null) {
    abd.setLazyInit(lazy.getBoolean("value"));
  }
  else if (abd.getMetadata() != metadata) {
    lazy = attributesFor(abd.getMetadata(), Lazy.class);
    if (lazy != null) {
      abd.setLazyInit(lazy.getBoolean("value"));
    }
  }
	// primary的处理
  if (metadata.isAnnotated(Primary.class.getName())) {
    abd.setPrimary(true);
  }
  // 依赖的处理
  AnnotationAttributes dependsOn = attributesFor(metadata, DependsOn.class);
  if (dependsOn != null) {
    abd.setDependsOn(dependsOn.getStringArray("value"));
  }
	// 角色的处理
  AnnotationAttributes role = attributesFor(metadata, Role.class);
  if (role != null) {
    abd.setRole(role.getNumber("value").intValue());
  }
  // 描述的处理
  AnnotationAttributes description = attributesFor(metadata, Description.class);
  if (description != null) {
    abd.setDescription(description.getString("value"));
  }
}
```

要点总结

- `AnnotatedBeanDefinitionReader`，封装了`BeanDefinition`构建并注入`BeanDefinitionRegistry`的流程，这里`BeanDefinitionRegistry`就是我们的容器
- `BeanDefinitionRegistry`，在前面介绍`ApplicationContext`就已经介绍过，用于接收并持有Bean定义
- bean名称生成器：`AnnotationBeanNameGenerator`，按照`@Component`及其子注解、`@ManagedBean`、`@Named`生成，详细分析见下
- `Scope`元信息，包含了`Scope`的作用范围、代理模式，通过`@Scope`注解标识，`AnnotationScopeMetadataResolver`就是解析`@Scope`注解的。如果未指定`@Scope`注解，得到的结果是：单例+不代理。
- `ConditionEvaluator`，条件解析器。针对`@Conditional`进行解析。详细分析见下文。

#### bean名称生成逻辑

AnnotationBeanNameGenerator这个类值得看一看，它有一些隐藏的功能

```java
public class AnnotationBeanNameGenerator implements BeanNameGenerator {
  // @Compenent注解通过字面量的形式呈现
  private static final String COMPONENT_ANNOTATION_CLASSNAME = "org.springframework.stereotype.Component";

  // 核心方法
  @Override
  public String generateBeanName(BeanDefinition definition, BeanDefinitionRegistry registry) {
    // 如果Bean有注解，则根据注解生成名称
    if (definition instanceof AnnotatedBeanDefinition) {
      String beanName = determineBeanNameFromAnnotation((AnnotatedBeanDefinition) definition);
      if (StringUtils.hasText(beanName)) {
        // Explicit bean name found.
        return beanName;
      }
    }
    // 如果Bean没有注解，则直接使用类名的首字母小写形式
    return buildDefaultBeanName(definition, registry);
  }

  protected String determineBeanNameFromAnnotation(AnnotatedBeanDefinition annotatedDef) {
    AnnotationMetadata amd = annotatedDef.getMetadata();
    Set<String> types = amd.getAnnotationTypes();
    String beanName = null;
    for (String type : types) {
      AnnotationAttributes attributes = AnnotationConfigUtils.attributesFor(amd, type);
      if (attributes != null) {
        // 获取元注解，即注解的注解，这样才能检测到@Service、@Repository之类的注解
        Set<String> metaTypes = this.metaAnnotationTypesCache.computeIfAbsent(type, key -> {
          Set<String> result = amd.getMetaAnnotationTypes(key);
          return (result.isEmpty() ? Collections.emptySet() : result);
        });
        if (isStereotypeWithNameValue(type, metaTypes, attributes)) {
          // 注解的value属性必须有值，且不为空串，才会取
          Object value = attributes.get("value");
          if (value instanceof String) {
            String strVal = (String) value;
            if (StringUtils.hasLength(strVal)) {
              if (beanName != null && !strVal.equals(beanName)) {
                throw new IllegalStateException("Stereotype annotations suggest inconsistent " +
                                                "component names: '" + beanName + "' versus '" + strVal + "'");
              }
              beanName = strVal;
            }
          }
        }
      }
    }
    return beanName;
  }

  // 
  protected boolean isStereotypeWithNameValue(String annotationType, Set<String> metaAnnotationTypes, @Nullable Map<String, Object> attributes) {
    // 这里也可以看到，还支持@ManagedBean、Named这样的JSR规定的注解
    boolean isStereotype = annotationType.equals(COMPONENT_ANNOTATION_CLASSNAME) ||
      metaAnnotationTypes.contains(COMPONENT_ANNOTATION_CLASSNAME) ||
      annotationType.equals("javax.annotation.ManagedBean") ||
      annotationType.equals("javax.inject.Named");

    return (isStereotype && attributes != null && attributes.containsKey("value"));
  }

  protected String buildDefaultBeanName(BeanDefinition definition) {
    String beanClassName = definition.getBeanClassName();
    Assert.state(beanClassName != null, "No bean class name set");
    String shortClassName = ClassUtils.getShortName(beanClassName);
    return Introspector.decapitalize(shortClassName);
  }
}
```

要点

- 支持生成Bean名称的注解有：`@Component`及其子注解、`@MangedBean`、`@Named`
- 如果这些注解没有显式指明名称，则回退成默认规则：类名首字母小写

#### 判定BeanDefinition是否需要被加载

ConditionEvaluator这个类也值得一看，它解释了`@Conditional`注解的工作原理。整个类就暴露一个方法：`shouldSkip()`

```java
public boolean shouldSkip(@Nullable AnnotatedTypeMetadata metadata, @Nullable ConfigurationPhase phase) {
  // 如果目标类没有被Conditional注解，则不应被跳过
  if (metadata == null || !metadata.isAnnotated(Conditional.class.getName())) {
    return false;
  }

  if (phase == null) {
  	// 如果没有指定配置过程，就根据其它条件判断是属于配置阶段还是创建Bean阶段
    if (metadata instanceof AnnotationMetadata && ConfigurationClassUtils.isConfigurationCandidate((AnnotationMetadata) metadata)) {
      return shouldSkip(metadata, ConfigurationPhase.PARSE_CONFIGURATION);
    }
    return shouldSkip(metadata, ConfigurationPhase.REGISTER_BEAN);
  }

  List<Condition> conditions = new ArrayList<>();
  // 从@Conditional注解中提取出Condition条件
  for (String[] conditionClasses : getConditionClasses(metadata)) {
    for (String conditionClass : conditionClasses) {
      Condition condition = getCondition(conditionClass, this.context.getClassLoader());
      conditions.add(condition);
    }
  }
	// 排序
  AnnotationAwareOrderComparator.sort(conditions);

  for (Condition condition : conditions) {
    ConfigurationPhase requiredPhase = null;
    if (condition instanceof ConfigurationCondition) {
      requiredPhase = ((ConfigurationCondition) condition).getConfigurationPhase();
    }
    // 当阶段匹配，且条件不匹配时，则跳过Bean注册
    if ((requiredPhase == null || requiredPhase == phase) && !condition.matches(this.context, metadata)) {
      return true;
    }
  }
	// 其它情况，不应当跳过
  return false;
}
```

分析一下`ConfigurationClassUtils.isConfigurationCandidate()`

```java
private static final Set<String> candidateIndicators = new HashSet<>(8);

static {
  // 有下面这四个注解，就说明是配置Bean
  candidateIndicators.add(Component.class.getName());
  candidateIndicators.add(ComponentScan.class.getName());
  candidateIndicators.add(Import.class.getName());
  candidateIndicators.add(ImportResource.class.getName());
}

public static boolean isConfigurationCandidate(AnnotationMetadata metadata) {
  // 接口上的注解不考虑
  if (metadata.isInterface()) {
    return false;
  }
	// 只要被上面那四个注解注解了，就说明是配置Bean
  for (String indicator : candidateIndicators) {
    if (metadata.isAnnotated(indicator)) {
      return true;
    }
  }
	// 否则，如果其内部存在被@Bean注解的方法，也算配置Bean
  return hasBeanMethods(metadata);
}

static boolean hasBeanMethods(AnnotationMetadata metadata) {
  try {
    return metadata.hasAnnotatedMethods(Bean.class.getName());
  }
  catch (Throwable ex) {
    ... ...
  }
}
```

理解关键

- `AnnotatedTypeMetadata`要理解，前面`AnnotatedBeanDefinition`看到过，Spring将`Bean`上的注解信息和类信息进行了抽象，使得不需要加载具体的类就能获取其上的注解，使用方便。
- `Condition`条件，它只有一个匹配方法`boolean matches(ConditionContext context, AnnotatedTypeMetadata metadata)`，用于匹配指定Bean在容器中是否满足条件，我们常用的`@ConditionalOnClassMissingBean`之类的注解，就是`@Conditional`派生注解+`Condition`派生类组合完成的。

要点总结

- `ConditionEvaluator`是用来判断某个Bean定义是否符合加载条件，是加载还是有应该被忽略。判断逻辑
  - 如果不存在`@Conditional`注解，则需要加载
  - 如果存在`@Conditional`注解，则需要看该注解的作用阶段和其内部`Condition`的行为
    - 如果`Condition`所指定的阶段与`@Conditional`实际作用的阶段不一致，则需要加载
    - 否则，根据`Condition.matches()`的结果来判定是否需要加载
- 当一个Bean定义被`@Component、@ComponentScan、@Import、@ImportResource`注解，或其内含有`@Bean`注解方法时，说明它是一个配置Bean。即作用阶段是`ConfigurationPhase.PARSE_CONFIGURATION`，否则，作用阶段是`ConfigurationPhase.REGISTER_BEAN`，作用阶段，也可以用来判断是否需要加载该Bean定义：当声明的作用阶段和`Condition`类的作用阶段不一致时，将忽略匹配过程，直接加载

### ClassPathBeanDefinitionScanner

![截屏2021-11-18 下午6.33.05](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/%E6%88%AA%E5%B1%8F2021-11-18%20%E4%B8%8B%E5%8D%886.33.05.png)

继承树如上

- `ClassPathScanningCandidateComponentProvider`用于在指定包下扫描并提供Bean定义（所谓的`CandidateComponent`），核心逻辑在`public Set<BeanDefinition> findCandidateComponents(String basePackage)`方法。
- `ClassPathBeanDefinitionScanner`用于批量扫描包下的Bean定义，核心逻辑在`protected Set<BeanDefinitionHolder> doScan(String... basePackages)`方法。

我们按照调用关系来看，从scan方法看起

```java
public int scan(String... basePackages) {
  // 扫描：从包下扫描出BeanDefinition，然后注入registry，详情见下
  doScan(basePackages);
  if (this.includeAnnotationConfig) {
    // 注册一批后置处理器，这个我们忽略，它注册了一批内部的后置处理器
    AnnotationConfigUtils.registerAnnotationConfigProcessors(this.registry);
  }
  // return什么不重要
  return ...
}

protected Set<BeanDefinitionHolder> doScan(String... basePackages) {
  Set<BeanDefinitionHolder> beanDefinitions = new LinkedHashSet<>();
  for (String basePackage : basePackages) {
    // 调用父类的findCandidateComponents，在指定包下找到符合要求的BeanDefinition
    Set<BeanDefinition> candidates = findCandidateComponents(basePackage);
    for (BeanDefinition candidate : candidates) {
      // 解析Scope元信息
      ScopeMetadata scopeMetadata = this.scopeMetadataResolver.resolveScopeMetadata(candidate);
      candidate.setScope(scopeMetadata.getScopeName());
      // 生成bean名称
      String beanName = this.beanNameGenerator.generateBeanName(candidate, this.registry);
      if (candidate instanceof AbstractBeanDefinition) {
        // 一波附加逻辑，详情见下
        postProcessBeanDefinition((AbstractBeanDefinition) candidate, beanName);
      }
      if (candidate instanceof AnnotatedBeanDefinition) {
        // 处理一波通用注解：@Lazy、@Primary、@DependsOn、@Role、@Description，该方法前面已经分析过了
        AnnotationConfigUtils.processCommonDefinitionAnnotations((AnnotatedBeanDefinition) candidate);
      }
      // 检查新建的BeanDefinition是否合法，主要是检查容器中是否已经有同名Bean了
      if (checkCandidate(beanName, candidate)) {
        // 构建BeanDefinitionHolder
        BeanDefinitionHolder definitionHolder = new BeanDefinitionHolder(candidate, beanName);
        // 应用scope的代理mode
        definitionHolder = AnnotationConfigUtils.applyScopedProxyMode(scopeMetadata, definitionHolder, this.registry);
        beanDefinitions.add(definitionHolder);
        // 注入registry
        registerBeanDefinition(definitionHolder, this.registry);
      }
    }
  }
  return beanDefinitions;
}

protected void postProcessBeanDefinition(AbstractBeanDefinition beanDefinition, String beanName) {
  // 应用默认设置：延迟加载、自动注入mode、依赖检查、初始化方法、销毁方法等
  beanDefinition.applyDefaults(this.beanDefinitionDefaults);
  if (this.autowireCandidatePatterns != null) {
    // 设置是否参与自动注入
    beanDefinition.setAutowireCandidate(PatternMatchUtils.simpleMatch(this.autowireCandidatePatterns, beanName));
  }
}

public void applyDefaults(BeanDefinitionDefaults defaults) {
  Boolean lazyInit = defaults.getLazyInit();
  if (lazyInit != null) {
    setLazyInit(lazyInit);
  }
  setAutowireMode(defaults.getAutowireMode());
  setDependencyCheck(defaults.getDependencyCheck());
  setInitMethodName(defaults.getInitMethodName());
  setEnforceInitMethod(false);
  setDestroyMethodName(defaults.getDestroyMethodName());
  setEnforceDestroyMethod(false);
}
```

上面有调用到`ClassPathScanningCandidateComponentProvider`的`findCandidateComponents`方法，我们再看

```java
public Set<BeanDefinition> findCandidateComponents(String basePackage) {
  if (this.componentsIndex != null && indexSupportsIncludeFilters()) {
    // 通过Index进行组件扫描
    return addCandidateComponentsFromIndex(this.componentsIndex, basePackage);
  } else {
    // 直接扫描
    return scanCandidateComponents(basePackage);
  }
}

// 直接扫描的过程：
private Set<BeanDefinition> scanCandidateComponents(String basePackage) {
  Set<BeanDefinition> candidates = new LinkedHashSet<>();
  try {
    // 路径：classpath*:{包转换后的路径名}/**/*.class，即所有jar包下的置顶包名下的所有层级的所有class文件
    String packageSearchPath = ResourcePatternResolver.CLASSPATH_ALL_URL_PREFIX + resolveBasePackage(basePackage) + '/' + this.resourcePattern;
    Resource[] resources = getResourcePatternResolver().getResources(packageSearchPath);
    for (Resource resource : resources) 
      if (resource.isReadable()) {
        try {
          MetadataReader metadataReader = getMetadataReaderFactory().getMetadataReader(resource);
          // 必须符合includeFilters中的过滤器要求才会被扫描出来
          if (isCandidateComponent(metadataReader)) {
            // 刚扫描出来的BeanDefinition，只创建了Bean定义的实例，还没开始解析，解析留给子类。
            ScannedGenericBeanDefinition sbd = new ScannedGenericBeanDefinition(metadataReader);
            sbd.setSource(resource);
            if (isCandidateComponent(sbd)) {
              candidates.add(sbd);
            }
          }
        } catch (Throwable ex) {
          throw new BeanDefinitionStoreException("Failed to read candidate component class: " + resource, ex);
        }
      }
    }
  } catch (IOException ex) {
    throw new BeanDefinitionStoreException("I/O failure during classpath scanning", ex);
  }
  return candidates;
}

protected boolean isCandidateComponent(MetadataReader metadataReader) throws IOException {
  // 在排除过滤器中，直接不符合要求
  for (TypeFilter tf : this.excludeFilters) {
    if (tf.match(metadataReader, getMetadataReaderFactory())) {
      return false;
    }
  }
  // 在include过滤器中匹配才符合要求
  for (TypeFilter tf : this.includeFilters) {
    if (tf.match(metadataReader, getMetadataReaderFactory())) {
      return isConditionMatch(metadataReader);
    }
  }
  return false;
}
```

上面只贴出了直接从类中扫描的代码，但另一个`addCandidateComponentsFromIndex`没说。我们需要先知道一下Spring中的Index是什么。可以参考[这篇文章](https://juejin.cn/post/6844904014509768712):

> 在项目中使用了`@Indexed`之后，编译打包的时候会在项目中自动生成`META-INT/spring.components`文件。 当Spring应用上下文执行`ComponentScan`扫描时，`META-INT/spring.components`将会被`CandidateComponentsIndexLoader` 读取并加载，转换为`CandidateComponentsIndex`对象，这样的话`@ComponentScan`不在扫描指定的package，而是读取`CandidateComponentsIndex`对象，从而达到提升性能的目的。

此时我们再去跟踪`addCandidateComponentsFromIndex()`方法，会发现和上面说的可以说是一模一样了。

要点总结

- 可以看到，`ClassPathBeanDefinitionScanner`做的事和`AnnotatedBeanDefinitionReader`差不多，都是构建`BeanDefinition`并向容器中注册；唯一的差别是，前者的Bean定义是自己扫描得来的，而后者的Bean定义是外界调用方法注册来的

- 通过`ClassPathScanningCandidateComponentProvider.findCandidateComponents()`我们知道，它只提供最原始的扫描并生成`BeanDefinition`的逻辑，而`BeanDefinition`各种属性的解析和设置放在其子类`ClassPathBeanDefinitionScanner`中了。

### 小结

这一个Reader，一个Scanner，都只是一个工具，最终完成了容器中的`BeanDefinition`创建。

## 如何创建Bean

### Bean的创建逻辑

Bean的创建有几个时机

- 对于非延迟加载的单例Bean，在容器refresh时就会被创建，在`ApplicationContext`源码分析时我们看到过
- 对于延迟加载的单例Bean，在第一次被获取时会被创建
- 对于原型Bean，每次被获取时都会被创建

我们先看第一种情况，直接进`org.springframework.beans.factory.support.DefaultListableBeanFactory#preInstantiateSingletons`，我删掉了不重要的代码。

```java
public void preInstantiateSingletons() throws BeansException {
  // Iterate over a copy to allow for init methods which in turn register new bean definitions.
  // While this may not be part of the regular factory bootstrap, it does otherwise work fine.
  List<String> beanNames = new ArrayList<>(this.beanDefinitionNames);

  // Trigger initialization of all non-lazy singleton beans...
  for (String beanName : beanNames) {
    // 获取合并后的BeanDefinition
    RootBeanDefinition bd = getMergedLocalBeanDefinition(beanName);
    // 单例且非延迟加载才会创建
    if (!bd.isAbstract() && bd.isSingleton() && !bd.isLazyInit()) {
      if (isFactoryBean(beanName)) {
        // 工厂Bean的名字有特殊前缀：&
        Object bean = getBean(FACTORY_BEAN_PREFIX + beanName);
        if (bean instanceof FactoryBean) {
          FactoryBean<?> factory = (FactoryBean<?>) bean;
          // 针对SmartFactoryBean的特殊处理
          boolean isEagerInit = (factory instanceof SmartFactoryBean && ((SmartFactoryBean<?>) factory).isEagerInit());
          if (isEagerInit) {
            // 真的去创建Bean
            getBean(beanName);
          }
        }
      } else {
        // 真的去创建Bean
        getBean(beanName);
      }
    }
  }

  for (String beanName : beanNames) {
    // 针对SmartInitializingSingleton的特殊处理
    Object singletonInstance = getSingleton(beanName);
    if (singletonInstance instanceof SmartInitializingSingleton) {
      SmartInitializingSingleton smartSingleton = (SmartInitializingSingleton) singletonInstance;
      smartSingleton.afterSingletonsInstantiated();
    }
  }
}

public Object getBean(String name) throws BeansException {
  return doGetBean(name, null, null, false);
}

/**
 * 真的去创建Bean
 * name: bean的名称
 * requiedType: 希望解析出来的Bean的类型
 * args: 用于创建bean时的构造方法的参数。如果只是获取已有的bean，则不需要
 * typeCheckOnly: 只检查得到的bean与目标类型是否匹配，而不真正地标记创建
 **/
protected <T> T doGetBean(String name, @Nullable Class<T> requiredType, @Nullable Object[] args, boolean typeCheckOnly) {
  // 名字转换：主要是处理别名，根据别名获取真名
  String beanName = transformedBeanName(name);
  Object beanInstance;

  // Eagerly check singleton cache for manually registered singletons.
  // 从单例缓存中获取已经注册号的单例Bean实例
  Object sharedInstance = getSingleton(beanName);
  if (sharedInstance != null && args == null) {
    // 根据共享实例创建Bean实例，如果共享实例是factoryBean，则用它创建一个Bean
    beanInstance = getObjectForBeanInstance(sharedInstance, name, beanName, null);
  } else {
    // Check if bean definition exists in this factory.
    BeanFactory parentBeanFactory = getParentBeanFactory();
    // 如果父容器中还不存在该Bean，则尝试从父容器中获取该Bean，逻辑和本类一致。
    if (parentBeanFactory != null && !containsBeanDefinition(beanName)) {
      String nameToLookup = originalBeanName(name);
      if (parentBeanFactory instanceof AbstractBeanFactory) {
        return ((AbstractBeanFactory) parentBeanFactory).doGetBean(nameToLookup, requiredType, args, typeCheckOnly);
      } else if (args != null) {
        // Delegation to parent with explicit args.
        return (T) parentBeanFactory.getBean(nameToLookup, args);
      } else if (requiredType != null) {
        // No args -> delegate to standard getBean method.
        return parentBeanFactory.getBean(nameToLookup, requiredType);
      } else {
        return (T) parentBeanFactory.getBean(nameToLookup);
      }
    }

    // 标记已创建
    if (!typeCheckOnly) {
      markBeanAsCreated(beanName);
    }

    // 从缓存和父容器中都没有获取到，就要重新创建了，这里获取BeanDefinition，用于创建
    RootBeanDefinition mbd = getMergedLocalBeanDefinition(beanName);
    // Guarantee initialization of beans that the current bean depends on.
    // 获取依赖
    String[] dependsOn = mbd.getDependsOn();
    if (dependsOn != null) {
      for (String dep : dependsOn) {
        // 如果当前Bean又被它的依赖所依赖，就产生的循环依赖，报错
        if (isDependent(beanName, dep)) {
          throw new BeanCreationException(mbd.getResourceDescription(), beanName, "Circular depends-on relationship between '" + beanName + "' and '" + dep + "'");
        }
        try {
          // 创建该依赖的Bean，逻辑还是本方法的逻辑
          getBean(dep);
        } catch (NoSuchBeanDefinitionException ex) {
          throw new BeanCreationException(mbd.getResourceDescription(), beanName, "'" + beanName + "' depends on missing bean '" + dep + "'", ex);
        }
      }
    }

    // Create bean instance.
    // 如果是单例的，从缓存中获取共享实例，如果没有共享实例，则创建它
    if (mbd.isSingleton()) {
      sharedInstance = getSingleton(beanName, () -> {
        try {
          // 创建Bean
          return createBean(beanName, mbd, args);
        } catch (BeansException ex) {
          // Explicitly remove instance from singleton cache: It might have been put there
          // eagerly by the creation process, to allow for circular reference resolution.
          // Also remove any beans that received a temporary reference to the bean.
          destroySingleton(beanName);
          throw ex;
        }
      });
      // 根据共享实例创建Bean实例，如果共享实例是factoryBean，则用它创建一个Bean
      beanInstance = getObjectForBeanInstance(sharedInstance, name, beanName, mbd);
    } else if (mbd.isPrototype()) {
      // 如果是原型的，则每次都创建新的
      // It's a prototype -> create a new instance.
      Object prototypeInstance = null;
      try {
        // 创建前回调：标记该bean正在创建
        beforePrototypeCreation(beanName);
        // 创建Bean
        prototypeInstance = createBean(beanName, mbd, args);
      } finally {
        // 创建后回调：标记该bean已经没在创建
        afterPrototypeCreation(beanName);
      }
      // 根据共享实例创建Bean实例，如果共享实例是factoryBean，则用它创建一个Bean
      beanInstance = getObjectForBeanInstance(prototypeInstance, name, beanName, mbd);
    } else {
      // 原型和单例之外的scope
      String scopeName = mbd.getScope();
      // 从scopes缓存中获取指定的Scope，该对象就是一个Bean持有器
      Scope scope = this.scopes.get(scopeName);
      try {
        // 整个scope只有一个实例，从中取，没有则创建。
        Object scopedInstance = scope.get(beanName, () -> {
          // 创建前回调：标记该bean正在创建
          beforePrototypeCreation(beanName);
          try {
            // 创建Bean
            return createBean(beanName, mbd, args);
          } finally {
            // 创建后回调：标记该bean已经没在创建
            afterPrototypeCreation(beanName);
          }
        });
        // 根据共享实例创建Bean实例，如果共享实例是factoryBean，则用它创建一个Bean
        beanInstance = getObjectForBeanInstance(scopedInstance, name, beanName, mbd);
      } catch (IllegalStateException ex) {
        throw new ScopeNotActiveException(beanName, scopeName, ex);
      }
    }
  }

  // 做最后的调整，如果实例化出来的类型和想要的类型不一致，还要进行一个类型转换
  return adaptBeanInstance(name, beanInstance, requiredType);
}

<T> T adaptBeanInstance(String name, Object bean, @Nullable Class<?> requiredType) {
  // Check if required type matches the type of the actual bean instance.
  if (requiredType != null && !requiredType.isInstance(bean)) {
    try {
      Object convertedBean = getTypeConverter().convertIfNecessary(bean, requiredType);
      if (convertedBean == null) {
        throw new BeanNotOfRequiredTypeException(name, requiredType, bean.getClass());
      }
      return (T) convertedBean;
    } catch (TypeMismatchException ex) {
      throw new BeanNotOfRequiredTypeException(name, requiredType, bean.getClass());
    }
  }
  return (T) bean;
}
```

上面虽然只是预加载单例Bean的代码，但方法`doGetBean()`却是获取Bean的通用方法，对此，可以有所总结：

- 单例Bean的创建， 先从缓存中获取；如果没有，再从父容器中获取，如果再没有，则执行创建逻辑
- 如果一个Bean有依赖的Bean，则该依赖Bean将会首先被创建；如果被依赖的Bean又依赖了原Bean，则构成循环依赖，Spring将会抛出异常
- scope的实现只有三种情况
  - 单例：当`BeanDefinition`的scope没有值（即默认单例）或为`singleton`时，为单例，整个容器只维护一份实例
  - 原型：当`BeanDefinition`的scope为`prototye`时，为原型，每次都会执行一遍新建Bean的逻辑
  - 其它：当`BeanDefinition`的scope非上述任何一种时，为其它，实现方式是容器维护一个名为`scopes`的Map，每个entry的值为`Scope`对象，它就是一个容器，新建的Bean会放入该容器。构成对同一个`Scope`只存在一份Bean。
- 创建完成的Bean实例，并不能直接使用：如果有指定预期的类型，还要调用容器内维护的类型转换器进行一次类型转换，得到最终值

对于正常情况下的Bean获取方法如`org.springframework.context.support.AbstractApplicationContext#getBean(java.lang.String)`，有如下

```java
public Object getBean(String name) throws BeansException {
  assertBeanFactoryActive();
  return getBeanFactory().getBean(name);
}

public Object getBean(String name) throws BeansException {
  // 可以看到它又是调用了doGetBean()，还是那个通用方法
  return doGetBean(name, null, null, false);
}
```

可以看到它又是调用了doGetBean()，还是那个通用方法，这里略过不记。

### MergedBeanDefinition

先说明，没有这个类或接口定义，但是前文”如何描述Bean“提到了合并Bean定义的概念，”Bean的创建逻辑“又再次看到了这个概念，它到底什么意思？我们从`org.springframework.beans.factory.support.AbstractBeanFactory#getMergedLocalBeanDefinition`方法来看

```java
protected RootBeanDefinition getMergedLocalBeanDefinition(String beanName) throws BeansException {
  // 先从缓存中获取结果
  RootBeanDefinition mbd = this.mergedBeanDefinitions.get(beanName);
  if (mbd != null && !mbd.stale) {
    return mbd;
  }
  return getMergedBeanDefinition(beanName, getBeanDefinition(beanName));
}

protected RootBeanDefinition getMergedBeanDefinition(String beanName, BeanDefinition bd) throws BeanDefinitionStoreException {
  return getMergedBeanDefinition(beanName, bd, null);
}
/**
 * 真实的获取mergedBeanDefinition的方法
 * 参数说明
 * beanName: bean的名称
 * bd: bean的定义
 * contaningBd: 包含该bean的bean定义（该bean是一个内部bean）
 **/
protected RootBeanDefinition getMergedBeanDefinition(String beanName, BeanDefinition bd, @Nullable BeanDefinition containingBd) throws BeanDefinitionStoreException {
  synchronized (this.mergedBeanDefinitions) {
    RootBeanDefinition mbd = null;
    RootBeanDefinition previous = null;

    // Check with full lock now in order to enforce the same merged instance.
    if (containingBd == null) {
      mbd = this.mergedBeanDefinitions.get(beanName);
    }

    if (mbd == null || mbd.stale) {
      previous = mbd;
      // 如果当前Bean定义没有父Bean定义，则创建RootBeanDefinition
      if (bd.getParentName() == null) {
        // Use copy of given root bean definition.
        if (bd instanceof RootBeanDefinition) {
          mbd = ((RootBeanDefinition) bd).cloneBeanDefinition();
        } else {
          mbd = new RootBeanDefinition(bd);
        }
      } else {
        // 否则，该Bean定义是一个子Bean定义，则需要和父Bean定义进行合并
        // Child bean definition: needs to be merged with parent.
        BeanDefinition pbd;
        try {
          String parentBeanName = transformedBeanName(bd.getParentName());
          // 递归逻辑获取父Bean定义，从当前容器或父容器中获取
          if (!beanName.equals(parentBeanName)) {
            pbd = getMergedBeanDefinition(parentBeanName);
          } else {
            BeanFactory parent = getParentBeanFactory();
            if (parent instanceof ConfigurableBeanFactory) {
              pbd = ((ConfigurableBeanFactory) parent).getMergedBeanDefinition(parentBeanName);
            }
          }
        } catch (NoSuchBeanDefinitionException ex) {
          throw new BeanDefinitionStoreException(bd.getResourceDescription(), beanName,
                                                 "Could not resolve parent bean definition '" + bd.getParentName() + "'", ex);
        }
        // Deep copy with overridden values.
        mbd = new RootBeanDefinition(pbd);
        // 用子Bean定义覆盖父Bean定义，得到一个”合并“后的Bean定义
        mbd.overrideFrom(bd);
      }

      // Set default singleton scope, if not configured before.
      // 默认设置为单例
      if (!StringUtils.hasLength(mbd.getScope())) {
        mbd.setScope(SCOPE_SINGLETON);
      }

      // A bean contained in a non-singleton bean cannot be a singleton itself.
      // Let's correct this on the fly here, since this might be the result of
      // parent-child merging for the outer bean, in which case the original inner bean
      // definition will not have inherited the merged outer bean's singleton status.
      // bean需要和包含它的bean的scope保持一致
      if (containingBd != null && !containingBd.isSingleton() && mbd.isSingleton()) {
        mbd.setScope(containingBd.getScope());
      }

      // Cache the merged bean definition for the time being
      // (it might still get re-merged later on in order to pick up metadata changes)
      if (containingBd == null && isCacheBeanMetadata()) {
        this.mergedBeanDefinitions.put(beanName, mbd);
      }
    }
    // 合并后的Bean定义可被标记为stale，标识需要重新被合并，这里执行合并逻辑
    if (previous != null) {
      copyRelevantMergedBeanDefinitionCaches(previous, mbd);
    }
    return mbd;
  }
}

private void copyRelevantMergedBeanDefinitionCaches(RootBeanDefinition previous, RootBeanDefinition mbd) {
  if (ObjectUtils.nullSafeEquals(mbd.getBeanClassName(), previous.getBeanClassName()) &&
      ObjectUtils.nullSafeEquals(mbd.getFactoryBeanName(), previous.getFactoryBeanName()) &&
      ObjectUtils.nullSafeEquals(mbd.getFactoryMethodName(), previous.getFactoryMethodName())) {
    ResolvableType targetType = mbd.targetType;
    ResolvableType previousTargetType = previous.targetType;
    if (targetType == null || targetType.equals(previousTargetType)) {
      mbd.targetType = previousTargetType;
      mbd.isFactoryBean = previous.isFactoryBean;
      mbd.resolvedTargetType = previous.resolvedTargetType;
      mbd.factoryMethodReturnType = previous.factoryMethodReturnType;
      mbd.factoryMethodToIntrospect = previous.factoryMethodToIntrospect;
    }
  }
}
```

关键是父Bean定义被子Bean定义覆盖，看`org.springframework.beans.factory.support.AbstractBeanDefinition#overrideFrom`

```java
// 不过你看，貌似也没什么不同，就正常的Bean定义的属性呀
public void overrideFrom(BeanDefinition other) {
  if (StringUtils.hasLength(other.getBeanClassName())) {
    setBeanClassName(other.getBeanClassName());
  }
  if (StringUtils.hasLength(other.getScope())) {
    setScope(other.getScope());
  }
  setAbstract(other.isAbstract());
  if (StringUtils.hasLength(other.getFactoryBeanName())) {
    setFactoryBeanName(other.getFactoryBeanName());
  }
  if (StringUtils.hasLength(other.getFactoryMethodName())) {
    setFactoryMethodName(other.getFactoryMethodName());
  }
  setRole(other.getRole());
  setSource(other.getSource());
  copyAttributesFrom(other);

  if (other instanceof AbstractBeanDefinition) {
    AbstractBeanDefinition otherAbd = (AbstractBeanDefinition) other;
    if (otherAbd.hasBeanClass()) {
      setBeanClass(otherAbd.getBeanClass());
    }
    if (otherAbd.hasConstructorArgumentValues()) {
      getConstructorArgumentValues().addArgumentValues(other.getConstructorArgumentValues());
    }
    if (otherAbd.hasPropertyValues()) {
      getPropertyValues().addPropertyValues(other.getPropertyValues());
    }
    if (otherAbd.hasMethodOverrides()) {
      getMethodOverrides().addOverrides(otherAbd.getMethodOverrides());
    }
    Boolean lazyInit = otherAbd.getLazyInit();
    if (lazyInit != null) {
      setLazyInit(lazyInit);
    }
    setAutowireMode(otherAbd.getAutowireMode());
    setDependencyCheck(otherAbd.getDependencyCheck());
    setDependsOn(otherAbd.getDependsOn());
    setAutowireCandidate(otherAbd.isAutowireCandidate());
    setPrimary(otherAbd.isPrimary());
    copyQualifiersFrom(otherAbd);
    setInstanceSupplier(otherAbd.getInstanceSupplier());
    setNonPublicAccessAllowed(otherAbd.isNonPublicAccessAllowed());
    setLenientConstructorResolution(otherAbd.isLenientConstructorResolution());
    if (otherAbd.getInitMethodName() != null) {
      setInitMethodName(otherAbd.getInitMethodName());
      setEnforceInitMethod(otherAbd.isEnforceInitMethod());
    }
    if (otherAbd.getDestroyMethodName() != null) {
      setDestroyMethodName(otherAbd.getDestroyMethodName());
      setEnforceDestroyMethod(otherAbd.isEnforceDestroyMethod());
    }
    setSynthetic(otherAbd.isSynthetic());
    setResource(otherAbd.getResource());
  }
  else {
    getConstructorArgumentValues().addArgumentValues(other.getConstructorArgumentValues());
    getPropertyValues().addPropertyValues(other.getPropertyValues());
    setLazyInit(other.isLazyInit());
    setResourceDescription(other.getResourceDescription());
  }
}
```

要点总结：所谓合并，就是有父子关系的`BeanDefinition`的合并，将他们合并为一个`BeanDefinition`，合并逻辑是：用子`BeanDefinition`覆盖父`BeanDefinition`，最终结果用`RootBeanDefinition`表示。

### 自动注入

> 自动注入这块的代码实在太多，这里分成几个部分分别来说

到现在为止，我们还没看到自动注入，`BeanPostProcessor`等的执行逻辑，它们都在`org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory#createBean(java.lang.String, org.springframework.beans.factory.support.RootBeanDefinition, java.lang.Object[])`中，前文创建Bean的源码有调用它

```java
protected Object createBean(String beanName, RootBeanDefinition mbd, @Nullable Object[] args) throws BeanCreationException {
  RootBeanDefinition mbdToUse = mbd;

  // Make sure bean class is actually resolved at this point, and
  // clone the bean definition in case of a dynamically resolved Class
  // which cannot be stored in the shared merged bean definition.
  Class<?> resolvedClass = resolveBeanClass(mbd, beanName);
  if (resolvedClass != null && !mbd.hasBeanClass() && mbd.getBeanClassName() != null) {
    mbdToUse = new RootBeanDefinition(mbd);
    mbdToUse.setBeanClass(resolvedClass);
  }

  // Prepare method overrides.
  // 不用管
  mbdToUse.prepareMethodOverrides();

  // Give BeanPostProcessors a chance to return a proxy instead of the target bean instance.
  // 在某些情况下，获得的Bean可能是一个代理，此时并不需要真正执行Bean的创建逻辑，InstantiationAwareBeanPostProcessor就是用来做这个事的
  Object bean = resolveBeforeInstantiation(beanName, mbdToUse);
  if (bean != null) {
    return bean;
  }
	// 如果没有什么额外设置，就真的去创建Bean
  Object beanInstance = doCreateBean(beanName, mbdToUse, args);
  return beanInstance;
}
```

- 这里唯一需要注意的点：可以通过`InstantiationAwareBeanPostProcessor`提供一个代理实例，这为Spy之类的测试功能提供了方便，使得他们可以伪造bean，构建测试环境。

#### 创建实例前的操作

对`resolveBeforeInstantiation`，有

```java
protected Object resolveBeforeInstantiation(String beanName, RootBeanDefinition mbd) {
  Object bean = null;
  if (!Boolean.FALSE.equals(mbd.beforeInstantiationResolved)) {
    // Make sure bean class is actually resolved at this point.
    if (!mbd.isSynthetic() && hasInstantiationAwareBeanPostProcessors()) {
      // 确定Bean的类型
      Class<?> targetType = determineTargetType(beanName, mbd);
      if (targetType != null) {
        // 应用InstantiationAwareBeanPostProcessor，产生的一般都是代理
        bean = applyBeanPostProcessorsBeforeInstantiation(targetType, beanName);
        if (bean != null) {
          // 如果产生了代理，就当成已经实例化，应用所有后置处理器。注意这里为什么要调用后置处理器，因为上面产生的代理将会直接返回，不会走bean创建逻辑了
          bean = applyBeanPostProcessorsAfterInitialization(bean, beanName);
        }
      }
    }
    mbd.beforeInstantiationResolved = (bean != null);
  }
  return bean;
}

// 应用InstantiationAwareBeanPostProcessor.postProcessBeforeInstantiation，该接口专门用于实例化之前调用，以便我们能够返回一个目标对象的代理
protected Object applyBeanPostProcessorsBeforeInstantiation(Class<?> beanClass, String beanName) {
  for (InstantiationAwareBeanPostProcessor bp : getBeanPostProcessorCache().instantiationAware) {
    Object result = bp.postProcessBeforeInstantiation(beanClass, beanName);
    if (result != null) {
      return result;
    }
  }
  return null;
}

// 实例化后调用所有的后置处理器
public Object applyBeanPostProcessorsAfterInitialization(Object existingBean, String beanName) throws BeansException {
  Object result = existingBean;
  for (BeanPostProcessor processor : getBeanPostProcessors()) {
    Object current = processor.postProcessAfterInitialization(result, beanName);
    if (current == null) {
      return result;
    }
    result = current;
  }
  return result;
}
```

- 注意点同上

#### 创建实例操作总览

对创建的实际操作，有

```java
protected Object doCreateBean(String beanName, RootBeanDefinition mbd, @Nullable Object[] args) throws BeanCreationException {
  // Instantiate the bean.
  // 创建的Bean并不是直接以对象的形式存在，而是以BeanWrapper的形式存在的
  BeanWrapper instanceWrapper = null;
  if (mbd.isSingleton()) {
    // 如果是单例，从缓存中移除BeanWrapper
    instanceWrapper = this.factoryBeanInstanceCache.remove(beanName);
  }
  if (instanceWrapper == null) {
    // 真实创建步骤
    instanceWrapper = createBeanInstance(beanName, mbd, args);
  }
  Object bean = instanceWrapper.getWrappedInstance();
  Class<?> beanType = instanceWrapper.getWrappedClass();
  if (beanType != NullBean.class) {
    // 回填最终信息
    mbd.resolvedTargetType = beanType;
  }

  // Allow post-processors to modify the merged bean definition.
  synchronized (mbd.postProcessingLock) {
    if (!mbd.postProcessed) {
      // 应用所有的MergedBeanDefinitionPostProcessor
      applyMergedBeanDefinitionPostProcessors(mbd, beanType, beanName);
      mbd.postProcessed = true;
    }
  }

  // Eagerly cache singletons to be able to resolve circular references
  // even when triggered by lifecycle interfaces like BeanFactoryAware.
  // 提前暴露单例Bean引用，主要为解决循环引用问题
  boolean earlySingletonExposure = (mbd.isSingleton() && this.allowCircularReferences && isSingletonCurrentlyInCreation(beanName));
  if (earlySingletonExposure) {
    addSingletonFactory(beanName, () -> getEarlyBeanReference(beanName, mbd, bean));
  }

  // Initialize the bean instance.
  Object exposedObject = bean;

  // 执行Bean注入
  populateBean(beanName, mbd, instanceWrapper);
  // 初始化Bean
  exposedObject = initializeBean(beanName, exposedObject, mbd);

  if (earlySingletonExposure) {
    // 循环依赖检查：正常来说，提前暴露那个对象，和初始化后的bean对象，应该是一个，否则就说明出现了问题
    Object earlySingletonReference = getSingleton(beanName, false);
    if (earlySingletonReference != null) {
      if (exposedObject == bean) {
        exposedObject = earlySingletonReference;
      } else if (!this.allowRawInjectionDespiteWrapping && hasDependentBean(beanName)) {
        String[] dependentBeans = getDependentBeans(beanName);
        Set<String> actualDependentBeans = new LinkedHashSet<>(dependentBeans.length);
        for (String dependentBean : dependentBeans) {
          if (!removeSingletonIfCreatedForTypeCheckOnly(dependentBean)) {
            actualDependentBeans.add(dependentBean);
          }
        }
        if (!actualDependentBeans.isEmpty()) {
          throw ... ...
        }
      }
    }
  }

  // Register bean as disposable.
  // 将该bean注册到对应Scope的销毁回调上
  registerDisposableBeanIfNecessary(beanName, bean, mbd);

  return exposedObject;
}
```

- 注意点1：创建Bean的步骤：创建、执行注入、执行初始化操作
- 注意点2：循环引用的解决方式

##### 循环引用的解决方式

需要注意的是，这里有两种循环引用的方式

- `Scope`为单例时，则如”创建实例操作总览“中的代码那样，确切来说，应该这么梳理

  首先，Spring维护三个有关单例缓存

  - `singletonObjects`：用于维护已经创建好的单例对象
  - `earlySingletonObjects`：用于维护创建了但尚未执行自动注入和初始化的单例对象
  - `singletonFactories`：用于维护单例对象产生的工厂实例

  然后来看注入的具体方法，比如按照name注入，它还是调用了`getBean`方法获取Bean，其中会调用`getSingleton`方法获取实例对象

  - 先从`singletonObjects`中获取已经创建好的单例对象
  - 再尝试从`earlySingletonObjects`中获取创建到一般的单例对象
  - 再尝试用对应的`singletonFactories`创建出一个单例对象，注意该对象会加入`earlySingletonObjects`，所以其实为了理解方便，`singletonFactories`您可以暂时忽略

  ```java
  protected Object getSingleton(String beanName, boolean allowEarlyReference) {
    // 已经简化成这样
    singletonObject = this.singletonObjects.get(beanName);
    if (singletonObject == null) {
      singletonObject = this.earlySingletonObjects.get(beanName);
      if (singletonObject == null) {
        ObjectFactory<?> singletonFactory = this.singletonFactories.get(beanName);
        if (singletonFactory != null) {
          singletonObject = singletonFactory.getObject();
          this.earlySingletonObjects.put(beanName, singletonObject);
          this.singletonFactories.remove(beanName);
        }
      }
    }
    return singletonObject;
  }
  ```

  然后再看创建Bean时干了什么（截取前文的代码）：增加了一个`singletonFactory`，结合前面的分析，其实就是把刚创建但还没有注入属性和初始化的bean放在了`earlySingletonObjects`中，使得如果有循环依赖时能够直接获取到该bean。避免死循环。

  ```java
  if (earlySingletonExposure) {
    // getEarlyBeanReference方法，其实就是直接将传入的bean传回来了
    addSingletonFactory(beanName, () -> getEarlyBeanReference(beanName, mbd, bean));
  }
  ```

  总结来说，这里的重点是将bean的创建和初始化（包括注入）分开进行，保有一个半初始化的状态，使得能够注入半初始化状态的Bean。

  **但是，这是setter注入时才可以这么做，构造器注入又当如何呢？**事实上，因为构造器注入时，当前对象尚未创建完成，没法有一个半初始化状态，因此构造器注入不允许循环依赖。

- `Scope`为原型时，参考`AbstractBeanFactory.doCreate.273行`，这里有检查当前线程下同名的原型Bean是否正在创建。Spring是一个同步框架，在创建原型Bean时，同一个线程不可能同时创建两个原型Bean，那么很明显了，就如注释所说，这里是不允许原型Bean循环引用。

  ```java
  // Fail if we're already creating this bean instance:
  // We're assumably within a circular reference.
  if (isPrototypeCurrentlyInCreation(beanName)) {
    throw new BeanCurrentlyInCreationException(beanName);
  }
  ```

  为什么原型时不支持循环依赖？因为Spring不会缓存任何有关原型的状态，虽然它也能有中间状态，但Spring并不缓存它，这是一个技术上可以实现，但Spring的设计思想上不允许存在的场景：所谓原型，每次获取Bean都要创建一个新的，那么当循环依赖时，应该获得的是一个与”我“完全不同的Bean。

#### BeanWrapper是什么

该类不是给我们直接使用的，而是在容器内部流通。用于提供实际Bean实例的分析和操作，如针对属性的操作、查询等。它常用的只有一个实现类`BeanWrapperImpl`。了解它有助于源码的查看，这里我们简要看一下接口定义

```java
public interface BeanWrapper extends ConfigurablePropertyAccessor {
	// 获取真实的Bean实例
	Object getWrappedInstance();
	// 获取真实的Bean类
	Class<?> getWrappedClass();
	// 获取所有实例的属性描述符
	PropertyDescriptor[] getPropertyDescriptors();
	// 获取指定属性的属性描述符
	PropertyDescriptor getPropertyDescriptor(String propertyName) throws InvalidPropertyException;
}
```

#### 创建实例的确切操作

```java
protected BeanWrapper createBeanInstance(String beanName, RootBeanDefinition mbd, @Nullable Object[] args) {
  // Make sure bean class is actually resolved at this point.
  // 解析真实的bean类对象
  Class<?> beanClass = resolveBeanClass(mbd, beanName);

  // 如果BeanDefinitino有提供用于创建实例的Supplier，则直接用它创建。Supplier的应用场景，有待探索
  Supplier<?> instanceSupplier = mbd.getInstanceSupplier();
  if (instanceSupplier != null) {
    return obtainFromSupplier(instanceSupplier, beanName);
  }

  // 如果有指定工厂方法，直接通过工厂方法创建
  if (mbd.getFactoryMethodName() != null) {
    return instantiateUsingFactoryMethod(beanName, mbd, args);
  }

  // Shortcut when re-creating the same bean...
  boolean resolved = false;
  boolean autowireNecessary = false;
  if (args == null) {
    synchronized (mbd.constructorArgumentLock) {
      if (mbd.resolvedConstructorOrFactoryMethod != null) {
        resolved = true;
        autowireNecessary = mbd.constructorArgumentsResolved;
      }
    }
  }
  // 如果BeanDefinition的构造器已经被解析出来了，则直接用他们创建
  if (resolved) {
    if (autowireNecessary) {
      // 通过构造器创建，并注入构造器参数
      return autowireConstructor(beanName, mbd, null, null);
    } else {
      // 直接使用无参构造器创建
      return instantiateBean(beanName, mbd);
    }
  }

  // 如果有SmartInstantiationAwareBeanPostProcessor提供构造器，则使用该构造器创建
  Constructor<?>[] ctors = determineConstructorsFromBeanPostProcessors(beanClass, beanName);
  if (ctors != null || mbd.getResolvedAutowireMode() == AUTOWIRE_CONSTRUCTOR ||
      mbd.hasConstructorArgumentValues() || !ObjectUtils.isEmpty(args)) {
    return autowireConstructor(beanName, mbd, ctors, args);
  }

  // 使用默认构造器创建
  ctors = mbd.getPreferredConstructors();
  if (ctors != null) {
    return autowireConstructor(beanName, mbd, ctors, null);
  }

  // 直接使用无参构造器创建
  return instantiateBean(beanName, mbd);
}
```

- 创建备选方式的顺序
  1. 提前设置的`Supplier`
  2. 指定的工厂方法
  3. 使用`BeanDefinition`提前解析好的构造器创建
  4. 使用`SmartInstantiationAwareBeanPostProcessor`提供的构造器创建
  5. 使用类自带的有参构造器创建，参数来自容器，自动注入
  6. 使用类自带的无参构造器创建

##### 按有参构造器注入并创建

```java
public BeanWrapper autowireConstructor(String beanName, RootBeanDefinition mbd, @Nullable Constructor<?>[] chosenCtors, @Nullable Object[] explicitArgs) {
  BeanWrapperImpl bw = new BeanWrapperImpl();
  // 这里初始化只是注入了类型转换相关内容
  this.beanFactory.initBeanWrapper(bw);

  Constructor<?> constructorToUse = null;
  ArgumentsHolder argsHolderToUse = null;
  Object[] argsToUse = null;

  if (explicitArgs != null) {
    // 给了args就直接用
    argsToUse = explicitArgs;
  } else {
    // 没给args，就从BeanDefinition中找到args拿出来用
    Object[] argsToResolve = null;
    synchronized (mbd.constructorArgumentLock) {
      constructorToUse = (Constructor<?>) mbd.resolvedConstructorOrFactoryMethod;
      if (constructorToUse != null && mbd.constructorArgumentsResolved) {
        // Found a cached constructor...
        argsToUse = mbd.resolvedConstructorArguments;
        if (argsToUse == null) {
          argsToResolve = mbd.preparedConstructorArguments;
        }
      }
    }
    if (argsToResolve != null) {
      argsToUse = resolvePreparedArguments(beanName, mbd, bw, constructorToUse, argsToResolve);
    }
  }

  if (constructorToUse == null || argsToUse == null) {
    // Take specified constructors, if any.
    Constructor<?>[] candidates = chosenCtors;
    // 获取类的所有构造方法作为候选
    if (candidates == null) {
      Class<?> beanClass = mbd.getBeanClass();
      candidates = (mbd.isNonPublicAccessAllowed() ? beanClass.getDeclaredConstructors() : beanClass.getConstructors());
    }
    // 如果对象只有一个无参构造器，则可以直接创建对象，不需要走自动注入
    if (candidates.length == 1 && explicitArgs == null && !mbd.hasConstructorArgumentValues()) {
      Constructor<?> uniqueCandidate = candidates[0];
      if (uniqueCandidate.getParameterCount() == 0) {
        synchronized (mbd.constructorArgumentLock) {
          mbd.resolvedConstructorOrFactoryMethod = uniqueCandidate;
          mbd.constructorArgumentsResolved = true;
          mbd.resolvedConstructorArguments = EMPTY_ARGS;
        }
        bw.setBeanInstance(instantiate(beanName, mbd, uniqueCandidate, EMPTY_ARGS));
        return bw;
      }
    }

    // Need to resolve the constructor.
    // 需要自动注入的判断标准：有构造器，或者BeanDefinition的注入模式为构造器注入
    boolean autowiring = (chosenCtors != null || mbd.getResolvedAutowireMode() == AutowireCapableBeanFactory.AUTOWIRE_CONSTRUCTOR);
    ConstructorArgumentValues resolvedValues = null;

    int minNrOfArgs;
    if (explicitArgs != null) {
      minNrOfArgs = explicitArgs.length;
    } else {
      ConstructorArgumentValues cargs = mbd.getConstructorArgumentValues();
      resolvedValues = new ConstructorArgumentValues();
      minNrOfArgs = resolveConstructorArguments(beanName, mbd, bw, cargs, resolvedValues);
    }

    AutowireUtils.sortConstructors(candidates);
    int minTypeDiffWeight = Integer.MAX_VALUE;
    Set<Constructor<?>> ambiguousConstructors = null;
    Deque<UnsatisfiedDependencyException> causes = null;
    // 寻找要用哪个构造器创建Bean
    for (Constructor<?> candidate : candidates) {
      int parameterCount = candidate.getParameterCount();

      ArgumentsHolder argsHolder;
      Class<?>[] paramTypes = candidate.getParameterTypes();
      if (resolvedValues != null) {
        String[] paramNames = ConstructorPropertiesChecker.evaluate(candidate, parameterCount);
        if (paramNames == null) {
          ParameterNameDiscoverer pnd = this.beanFactory.getParameterNameDiscoverer();
          if (pnd != null) {
            paramNames = pnd.getParameterNames(candidate);
          }
        }
        // 这里在容器中寻找符合要求的bean，构建出符合要求的参数，以便在后面使用
        argsHolder = createArgumentArray(beanName, mbd, resolvedValues, bw, paramTypes, paramNames, getUserDeclaredConstructor(candidate), autowiring, candidates.length == 1);
      } else {
        // Explicit arguments given -> arguments length must match exactly.
        if (parameterCount != explicitArgs.length) {
          continue;
        }
        argsHolder = new ArgumentsHolder(explicitArgs);
      }
			// 权重计算规则：将给的参数类型和实际构造器对应位置的参数进行类型对比，越符合得分越高。
      int typeDiffWeight = (mbd.isLenientConstructorResolution() ?  argsHolder.getTypeDifferenceWeight(paramTypes) : argsHolder.getAssignabilityWeight(paramTypes));
      // Choose this constructor if it represents the closest match.
      // 冒泡法找出最符合要求那个，如果两个权重一致，则加入 ”无法区分“ 的列表
      if (typeDiffWeight < minTypeDiffWeight) {
        constructorToUse = candidate;
        argsHolderToUse = argsHolder;
        argsToUse = argsHolder.arguments;
        minTypeDiffWeight = typeDiffWeight;
        ambiguousConstructors = null;
      } else if (constructorToUse != null && typeDiffWeight == minTypeDiffWeight) {
        if (ambiguousConstructors == null) {
          ambiguousConstructors = new LinkedHashSet<>();
          ambiguousConstructors.add(constructorToUse);
        }
        ambiguousConstructors.add(candidate);
      }
    }

    // 最终没有构造器被选中，报错
    if (constructorToUse == null) {
      throw new BeanCreationException(......);
    } else if (ambiguousConstructors != null && !mbd.isLenientConstructorResolution()) {
      // 最终有多个构造器符合条件，无法区分用哪个，也报错
      throw new BeanCreationException(......);
    }
  }

  Assert.state(argsToUse != null, "Unresolved constructor arguments");
  // 利用反射创建Bean实例
  bw.setBeanInstance(instantiate(beanName, mbd, constructorToUse, argsToUse));
  return bw;
}
```

- Spring会先从容器中找出满足类型要求的参数组合，然后找出与这些参数类型最为匹配的构造器，用以创建实例
- 可以想见，只要有精确类型的bean被创建，就一定能够实例化成功，因为不可能有完全一样参数类型的构造器嘛

##### 使用无参构造器创建

```java
protected BeanWrapper instantiateBean(String beanName, RootBeanDefinition mbd) {
  // 这里不用再追进去看了，它就是获取了类的无参构造方法，然后通过反射实例化
  Object beanInstance = getInstantiationStrategy().instantiate(mbd, beanName, this);
  // 包装成BeanWrapper
  BeanWrapper bw = new BeanWrapperImpl(beanInstance);
  initBeanWrapper(bw);
  return bw;
}
```

#### 自动注入逻辑的执行

对自动注入的逻辑，即`populateBean()`，有

```java
// 执行Bean注入
protected void populateBean(String beanName, RootBeanDefinition mbd, @Nullable BeanWrapper bw) {
  // Give any InstantiationAwareBeanPostProcessors the opportunity to modify the
  // state of the bean before properties are set. This can be used, for example,
  // to support styles of field injection.
  if (!mbd.isSynthetic() && hasInstantiationAwareBeanPostProcessors()) {
    // 应用InstantiationAwareBeanPostProcessor，在实例刚刚创建后，属性被设置之前执行
    for (InstantiationAwareBeanPostProcessor bp : getBeanPostProcessorCache().instantiationAware) {
      if (!bp.postProcessAfterInstantiation(bw.getWrappedInstance(), beanName)) {
        return;
      }
    }
  }

  PropertyValues pvs = (mbd.hasPropertyValues() ? mbd.getPropertyValues() : null);

  // 自定注入模式：自动检测、按名字、按类型；
  int resolvedAutowireMode = mbd.getResolvedAutowireMode();
  if (resolvedAutowireMode == AUTOWIRE_BY_NAME || resolvedAutowireMode == AUTOWIRE_BY_TYPE) {
    MutablePropertyValues newPvs = new MutablePropertyValues(pvs);
    // Add property values based on autowire by name if applicable.
    if (resolvedAutowireMode == AUTOWIRE_BY_NAME) {
      // 按名称注入
      autowireByName(beanName, mbd, bw, newPvs);
    }
    // Add property values based on autowire by type if applicable.
    if (resolvedAutowireMode == AUTOWIRE_BY_TYPE) {
      // 按类型注入
      autowireByType(beanName, mbd, bw, newPvs);
    }
    pvs = newPvs;
  }

  boolean hasInstAwareBpps = hasInstantiationAwareBeanPostProcessors();
  boolean needsDepCheck = (mbd.getDependencyCheck() != AbstractBeanDefinition.DEPENDENCY_CHECK_NONE);

  PropertyDescriptor[] filteredPds = null;
  if (hasInstAwareBpps) {
    if (pvs == null) {
      pvs = mbd.getPropertyValues();
    }
    // 应用InstantiationAwareBeanPostProcessor.postProcessProperties和postProcessPropertyValues方法
    for (InstantiationAwareBeanPostProcessor bp : getBeanPostProcessorCache().instantiationAware) {
      PropertyValues pvsToUse = bp.postProcessProperties(pvs, bw.getWrappedInstance(), beanName);
      if (pvsToUse == null) {
        if (filteredPds == null) {
          filteredPds = filterPropertyDescriptorsForDependencyCheck(bw, mbd.allowCaching);
        }
        pvsToUse = bp.postProcessPropertyValues(pvs, filteredPds, bw.getWrappedInstance(), beanName);
        if (pvsToUse == null) {
          return;
        }
      }
      pvs = pvsToUse;
    }
  }
  if (needsDepCheck) {
    if (filteredPds == null) {
      filteredPds = filterPropertyDescriptorsForDependencyCheck(bw, mbd.allowCaching);
    }
    // 依赖检查：检查是否所有需要的属性都已被设置
    checkDependencies(beanName, mbd, filteredPds, pvs);
  }
  if (pvs != null) {
    // 真正地去应用这些属性
    applyPropertyValues(beanName, mbd, bw, pvs);
  }
}

// 按照名称注入，就是从容器中找出指定名称的bean，然后加到暂存的属性集中，以便后面使用
protected void autowireByName(String beanName, AbstractBeanDefinition mbd, BeanWrapper bw, MutablePropertyValues pvs) {
  String[] propertyNames = unsatisfiedNonSimpleProperties(mbd, bw);
  for (String propertyName : propertyNames) {
    if (containsBean(propertyName)) {
      // 获取指定名称的Bean
      Object bean = getBean(propertyName);
      pvs.add(propertyName, bean);
      // 注册Bean依赖缓存
      registerDependentBean(propertyName, beanName);
    }
  }
}

// 按类型注入，稍微复杂一点，大致就是从容器找出符合类型的所有bean，再按照一定规则得到确切的那个
protected void autowireByType(String beanName, AbstractBeanDefinition mbd, BeanWrapper bw, MutablePropertyValues pvs) {

  TypeConverter converter = getCustomTypeConverter();
  if (converter == null) {
    converter = bw;
  }

  Set<String> autowiredBeanNames = new LinkedHashSet<>(4);
  String[] propertyNames = unsatisfiedNonSimpleProperties(mbd, bw);
  for (String propertyName : propertyNames) {
    PropertyDescriptor pd = bw.getPropertyDescriptor(propertyName);
    // Don't try autowiring by type for type Object: never makes sense,
    // even if it technically is a unsatisfied, non-simple property.
    if (Object.class != pd.getPropertyType()) {
      // 获取属性的set方法
      MethodParameter methodParam = BeanUtils.getWriteMethodParameter(pd);
      // Do not allow eager init for type matching in case of a prioritized post-processor.
      boolean eager = !(bw.getWrappedInstance() instanceof PriorityOrdered);
      DependencyDescriptor desc = new AutowireByTypeDependencyDescriptor(methodParam, eager);
      Object autowiredArgument = resolveDependency(desc, beanName, autowiredBeanNames, converter);
      if (autowiredArgument != null) {
        pvs.add(propertyName, autowiredArgument);
      }
      for (String autowiredBeanName : autowiredBeanNames) {
        // 注册Bean依赖缓存
        registerDependentBean(autowiredBeanName, beanName);
      }
      autowiredBeanNames.clear();
    }
  }
}
```

#### 实例初始化的操作

对初始化的逻辑有

```java
// 初始化Bean
protected Object initializeBean(String beanName, Object bean, @Nullable RootBeanDefinition mbd) {
  // 调用xxxAware，注入对应内容，这里管的有：BeanNameAware、BeanClassLoaderAware、BeanFactoryAware三个
  invokeAwareMethods(beanName, bean);
  Object wrappedBean = bean;
  if (mbd == null || !mbd.isSynthetic()) {
    // 应用所有的BeanPostProcessor.postProcessBeforeInitialization方法
    wrappedBean = applyBeanPostProcessorsBeforeInitialization(wrappedBean, beanName);
  }
  // 调用初始化方法，这里管的有：InitializingBean.afterPropertiesSet、自定义的init方法
  invokeInitMethods(beanName, wrappedBean, mbd);
  if (mbd == null || !mbd.isSynthetic()) {
    // 应用所有BeanPostProcessor.postProcessAfterInitialization方法
    wrappedBean = applyBeanPostProcessorsAfterInitialization(wrappedBean, beanName);
  }

  return wrappedBean;
}
```

- 实例化包含内容
  - `BeanxxxAware`接口的调用
  - `BeanPostProcessor.postProcessBeforeInitialization`的调用
  - `InitializingBean.afterPropertiesSet`的调用
  - 自定义初始化方法的调用
  - `BeanPostProcessor.postProcessAfterInitialization`的调用

#### 根据依赖类型得到依赖实例的操作

在执行自动注入逻辑时，有用到如下方法，我们一起来看看它干了什么：`org.springframework.beans.factory.config.AutowireCapableBeanFactory#resolveDependency(org.springframework.beans.factory.config.DependencyDescriptor, java.lang.String, java.util.Set<java.lang.String>, org.springframework.beans.TypeConverter)`

```java
javaxInjectProviderClass = ClassUtils.forName("javax.inject.Provider", DefaultListableBeanFactory.class.getClassLoader());
/**
 * 在当前容器下，解析指定的依赖所对应的Bean
 * desciptor: 依赖描述类，该依赖可以是字段、方法、构造器依赖，该描述类包含了这些参数信息
 * requestingBeanName: 声明该依赖的bean名称
 * autowiredBeanNames: 一个放结果的地方，用来存找到的依赖的bean名称
 * typeConverter: 需要用到的类型转换器
 * 返回值：返回依赖的Bean
 **/
public Object resolveDependency(DependencyDescriptor descriptor, @Nullable String requestingBeanName, @Nullable Set<String> autowiredBeanNames, @Nullable TypeConverter typeConverter) throws BeansException {
  // 初始化参数名搜索器
  descriptor.initParameterNameDiscovery(getParameterNameDiscoverer());
  if (Optional.class == descriptor.getDependencyType()) {
    // 如果依赖的类型是Optional的，则按照对应逻辑创建
    return createOptionalDependency(descriptor, requestingBeanName);
  } else if (ObjectFactory.class == descriptor.getDependencyType() || ObjectProvider.class == descriptor.getDependencyType()) {
    // 如果依赖的类型是工厂或Provider（也是工厂的一种），则返回DependencyObjectProvider
    return new DependencyObjectProvider(descriptor, requestingBeanName);
  } else if (javaxInjectProviderClass == descriptor.getDependencyType()) {
    // 如果依赖的类型是javax.inject.Provider，则按照JSR330解析
    return new Jsr330Factory().createDependencyProvider(descriptor, requestingBeanName);
  } else {
    // 如果支持延迟创建，则解析结果是一个代理
    Object result = getAutowireCandidateResolver().getLazyResolutionProxyIfNecessary(descriptor, requestingBeanName);
    if (result == null) {
      // 这才是真正的创建
      result = doResolveDependency(descriptor, requestingBeanName, autowiredBeanNames, typeConverter);
    }
    return result;
  }
}

public Object doResolveDependency(DependencyDescriptor descriptor, @Nullable String beanName, @Nullable Set<String> autowiredBeanNames, @Nullable TypeConverter typeConverter) throws BeansException {
  // 获取该依赖的类型
  Class<?> type = descriptor.getDependencyType();
  // 获取用户设置注入时显式指定的值，比如@Qualifier中的值，这里的suggest是用户建议的意思，并非自动推算出来的
  Object value = getAutowireCandidateResolver().getSuggestedValue(descriptor);
  if (value != null) {
    // 如果建议值为字符串，则解析该字符串，并从容器中获取解析后对应的name的容器
    if (value instanceof String) {
      // 解析字符串，这意味着该字符串可以是SPEL表达式
      String strVal = resolveEmbeddedValue((String) value);
      BeanDefinition bd = (beanName != null && containsBean(beanName) ? getMergedBeanDefinition(beanName) : null);
      // 获取最终值，这里的BeanDefinition传进去只是为了获取scope值
      value = evaluateBeanDefinitionString(strVal, bd);
    }
    TypeConverter converter = (typeConverter != null ? typeConverter : getTypeConverter());
    // 类型转换
    return converter.convertIfNecessary(value, type, descriptor.getTypeDescriptor());
  }
  // 尝试将Bean当做集合类型取解析
  Object multipleBeans = resolveMultipleBeans(descriptor, beanName, autowiredBeanNames, typeConverter);
  if (multipleBeans != null) {
    return multipleBeans;
  }
  // 从整个容器中获取符合要求的bean
  Map<String, Object> matchingBeans = findAutowireCandidates(beanName, type, descriptor);
  if (matchingBeans.isEmpty()) {
    if (isRequired(descriptor)) {
      raiseNoMatchingBeanFound(type, descriptor.getResolvableType(), descriptor);
    }
    // 还是找不到，就是null
    return null;
  }

  String autowiredBeanName;
  Object instanceCandidate;

  // 如果匹配到的bean个数大于1，则需要做一个挑选
  if (matchingBeans.size() > 1) {
    // 首先根据Primary进行挑选，然后根据Priority进行排序挑选，最后根据找到的name和依赖的name是否一致进行挑选
    autowiredBeanName = determineAutowireCandidate(matchingBeans, descriptor);
    // 当没有Primary，又没有实现Priority，名字又不匹配时，就可能找不到
    if (autowiredBeanName == null) {
      if (isRequired(descriptor) || !indicatesMultipleBeans(type)) {
        // 有可能描述符有自己定义的应办法
        return descriptor.resolveNotUnique(descriptor.getResolvableType(), matchingBeans);
      } else {
        // In case of an optional Collection/Map, silently ignore a non-unique case:
        // possibly it was meant to be an empty collection of multiple regular beans
        // (before 4.3 in particular when we didn't even look for collection beans).
        // 描述符都没有，那就诶null
        return null;
      }
    }
    // 这就是匹配到的那个
    instanceCandidate = matchingBeans.get(autowiredBeanName);
  } else {
    // We have exactly one match.
    // 刚好有一个匹配时，一切都很美好
    Map.Entry<String, Object> entry = matchingBeans.entrySet().iterator().next();
    autowiredBeanName = entry.getKey();
    instanceCandidate = entry.getValue();
  }

  if (autowiredBeanNames != null) {
    // 将找到的bean name放到接收集合中
    autowiredBeanNames.add(autowiredBeanName);
  }
  if (instanceCandidate instanceof Class) {
    // 解析得到最终的实例
    instanceCandidate = descriptor.resolveCandidate(autowiredBeanName, type, this);
  }
  Object result = instanceCandidate;

  return result;
}

protected Map<String, Object> findAutowireCandidates(@Nullable String beanName, Class<?> requiredType, DependencyDescriptor descriptor) {
  // 获取当前容器和所有父容器中指定类型的所有bean名字，作为候选
  String[] candidateNames = BeanFactoryUtils.beanNamesForTypeIncludingAncestors(this, requiredType, true, descriptor.isEager());
  Map<String, Object> result = CollectionUtils.newLinkedHashMap(candidateNames.length);
  for (Map.Entry<Class<?>, Object> classObjectEntry : this.resolvableDependencies.entrySet()) {
    Class<?> autowiringType = classObjectEntry.getKey();
    if (autowiringType.isAssignableFrom(requiredType)) {
      Object autowiringValue = classObjectEntry.getValue();
      autowiringValue = AutowireUtils.resolveAutowiringValue(autowiringValue, requiredType);
      if (requiredType.isInstance(autowiringValue)) {
        result.put(ObjectUtils.identityToString(autowiringValue), autowiringValue);
        break;
      }
    }
  }
  for (String candidate : candidateNames) {
    // 如果这些候选bean开启了自动注入开关
    if (!isSelfReference(beanName, candidate) && isAutowireCandidate(candidate, descriptor)) {
      // 加入候选
      addCandidateEntry(result, candidate, descriptor, requiredType);
    }
  }
  ... ...
    return result;
}
private void addCandidateEntry(Map<String, Object> candidates, String candidateName, DependencyDescriptor descriptor, Class<?> requiredType) {
  // 下面就是不同类型的描述符的不同解析方式，这里不深究。
  if (descriptor instanceof MultiElementDescriptor) {
    Object beanInstance = descriptor.resolveCandidate(candidateName, requiredType, this);
    if (!(beanInstance instanceof NullBean)) {
      candidates.put(candidateName, beanInstance);
    }
  } else if (containsSingleton(candidateName) || (descriptor instanceof StreamDependencyDescriptor && ((StreamDependencyDescriptor) descriptor).isOrdered())) {
    Object beanInstance = descriptor.resolveCandidate(candidateName, requiredType, this);
    candidates.put(candidateName, (beanInstance instanceof NullBean ? null : beanInstance));
  } else {
    candidates.put(candidateName, getType(candidateName));
  }
}
```

### 小结

Bean的创建，可说是重中之重，因为它关系到Spring的生命周期，这是面试中超高频率被问到的问题。有了上面的分析，我们可以自己总结一波创建过程会经过哪些关键过程，这其实有两种case

**case1**

1. 首先执行`InstantiationAwareBeanPostProcessor.postProcessBeforeInstantiation()`提供一个创建代理的机会，如果代理创建成功
2. 执行所有的`BeanPostProcessor.postProcessAfterInitialization()`方法
3. 对于预加载的单例Bean，还会调用`SmartInitializingSingleton.afterSingletonsInstantiated()`
4. 结束

**case2**

1. 实例化Bean
    1. 尝试使用指定的工厂方法创建
    2. 尝试使用构造方法创建，如果使用有参构造方法，构造方法的参数会被自动注入
2. 应用`InstantiationAwareBeanPostProcessor.postProcessAfterInstantiation()`
3. 对需要的属性进行自动注入，按名称或类型从容器中寻找符合要求的Bean，注入
4. 调用`BeanNameAware、BeanClassLoaderAware、BeanFactoryAware`
5. 应用`BeanPostProcessor.postProcessBeforeInitialization()`
6. 应用`InitializingBean.afterPropertiesSet()`
7. 应用自定义init方法
8. 应用`BeanPostProcessor.postProcessAfterInitialization`
9. 对于预加载的单例Bean，还会调用`SmartInitializingSingleton.afterSingletonsInstantiated()`
9. 结束

注意这里讨论的是Spring中Bean的生命周期，而不是Spring的生命周期，如果是后者，请翻看第一篇文章分析。

## 如何销毁Bean

JVM中的对象，通过可达性分析，垃圾回收机制，进行回收；Spring中的Bean对象，总是被容器持有，岂不是永远不可能被垃圾回收？这个想法是正确的，这种设计也是合理的。但要注意到有一个前提：`Scope`，正因为有它的存在，Bean的生命周期管理才变得方便。

- 对于`Scope`为单例的Bean，容器全局唯一，被容器引用，当然不会也不能被销毁
- 对于`Scope`为原型的Bean，创建完成后容器内部并没有引用，交给应用程序，这和普通new出来的对象一致，是能够被回收的
- 对于`Scope`为其它的Bean，则看`Scope`而定，`Scope`销毁，Bean对象一并被回收，这种情况没见过；要不然就交给`Scope`自己处理了，这倒是见过，比如web里面的Request或Session范围的Scope，它是将Bean对象保存在`HttpServletRequest`或`HttpSession`中，即生命周期随请求或Session的销毁而结束。

我们关注两个点：随容器一起销毁的Bean如何销毁；生命周期不跟随容器的Bean如何销毁

### 被容器销毁

容器的销毁方法

```java
protected void doClose() {
  // Check whether an actual close attempt is necessary...
  if (this.active.get() && this.closed.compareAndSet(false, true)) {
    // 发布容器关闭事件
    publishEvent(new ContextClosedEvent(this));

    // 调用生命周期处理器的关闭方法.
    if (this.lifecycleProcessor != null) {
      this.lifecycleProcessor.onClose();
    }

    // 重头戏：销毁Bean
    destroyBeans();

    // Close the state of this context itself.
    // 其实没干啥
    closeBeanFactory();

    // Let subclasses do some final clean-up if they wish...
    // 容器的生命周期方法
    onClose();

    // Switch to inactive.
    this.active.set(false);
  }
}

protected void destroyBeans() {
  getBeanFactory().destroySingletons();
}

public void destroySingletons() {
  String[] disposableBeanNames;
  synchronized (this.disposableBeans) {
    disposableBeanNames = StringUtils.toStringArray(this.disposableBeans.keySet());
  }
  for (int i = disposableBeanNames.length - 1; i >= 0; i--) {
    destroySingleton(disposableBeanNames[i]);
  }
}

public void destroySingleton(String beanName) {
  ... ... 
  destroyBean(beanName, disposableBean);
}

protected void destroyBean(String beanName, @Nullable DisposableBean bean) {
  ... ...
  bean.destroy();
  ... ...
}
```

可以看到，容器关闭时，只销毁了单例Bean，调用了两个有关生命周期的方法

- `LifyCycle.close()`
- `DisposableBean.destroy()`

但还有一种Bean的销毁回调没有被我们看到：自定义销毁方法的调用

### 被JVM销毁

正如注解方法`org.springframework.context.annotation.Bean#destroyMethod`上的注释而言，只有生命周期被容器完全控制的Bean才能正常被容器调用各种销毁方法，也就是单例，其它`Scope`都无法保证。因此类似原型、上面说的Session之类的生命周期方法，都是不能被正常调用的，因为容器管不了他们呀。

> Note: Only invoked on beans whose lifecycle is under the full control of the factory, which is always the case for singletons but not guaranteed for any other scope.

## 总结

这文章写了三天你能信？？？

总结一下，本文从源码的角度，介绍了Spring如何描述Bean，如何在容器创建时扫描Bean，在不同的时机如何创建Bean，Bean的循环依赖的解决方式，自动注入的逻辑，不同`Scope`的Bean的销毁场景等问题。但已就算是走马观花，不过今后遇到问题时应该很快能够定位问题吧🤔。

### 命名规则

- xxxxProvider：Provider算是策略模式+抽象工厂模式的结合。所谓抽象工厂模式，意味着它封装了创建实例的过程；所谓策略模式，意味着它可以被当做策略传入其它以他为基础的类中。比如`ClassPathScanningCandidateComponentProvider`之于`AnnotationConfigApplicationContext`。

### 下一篇写什么

Spring源码剖析 - 强大的`BeanPostProcessor`
