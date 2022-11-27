---
created_at: 2020-03-07 16:16:23.0
updated_at: 2021-02-16 23:22:51.109
slug: python-logging-introduction
tags: 
- Python
- 日志
---

我的Python是从使用开始的，因此很多Python基础理论并不是很足，之前在使用Celery时，因为日志无法正常打印而排查了一天。所以，为了节省时间，同时知其所以然，是时候系统梳理一下Python中日志的使用方法了。

<!-- more -->

# 基础

Python日志位于logging包，其中仅包含两个module。在不进行任何额外配置的情况下，可以按照如下方式使用

```python
import logging

logging.warn("Hello World!!!")
```

输出

```shell
WARNING:root:hello
```

接着来详细了解其使用方式。

## 日志级别

在很多Java日志框架中，将日志由严重要普通，依次为  Fatal -> Error -> Warning -> Info -> Debug。在Python中，也一行，只不过Fatal不叫Fatal，叫Critical，所以是 Fatal -> Error -> Warning -> Info -> Debug。使用场景也是一样，如下

| `DEBUG`    | 细节信息，仅当诊断问题时适用。                               |
| :--------- | :----------------------------------------------------------- |
| `INFO`     | 确认程序按预期运行                                           |
| `WARNING`  | 表明有已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行 |
| `ERROR`    | 由于严重的问题，程序的某些功能已经不能正常执行               |
| `CRITICAL` | 严重的错误，表明程序已不能继续执行                           |

Python默认的日志级别是Warning，默认输出到控制台。这意味着，**默认情况下，Info和Debug日志是不会输出的**。

> 小贴士：日志的输出级别，确切地说应该是日志的输出阈值，即指定级别及以下级别的日志会输出，其上的不会输出。比如设置日志级别为Warning，则除Info、Debug外其它日志都会输出。

## 简单配置

### 命令行

可以在使用命令启动python时指定logging的执行级别

```shell
# 执行脚本hello.py，日志级别设置为INFO
python hello.py --log=INFO
```

### basicConfig方法

一般来说，logging的配置都可以在logging.basicConfig()方法完成，如下展示了常用的配置

```python
# 设置日志输出到文件，日志级别设为debug，默认为追加模式
logging.basicConfig(filename='celery.log', level=logging.DEBUG)
# 输出到文件，覆盖模式
logging.basicConfig(filename='celery.log', filemode='w', level=logging.DEBUG)
```

> 小贴士：`logging.basicConfig`方法被设置为只能调用一次，因此针对他的第一次调用是有效的，但以后的调用不会生效。这也是很多问题的发源地：你可能不自觉地多次调用了`basicConfig()`

### 日志格式

还是在`basicConfig()`中，我们可以配置日志输出格式，通过format参数进行设置

```python
# 输出格式为asc时间+空格+消息内容
logging.basicConfig(format='%(asctime)s %(message)s')
```

