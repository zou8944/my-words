---
created_at: 2020-04-11 19:43:57.0
updated_at: 2021-02-16 23:21:53.963
slug: java-time
---



Java8中引入了新的库java.time，提供更为好用的日志API，从此不再在Date、Calendar这些类中纠结。本文基于[java.time API文档](https://docs.oracle.com/javase/8/docs/api/java/time/package-summary.html)进行记录和总结。

<!-- more -->

# 包简介

该包下的类定义了基础的日期-时间概念，包括instant、duration、date、time、time-zone、period等，他们都是基于ISO日历系统。

所有的类都是不可变的，意味着它们是线程安全的

各个子包的作用

- java.time.temporal 取得底层字段
- java.time.format 解析字符串或格式化
- java.time.chrono 中立的日历API

# API介绍

## 核心API

### Instant

本质上是一个数字时间戳，即在时间线上的某一点，某一时刻。使用可以从Clock中取得。打印日志或持久化时标记时间很有用。曾和System.currentMillis()关联

Instant是与java.util.Date. ZonedDateTime同等的类

Instant的组成，包含一个long用于存储epoch秒数，即1970-01-01T00:00:00Z到现在的秒数；还有一个int用于存储纳秒。

### Clock

Clock提供访问当前Instant，带时区的日期和时间

他可以替代System.currentMillis()和TimeZone.getDefault()，用于获取当前的毫秒数和默认时区

时钟不是必须的，因为上面的LocalDate等类都有一个now()方法。Clock存在的意义在于允许我们将时间当做对象进行传递，因为一个Clock对象包含了比较全面的信息。

### LocalDate

仅有日期，可用于存储生日之类的数据

它不存储时间或时区，它仅仅是对日期的描述，不能代表时间线上的一个瞬间

在日期上的操作支持很好，可以访问年、月、日、年中日等

### LocalTime

仅有时间，没有日期，即所谓的wall time

### LocalDateTime

存储日期和时间，精确度为纳秒

它不存储时区，因此不能代表时间线上的一个瞬间

### ZonedDateTime

带时区的日期和时间，在将ZoneId带入计算时非常有用。尽可能不要使用它，带有时区将使得应用变得复杂。

ZonedDateTime是和java.util.GregorianCalendar同等的类

### Duration

两个时间的差，纳秒计

### Period

表示对人类有意义的一段时间，比如一年、一天

## API命名约定

java.time提供了丰富但统一的API，不同前缀代表不同意思

- of - 静态工厂方法
- parse - 用于解析的静态方法
- get - 获取
- is - 检查是否为true
- with - setter的不可变等价方法
- plus - 向一个对象增加
- minus - 减少
- to - 将一个对象转换为另一个类型
- at - 将一个对象和另一个对象结合，例如将LocalDate和LocalTime结合成LocalDateTime

# 闰秒的处理

太阳日的长度是人类测量时间的标准方法，通常一个太阳日被分为24小时60分钟60秒，形成86400秒。

现代计时是以原子钟为基础，它精确地定义了一个名为SI second的东西代表1秒（这是铯原子跃迁的时间），SI second非常接近86400分之一天。

SI second和太阳时的关系，在于前者是观测地球自转得来，是绝对意义上的准确时间；后者是计时得来的，和地球自转无关。在计算机系统中使用的时间就是计时得来。

然而，地球自转并不绝对稳定，使得一天的长度会发生变化；随着时间的推移，地球自转变慢，一天的平均时间边长，导致SI second和太阳时出现偏差。

UTC time-scale是将额外变化的时间捆绑成整秒的标准做法。现在的UTC时间于1972年提出，引入闰秒的概念，然而闰秒的定义是复杂的。鉴于此，java.time中的API定义了自己的time-scale

Java time-scale将每个日历日精确地划分为86400个细分，即秒。 这些秒数可能与 SI second不同。

Java time-scale对不同时间段的定义略有不同，每个时间段都基于作为公民时间基础的协商一致的国际时间表。 每当修改或替换国际商定的时间表时，必须为其定义新的 Java time-scale。

截止2013年，Java time-scale分为两部分

- 1972-11-03至今，java time-scale和UTC一致，与UTC没有闰秒的时间相同，对于闰秒的天，闰秒被平均分配在一天的最后1000秒中，以保证每天看起来还是86400秒。即意味着这天的最后1000秒，java的每一秒都比普通的时间快或慢1ms
- 1972-11-03之前，UTC时间尚未提出，世界协商时间为UT1，相当于格林威治上的太阳时，由于没有闰秒的说法，java的time-sclae和世界协商时间一致。

# 时区ID

时区ID在整个系统中是唯一的，总共有三种时区ID

- 最简单的时区ID，以+或-开头。

- 带有前缀的和偏移量后缀的时区ID。如GMT+2、UTC+01:00，合法的前缀有GMT、UTC、UT。由于它有固定偏移量，因此可以调用ZoneId.normalized()标准化成一个ZoneOffset

- 基于地理区域的ID。必须由两个以上字符组成，且不能是UTC、GMT、UT、+、- 。基于地理区域的ID的转换规则是被定义在配置中的，由ZoneRulesProvider实现。

  翻看ZoneRulesProvider的手册，发现对时区的配置可以自定义，按照指定的规则来即可。默认情况下，它使用了位于java home的lib文件夹下tzdb.dat文件中定义的数据加载规则。我们可以覆盖这个操作，通过设置系统变量java.time.zone.DefaultZoneRulesProvider

时区由政府部门指定，且修改频繁。有好几个组织做这件事。Java默认使用IANA Time Zone Database (TZDB)的规则，其它组织包括IATA和微软。每个组织的区域ID都不一样，我们遵循默认的TZDB就好。

## 时区相关类

- OffsetTime

  存储相对于UTC时间的时间和偏移量，如'11:30+01:00'

- OffsetDateTime

  存储相对于UTC时间的日期时间和偏移量，如'2010-12-03T11:30+01:00'，精度也是纳秒

  Offsetdatetime、 ZonedDateTime 和 Instant都能存储时间线上的一个瞬间，因为他们有时区或偏移量

- 如上两个Offset类最初是被设计用来支持网络协议和数据库操作的。因为很多数据库不支持'Europe/Paris这样的时区，但支持+02:00这样的偏移量

- ZoneId

  时区ID，是用来确定Instant和LocalDateTime之间的转换规则的，有两种ZoneID

  1. 固定偏移量，相对于UTC时间，如东八区。对应子类ZoneOffset
  2. 地理区域，如Europe/Paris，用于对应UTC时间某个偏移量的地区，对应子类ZoneRegion

  实际规则由ZoneRules类描述。

  ZoneRules定义了每个时区的时区偏移规则。这些规则对时区的历史和未来转换建模，Zoneoffsettransition用于过去时间的转换；Zoneoffsettransitionrule基于算法对未来实现转换。

# 参考文档

1. [java.time Java doc](https://docs.oracle.com/javase/8/docs/api/java/time/package-summary.html)
2. [关于闰秒 - 陈皓](https://coolshell.cn/articles/7804.html)