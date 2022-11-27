---
created_at: 2021-09-28 16:36:39.81
updated_at: 2021-09-28 16:36:39.81
slug: spring-data-jpa-introduction
tags: 
- Spring
- JPA
---

震惊，查询SQL的创建居然是根据Repository的方法名来生成的。

对于JPA，我们只需要掌握几点。

<!-- more -->

### 使用步骤

- 配置开启JPA，提供EntityBeanFactory，提供repositories的配置包路径
- 定义Entity。不用自己写，使用IEAD的插件可以做到
- 定义Repository，提供灵活的定义方式
    - 定义查询方法，根据方法名来生成SQL的。这个叫做NamedQuery
    - 自定义查询SQL，使用Query注解
- 在需要使用的地方注入Repository

### 特色功能

- Repository的查询方法有点意思，相当于直接吧SQL写成了查询方法
- 支持Querydsl，一种Java语言的SQL DSL，怎么说呢，如果代码过长，写起来还是不大方便吧
- 支持将Repository中查询方法的返回类型指定为非Entity的类，比如我们DTO
- 支持存储过程
- 如果为IDEA添加了JPA支持，在写Repository时会有提示呢，看起来还挺高级的

    ![截屏20210928 下午4.34.31.png](https://gdz.oss-cn-shenzhen.aliyuncs.com/halo/%E6%88%AA%E5%B1%8F2021-09-28%20%E4%B8%8B%E5%8D%884.34.31_1632818107252.png)

### web支持

- 通过添加EnableSpringDataWebSupport注解，能够提供支持
    - 定义的Entity能够被web解析和编码到消息体中
    - 能够正常解析Sort、Pageable等参数
    - 能够解析Point、Distance等类，根据具体使用的Spring Data模块而言。如使用Spring Data Redis，可能就有Distance
    - 甚至能够直接把url中的查询参数转换为Querydsl的Predicte对象，即查询条件

## 优缺点总结

优点

1. IDEA支持好
2. 使用简单，只需要配置IDEA生成Entity，然后配置Repository即可
3. 对于创建规范的表格，简单的查询需求，用起来非常不错
4. 一般不让我们直接写裸SQL，而是类SQL，屏蔽了数据库差异。

缺点

1. 查询效率优化比较麻烦，JPA的设计思想，就是不要让你去管SQL的事情，而是专注业务
2. 但正是这样，有时候生成的SQL并不是我们想要的
3. SQL能力不如MyBatis强，比如动态SQL能力。举个例子，JPA中，要做in查询，in中的个数是动态，这样怎么办呢？

## JPA对比MyBatis

下面这个回答比较中肯。两句话概括

- JPA面向对象，让用户不要去管SQL的事情。使用友好，但SQL优化不大行。
- MyBatis面向SQL，可以直接写SQL。但跨数据源能力不大行。

[SpringData JPA也能写sql，为什么还要用mybatis?](https://www.zhihu.com/question/348496459/answer/842120407)

如果公司自己做业务，看重性能和优化，用MyBatis比较好，而且现在MyBatis有MybatisPlus，也支持Active Record，一定程度上算是集合了JPA和MyBatis的优势。

但如果公司的卖代码的，跨数据库这一点就很重要，使用JPA就很有必要。

## 个人认为

我个人的看法，首先，在代码中写复杂SQL这件事，必须PASS，这在呼啦亲子中已经实践过了，是不大可行的。JOOQ的DSL能力尚且不行，那Querydsl的SQL能力肯定是更加不能接受的。

其次，如果使用PG，其中有很多非典型SQL的语法，肯定是要写裸SQL的。但是JPA写裸SQL的能力，肯定是不如MyBatis的。

我也很喜欢JPA，但如果在一个长期维护的项目中使用JPA，很可能出现开始时写得很开心，到后面项目中充斥着大量不符合JPA设计哲学的代码。

所以我会选择MyBatis。

但是。。。如果是自己的小项目，我还是愿意尝试一下JPA。