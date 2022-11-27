---
created_at: 2021-12-05 18:08:34
updated_at: 2021-12-05 18:08:34
slug: docker-dockerfile
---

本文介绍Dockerfile中主要命令的用途

<!--more-->

## FROM

指定基础镜像，推荐的方式是 image:tag，精确指定。注意：可以使用多条FROM，这样就会构建多个镜像。

比如我同时想要busybox和nginx，我可以这么写

```dockerfile
FROM busybox:latest
FROM nginx:latest
```

然后构建运行

```shell
# 构建
root@10-9-175-15:/home/ubuntu/docker-learn$ docker build -t busybox-nginx .
Sending build context to Docker daemon  40.96kB
# layer 1
Step 1/2 : FROM busybox
 ---> d23834f29b38
# layer 2
Step 2/2 : FROM nginx
latest: Pulling from library/nginx
e5ae68f74026: Pull complete 
21e0df283cd6: Pull complete 
ed835de16acd: Pull complete 
881ff011f1c9: Pull complete 
77700c52c969: Pull complete 
44be98c0fab6: Pull complete 
Digest: sha256:9522864dd661dcadfd9958f9e0de192a1fdda2c162a35668ab6ac42b465f0603
Status: Downloaded newer image for nginx:latest
 ---> f652ca386ed1
Successfully built f652ca386ed1
Successfully tagged busybox-nginx:latest

# 我们运行它，并进入shell
root@10-9-175-15:/home/ubuntu/docker-learn$ docker run -it f652ca386ed1 sh

# 查看nginx，没错，在的
$ nginx -v
nginx version: nginx/1.21.4
```

## ENV和ARG

ENV为创建出来的容器声明环境变量。该环境变量在启动的容器中可用，在特定的指令中也能够使用，这些指令包括ENV、ADD、COPY、WORKDIR、EXPOSE、VOLUME、USER。

ARG类似，但它声明的变量只能在Dockerfile中使用，不能再启动的容器中使用。

我们做个实验，在docker build过程中输出定义的环境变量，在容器中输出该环境变量

```dockerfile
FROM busybox
  
ENV ENVTEST="hello,world"

RUN echo $ENVTEST
```

然后构建运行

```shell
root@10-9-175-15:/home/ubuntu/docker-learn$ docker build -t busybox-env .
Sending build context to Docker daemon  40.96kB
# layer 1
Step 1/3 : FROM busybox
 ---> d23834f29b38
# layer 2
Step 2/3 : ENV ENVTEST="hello,world"
 ---> Running in 4e20395f2f9a
Removing intermediate container 4e20395f2f9a
 ---> 79a34075b8ca
# layer 3
Step 3/3 : RUN echo $ENVTEST
 ---> Running in 3a9ca99e38c6
hello,world
Removing intermediate container 3a9ca99e38c6
 ---> 79b312023015
Successfully built 79b312023015
Successfully tagged busybox-env:latest

# 运行起来
root@10-9-175-15:/home/ubuntu/docker-learn$ docker run -it --name busybox-env busybox-env sh

# 打印上面设置的环境变量
/ $ env | grep ENVTEST
ENVTEST=hello,world
```

## RUN

RUN会在前一条命令创建出来的镜像的基础上创建一个容器，并在容器中运行命令，结束后将容器提交为新的镜像，新镜像作为下一条命令的基础。

RUN有两种格式

```dockerfile
# shell格式，通过/bin/sh -c运行的
RUN ls -a -l
# exec格式，直接运行可执行文件，后面跟的参数
RUN ["ls", "-a", "-l"]
```

几个注意点

- 推荐使用exec格式。
- exec格式中，`["ls", "-a", "-l"]`会被Docker当成json数组解析，因此必须使用双引号
- exec格式中，由于没有使用sh运行，因此环境变量是不会被解析的，除非你的可执行文件指的就是sh，即`["sh", "-c", "ls", "-al"]`

这里就不演示了，在ENV我们演示过了，截取片段：如下，启动的临时容器id为3a9ca99e38c6，运行了echo后移除了该容器，并生成了id为79b312023015的层。

```shell
Step 3/3 : RUN echo $ENVTEST
 ---> Running in 3a9ca99e38c6
hello,world
Removing intermediate container 3a9ca99e38c6
 ---> 79b312023015
```

## COPY和ADD

这两个很相似，它们的共同点是：作用在本地文件时候，都是普通的复制关系，即将本地文件或文件夹复制到新镜像中；不同点是，ADD额外增加了两个功能，当源文件是URL时，它会下载下来，然后放到镜像中，当源文件是本地压缩文件时，它能将该文件解压然后复制到镜像中。

