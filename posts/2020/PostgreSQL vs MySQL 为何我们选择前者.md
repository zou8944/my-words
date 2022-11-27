---
created_at: 2020-07-07 23:45:29.0
updated_at: 2021-02-16 23:45:53.959
slug: why-we-choose-mysql-instead-of-postgresql
tags: 
- PostgreSQL
- MySQL
---

## 与MySQL相比，有何优势

1. SQL标准的null判断用is null，而不是=null。PG可以设置transform_null_equals把=null翻译成is null

<!-- more -->

2. MySQL显示emojji时，需要将字符集设置为[utf8mb4](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode.html)。而PG就不用

   在MySQL中，对Unicode的支持，主要又如下几种字符集

   - utf8mb4
   - utf8mb3
   - utf8
   - ucs2
   - utf16
   - utf16le
   - utf32

   这里我们只关心前三个，其中utf8mb4表示使用1-4字节来描述一个Unicode字符；utf8mb3表示使用1-3字节来描述一个Unicode字符。而utf8是utf8mb3的别名。

   而Unicode字符分两种

   - 基本的BMP字符

     码点位于U+0000 到 U+FFFF之间；能够使用1-3个字节变长表示；也能使用2字节定长表示；它之间包含了世界上的绝大多数语言。

   - BMP字符之外的附加字符

     码点在U+10000 到 U+10FFFF之间；需要最多四个字节表示

   emojji字符也在unicode中，2010年Unicode开始为emojji分配码点。而它就在基础的BMP码点之外。因此utf8mb3是无法表示emojji字符的。

   那PostgreSQL是如何做的呢？

   依据[手册](https://www.postgresql.org/docs/10/multibyte.html)，PostgreSQL的text能够存各种类型的字符集，其中针对Unicode的UTF8，是1-4字节变长，因此PG天然就能存emojji字符。而PG服务端和客户端具体支持的其他字符集类型，还是参见手册。

## 与其他关系型数据库，有何优势

1. 自带NoSQL属性：可以存储array和json，甚至可以在array和json上建立索引，他的jsonb的性能已经比MongoDB的BSON性能要好了。
2. 自带全文搜索功能，不过中文的话就要额外安装中文分词插件。
3. 他有GIS，即地理信息扩展，可以非常方便地进行地理位置计算，可做地图服务器。这是PG的杀手级功能。
4. 能够高效地处理图结构。
5. 能够当作时序数据库

## 结尾

PostgreSQL功能强大，基本日常用到的需求它都有了，并且做的都不错。它是一个全栈数据库。

国内比较有名的使用PG的公司是探探。百万日活、上百TB数据量，数据组件还只用了PG。直到千万日活才引入独立的数据仓库。

**OLTP**：事务处理是PostgreSQL的本行

**OLAP**：citus分布式插件，ANSI SQL兼容，窗口函数，CTE，CUBE等高级分析功能，任意语言写UDF

**流处理**：PipelineDB扩展，Notify-Listen，物化视图，规则系统，灵活的存储过程与函数编写

**时序数据**：timescaledb时序数据库插件，分区表，BRIN索引

**空间数据**：PostGIS扩展（杀手锏），内建的几何类型支持，GiST索引。

**搜索索引**：全文搜索索引足以应对简单场景；丰富的索引类型，支持函数索引，条件索引

**NoSQL**：JSON，JSONB，XML，HStore原生支持，至NoSQL数据库的外部数据包装器

**数据仓库**：能平滑迁移至同属Pg生态的GreenPlum，DeepGreen，HAWK等，使用FDW进行ETL

**图数据**：递归查询

**缓存**：物化视图

## 参考资料

1. [MySQL手册](https://dev.mysql.com/doc/refman/8.0/en/charset-unicode.html)
2. [PostgreSQL手册](https://www.postgresql.org/docs/10/multibyte.html)
3. [PostgreSQL和探探见证4亿次心动](http://www.postgres.cn/downfiles/pg2016conf_day1_s1_pm4.pdf)
4. [https://developer.aliyun.com/article/60027](https://developer.aliyun.com/article/60027)

