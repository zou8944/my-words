---
created_at: 2021-09-27 20:43:49.826
updated_at: 2021-09-27 20:56:20.48
slug: java-cache-introduction
tags:
- Java
- 缓存
---

> 本文，我们主要聊一下Java中缓存的使用，几个点
>
> - Java对缓存的抽象——JSR107
> - Spring对缓存的抽象——Spring Cache
> - Redis如何集成到Spring中——作为Spring Cache的实现、直接使用RedisCache、使用RedisTemplate

<!-- more -->

## 先说点啥

缓存嘛，都知道是咋回事。常见的缓存如Memcached、Redis、Caffine等，各自也有对应的API。使用它们，直接操作API即可。当然，本文并非讨论各种缓存的API的用法，而是在Java中使用缓存的标准方法。无关具体实现，即，Java中的缓存抽象。

就Java本身而言，有JSR107，专门对缓存定义的抽象；如果使用Spring，则有Spring Cache抽象，二者虽不同，但大体思想一致，且Spring Cache还提供了对JSR107注解的兼容。我们具体来看。

## JSR107

JSR107是Java针对缓存所定的规范，旨在让Java程序员以最低的学习成本学会缓存的使用。有兴趣可阅读[规范原文](https://docs.google.com/document/d/1ijduF_tmHvBaUS7VBBU2ZN8_eEBiFaXXg9OI0_ZxCrA/edit)。
简单来讲，它包含几个方面

- 一套核心接口，用于编程式缓存
- 一套注解，用于声明式缓存
- 其它

### 核心接口

定义了如下五个核心接口，也就是说，如果要定义自己的缓存实现，实现这些接口即可。

| 接口            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| CachingProvider | 用于管理CacheManager                                         |
| CacheManager    | 用于管理Cache，具体来说，它的作用有<br />- 创建、配置具有特定名称的Cache，配置通过xxxConfiguration类实现<br />- 根据名称获取Cache<br />- 关闭Cache<br />- 销毁Cache及其中的内容<br />- 关闭自己及所管理的Cache<br />- 提供Cache的统计信息<br />- 获取CachingProvider中特定的属性 |
| Cache           | 类似Map的数据结构，用于存储键值对，存储的是Entry<br />用于获取、更新、移除这些键值对 |
| Entry           | 即一个单独的键值对，存储于Cache中                            |
| ExpiryPolicy    | 过期策略                                                     |

它们之间的关系，用一个图来表示的话（我在网上偷了一张图）。

![image-20210925225220620](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210925225220620.png)

### 注解

定义了几个核心注解，Spring兼容的，就是这几个注解

| 注解           | 说明                                                         |
| -------------- | ------------------------------------------------------------ |
| CacheDefaults  | 类级别注解。用于设置应用于整个类的属性<br />- 缓存名<br />- 缓存解析器<br />- key生成器 |
| CacheResult    | 方法级别注解。表明该方法的返回值将被缓存<br />- 缓存key由方法参数参与生成<br />- 下次调用将优先取缓存中的值 |
| CachePut       | 方法级别注解。表明该方法的某个参数将被写入缓存<br />- 目标参数必须用@CacheValue标注，否则会报错 |
| CacheRemove    | 方法级别注解。表明方法调用结果对应的缓存entry将被删除，通过key匹配 |
| CacheRemoveAll | 方法级别注解。表明将删除所有匹配的entry，通过value匹配，value满足条件就会被删除 |

### 其它

下面这些不是该标准的主要内容，但我认为有参考价值，特拿出来讲讲。

#### Cache和Map的不同

从API长相来看，Cache和Map大差不差，有很多相似之处，但这里只关注不同点。

- Cache的key和value都不能为null
- Cache的key和value需要支持序列化和反序列化
- Cache的entry可以过期
- Cache的entry可能因为某种策略被驱逐
- Cache支持CAS操作
- Cache可以按值存储，也可以按引用存储

>注意，这里的不同，仅限于JSR107的定义，在别处不一定是这样

#### 缓存值还是引用

这是一个问题。我们常用Redis，它缓存的肯定是值嘛，缓存值时就涉及到序列化问题；但还有一种选择是缓存引用，这在本机的堆缓存是比较有用的，我们不一定能够用到，但要知道还有缓存引用这种方式。

#### 一致性考量

同上，日常调用时可能不大会用，但要知道。

一致性，指的是并发操作缓存时，缓存所表现出的样子。JSR107定义了三种一致性结果。

- happen-before：即悲观锁，各个线程依顺序获取锁
- last value：无锁，各线程并发调用缓存，但是以最后一个操作成功的线程的结果为准
- CAS：乐观锁，即满足给定条件才执行

这三种一致性结果应用于不同的API，我们这里大致列一下。

![image-20210926090210075](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210926090210075.png)

#### 哪些没讲

JSR107涉及到方方面面，当然还有没讲到的，这部分可以直接去看官方手册，列一下。

- 缓存的类型安全保证：分为编译器类型安全和运行时类型安全。前者通过泛型保证，后者通过传入类对象在运行时校验保证
- 分布式缓存的实现方式：涉及到一系列缓存事件和事件监听器
- 缓存过期策略：按照缓存创建、访问等时间
  ![image-20210926091050637](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210926091050637.png)

### 哪些缓存实现了JSR107

说是Java标准，但并非所有库都支持，我们大致看一下。

| 库        | 支持与否                                  |
| --------- | ----------------------------------------- |
| Caffeine  | 支持                                      |
| Lettuce   | 不支持，但可以通过Spring Data变相部分支持 |
| Jedis     | 不支持，但可以通过Spring Data变相部分支持 |
| Hazalcast | 支持                                      |


>注：这里说的变相支持，是因为Spring Data底层使用了lettuce或jedis，而Spring Data Cache支持JSR107的注解，因此可以说是部分兼容了。

## Spring Cache

在介绍篇幅上，读者很容易被Spring手册骗了，因为它花了大量篇幅在注解及其功能的介绍上，即更多地关注声明式的使用方式，弱化了编程式的使用方式。其实后者也是可以使用的。

就缓存抽象本身，无论从定义的内容，还是关注的点，和JSR107是差不多的。

- 一套核心接口
- 一套注解
- 扩展功能和一致性考量等

### 注解

| Spring注解  | 说明                                                         | 对应JSR107注解             |
| ----------- | ------------------------------------------------------------ | -------------------------- |
| Cacheable   | 将调用结果作为缓存，且下次调用时直接取缓存                   | CacheResult                |
| CacheEvict  | 缓存驱逐，如果加上allEntries，则是驱逐value值匹配到的所有条目 | CacheRemove/CacheRemoveAll |
| CachePut    | 将方法的执行结果放入缓存                                     | CachePut                   |
| Caching     | 一个大的调用，Caching内部可以使用上面那三个注解              |                            |
| CacheConfig | 针对整个类的配置                                             | CacheDefaults              |

>注意，这些注解在语义上和JSR107可以说是一一对应，但在实际使用方式上其实是不同的，比如CachePut，Spring是将方法的执行结果放入缓存，而JSR107是将带有@CacheValue的参数放入缓存。

Spring Cache兼容JSR107的注解，即，直接使用JSR107的注解，在Spring环境中依然能够正常工作。

### 核心接口

Spring文档开头，指出了实现缓存抽象的关键接口

- org.springframework.cache.Cache：缓存，实际执行缓存操作的接口
- org.springframework.cache.CacheManager：缓存管理器，管理Cache实例

如果要为Spring的缓存抽象适配缓存实现，只需要实现这两个接口。比如Redis，有RedisCache和RedisCacheManager实现，使用时只需创建RedisCacheManager并注入容器，其它的就不用管了，RedisCacheManager会为我们创建并管理RedisCache。

具体使用方法，后文会有详细描述。

### 其它功能

- 自定义key：可通过注解的key属性+SPEL表达式，还有，keyGenerator属性这两种方式自定义key
- 同步缓存：通过sync属性指定。这一点对应JSR107的一致性考量
- 条件缓存：通过condition或unless属性+SPEL表达式指定缓存条件，即什么情况下使用缓存，什么情况下不使用缓存

## 对比

两相对比，Spring Cache简单不少，毕竟只有两个接口。日常使用较多的还是Spring Cache，JSR107仅作了解。

## Spring中使用Redis

现在来用用看。假设使用场景：一个简单的视频系统——两张表，如下：

![undefined](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210927185529108.png)

video表存储视频的描述信息，如标题、描述、封面地址等；video_play_info存储视频播放地址和来源，他们是一对多的关系。

考虑到这里重缓存的演示，一切从简，数据库使用HashMap模拟；路由层去除，直接在单元测试中调用。于是，总共就这么几个类：配置、数据定义、数据操作、逻辑操作、一些全局变量、Spring Boot启动类。



![undefined](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210927151957978.png)

数据定义

```kotlin
data class Video(
    private val videoId: String,
    private val title: String,
    private val description: String,
    private val coverUrl: String
)

data class VideoPlayInfo(
    val id: String,
    val videoId: String,
    val playUrl: String,
    val source: String
)
```

repo操作接口，稍后需要在它的实现类添加缓存支持。

```kotlin
interface VideoRelatedRepo {

    fun addVideo(video: Video): Boolean

    fun getVideo(id: String): Video

    fun updateVideo(video: Video): Video

    fun deleteVideo(id: String): Video

    fun addVideoPlayInfo(videoPlayInfo: VideoPlayInfo): Boolean

    fun listVideoPlayInfo(videoIds: List<String>): List<VideoPlayInfo>

    fun updateVideoPlayInfo(videoPlayInfo: VideoPlayInfo): VideoPlayInfo

    fun deleteVideoPlayInfo(id: String): VideoPlayInfo

}
```

下面，我们结合实际代码，解读使用方式。

### 使用前配置

如前所说，为Spring Cache提供实现，只需要实现CacheManager和Cache接口，而由于Cache实例实际由CacheManager创建和管理，因此在配置时只需提供CacheManager，对于Redis，引入Spring-Data-Redis后，在配置类中创建RedisCacheManger。

```kotlin
/**
 * 这里我们提供一个超级简单的配置
 */

const val REDIS_CACHE_NAME_VIDEO = "VIDEO"
const val REDIS_CACHE_NAME_PLAY_INFO = "PLAY_INFO"
const val REDIS_CACHE_PREFIX = "SPRING_DEMO_VIDEO"
const val REDIS_CACHE_EXPIRE_DAYS = 1L

@Configuration
@EnableCaching
class CacheConfig {

    @Bean
    fun cacheManager(connectionFactory: RedisConnectionFactory): RedisCacheManager {
        val objectMapper = jacksonObjectMapper().apply {
            this.activateDefaultTyping(
                LaissezFaireSubTypeValidator.instance,
                ObjectMapper.DefaultTyping.EVERYTHING,
                JsonTypeInfo.As.PROPERTY
            )
        }
        val valueSerializer = GenericJackson2JsonRedisSerializer(objectMapper)
        val shareConfiguration = RedisCacheConfiguration.defaultCacheConfig()
            .entryTtl(Duration.ofDays(REDIS_CACHE_EXPIRE_DAYS))
            .disableCachingNullValues()
            .serializeKeysWith(RedisSerializationContext.SerializationPair.fromSerializer(RedisSerializer.string()))
            .serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(valueSerializer))
            .computePrefixWith { cacheName -> "${REDIS_CACHE_PREFIX}${CacheKeyPrefix.SEPARATOR}${cacheName}${CacheKeyPrefix.SEPARATOR}" }
        return RedisCacheManager
            .builder(connectionFactory)
            .withCacheConfiguration(REDIS_CACHE_NAME_VIDEO, shareConfiguration)
            .withCacheConfiguration(REDIS_CACHE_NAME_PLAY_INFO, shareConfiguration)
            .build()
    }

}
```

做几点说明

1. 需要提供RedisConnectionFactory，即连接信息。如果在配置文件配过了，则直接注入即可；或者直接创建RedisConnectionFactory的bean也可。

```properties
spring.redis.host=120.78.147.168
spring.redis.port=16379
spring.redis.password=test123
spring.redis.database=0
spring.redis.timeout=2000
spring.redis.jedis.pool.max-active=8
spring.redis.jedis.pool.max-idle=8
spring.redis.jedis.pool.min-idle=2
```

1. 创建Manager时需要同时提供针对缓存的配置，可以针对特定名的Cache配置，也可以提供针对所有名字的Cache配置。上面，分别为名为video和videoPlayInfo的缓存实例，提供配置。配置类是RedisCacheConfiguration。
2. RedisCacheConfiguration配置能力如下

- TTL

- 是否缓存null值，这里是指value为null，且缓存null时也并非真的写入一个null进去，而是使用替代对象，如下

  ```kotlin
  private static final byte[] BINARY_NULL_VALUE = RedisSerializer.java().serialize(NullValue.INSTANCE);
  ```

- key的前缀，这个最最常用。因为我们往往是多个系统共用一个Redis DB，难免会有key冲突的情况，为每个系统设置自己的前缀，可以避免这个问题。
  有三种方式提供前缀

- 写死的字符串

- CachePrefix对象

- lambda表达式

  这里使用了lambda表达式，使得固定前缀为SPRING_DEMO_VIDEO::VIDEO::。其中"::"分隔符来自CachePrefix的常量。

- 针对key和value的序列化对，即序列化和反序列化器，这个比较常用，如果对序列化有特殊需求，就要配置它们

  我们要将对象序列化为json，因此有所自定义，序列化器这点，在下文的“问题”中有所描述。

- 类型转换器，用的是Spring Core的ConversionService

**关于缓存名**

问：cache name，即缓存的名字，会发现它无处不在：获取缓存实例时需要、配置缓存时需要、使用注解时也需要。该怎么理解它？

答：它，就是用来区分Cache实例的，一个CacheManager，可以管理多个Cache实例，使用name区分。

**关于Cache实例**

问：Cache这个接口，及其实例，存在的必要是什么？与缓存连接有什么关系？多个Cache实例之间是什么关系？Cache实例创建几个比较好？

答：这些问题，可以结合Cache接口和RedisCache实现来看。

看Cache接口，它只是提供了缓存的抽象，上面我们说过，Cache和Map很像，Cache接口就用于提供缓存的基本操作的；

再看RedisCache，其主要包含的四个属性。其中CacheWriter中包含了RedisConnectionFactory，是共享的；RedisCacheConfiguration、ConversionService是独享的。可以看出，RedisCache只是为不同场景持有不同的配置提供了方便，即，一个项目，多套配置，使用name区分。比如对用户的缓存需要ttl为1天，对session的缓存只要一小时，这就形成了两套配置需求。

```kotlin
private final String name;
private final RedisCacheWriter cacheWriter;
private final RedisCacheConfiguration cacheConfig;
private final ConversionService conversionService;
```

针对上面的问题：

- Cache存在的必要

  就是缓存的抽象而已。

- 与Redis的连接关系

  没有关系，不管多少个Cache实例，他们共用一个RedisConnectionFactory，连接池共享。

- 多个Cache实例之间的关系

  共享连接池；独享缓存配置。

- Cache实例创建几个

  依据情况而定，有几个缓存场景就可以创建多少个Cache实例，不会影响性能

### 声明式缓存 — 注解

大部分情况，都可以用注解解决问题，在获取单个对象时创建缓存，在更新时更新缓存，在删除时驱逐缓存。下面是对video对象操作的例子：

```kotlin
@Repository
class VideoRelatedRepoImpl(cacheManager: CacheManager) : VideoRelatedRepo {
 
  ... ...
  @Cacheable(cacheNames = [REDIS_CACHE_NAME_VIDEO], key = "#id")
  override fun getVideo(id: String): Video {
    logger.info("通过数据库获取值")
    return videoDB[id] as Video
  }

  @CachePut(cacheNames = [REDIS_CACHE_NAME_VIDEO], key = "#video.id")
  override fun updateVideo(video: Video): Video {
    videoDB[video.id] = video
    return videoDB[video.id] as Video
  }

  @CacheEvict(cacheNames = [REDIS_CACHE_NAME_VIDEO], key = "#id")
  override fun deleteVideo(id: String): Video {
    return videoDB.remove(id) as Video
  }
  
  ... ...
}
```

### 编程式缓存 — RedisCache

本例有一个特殊场景，根据videoId批量获取播放信息，由于播放信息可能随时变化，因此缓存单个播放信息比较科学，这就需要部分从缓存中取，部分从数据库中取。此时注解无能为力。需要直接使用RedisCache操作

```kotlin
@Repository
class VideoRelatedRepoImpl(cacheManager: CacheManager) : VideoRelatedRepo {
  
  // 获取Cache对象的方式
  private val videoPlayInfoCache = cacheManager.getCache(REDIS_CACHE_NAME_PLAY_INFO)!!
  
  ... ...
  override fun listVideoPlayInfo(videoIds: List<String>): List<VideoPlayInfo> {
    // 读取对应关系
    val playInfoIds = selectIdByVideoIds(videoIds)
    // 先从缓存获取
    val infosInCache = playInfoIds.mapNotNull { videoPlayInfoCache.get(it, VideoPlayInfo::class.java) }
    val infoIdsInDB = playInfoIds.filterNot { id -> infosInCache.any { it.id == id } }
    // 再从数据库获取
    val infosInDB = videoPlayInfoDB.multiGet(infoIdsInDB).map { it as VideoPlayInfo }
    // 再写入缓存
    infosInDB.forEach { videoPlayInfoCache.put(it.id, it) }
    logger.info("通过缓存获取了${infosInCache.size}; 通过数据库获取了${infosInDB.size}")
    return infosInCache + infosInDB
  }
  ... ...
}
```

### RedisTemplate怎么说

这算乱入了，RedisTemplate和缓存抽象半毛钱关系没有。它只是一个Redis客户端，关于它的使用方式，官方手册也有说明。这里就不说了。

倒是值得分清楚几个问题

**分清楚RedisTemplate和CacheManager**

我好奇过：为啥配置了CacheManager，还要配置一遍RedisTemplate？

因为它们根本就没关系呀，前者是Spring Cache抽象的一部分；后者是Redis客户端。谁也不包含谁，当然要分开配置。

**分清楚RedisCache和RedisTemplate**

他俩没关系，前者只是缓存抽象的实现，功能简单，顶多不过put数据、驱逐数据等缓存常规操作；后者是**全功能**Redis客户端。

**RedisTemplate强滴很**

翻翻看RedisTemplate源码，可以看到它包含了Redis的几乎所有操作，三个字：强滴很。

**啥时候用RedisTemplate**

它强是强，但用起来也复杂呀，并且能统一设置前缀、过期时间等。

```kotlin
 redisTemplate.opsForValue().set("key", "value", Duration.ofHours(1))
```

因此，在只有缓存需求时，使用Cache抽象最方便，有额外需求时，才考虑使用RedisTemplate。

### 可能会遇到的问题

上面展示的配置是最终版，但中间是有遇到问题的

- 序列化问题：DefaultSerializer requires a Serializable payload but received an object of type [xxx.VideoPlayInfo]

  首先，前面提到过我们可以指定key和value的序列化器和反序列化器，如果我们不指定，就会使用DefaultSerializer，而它是要求目标类实现Serializable接口的，然后，我们并没有实现该接口。

  解决方案1：为目标类实现Serializable接口，尝试过，这样是OK的。

  解决方案2：换一个序列化和反序列化器，我们使用RedisSerializer.json()得到一个json序列化器

```kotlin
// 配置片段
.serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(RedisSerializer.json()))
```

- 反序列化问题：Could not read JSON: Could not resolve subtype of [simple type, class java.lang.Object]: missing type id property '@class'

  对象序列化成JSON写入Redis了，读出来却无法转回目标对象。因为少了@class属性。所以这里还少了一点配置。

```kotlin
val objectMapper = jacksonObjectMapper().apply {
  // 管家配置
  this.activateDefaultTyping(
    LaissezFaireSubTypeValidator.instance,
    ObjectMapper.DefaultTyping.EVERYTHING,
    JsonTypeInfo.As.PROPERTY
  )
}
val valueSerializer = GenericJackson2JsonRedisSerializer(objectMapper)
// 配置片段
.serializeValuesWith(RedisSerializationContext.SerializationPair.fromSerializer(valueSerializer))
```

## 这里有个Demo

说是这么说，写是这么写，上面的内容，构建了一个可运行的项目，忘了的时候，可以来看看。

[<我就是那个项目>](https://gitee.com/zou8944/spring-me/tree/master/spring-cache)

>注意，我们没有使用数据库，因此在启动SpringBoot时要排除数据源

```kotlin
@SpringBootApplication(exclude = [DataSourceAutoConfiguration::class, HibernateJpaAutoConfiguration::class])
class SpringMeApplication
```

运行项目的单元测试，可以观察到缓存内容，如下图展示：一个视频信息、两个播放信息，注意观察key的组成和存储值的格式。
![undefined](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20210927203046805.png)

## 参考

1. [JSR107](https://docs.google.com/document/d/1ijduF_tmHvBaUS7VBBU2ZN8_eEBiFaXXg9OI0_ZxCrA/edit)
2. [Spring Cache Abstraction](https://docs.spring.io/spring-framework/docs/4.3.x/spring-framework-reference/html/cache.html)
3. [Spring Data Redis](https://docs.spring.io/spring-data/redis/docs/2.5.5/reference/html/#reference)