一般来说推荐使用COPY，因为它更方便理解。能用ADD的地方，完全可以用RUN加上wget或的命令完成。下面演示

```shell
FROM busybox
  
ENV ENVTEST="hello,world"

RUN echo $ENVTEST

# 镜像中创建/data/test文件夹
RUN mkdir -p /data/test
# 当前目录的Dockerfile复制进来
COPY ./Dockerfile /data/test/
# namespace.c复制进来
ADD ./namespace.c /data/test/
# 远程下载一个文件然后复制进来
ADD https://github.com/moby/moby/blob/master/client/client.go /data/test/
# 本地压缩文件解压然后复制进来
ADD ./test.tar.gz /data/test/
```

验证

```shell
root@10-9-175-15:/home/ubuntu/docker-learn# docker build -t busybox-add-copy .
Sending build context to Docker daemon  25.09kB
Step 1/8 : FROM busybox
 ---> d23834f29b38
Step 2/8 : ENV ENVTEST="hello,world"
 ---> Using cache
 ---> 79a34075b8ca
Step 3/8 : RUN echo $ENVTEST
 ---> Using cache
 ---> 79b312023015
# 创建目录
Step 4/8 : RUN mkdir -p /data/test
 ---> Running in 221ac6587f2e
Removing intermediate container 221ac6587f2e
 ---> 4e3602a7ab46
# 复制
Step 5/8 : COPY ./Dockerfile /data/test/
 ---> ad3cb3d4e974
# 复制
Step 6/8 : ADD ./namespace.c /data/test/
 ---> 057dfbef575c
# 下载
Step 7/8 : ADD https://github.com/moby/moby/blob/master/client/client.go /data/test/
Downloading  283.9kB

 ---> 587b68473628
# 解压
Step 8/8 : ADD ./test.tar.gz /data/test/
 ---> 908872aeb387
Successfully built 908872aeb387

# 启动容器
root@10-9-175-15:/home/ubuntu/docker-learn# docker run -it --name busybox-add-copy busybox-add-copy sh
# 跳转到目标目录下，查看
/ # cd data/test/
/data/test # ls
Dockerfile   client.go    namespace.c  namespace.o
```

可以看到

- Dockerfile被复制进来了
- namespace.c被复制进来了
- client.go被下载然后复制进来了
- test.tar.gz被解压成namespace.o并复制进来了

## CMD和ENTRYPOINT

这两个必须一起提，因为很多时候开发者都搞不懂他们之间的关系

我们先看CMD，它有三种格式

```dockerfile
# shell格式
CMD ls
# exec格式
CMD ["ls", "-a", "-l"]
# param格式，为ENTRYPOINT指定提供参数用
CMD ["-a", "-l"]
```

它的注意事项

- 一个Dockerfile中可以有多个CMD指令，但只有最后一个会生效
- CMD的前两种格式与RUN类似，但它本身的作用于RUN完全不同。它不会在容器构建过程中执行，而是在容器启动时作为第一条执行指令
- 如果用户在docker run时明确指定了指令，则会覆盖CMD指定的指令

再来看ENTRYPOINT，它只有两种格式

```dockerfile
# shell格式
ENTRYPOINT ls
# exec格式
ENTRYPOINT ["ls", "-a", "-l"]
```

它的注意事项

- 一个Dockerfile可以有多个ENTRYPOINT指令的，但只有最后一个会生效

- 使用shell格式时，ENTRYPOINT会忽略任何CMD和docker run指定的指令，并会运行在sh -c中。这意味着我们指定的进程PID将不会是1，不能接收Unix信号。在使用docker stop结束容器时，我们的进程收不到结束信号。

- 使用exec格式时，docker run传入的参数会覆盖CMD指定的内容，并附加到ENTRYPOINT指令的参数中。

  也就是说，如果我有如下dockerfile声明

  ```dockerfile
  CMD ["java", "-jar", "hello.jar"]
  ENTRYPOINT ["sh", "-c"]
  ```

  不带任何参数启动容器时，实际执行的是：`sh -c java -jar hello.jar`。

  如果运行`docker run xxx ls`，实际执行的就是：`sh -c ls`

### 验证CMD

```dockerfile
FROM ubuntu
  
ENV ENVTEST="hello,world"

RUN echo $ENVTEST

CMD ["/bin/bash"]
```

运行

