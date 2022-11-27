---
created_at: 2021-11-24 23:59:46
updated_at: 2021-11-24 23:59:46
slug: acl-in-postgresql
tags:
- PostgreSQL
- 权限管理
---

本文介绍`PostgreSQL`中如何管理用户和权限，这些是正确管理`PostgreSQL`权限必备的前置知识。

<!-- more -->

## 角色 - [ROLE](https://www.postgresql.org/docs/13/user-manag.html)

PG中，围绕角色进行权限的管理。它可以被看做是一个user，或一组user。区分role、user、group。user和group是PG 8.1之前的两个实体，role是那之后唯一存在的实体，现在user和role，等价。

### 初始角色

数据库刚创建时，会自动创建一个超级用户的角色：postgres。任何操作都是从该用户开始的。

### 创建角色

```sql
CRAETE ROLE {角色名} [LOGIN] [SUPERUSER] [CREATEDB] [CREATEROLE] [REPLICATION] [INHERIT] [WITH ENCRYPTED PASSWORD '密码']
```

- `LOGIN`：允许登录
- `SUPERUSER`：拥有超级用户权限
- `CREATEDB`：允许创建database
- `CREATEROLE`：允许创建角色
- `REPLICATION`：允许备份
- `INHERIT`：是否继承权限，权限来是其它角色，通过`GRANT`将其它角色赋予该角色
- `PASSWORD`：指定密码

> 注意事项1：如下两句话等价
>
> ```sql
> CREATE ROLE {角色名} LOGIN
> CREATE USER {角色名}
> ```

> 注意事项2：不要使用超级用户，而是创建一个具有`CREATEDB`、`CREATEROLE`的角色进行日常管理，以避免误操作带来的危险。

> 注意事项3：创建database、创建角色算是特殊的权限，要与后文介绍的可授予的权限区分开来

### 建立角色关系

PG中并没有组的概念，各个角色之间都是平级的，但并不妨碍他们组成逻辑上的组，这通过`GRANT`语句达成。它能够将角色A赋予角色B，使得角色B成为角色A的成员，此后，赋予角色A的权限，角色B也将得到。

```sql
GRANT rolea TO roleb;
```

> 创建角色时有指定`INHERIT`参数，如果有，则角色B将会自动继承来自角色A的权限；如果没有，则只有将角色B手动切换到角色A时，才具有其权限
>
> ```sql
> -- 切换到角色A
> SET ROLE rolea;
> -- 充值角色到它自己，即回到角色B
> RESET ROLE；
> ```

### 默认角色

下面这些角色是预创建的，相当于一堆权限集合，可以将其赋予我们的角色，达到快速授权的目的。

| Role                      | Allowed Access                                               |
| ------------------------- | ------------------------------------------------------------ |
| pg_read_all_settings      | Read all configuration variables, even those normally visible only to superusers. |
| pg_read_all_stats         | Read all pg_stat_* views and use various statistics related extensions, even those normally visible only to superusers. |
| pg_stat_scan_tables       | Execute monitoring functions that may take `ACCESS SHARE` locks on tables, potentially for a long time. |
| pg_monitor                | Read/execute various monitoring views and functions. This role is a member of `pg_read_all_settings`, `pg_read_all_stats` and `pg_stat_scan_tables`. |
| pg_signal_backend         | Signal another backend to cancel a query or terminate its session. |
| pg_read_server_files      | Allow reading files from any location the database can access on the server with COPY and other file-access functions. |
| pg_write_server_files     | Allow writing to files in any location the database can access on the server with COPY and other file-access functions. |
| pg_execute_server_program | Allow executing programs on the database server as the user the database runs as with COPY and other functions which allow executing a server-side program. |

### 关于ROLE的命令

```sql
-- 创建ROLE
CREATE ROLE bosslist LOGIN INHERIT;
createuser bosslist;
-- 删除ROLE
DROP ROLE bosslist;
dropuser bosslist;
-- 查看现有的角色
SELECT * from pg_roles;
\du
```

对于查看角色，从`pg_roles`中查询和`\du`得到的结果一样，只不过呈现方式不同。

`\du`将角色的属性以字符串的形式展现

![image-20211124192250160](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211124192250160.png)

`pg_roles`查询结果如下，将每个属性都列出，可以使用SQL的形式查询、排序等。

![image-20211124192304590](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211124192304590.png)

## 权限 - [PRIVILEGES]()

角色有了，决定角色能够执行哪些数据库操作，则需要权限进行管理。PG将权限分为了两部分。这里所说的权限，主要指第二部分

- 能否登录、创建database、创建role，这类重要权限，在创建role时指定；在`pg_roles`表中可查看
- 对数据库对象的各类操作的权限，通过`GRANT`手动授予；在`information_schema.xxx_privileges`表中可查看，比如`information_schema.table_privileges`

