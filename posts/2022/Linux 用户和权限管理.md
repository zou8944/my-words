---
created_at: 2022-01-10 22:09:40
updated_at: 2022-01-10 22:09:40
slug: linux-user-and-permission
---

这是Linux系列第二篇文章，本来觉得Shell写完就OK了。但仔细一梳理发现对很多Linux要么是一知半解，要么是忘了。既然如此，还是遇到什么就回顾什么吧。本文试图解决以下问题

- Linux如何做用户管理
- 用户和权限的关系
- 一个用户安装软件后，其它用户能否使用，这是如何决定的？
- 与此相关的命令的使用方式

<!--more-->

## 概览

Linux的权限管理，与两个重要的特性关联甚密：一切皆文件；多用户操作系统。多用户操作系统，意味着用户之间的资源需要隔离，就有了权限存在的必要性；一切皆文件，意味着权限管理的目标只有文件。

Linux有两种权限管理机制

- 原生的权限管理机制(Discretionary Access Control, DAC)，也就是UGO+RWX/ACL的权限控制。UGO标识User、Group、Other；RWX表示Read、Write、Execute；ACL表示Access Control List，即权限控制列表。这是默认的控制方式，也是我们需要关注的方式。
- SELinux的强制访问控制(Mandatory Access Control )，即基于标签的访问控制，将所有资源打上标签，程序只能访问有标签的资源，不能访问无标签的资源。这个不在本文讨论范围内。

## 基于用户角色的管理机制

### 用户、组

Linux对账户和组的管理通过ID实现，而不是用户名。用户和组的ID分别对应UID和GID。一个用户可以属于多个组，但只能属于一个基本组，可以属于多个附加组。用户用于精确授权，组用于批量授权。可以理解为RBAC中的用户和角色关系。

> 基本组和附加组的区别
>
> 基本组：如果没有指定用户组，创建用户的时候系统会默认同时创建一个和这个用户名同名的组，这个组就是基本组，不可以把用户从基本组中删除。在创建文件时，文件的所属组就是用户的基本组。
>
> 附加组：除了基本组之外，用户所在的其他组，都是附加组。用户是可以从附加组中被删除的。

#### useradd

```shell
# 创建账号guodong
useradd guodong
# 创建账号guodong，设置描述信息为Administrator、家目录为/home/guodong、设置失效日期为03-04、基本组为root、附加组为mail
useradd -c administrator -d /home/guodong -e 2022-03-04 -g root -G mail guodong
```

创建完后可以到/etc/passwd文件下查看刚创建的用户，其含义在后文描述。

```shell
guodong:x:1002:1002::/home/guodong:/bin/sh
```

所有的参数说明如下，它能够设置的参数包括家目录、组、是否同时创建家目录、密码(编码后的)、指定UID、指定shell等。

```shell
root@VM-20-5-ubuntu:~# useradd --help
Usage: useradd [options] LOGIN
       useradd -D
       useradd -D [options]

Options:
      --badnames                do not check for bad names
  -b, --base-dir BASE_DIR       base directory for the home directory of the
                                new account
      --btrfs-subvolume-home    use BTRFS subvolume for home directory
  -c, --comment COMMENT         GECOS field of the new account
  -d, --home-dir HOME_DIR       home directory of the new account
  -D, --defaults                print or change default useradd configuration
  -e, --expiredate EXPIRE_DATE  expiration date of the new account
  -f, --inactive INACTIVE       password inactivity period of the new account
  -g, --gid GROUP               name or ID of the primary group of the new
                                account
  -G, --groups GROUPS           list of supplementary groups of the new
                                account
  -h, --help                    display this help message and exit
  -k, --skel SKEL_DIR           use this alternative skeleton directory
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -l, --no-log-init             do not add the user to the lastlog and
                                faillog databases
  -m, --create-home             create the user's home directory
  -M, --no-create-home          do not create the user's home directory
  -N, --no-user-group           do not create a group with the same name as
                                the user
  -o, --non-unique              allow to create users with duplicate
                                (non-unique) UID
  -p, --password PASSWORD       encrypted password of the new account
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -s, --shell SHELL             login shell of the new account
  -u, --uid UID                 user ID of the new account
  -U, --user-group              create a group with the same name as the user
  -Z, --selinux-user SEUSER     use a specific SEUSER for the SELinux user mapping
      --extrausers              Use the extra users database
```

如果什么选项都不加，默认会做如下几件事