```shell
root@10-9-175-15:/home/ubuntu/docker-learn# docker build -t ubuntu-cmd .
Sending build context to Docker daemon  25.09kB
Step 1/4 : FROM ubuntu
 ---> ba6acccedd29
Step 2/4 : ENV ENVTEST="hello,world"
 ---> Running in 1f3709504258
Removing intermediate container 1f3709504258
 ---> 0ff22c83d97b
Step 3/4 : RUN echo $ENVTEST
 ---> Running in 270682e9ba4c
hello,world
Removing intermediate container 270682e9ba4c
 ---> 61316edd34e2
Step 4/4 : CMD ["/bin/bash"]
 ---> Running in 4178afd282b1
Removing intermediate container 4178afd282b1
 ---> ddf82bc91062
Successfully built ddf82bc91062
Successfully tagged ubuntu-cmd:latest

# 运行起来
root@10-9-175-15:/home/ubuntu/docker-learn# docker run -it ubuntu-cmd

# 查看当前进程号
root@a0bf5cba468b:/# echo $$
1
```

可见：容器启动时默认运行了/bin/bash，并且，该进程号为1。

使用docker run进行覆盖

```shell
# 指定容器启动运行ls，这里看到，确实运行了ls，然后马上退出了容器，说明确实已经覆盖了CMD指令
root@10-9-175-15:/home/ubuntu/docker-learn# docker run -it ubuntu-cmd ls
bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  etc  lib   lib64  media   opt  root  sbin  sys  usr
```

### 验证ENTRYPOINT

```dockerfile
FROM ubuntu
  
ENV ENVTEST="hello,world"

RUN echo $ENVTEST

# 故意构建一个错误的指令，/bin/bash ls -a -l，会执行失败
CMD ["ls", -a", "-l"]
ENTRYPOINT ["/bin/bash"]
```

运行

```shell
root@10-9-175-15:/home/ubuntu/docker-learn# docker build -t ubuntu-entrypoint .
Sending build context to Docker daemon  25.09kB
Step 1/5 : FROM ubuntu
 ---> ba6acccedd29
Step 2/5 : ENV ENVTEST="hello,world"
 ---> Using cache
 ---> 0ff22c83d97b
Step 3/5 : RUN echo $ENVTEST
 ---> Using cache
 ---> 61316edd34e2
Step 4/5 : CMD ["ls", -a", "-l"]
 ---> Running in 5eb37a4b1820
Removing intermediate container 5eb37a4b1820
 ---> eb29627384d0
Step 5/5 : ENTRYPOINT ["/bin/bash"]
 ---> Running in fe3f5150adb5
Removing intermediate container fe3f5150adb5
 ---> 74c6f840a68c
Successfully built 74c6f840a68c
Successfully tagged ubuntu-entrypoint:latest

# 启动报ls错误，说明CMD确实被加到参数中去了
root@10-9-175-15:/home/ubuntu/docker-learn# docker run --name ubuntu-entrypoint ubuntu-entrypoint
/usr/bin/ls: /usr/bin/ls: cannot execute binary file

# docker run指定启动参数touch，包touch错误，说明替代了CMD，但ENTRYPOINT没被改变
root@10-9-175-15:/home/ubuntu/docker-learn# docker run --name ubuntu-entrypoint ubuntu-entrypoint touch
/usr/bin/touch: /usr/bin/touch: cannot execute binary file
```

### 小问题

- 注意不同启动方式的影响，参考[这篇文章](https://zou8944.com/2022/05/19/Kubernetes%E9%85%8D%E7%BD%AE%E7%8E%AF%E5%A2%83%E5%8F%98%E9%87%8F%E5%AE%B9%E5%99%A8%E5%86%85%E9%83%A8%E4%B8%8D%E7%94%9F%E6%95%88/)

- 如何在容器启动时执行两条命令？

  使用`shell`格式启动，比如`CMD ["sh", "-c", "command1 && command2"]`

  要注意的是，command1必须是能结束的命令，否则command2不会执行。

## <未完待续>

Dockerfile肯定不止这么写指令，但这几个是最重要的内容，能够正确实用Dockerfile的关键，其它等有需要时再添加

## 其它

几个原则和注意事项

- 共享Dockerfile比共享Docker镜像好，因为Dockerfile容易版本控制，构建过程清晰，占用空间少
- CMD指令和ENTRYPOINT并不存在取舍，二者结合使用最后。CMD由于可被docker run覆盖的特性，适用于指定可变参数，ENTRYPOINT相应地适用于指定不可变指令。
- 使用保证镜像尽量小
  - 使用足够轻量的基础镜像
  - 不要在镜像中放置无用的内容
  - 如果有文件需要共享，用volume进行挂载，不要放到镜像中
- 充分利用缓存，Docker镜像时分层的，无论构建、拉取都会有缓存，减小Dockerfile的变化部分，有利于提升缓存命中率
