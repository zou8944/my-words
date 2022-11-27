---
created_at: 2019-12-07 10:35:21.0
updated_at: 2021-02-16 23:23:47.768
slug: pipenv-introduction
tags: 
- Python
- pipenv
---



Pipenv是一个包管理和虚拟环境工具，致力于将所有的打包工具（bundler, composer, npm, cargo, yarn等）中的优点带到python世界。它将pip和virtualenv结合起来，为每个project创建一个虚拟环境，同时通过Pipfile指定需要安装的依赖，并自动解析依赖的依赖，生成的Pipfile.lock将各依赖版本锁定，以使各个环境保持一致。
<!--more-->
## 简单使用

假设场景：创建一个新项目，访问某度，输出访问结果。使用Pycharm创建，目录结构和代码如下。

![image-20191207113857861](image-20191207113857861.png)

- 安装pipenv

  ```shell
  python3.8 -m pip install pipenv
  ```

- 安装依赖

  ```shell
  pipenv install requests
  ```

  初次安装依赖会先初始化虚拟环境，然后将requests写入Pipfile文件并下载，整个安装过程控制台输出如下

  ![image-20191207114240569](image-20191207114240569.png)

  安装完成后目录结构：新生成Pipfile和Pipfile.lock两个文件

  ![image-20191207114424866](image-20191207114424866.png)

- 运行代码

  ```shell
  pipenv run python test.py
  ```

  ![image-20191207114905560](image-20191207114905560.png)

可以看到，非常简单，但还是不免出错，这里列出我遇到过的问题

- pip安装后找不到pipenv命令

  这和pipenv的安装没有关系，是python配置的问题，可通过绝对路径调用，新安装的命令位置一般在pip对应的python安装位置的bin目录下。

- 运行pipenv run python时将virtualenv目录定位到/root/.local/share/..目录下，导致Permission deny

  由于暂时不了解pipenv确定虚拟环境安装目录的依据，因此我的解决方案时让他安装在一个明确的位置——项目目录，方式是设置环境变量PIPENV_VENV_IN_project="true"

  ```shell
  export PIPENV_VENV_IN_project="true"
  ```

## 执行结果分析

### 虚拟环境

初次运行时pipenv会在某个位置为当前项目创建一个唯一的虚拟环境，该位置一般为执行用户的目录，上例中是/home/floyd/.local/share/virtualenvs/demo-G7_K1YDZ。如果觉得该位置不好，也可以设置系统环境变量PIPENV_VENV_IN_project="true"建立在当前项目目录，这是我比较倾向的方式，方便管理。

一旦虚拟环境安装完成，后面所有针对pipenv的操作均是在该环境中进行，包括库的安装、任务的执行等。注意这种**非全局性**，这样OK，保证了隔离性，但也意味着我们必须对每个项目重新安装一次相同的依赖，很麻烦，尤其是经常需要创建多个项目的场景；使用IDE时也会带来问题：IDE默认解释器是全局的，因此即使使用pipenv安装完成，也会报import错误，因为全局python的路径中并无该库，这会造成一定程度上的困扰。

### Pipfile

通过pipenv install安装的依赖会写入此文件，本例中初始内容如下。pipfile有着较为丰富的表现力，可以直接修改然后运行pipenv install裸命令完全按照该文件进行下载。

```python
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
requests = "*"

[requires]
python_version = "3.8"
```

我们能操作的事项较多，例如可以自由更换源，设置dev和prod环境依赖的不同，指定目标python版本等，甚至可以指定多个源，每个依赖使用指定的源进行下载。如下展示了我的一个正式项目中的配置

```shell
[[source]]
url = "https://pypi.tuna.tsinghua.edu.cn/simple/"
verify_ssl = true
name = "pypi"

[packages]
aliyun-log-python-sdk = {version = "*"}
aliyun-python-sdk-core-v3 = {version = "*"}
celery = {version = "*"}
Django = {version = "==2.2.4"}
django-admin = {version = "*"}
django-postgres-extensions = {version = "*"}
django_pgjsonb = {version = "*"}
peewee = {version = "*"}
psycopg2 = {version = "*"}
PyYAML = {version = "*"}
requests = {version = "*"}
redis = {version = "*"}
oss2 = {version = "*"}
fake_useragent = {version = "*"}
lxml = {version = "*"}
eventlet = {version = "*"}

[requires]
python_version = "3"
```