- 创建用户
- 创建用户的主目录
- 创建用户同名的组，并将用户放入其中

#### groupadd

添加组

```shell
# 创建gg组
groupadd gg
# 创建用户guodong，并将gg作为其primary组。
useradd guodong -g gg
```

添加后/etc/group文档，含义后面说

```shell
guodong:x:1002:
```

命令详情

```shell
ubuntu@VM-20-5-ubuntu:~$ groupadd --help
Usage: groupadd [options] GROUP

Options:
  -f, --force                   exit successfully if the group already exists,
                                and cancel -g if the GID is already used
  -g, --gid GID                 use GID for the new group
  -h, --help                    display this help message and exit
  -K, --key KEY=VALUE           override /etc/login.defs defaults
  -o, --non-unique              allow to create groups with duplicate
                                (non-unique) GID
  -p, --password PASSWORD       use this encrypted password for the new group
  -r, --system                  create a system account
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       directory prefix
      --extrausers              Use the extra users database
```

#### id

查看某个用户的详情，会打印出uid、所属组gid、所属组等。

```shell
ubuntu@VM-20-5-ubuntu:~$ id guodong
uid=1002(guodong) gid=1002(guodong) groups=1002(guodong),0(root)
```

命令详情，增加参数可以仅打印部分内容

```shell
ubuntu@VM-20-5-ubuntu:~$ id --help
Usage: id [OPTION]... [USER]
Print user and group information for the specified USER,
or (when USER omitted) for the current user.

  -a             ignore, for compatibility with other versions
  -Z, --context  print only the security context of the process
  -g, --group    print only the effective group ID
  -G, --groups   print all group IDs
  -n, --name     print a name instead of a number, for -ugG
  -r, --real     print the real ID instead of the effective ID, with -ugG
  -u, --user     print only the effective user ID
  -z, --zero     delimit entries with NUL characters, not whitespace;
                   not permitted in default format
      --help     display this help and exit
      --version  output version information and exit
```

#### passwd

修改某个用户的密码

```shell
ubuntu@VM-20-5-ubuntu:~$ sudo passwd guodong
New password: 
Retype new password: 
passwd: password updated successfully
```

#### usermod

修改用户信息，如密码、家目录、组信息等。能够修改的信息和useradd类似

```shell
# 修改guodong的描述信息
ubuntu@VM-20-5-ubuntu:~$ usermod guodong -c 果冻
ubuntu@VM-20-5-ubuntu:~$ cat /etc/passwd | grep guodong
guodong:x:1002:1002:果冻:/home/guodong:/bin/sh
```

#### userdel、groupdel

删除用户

```shell
# 删除用户
userdel guodong
# 删除组
groupdel guodong
```

#### 相关文件

- /etc/passwd

  存放用户的问题

  ```shell
  root@VM-20-5-ubuntu:~# cat /etc/passwd | grep ubuntu
  ubuntu:x:1000:1000:ubuntu:/home/ubuntu:/bin/bash
  ```

  总计被分为7段。从左到右，为，`用户名 : 口令 : UID : GID : 描述信息 : 家目录 : 登录shell`

  注意口令字段，存储的只是一个x，它只是表示有密码，真正的密码在/etc/shadow中

  > 伪用户：整个passwd文件中还有很多没有登录shell的用户，他们叫做伪用户，不能登录，只是为了方便系统管理而存在的。

- /etc/group

  存放组的文件

  ```shell
  root@VM-20-5-ubuntu:~# cat /etc/group | grep ubuntu
  adm:x:4:syslog,ubuntu
  cdrom:x:24:ubuntu
  sudo:x:27:ubuntu
  dip:x:30:ubuntu
  plugdev:x:46:ubuntu
  lxd:x:116:ubuntu
  ubuntu:x:1000:
  
  root@VM-20-5-ubuntu:~# id ubuntu
  uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)
  ```

  总计4个字段，`组名:组密码:GID:组内用户列表`。上面的命令中，刚好可以把`id ubuntu`得到的groups和上面的`/etc/group`包含ubuntu用户的组对应起来。

  > 组密码，用于在非本组用户切换到本组时的鉴权

