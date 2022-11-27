---
created_at: 2022-05-19 14:22:29
updated_at: 2022-05-19 14:22:29
slug: kubernetes-trouble-shooting-deployment-environment-variable
---

> 记一个卡了两天的问题

<!--more-->

## 问题

Dockerfile中，指定不同的启动方式，会有不同的读取环境变量的效果。有的能够读到，有的读不到。具体来说，如下

- 能够读取到的方式
  - 直接启动 `CMD ["java", " -jar", "xxxx.har"]`
  - tini+直接启动 `CMD ["/tini", "--", "java", " -jar", "xxxx.har"]`
  - tini+sh启动 `CMD ["/tini", "--", "sh", "-c", "java -jar xxxx.jar"]`
- 不能读取的方式
  - sh启动 `CMD ["sh", "-c", "java -jar xxxx.jar"]`
  - sh启动 `CMD java -jar xxxx.jar`

## 原因

没有找到官方说明，只在这篇文章中发现了一样的问题：[k8s 中env小写环境变量未注入到容器中](https://blog.csdn.net/zhaopeng_yu/article/details/121375222)。

分析原因：Kubernetes不会将环境变量传给`sh`，但是会传给`/bin/bash`。一般情况下，`sh`都是链接到某个具体的shell命令，但是不同的Linux发行版有不同的行为，如果是链接到`/bin/bash`则任何方式启动都能正常读取环境变量；否则，使用`sh`的方式启动就读不到了。

而我的情况，`sh`链接到了`dash`

```shell
root@app-xxx-548f5df7bf-2gc42:/# ls -l /bin/sh
lrwxrwxrwx 1 root root 4 Dec 20 08:00 /bin/sh -> dash
```

## 解决办法

对于读取不到的方式，可以手动将`sh`链接到`/bin/bash`。一个Djando admin的Dockerfile如下

```dockerfile
FROM python:3.10

# 省略若干行
... ...

# 修改sh的链接
RUN  ln -sf /bin/bash /bin/sh

CMD ["sh", "-c", "python mampod/manage.py migrate && python mampod/manage.py runserver 0.0.0.0:8969"]

```

## 扩展 - 再看ENTRYPOINT 和 CMD

[之前的文章](https://zou8944.com/2021/12/05/Dockerfile/)我们有讲过这个问题，但那侧重容器启动时哪个命令生效的问题，现在我们来捋一下它们的启动方式。

- `ENTRYPOINT`的几种方式

  - `ENTRYPOINT ["executable", "param1", "param2"]`

    **exec格式，推荐方式**。直接执行指定的命令，不会以任何shell形式启动

  - `ENTRYPOINT command param1 param2`

    shell格式，相当于`/bin/sh -c "command param1 param2" `

- `CMD`的几种方式

  - `CMD ["executable","param1","param2"]`

    **exec格式，推荐方式**。直接执行，不会以任何shell的形式启动。

  - `CMD command param1 param2`

    shell格式，相当于`/bin/sh -c "command param1 param2" `

  - `CMD ["param1","param2"]`

    仅作为ENTRYPOINT的参数，不能单独使用

总结下来，无非两种启动方式

- 直接执行指定的命令
  - 以exec格式启动
- 以`shell`方式启动
  - exec格式的命令指定为`"sh", "-c"`
  - 以shell格式启动

这里的启动方式，也佐证了前面描述的问题：凡是以`sh`方式启动的case，都拿不到环境变量。

## 总结

- Linux知识很重要
- 细节很重要
- 耐心很重要