### 权限的组成

一个完整的权限描述：角色A对表table1具有`SELECT`权限，有三部分组成

- 角色：A
- 授权目标：table1
- 权限：`SELECT`

### 权限列举

| 权限         | 授权目标                             | 说明                                                         |
| ------------ | ------------------------------------ | ------------------------------------------------------------ |
| `SELECT`     | 表和视图的所有列、指定的列；序列     | 读取                                                         |
| `INSERT`     | 表和视图的所有列、指定的列           | 插入，指定列时，插入语句只能出现指定的列                     |
| `UPDATE`     | 表和视图的所有列、指定的列；序列     | 更新，指定列时，更新语句只能出现指定的列<br />依赖SELECT权限定位 |
| `DELETE`     | 表和视图的所有列，即一整行           | 删除<br />依赖SELECT权限定位                                 |
| `TRUNCATE`   | 表                                   | 清空整张表                                                   |
| `REFERENCES` | 表的所有列、指定的列                 | 创建外键                                                     |
| `TRIGGER`    | 表、视图                             | 在表或视图上创建触发器                                       |
| `CREATE`     | database<br />schema<br />tablespace | database: 允许创建schema、publications、安装插件<br />schema: 创建新的对象；如果要修改已有对象，你必须是该对象的owner，并且拥有schema的CREATE权限<br />tablespace: 允许创建表、索引、临时文件；允许创建默认表空间为该表空间子的database |
| `CONNECT`    | database                             | 允许连接指定的database，这是pg_hba.conf之后，额外的检查      |
| `TEMPORARY`  | 临时表                               | 允许创建临时表                                               |
| `EXECUTE`    | 函数、存储过程                       | 允许执行函数或存储过程                                       |
| `USAGE`      | schema<br />序列<br />类型           | schema：允许使用该schema内的对象<br />序列：允许使用`currval`和`nextval`函数<br />类型：允许使用该类型 |

### 特殊的权限

- owner拥有特权

  当一个数据库对象被创建后，它会被自动分配一个owner，一般来说是执行创建语句的那个角色。大多数情况下，owner及其成员能够对该对象做任何事，如果其他人想要操作它，则需要`GRANT`授权。

  可修改owner，超级用户、对象原本的owner、owner的成员都能够调整对象的owner

  ```sql
  alter table table_name owner to new_owner;
  ```

- `PUBLIC`

  `PUBLIC`并不是一个真正的角色，确切地说，它应该算一个关键字，当授权的目标是它时，表示：授予系统中的所有角色，包括今后定义的角色。

  `PUBLIC`默认是拥有以下权限

  - 本地登录
  - 对public的`USAGE`权限
  - 对public的`CREATE`权限

  字面意思理解，相当于将该权限公开。

## 授权 - [GRANT](https://www.postgresql.org/docs/13/sql-grant.html)

```sql
-- 授予权限
GRANT {权限} ON {授权目标} TO {被授权角色} [WITH GRANT OPTION]
-- 授予角色
GRATE {角色} TO {被授权角色} [WITH ADMIN OPTION] [GRANTED BY 角色]
```

### 权限

| 权限         | 缩写           | 授权目标类型                                                 |
| ------------ | -------------- | ------------------------------------------------------------ |
| `SELECT`     | `r` (“read”)   | `LARGE OBJECT`, `SEQUENCE`, `TABLE` (and table-like objects), table column |
| `INSERT`     | `a` (“append”) | `TABLE`, table column                                        |
| `UPDATE`     | `w` (“write”)  | `LARGE OBJECT`, `SEQUENCE`, `TABLE`, table column            |
| `DELETE`     | `d`            | `TABLE`                                                      |
| `TRUNCATE`   | `D`            | `TABLE`                                                      |
| `REFERENCES` | `x`            | `TABLE`, table column                                        |
| `TRIGGER`    | `t`            | `TABLE`                                                      |
| `CREATE`     | `C`            | `DATABASE`, `SCHEMA`, `TABLESPACE`                           |
| `CONNECT`    | `c`            | `DATABASE`                                                   |
| `TEMPORARY`  | `T`            | `DATABASE`                                                   |
| `EXECUTE`    | `X`            | `FUNCTION`, `PROCEDURE`                                      |
| `USAGE`      | `U`            | `DOMAIN`, `FOREIGN DATA WRAPPER`, `FOREIGN SERVER`, `LANGUAGE`, `SCHEMA`, `SEQUENCE`, `TYPE` |

> 这里指定的缩写，在执行`\dp 表名`时会有用。

除上面指定的，还有如下权限体

- `ALL PRELEGES`：它是针对一个授权目标的所有权限的总和，不同目标有不同的权限，参见下面那张表。

### 授权目标