- /etc/shadow

  存放用户密码的文件

  ```shell
  root@VM-20-5-ubuntu:~# cat /etc/shadow | grep ubuntu
  ubuntu:$6$jljvtYI5RLrh6ZwE$C/s2cHElV8XZ./cWGEV09ICjEavrLivzkpa0T/Sil1Xjv5rFTGAmSzOVDlBx8a8zUnvMlMNFcqrWt8k.F1ZHF0:18979:0:99999:7:::
  ```

  总计9个字段，`用户名:加密密码:最后一次修改时间:最小修改时间间隔:密码有效期:密码需要变更前的警告天数:密码过期后的宽限时间:账号失效时间:保留字段`

  加密密码使用了SHA512散列算法。

  > 伪用户的密码为!!或*，代表不能登录

- /etc/gshadow

  ```shell
  root@VM-20-5-ubuntu:~# cat /etc/gshadow | grep ubuntu
  adm:*::syslog,ubuntu
  cdrom:*::ubuntu
  sudo:*::ubuntu
  dip:*::ubuntu
  plugdev:*::ubuntu
  lxd:!::ubuntu
  ubuntu:!::
  ```

  总计4个字段，`组名:组密码:组管理员名:支持的账号名`

- /etc/login.defs

  设置用户账号限制的文件，该文件的配置对root用户无效。它用户在Linux创建用户时，对用户做一些默认的设置，比如UID范围、用户过期时间等。

### 文件权限

#### 详述

随便看一个文件

```shell
root@VM-20-5-ubuntu:~# ls -l /etc/login.defs
-rw-r--r-- 1 root root 10550 Feb  7  2020 /etc/login.defs
```

从左到右，依次为

- 文件类型：-表示文件，d表示目录，c表示字符型文件，l表示链接文件
- UGO权限：文件所有者、文件所有人所属组、其它人的权限，依次为读、写、执行，即RWX
- 连接计数：连接计数-2=本目录直接包含的子目录和文件总数；文件为1
- 文件所有者
- 文件所属组
- 大小，单位Byte
- 修改日期
- 文件名

> rwx，文件和目录不一样，目录的如下
>
> | rwx 权限      | 对目录的作用                                                 |
> | ------------- | ------------------------------------------------------------ |
> | 读权限（r）   | 表示具有读取目录结构列表的权限，也就是说，可以看到目录中有哪些文件和子目录。一旦对目录拥有 r 权限，就可以在此目录下执行 ls 命令，查看目录中的内容。 |
> | 写权限（w）   | 对于目录来说，w 权限是最高权限。对目录拥有 w 权限，表示可以对目录做以下操作：在此目录中建立新的文件或子目录；删除已存在的文件和目录（无论子文件或子目录的权限是怎样的）；对已存在的文件或目录做更名操作；移动此目录下的文件和目录的位置。一旦对目录拥有 w 权限，就可以在目录下执行 touch、rm、cp、mv 等命令。 |
> | 执行权限（x） | 目录是不能直接运行的，对目录赋予 x 权限，代表用户可以进入目录，也就是说，赋予 x 权限的用户或群组可以使用 cd 命令。 |

> 如果对rwx不了解，可以网上搜索，一搜一大堆

#### chmod

修改文件或目录权限

```shell
chmod +x hello.sh # 为hello.sh添加执行权限
```

所有可能的权限为`[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+`

#### chown

修改文件所有者，贴两个示例感受一下

```shell
chown root /u        Change the owner of /u to "root".
chown root:staff /u  Likewise, but also change its group to "staff".
chown -hR root /u    Change the owner of /u and subfiles to "root".
```

## 其它

### 决定用户是否能sudo

通过文件`/etc/sudoers`控制。文件不长，可以完整看一看

```shell
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
# 使用sudo时，会重置环境变量
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
# admin组下的所有用户能够sudo
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
# sudo组下的所有用户能够sudo
%sudo   ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
lighthouse ALL=(ALL) NOPASSWD: ALL
# 用户ubuntu可以在所有主机上，切换到所有用户和组上，在不用输密码的情况下，执行所有命令
ubuntu  ALL=(ALL:ALL) NOPASSWD: ALL
```

配置用户的sudo权限：**授权用户/组 主机=[(切换到哪些用户或组)] [是否需要输入密码验证] 命令1,命令2,...**

> 结合这个文件的Defaults，可以了解到，使用sudo执行命令时，当前用户shell的环境变量会被重置。

### 决定用户是否能远程ssh

如果需要禁止一个用户ssh登录怎么办。方法有两类

- 进制该用户登录

  - 锁定账号`usermod -L guodong`
  - 修改用户shell为不可登录`/sbin/nologin`

- 修改`/etc/ssh/sshd_config`

  ```shell
  # 禁止root用户登录
  PermitRootLogin no
  # 拒绝用户
  DenyUsers guodong
  ```