日志格式中可以详细设置的内容可以在[这里](https://docs.python.org/zh-cn/3.8/library/logging.html#logrecord-attributes)找到，我们列出几个看似很有用的

| 属性名    | 使用格式        | 作用                       |
| --------- | --------------- | -------------------------- |
| asctime   | `%(asctime)s`   | 日志输出时间，对阅读友好的 |
| filename  | `%(filename)s`  | 输出日志的文件             |
| funcName  | `%(funcName)s`  | 输出日志的方法             |
| levelname | `%(levelname)s` | 级别名称，如DEBUG、LEVEL   |
| lineno    | `%(lineno)d`    | 输出日志的源码行号         |
| message   | `%(message)s`   | 输出的消息                 |
| process   | `%(process)d`   | 进程ID                     |
| thread    | `%(thread)d`    | 线程ID                     |

# 原理

上面所介绍的内容仅解决了记录的问题，并不能满足许多实际项目的需求。比如希望针对不同的日志级别将日志输出到不同的位置、当出现ERROR日志时通过邮件报警、自动记录ERROR log的个数等。要做到这些需求，我们需要更加深入Python日志系统，了解其基本工作原理。

> 这里有一点忌讳的是，在不了解Python日志基本构成的情况下，直接使用网上搜索的方式进行复杂的日志配置。这样成功的概率不高，且出问题时往往面临束手无策的尴尬境地。

Python日志库采用模块化方法，通过几类组件协同工作，完成日志从发起到输出终点的全流程。如下

- Logger - 记录器：用户暴露接口给用户直接调用。它产生LogRecord对象传递给下一个组件。
- Handler - 处理器：处理Logger产生的LogRecord
- Filter - 过滤器：更加精确地控制日志的输出
- Formatter - 格式化器：用户将日志处理成最终输出的样子

其中，Logger是层次结构的，有父子关系。几个组件的协同处理流程如下图所示

![image-20200307190901858](https://www.tapd.cn/tfl/pictures/202003/tapd_61207716_1583592896_17.png)

## Logger

Logger类，即记录器，用于暴露接口给用户调用，其简单创建和使用方法如下

```python
import logging

logger = logging.getLogger(__name__)
logger.warning('Hello, World!!!')
```

创建Logger使用`logging.getLogger('name')`方法，当Logger实例已存在，则直接返回，不存在则创建。

Logger具有层次结构，主要通过名称体现，以.分隔。如名为root的Logger实例是名为root.hello、root.world的Logger实例的父级。

层级结构的好处在于减少配置的冗余，以及消息的冒泡传递：在子Logger没有声明级别的情况下，使用父Logger的级别，以此类推，如果都没有设置级别，则会使用root的Warning级别；日志输出时，除了执行当前Logger的所有逻辑外，还可以传递给父Logger，如上图所示。

接口方面，Logger主要提供配置和消息创建两类接口

- 配置
  - Logger.setLevel() 设置当前Logger的日志级别
  - Logger.addHandler()/removeHandler() 添加/删除处理器
  - Logger.addFilter()/removeFilter 添加/删除过滤器

- 创建消息
  - Logger.debug()/info()/warning()/error()/critical() 创建不同级别的日志
  - Logger.exception() 输出ERROR级别的日志，不同的是还附带堆栈信息
  - Logger.log() 显式自定义日志输出级别并创建日志信息

## Handler

Handler类，即处理器。决定如何处理Logger发送的消息对象，即将消息对象发送到哪个目标

Handler暴露给用户的接口如下

- Handler.setLevel() 设置当前Handler的日志级别。这意味着，Logger能够处理的日志级别和Handler的日志级别可以不同，即Handler可以选择性处理日志消息
- Handler.setFormatter() 指定格式化器
- Handler.addFilter()/revmoFilter() 添加/删除过滤器

Python内建了很多处理器，如下。通过这些Handler，可将日志输出到文件、内存、邮件、网络

![image-20200307193416476](https://www.tapd.cn/tfl/pictures/202003/tapd_61207716_1583592919_91.png)

## Filter

Filter类，即过滤器。Python只定义了一个Filter基类，该类构造器接收一个name参数，其过滤逻辑为：仅允许与Logger同级或子级的LogRecord通过，其余被滤出。如Filter名为A.B，则名称为A.B、A.B.C、A.B.D的Logger创建的LogRecord均可通过，A.F的Logger创建的LogRecord将被滤出。

```python
filter = logging.Filter('hello')
```

要实现自定义的Filter，集成`logging.Filter`类，并重写其`filter()`方法即可

## Formatter

Formatter类，即格式化器。决定了日志输出格式，用户只需要创建它并扔给Handler就好。

```python
formatter = logging.Formatter(fmt='%(filename)s %(funcName)s %(message)s', datefmt=None, style='%')
```

参数解释如下

- fmt - 格式设置，和基础部分一样。能够输出[LogRecord对象的所有属性](https://docs.python.org/zh-cn/3.8/library/logging.html#logrecord-attributes)。如果临时忘了，在Formatter类定义注释中，有详细的说明。

- datefmt - 指定日期的格式化，举例

  ```python
  '%m/%d/%Y %I:%M:%S %p'
  ```

- style - 格式化风格，%和\$二选一，两个风格区别如下。

  ```python
  # %风格
  "%s %s" % ('hello', 'world')
  # $风格
  "{} {}".format('hello', 'world')
  ```

## LogRecord

LogRecord类，用户每调用一次Logger的输出接口，就会创建一个LogRecord类实例，该实例作为在日志系统各组件的最小单位。基于其重要性，这里单独提了出来。

# 配置

Python提供了三种配置日志的方式

- 使用各组件提供的配置方法手动配置
- 按照指定格式创建配置文件，然后使用`logging.config.fileConfig()`读取
- 按照指定格式创建配置字典，然后使用`logging.config.dictConfig()`读取

下面直接搬运官方文档给出的三种方式

## 代码配置

```python
import logging

# create logger
logger = logging.getLogger('simpleExample')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
```

## 文件配置

```
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
```

文件配置内容格式具有自解释作用，这里不做讲解。

唯一需要注意的是，在指定处理器的class时，类名称是相对于Python的日志记录模块（注意是Python的日志模块，即logging的位置），或按照导入机制能够正常导入的绝对import路径。

如StreamHandler，因它在logging模块中定义，因此可以直接写StreamHandler即可。

再如com.github.zou.HelloHandler，属于自定义，因此需要全路径。

```python
import logging
import logging.config

# 上面的文件名为logging.conf
logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')
```

## dict配置

```yaml
version: 1
formatters:
  simple:
    format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    level: DEBUG
    formatter: simple
    stream: ext://sys.stdout
loggers:
  simpleExample:
    level: DEBUG
    handlers: [console]
    propagate: no
root:
  level: DEBUG
  handlers: [console]
```

```python
import logging
import logging.config
import yaml

# 将yaml文件读取为dict，再进行配置
config = yaml.load(open('logging.yml'), Loader=yaml.FullLoader)
logging.config.dictConfig('logging.yml')

# create logger
logger = logging.getLogger('simpleExample')
```

## 有坑

### 配置覆盖问题

使用`fileConfig()`时，**带有默认参数`disable_existing_logger=True`，因此之前的除root之外的所有Logger全都会被禁用**，这一点要非常注意。如果不希望如此，可手动将其设置为False

```python

def fileConfig(fname, defaults=None, disable_existing_loggers=True):
    """
    Read the logging configuration from a ConfigParser-format file.

    This can be called several times from an application, allowing an end user
    the ability to select from various pre-canned configurations (if the
    developer provides a mechanism to present the choices and load the chosen
    configuration).
    """
. . . . . .

```

### 无配置注意事项

如果对应的Logger没有进行配置，会出现找不到对应处理器来处理消息的情况。根据版本不同会有如下表现

Python版本<3.2时

- 若logging.raiseException为False，则静默丢弃消息
- 若logging.raiseException为True，则打印“无法找到记录器的处理程序”

Python版本>=3.2时

- 使用logging.lastResort中存储的处理器进行输出。该处理器与任何Logger都没有关联，直接将描述信息写入sys.sterr，并且信息不会被格式化，输出级别为Warning
- 如果我们将logging.lastResort手动设置为None，其表现将和3.2之前的版本一致。

# 参考文档

1. [Python日志教程](https://docs.python.org/zh-cn/3.8/howto/logging.html)
2. [日志操作手册](https://docs.python.org/zh-cn/3.8/howto/logging-cookbook.html#logging-cookbook)
3. [日志格式化内容](https://docs.python.org/zh-cn/3.8/library/logging.html#logrecord-attributes)