| 对象类型                         | All Privileges包含 | Default `PUBLIC` Privileges | psql Command |
| -------------------------------- | ------------------ | --------------------------- | ------------ |
| `DATABASE`                       | `CTc`              | `Tc`                        | `\l`         |
| `DOMAIN`                         | `U`                | `U`                         | `\dD+`       |
| `FUNCTION` or `PROCEDURE`        | `X`                | `X`                         | `\df+`       |
| `FOREIGN DATA WRAPPER`           | `U`                | none                        | `\dew+`      |
| `FOREIGN SERVER`                 | `U`                | none                        | `\des+`      |
| `LANGUAGE`                       | `U`                | `U`                         | `\dL+`       |
| `LARGE OBJECT`                   | `rw`               | none                        |              |
| `SCHEMA`                         | `UC`               | none                        | `\dn+`       |
| `SEQUENCE`                       | `rwU`              | none                        | `\dp`        |
| `TABLE` (and table-like objects) | `arwdDxt`          | none                        | `\dp`        |
| Table column                     | `arwx`             | none                        | `\dp`        |
| `TABLESPACE`                     | `C`                | none                        | `\db+`       |
| `TYPE`                           | `U`                | `U`                         | `\dT+`       |

### 被授权人

| 被授权人       | 说明                                           |
| -------------- | ---------------------------------------------- |
| `PUBLIC`       | 授予系统中的所有角色，包括今后定义的角色       |
| `role_name`    | 授予指定的角色，角色中的所有成员将会继承该权限 |
| `CURRENT_USER` | 当前用户                                       |

### WITH GRANT OPTION

表示被授权人能够将该权限授予其他人，不能对PUBLIC使用该选项。

### 授予角色而不是权限

第二条语句是将一个角色授予另一个角色，作用是将一个角色的成员授予其它角色。前文“建立角色关系”已描述过了。

`WITH ADMIN OPTION`：授权传递，被授权的角色，可以传递授权

### 关于授权的命令

```sql
-- 授予database的所有操作给一个角色
GRANT ALL PRIVILEGES ON DATABASE bosslist TO bosslist;
-- 授权当前database的指定schema的所有表的只读权限给一个角色
GRANT SELECT ON ALL TABLES IN SCHEMA public TO bosslist;
-- 将mytable.col1的SELECT、UPDATE赋予miriam_rw
GRANT SELECT (col1), UPDATE (col1) ON mytable TO miriam_rw;
-- 查看一个表的权限详情
\dp <表名>
```

比如，如下查询结果表示：resource表，mylog用户拥有所有权限；mylogs_r拥有SELECT权限，都是mylog用户授予的。

![image-20211124193136549](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211124193136549.png)

如果这里看到的`Access privileges`为空，则该表适用于如下权限

- 其owner对该表有完整的权限
- 如果针对`PUBLIC`角色有设置关于该表的权限，则会予以应用

## 默认权限 - [DEFAULT PRIVILEGES](https://www.postgresql.org/docs/13/sql-alterdefaultprivileges.html)

当一个数据库对象刚被创建时，满足条件的默认权限会自动应用。

通过`\ddp`可以查看适用当前schema的默认权限（默认啥都没有）。

```sql
ALTER DEFAULT PRIVILEGES [FOR {目标角色}] [IN SCHEMA {schemaname}] {GRANT或REVOKE语句}
```

举几个例子

```sql
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT SELECT ON TABLES TO PUBLIC;
ALTER DEFAULT PRIVILEGES IN SCHEMA myschema GRANT INSERT ON TABLES TO webuser;
```

`\ddp`的例子