更多配置可参考[官方手册](https://pipenv.kennethreitz.org/en/latest/basics/#example-pipfile-pipfile-lock)

### Pipfile.lock

一个Pipfile.lock文件如下，它固定了所有依赖和运行环境等内容，由Pipfile生成，不归我们修改，这里仅做展示。

```python
{
    "_meta": {
        "hash": {
            "sha256": "acbc8c4e7f2f98f1059b2a93d581ef43f4aa0c9741e64e6253adff8e35fbd99e"
        },
        "pipfile-spec": 6,
        "requires": {
            "python_version": "3.8"
        },
        "sources": [
            {
                "name": "pypi",
                "url": "https://pypi.org/simple",
                "verify_ssl": true
            }
        ]
    },
    "default": {
        "certifi": {
            "hashes": [
                "sha256:017c25db2a153ce562900032d5bc68e9f191e44e9a0f762f373977de9df1fbb3",
                "sha256:25b64c7da4cd7479594d035c08c2d809eb4aab3a26e5a990ea98cc450c320f1f"
            ],
            "version": "==2019.11.28"
        },
        "chardet": {
            "hashes": [
                "sha256:84ab92ed1c4d4f16916e05906b6b75a6c0fb5db821cc65e70cbd64a3e2a5eaae",
                "sha256:fc323ffcaeaed0e0a02bf4d117757b98aed530d9ed4531e3e15460124c106691"
            ],
            "version": "==3.0.4"
        },
        "idna": {
            "hashes": [
                "sha256:c357b3f628cf53ae2c4c05627ecc484553142ca23264e593d327bcde5e9c3407",
                "sha256:ea8b7f6188e6fa117537c3df7da9fc686d485087abf6ac197f9c46432f7e4a3c"
            ],
            "version": "==2.8"
        },
        "requests": {
            "hashes": [
                "sha256:11e007a8a2aa0323f5a921e9e6a2d7e4e67d9877e85773fba9ba6419025cbeb4",
                "sha256:9cf5292fcd0f598c671cfc1e0d7d1a7f13bb8085e9a590f48c010551dc6c4b31"
            ],
            "index": "pypi",
            "version": "==2.22.0"
        },
        "urllib3": {
            "hashes": [
                "sha256:a8a318824cc77d1fd4b2bec2ded92646630d7fe8619497b142c84a9e6f5a7293",
                "sha256:f3c5fd51747d450d4dcf6f923c81f78f811aab8205fda64b0aba34a4e48b0745"
            ],
            "version": "==1.25.7"
        }
    },
    "develop": {}
}
```

# Pycharm配置pipenv

> 更新于次日

上面的例子说到，安装pipenv并创建虚拟环境后，新安装的库不会在全局解释器中生效，导致Pycharm无法给予正确的提示，非常不便。而Pycharm实际上是提供将解释器设置为pipenv的方式，可以解决这个问题。这里以已经存在的项目为例进行pipenv环境配置，按下列方式进入设置界面

File => Settings => Project:{你的项目名} => Project Intercepter

![image-20191209145003311](image-20191209145003311.png)

点击图中标记设置图片，选择“Add”，来到解释器添加界面。选择Pipenv Environment。两项需要填写：

- Base intercepter: 选择你安装pipenv的python可执行文件
- Pipenv executable: 选择你事先安装的pipenv的执行文件

![image-20191209145341432](image-20191209145341432.png)

> - 注意事项1： 在Pycharm中添加pipenv环境前必须先手动将原先生成的virtualenv文件夹删除，否则会出现环境设置失败的情况。
> - 注意事项2： 该配置方式在IDEA中同样适用，因为Pycharm本就是IDEA的子集

# 参考资料

1. [pipenv官方手册](https://pipenv.kennethreitz.org/en/latest/install/)
2. [Configure Pipenv environments（IntelliJ IDEA官方手册）](https://www.jetbrains.com/help/idea/pipenv.html)