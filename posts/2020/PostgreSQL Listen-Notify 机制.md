---
created_at: 2020-06-06 10:29:54.0
updated_at: 2021-02-16 23:21:09.189
slug: postgresql-listen-notify-mechanism
tags: 
- PostgreSQL
- 队列
---

Postgresql提供 监听 - 通知 的订阅服务，使得数据库客户端向服务端的指定通道注册为监听客户端，服务端在发出Notify通知时，所有已注册的监听客户端将能够收到该通知。

<!-- more -->

# 使用示例

**服务端**

```sql
-- 不带消息的通知
users=> NOTIFY test_channel;
NOTIFY

-- 带消息的通知
users=> NOTIFY test_channel, 'I am payload';
NOTIFY
```

**客户端**

```sql
-- 不带消息的通知
users=> LISTEN test_channel;
LISTEN
Asynchronous notification "test_channel" received from server process with PID 9501.

-- 带消息的通知
users=> LISTEN test_channel;
LISTEN
Asynchronous notification "test_channel" with payload "I am payload" received from server process with PID 9501.
```

**注意**

- 上面的例子看起来并不像发布-订阅，因为客户端LISTEN后并不会被主动通知，而是每次要服务端NOTIFY后，客户端再去LISTEN，这其实是误会——Postgresql客户端检测通知事件的方式取决于该客户端底层应用的编程接口。支持同步轮询异步通知两种方式。很多第三方库是支持异步通知的。
- 通道名可以使任意有效字符串，通道不需要预先创建。

# 命令介绍

## LISTEN

```sql
LISTEN channel （channel值任意）
```

- 命令干了啥

  将当前会话注册为一个channel的监听者，如果当前会话已经注册，则啥都不干

- 何时被通知

  无论何时当命令 NOTIFY channel 被调用时，注册在该channel上的所有监听者都会被通知。

- 合适终止监听

  当调用UNLISTEN或会话关闭时，监听终止

- 监听原理

  客户端检测通知事件使用的方法取决于它使用的 PostgreSQL 应用程序编程接口。

  - 如果使用libpq库，只是相当于定期执行SQL命令调用PQnotifies方法查询是否有新的通知
  - 其它接口如libpgtcl提供更高级的方法来处理通知

- 事务相关性

  LISTEN命令在事务提交时生效，如果执行LISTEN的事务最终回滚了，则LISTEN不会生效。

## NOTIFY

```sql
NOTIFY channel [, payload] （payload默认要求小于8000字节, 且必须是常量）
```

- 命令干了啥

  NOTIFY向每一个在channel上注册的客户端发送通知，通知可附带可选的字符串载荷payload。通知对所有用户都是可见的。

- 通知信息包括

  - 通知的channel名
  - 发出通知的服务端的进程PID
  - 可选的payload字符串，没有时则为空字符串

- channel命名规则

  channel没有具体的命名规则。一般来说，channel会和某个表名一致，这样对该channel发出通知在语义上表示“我修改了这个表，看看有什么新内容吧”（配套的是将这样的NOTIFY语句放入表更新的触发器中）。不过还是要具体情况具体分析

- 事务相关性

  如果NOTIFY用于事务中，则只有当事务提交时才会真正执行通知，如果事务取消则压根不会通知。

  如果一个待接收通知的监听会话正处于事务中，则通知事件会等到它的事务处结束后在发送到它。这是合理的，因为通知发送了就不能取消，如果在事务中发送或接收，遇到想要取消通知的情况就没办法了。

  这样的缺点导致了实时性不好，因此如果要求实时性高，就要把事务写短一点。

- 通知折叠规则

  - 一个事务中对同一个channel发送多个paylaod一样的通知，可能会被折叠成一个通知
  - 一个事务中对同一个channel发送不同的payload通知，不会执行折叠操作
  - 不同事务，无论channel和payload是否重复，都不会执行折叠操作

- 顺序

  NOTIFY保证顺序

  - 同一事务中，通知发出的顺序按NOTIFY声明的顺序进行
  - 不同事务，通知发出的顺序按事务提交的顺序走

- 避免额外的工作

  在一个客户端上发送NOTIFY命令，同时该客户端监听同样的channel，会出现通知发给自己的情况，此时可以通过通知中带的进程PID发现发送者就是自己，从而忽略本来要执行的逻辑，节省性能。

- 队列

  有一个队列用于存储已经NOTIFY但还没被所有注册的客户端获取的通知，如果队列满了，则NOTIFY在提交时会失败。

  该队列默认大小为8GB，足够大多数情况。

  如果一个监听会话长时间处于事务中，则对应通知会持续累积，当队列满了一半时，会打出警告日志。

  pg_notification_queue_usage函数可以查看用了多少。

- pg_notify(channel, payload)

  该方法执行同样的事情，好处是payload不再要求必须是常量，可以通过变量运算得到。

## UNLISTEN

```sql
UNLISTEN { channel | *)}
```

用于将当前会话移除出channel的监听列表，*表示移除当前会话监听的所有channel。

在会话期间，使用UNLISTEN channel的方式移除监听

在会话结束时，会自动执行UNLISTEN *

# 参考资料

- [Postgresql-10官方手册 - LISTEN](https://www.postgresql.org/docs/10/sql-listen.html)
- [Postgresql-10官方手册 - NOTIFY](https://www.postgresql.org/docs/10/sql-notify.html)
- [Postgresql-10官方手册 - UNLISTEN](https://www.postgresql.org/docs/10/sql-unlisten.html)

- [Postgresql-10官方手册 - Asynchronous Notification](https://www.postgresql.org/docs/10/libpq-notify.html)