> 补充一个知识点：我们可以限制ssh的账号密码登录
>
> ```shell
> # 禁止guodong和root使用账号密码登录，其它允许
> Match User guodong,root
>   PasswordAuthentication no
> Match all
>   PasswordAuthentication yes
> ```

## 权限控制与软件安装

软件安装，本质上就是将软件包的各个部分放到适当的位置，即在不同目录下创建文件或目录，有几个点比较重要

- 软件的安装位置，会安装到用户的家目录吗？

- 新创建的文件或目录所有人、所有组是谁？这决定了那些人能够访问新安装的软件

### 软件安装位置

`apt insall`、`yum insall`、`dpkg -i `、`自由安装`的软件，它们最终到了哪个目录下？关于这个，了解两个点

1. linux目录众多，但某些目录一般是有专门用途的
2. apt、yum等安装软件时软件文件存放的位置，不是由安装器自己决定的，而是软件维护者决定，所以不能一概而论

对于第一点，首先了解你操作系统的PATH

```shell
root@VM-20-5-ubuntu:~# env | grep PATH
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
```

> PATH的作用，默认操作提供到PATH指定的目录中查找命令

关于文件夹管理这玩意儿，其实[Linux还有个标准](https://www.linuxbase.org/betaspecs/fhs/fhs/index.html)。

常见的与软件安装有关的目录有

| 路径                                                      | 作用                                                         |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| /usr/local/sbin                                           | 自己编译的、根用户才能访问的命令                             |
| /usr/local/bin                                            | 自己编译的、大家都能访问的命令                               |
| /usr/sbin、/sbin（只是/usr/sbin的链接，至少ubuntu是如此） | 系统的或安装的、根用户才能访问的命令                         |
| /usr/bin、/bin（它只是/usr/bin的链接，至少ubuntu是如此）  | 系统的或安装的、大家都能访问的命令                           |
| /usr/share                                                | 存放一些共享数据，如文档等                                   |
| /usr/lib                                                  | 存放软件所需的库文件                                         |
| /etc                                                      | 存放配置文件                                                 |
| /opt                                                      | 一些可选的软件会安装在这里。<br />可选就是用户自己安装的一些无足轻重与系统无关的应用<br />比如tomcat |

要点1：区分`bin和sbin`、`/usr和/usr/local`，可以看看[知乎](https://www.zhihu.com/question/21265424?sort=created)

要点2：我们可以查看一下usr下目录的权限，可以看到所有人都是root，只有root能够写，但是其它用户具有读和执行权限。那么可以猜测，将软件安装到这些目录，需要root权限。

```shell
ubuntu@VM-20-5-ubuntu:~$ ls -l /usr
total 136
drwxr-xr-x   2 root root 57344 Dec 18 11:26 bin
drwxr-xr-x   2 root root  4096 Dec 18 10:56 config
drwxr-xr-x   2 root root  4096 Apr 15  2020 games
drwxr-xr-x  10 root root 16384 Dec 18 10:33 include
drwxr-xr-x  94 root root  4096 Dec 18 11:26 lib
drwxr-xr-x   2 root root  4096 Apr 23  2020 lib32
drwxr-xr-x   2 root root  4096 Jun  5  2021 lib64
drwxr-xr-x   4 root root  4096 Dec 18 12:29 libexec
drwxr-xr-x   2 root root  4096 Apr 23  2020 libx32
drwxr-xr-x  12 root root  4096 Dec 18 10:33 local
drwxr-xr-x   2 root root 20480 Jan 12 10:50 sbin
drwxr-xr-x 159 root root  4096 Dec 18 11:09 share
drwxr-xr-x   4 root root  4096 Nov  9 21:41 src
```

### 安装人的影响

为什么有些安装需要sudo，sudo就是以root用户的身份执行此条命令。所有部分命令的执行如果需要访问root用户才有权限修改的文件或目录，则需要sudo。

另一个问题，一个普通用户安装的软件，另一个普通用户能用吗？这要看情况，如果将软件正常安装到上述目录中，则所有用户都能访问。但理论上可以进行不规范操作，在用户自己的家目录下安装软件，并加入PATH，则其它用户无法访问。

所以，这还是一个文件权限管理的问题。

## 总结

Linux的权限，归根结底管理的是文件，搞清楚文件权限、用户和组之间的关系，掌握几个关键命令，应对日常维护问题不大。