![image-20211124193049403](https://gdz.oss-cn-shenzhen.aliyuncs.com/local/image-20211124193049403.png)

## 撤权 - [REVOKE](https://www.postgresql.org/docs/13/sql-revoke.html)

```sql
-- 取消权限
REVOKE [GRANT OPTION FOR] {权限} ON {授权目标} FROM {被授权人} [CASCADE | RESTRICT]
-- 取消角色
REVOKE [ADMIN OPTION FOR] {角色} FROM {被授权角色} [CASCADE | RESTRICT]
```

各部分和GRANT一样，区别在于

- `GRANT OPTION FOR`：取消权限的授予权限，而不是权限本身；没有这一项就同时取消权限和授权权限
- `CASCADE`：递归取消，适用于带有授权选项的用户将权限授予了其它用户，带上它则会将这些权限递归取消
- `RESTRICT`：区别于`CASCADE`，不会递归取消，**这是默认选项**

## 总结

`PostgreSQL`中，权限有两种，一种是创建角色时指定的那几个大类；一种就是所谓的`PRIVILEGES`，搞清楚这一点，一切都好办很多。

### 自问自答

- 谁能发起`GRANT `?

  `GRANT`本身并不是一种权限，任何角色都能`GRANT`，但要分为两种情况

  - 角色的某个权限是别的角色授权过来的，如果对方授权时未指定`WITH GRANT OPTION`，则它无权将该权限授权给其它角色
  - 角色是某个对象的owner，则该角色能将该对象的权限授予其它角色

  只要我们堵死这两条路，一个角色就无法授权给别人。前面那条路好说，后面这条路，就要求角色不能拥有创建对象的能力，我们可以通过`ALTER USER SET default_transaction_read_only=on`达成。

- 新创建的角色拥有什么样的权限 ?

  依据角色创建语句决定它是否拥有创建角色或database的权限；`PRIVILEGES`则包含所有授予`PUBLIC`的角色。

- 如何查看`PUBLIC`拥有哪些权限？

  目前没找到查看的方式

- 如何查看某个角色是否对schema具有`CREATE`权限？其它类推？

  待查

## 彩蛋 - 客户端鉴权

角色创建后好，并不能直接通过网络连接到PG服务端，`pg_hba.conf`文件要配置一下。一个典型的配置如下

```shell
# Allow any user on the local system to connect to any database with
# any database user name using Unix-domain sockets (the default for local
# connections).
#
# TYPE  DATABASE        USER            ADDRESS                 METHOD
local   all             all                                     trust

# The same using local loopback TCP/IP connections.
#
# TYPE  DATABASE        USER            ADDRESS                 METHOD
host    all             all             127.0.0.1/32            trust
```

组成部分

- `TYPE`

  - local：本地连接
  - host：使用TCP/IP连接

- `DATABASE`

  允许连接的database

- `USER`

  允许连接的角色

- `ADDRESS`

  允许的客户端地址，`0.0.0.0/0`表示允许所以客户端连接

- `METHOD`

  鉴权方式

  - `trust`：无条件允许连接
  - `reject`：无条件拒绝
  - `password`：要求客户端提供未加密的密码进行身份验证，密码在网络上以明文形式传输，如果使用SSL，可以加密传输
  - `scram-sha-256`：执行 SCRAM-SHA-256 身份验证，这是一种质询响应机制，这是目前最安全的方式，不过有的数据库客户端可能不支持。
  - `md5`：也是一种质询响应机制
  - `peer`：获取客户端操作系统的用户名，如果和请求连接的用户名一样。这只有在本地连接时才有用。
  - `xxx`：都是其它的鉴权方式，参考[官方文档](https://www.postgresql.org/docs/13/auth-pg-hba-conf.html)

## 最佳实践1 - 创建只读用户

```sql
-- 创建用户doki
CREATE USER doki PASSWORD 'password';
-- 更新用户的默认事务为只读的（这意味着它只能执行读操作，不能CUD）
ALTER USER doki set default_transaction_read_only=on;
-- 授权连接
GRANT CONNECT ON DATABASE doki_database TO doki;
-- 授权public的使用
GRANT USAGE ON SCHEMA PUBLIC TO doki;
-- 切换到doki_database
\c doki_database
-- 授予doki_database下public下所有表、序列、函数
GRANT SELECT ON ALL TABLES IN SCHEMA public TO doki;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO doki;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO doki;
-- 对于新建的对象，也授予上面三个权限
ALTER DEFAULT PRIVILEGES FOR ddl_user IN SCHEMA public GRANT SELECT ON TABLES TO doki;
ALTER DEFAULT PRIVILEGES FOR ddl_user IN SCHEMA public GRANT SELECT ON SEQUENCES TO doki;
ALTER DEFAULT PRIVILEGES FOR ddl_user IN SCHEMA public GRANT EXECUTE ON FUNCTIONS TO doki;
```

修改`pg_hba.conf`，添加如下一行（注意这是危险的，因为0.0.0.0/0），如果已经有符合要求的行，也可以不添加。

```shell
host all all 0.0.0.0/0 md5
```

使用psql从远端测试访问

```shell
psql -h <数据库地址> -p <数据库端口，默认5432> -U doki -d doki_database
```

## 最佳实践2 - 重新为用户授权

```sql
-- 切换到doki_database下
\c doki_database
-- 收回用户在public下所有表的所有权限
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM doki
-- 为doki赋予doki_database下的所有权限
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO doki;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO doki;
```

注意，如果我们要收回某个database下所有权限，是无法通过如下语句达成的，参考“授权目标”那张表，对于`DATABASE`,`ALL PRIVILEGES`代表`CTc`，即`CREATE TEMPORY CONNECT`，即创建`schema`、安装插件、创建临时文件、连接，收回的也只是这几个权限而已，要收回全部权限，还是得一个一个目标地做。

```sql
REVOKE ALL PRIVILEGES ON DATABASE doki_database FROM doki;
```

## 好文推荐

- [Managing rights in postgresql](https://wiki.postgresql.org/images/d/d1/Managing_rights_in_postgresql.pdf)
