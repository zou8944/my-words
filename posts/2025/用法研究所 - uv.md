---
created_at: 2025-05-27 12:00:00
updated_at: 2025-05-27 12:00:00
title: 用法研究所 - uv
slug: usage-research-uv
categories:
  - 工具
tags:
  - "uv"
  - "工具"
  - "Python"
---
## What and Why
`uv` 是由 [Astral](https://astral.sh/) 开发的 Python 工具。在一定程度上是可以取代 `pip`、`poetry`、`pyenv`、`twine`、`virtualenv` 等工具，主要用于做 Python 依赖管理和 Python 版本管理。通过 `uv` 命令可以完成从运行单个 Python 脚本、项目依赖管理（依赖声明和版本锁定）、虚拟环境管理等几乎所有维护 Python 项目需要的功能。
之前的工具都只负责部分功能，如 `pyenv` 负责系统上的 Python 版本管理；`virtualenv` 负责虚拟 Python 环境的创建；`pip` 负责依赖管理；`uv` 实现了所有这些功能。当然 `poetry` 也实现了这些功能，但 `uv` 说它比 `poetry` 更快。

> **为什么 uv 更快？**
> 用 Rust 重写了包解析器；在包管理上完全脱离 Python 本身工具链，甚至不会启动 Python，在 Rust 层面处理问题；用了 Rust 相比 Python 就有了并发优势（Python 有 GIL 限制）。相比之下，像 `poetry` 这样的工具仍基于 Python 运行，受限于解释器启动时间、单线程执行等因素，会比较慢。

> **注意事项**
> `uv` 并不等同于 `pyenv`（用于管理系统中的多个 Python 版本）或 `twine`（用于将包发布到 PyPI），这些功能目前还不在 `uv` 的职责范围内。`uv` 只能管理通过 `uv run` 运行时使用的 Python 版本。

## Python 版本管理
当我们说 Python 版本管理时，我们就是在说 Python 可执行文件和标准库等完整配套的管理。先看使用方法
```shell
# 展示第一个选中的 Python 安装位置。一般来说这就是当前生效的 python 版本
uv python find
# 列出当前系统下所有 Python 版本，包括系统的、pyenv 安装的、conda 安装的
uv python list
# 安装 Python 3.12（无论系统是否存在，都会安装，安装源是 uv 自己提供的）
uv python install 3.12
# 移除 uv 安装的 Python 版本（非 uv 安装的不会动）
uv python uninstall 3.12
# 展示 uv 安装的 Python 所在目录
uv python dir
# 在当前目录下创建 `.python-version` 并将 3.12 写入其中
uv python pin 3.12
# 展示当前 `pin` 的 Python 版本
uv python pin

# 使用 `uv python find` 规则找到的 Python 版本创建虚拟环境
uv venv

# 以当前版本的 Python 运行 `main.py`
uv run main.py
```

**确定 Python 版本 [ref](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version)**
我们用 `uv run` 运行脚本时，使用 `uv add` 安装依赖时，都需要用到 Python 环境，`uv` 按照如下规则确定使用哪个版本的 Python 环境。
- 当前目录下的 `.python-version` 文件指定的版本
- 父目录（不超过当前项目目录）下的 `.python-version` 文件指定的版本
- 用户目录下的 `.python-version` 文件指定的版本
- 如果都没有，则不指定，使用当前系统中生效的 Python 版本

**发现 Python 版本 [ref](https://docs.astral.sh/uv/concepts/python-versions/#discovery-of-python-versions)**
在确定了 Python 版本后，`uv` 按照如下规则搜索符合版本的执行环境
- 首先尝试虚拟环境的发现规则
    - 优先尝试 `VIRTUAL_ENV` 变量指定的虚拟环境
    - 其次尝试 `CONDA_PREFIX` 指定的虚拟环境
    - 最后尝试当前目录下的 `.venv` 或父目录下的 `.venv` 环境
- 然后尝试自己的发现规则
    - 首先搜索 `uv` 自己的 Python 安装目录下的版本
    - 其次检查系统中符合要求的 Python 版本

`uv python find` 得到的结果就是按照上述规则找到的第一个符合要求的 Python 版本路径。如果我们使用 `uv python pin` 改变当前目录下的 `.python-version` 文件所记录的版本，会发现 `uv python find` 得到的结果已经更新了。**你可能会有疑问，之前创建的 `venv` 还是旧版本，`uv run` 会发生什么，答案是执行 `uv run` 时，`uv` 会将旧的 `venv` 移除，创建符合新版本的 `venv`**。下面的例子有展示
```shell
# 固定 3.10 版本
zouguodong@MacBook-Pro-2 demo % uv python pin 3.10
Pinned `.python-version` to `3.10`

# 创建 3.10 版本的虚拟环境
zouguodong@MacBook-Pro-2 demo % uv venv
Using CPython 3.10.0 interpreter at: /Users/zouguodong/.pyenv/versions/3.10.0/bin/python3.10
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

# 查看 `uv python find` 生效的是 3.10 版本
zouguodong@MacBook-Pro-2 demo % uv python find
/Users/zouguodong/.pyenv/versions/3.10.0/bin/python3.10

# 查看 `uv run` 运行的也是 3.10 版本
zouguodong@MacBook-Pro-2 demo % uv run -- python --version;
Python 3.10.0

# 重新固定为 3.12 版本
zouguodong@MacBook-Pro-2 demo % uv python pin 3.12
Updated `.python-version` from `3.10` -> `3.12`

# 查看 `uv python find` 生效的是 3.12 版本
zouguodong@MacBook-Pro-2 demo % uv python find
/opt/homebrew/opt/python@3.12/bin/python3.12

# `uv run` 自动重建了新的虚拟环境
zouguodong@MacBook-Pro-2 demo % uv run -- python --version;
Using CPython 3.12.10 interpreter at: /opt/homebrew/opt/python@3.12/bin/python3.12
Removed virtual environment at: .venv
Creating virtual environment at: .venv
Python 3.12.10
```

**pyproject.toml 的 `requires-python` 的作用**
`.python-version` 约束了当前文件夹下的固定的 Python 版本，而 `pyproject.toml` 下的 `requires-python` 约束了当前项目(其实也是当前文件夹)的 Python 版本。我们应该保持二者兼容，当不兼容时，执行 `uv sync` 或 `uv run` 等命令时会报错，如下
```shell
$ uv run -- python -c "import sys; print(sys.executable)";
Using CPython 3.10.0 interpreter at: /Users/zouguodong/.pyenv/versions/3.10.0/bin/python3.10
error: The Python request from `.python-version` resolved to Python 3.10.0, which is incompatible with the project's Python requirement: `>3.10`. Use `uv python pin` to update the `.python-version` file to a compatible version.
```

## 依赖管理
```shell
# 添加依赖
uv add requests
# 升级依赖
uv add -U requests
# 移除依赖
uv remove requests
# 添加 `requirements.txt` 中的所有依赖
uv add -r requirements.txt
# 添加时指定源，使用 `default-index` 设置默认源之后就不用加了
uv add requests --default-index https://mirrors.aliyun.com/pypi/simple/

# 生成或者更新 `uv.lock` 文件
uv lock
# 检查当前 `uv.lock` 文件是否符合 `pyproject.toml` 中依赖的描述要求
uv lock --check
# 同步依赖（将当前环境的依赖同步到 `uv.lock` 中的状态）
uv sync

# 将 `uv.lock` 导出为 `requirements.txt`
uv export --format requirements-txt
```

> 添加依赖时，依赖可以有多种约束形式。详情参考[手册](https://docs.astral.sh/uv/concepts/projects/dependencies/#dependency-sources)

> 默认源也可以通过 `UV_DEFAULT_INDEX` 环境变量设置

**依赖安装到哪里去了**
当我们执行 `uv add` 时，会在 `pyproject.toml` 中添加依赖声明，然后安装依赖到当前环境。当前环境就是按照[Python 版本管理](#python版本管理)所述规则确定的环境。

**`uv lock` 时版本如何确定**
`uv lock` 当前项目的依赖写到 `uv.lock` 文件，当前项目的依赖是指 Python 运行环境中的依赖版本。

**`uv sync` 做了什么**
`uv sync` 将 `uv.lock` 文件中声明的依赖安装到当前项目环境

**`pyproject.toml`、`uv.lock` 与当前 Python 环境已安装依赖的关系**
如果 `pyproject.toml`、`uv.lock` 都有声明依赖 A，但版本不兼容；当前 Python 环境也有 A，版本与前两个也不兼容，此时会发生什么？应该怎么解决这种状态。
- 首先不建议直接修改 `pyproject.toml` 文件，而是应该使用 `uv add`、`uv remove` 等命令去统一管理当前环境的依赖。
- 其次，如果真的出现了这种情况，我们应该按照如下原则处理
    - 如果想要依照 `uv.lock` 中的版本，执行 `uv sync` 即可将当前环境和 `pyproject.toml` 中的版本进行统一
    - 如果想要指定版本，则应该通过 `uv add xxx` 来更新这三个地方的依赖

**`uv add` 会更新 `uv.lock` 吗？如果会，`uv lock` 有什么用**
会更新 `uv.lock`，`uv lock` 命令主要用于手动生成或更新锁文件。

**lock 和 sync 是自动执行的**
当 `uv run` 之类的命令运行时，会自动 `sync` 并 `lock`。
在 Python 版本管理中我们也有看到，`uv run` 之前也会同步更新 Python 版本到符合要求的状态。

> [**不建议同时使用 `uv.lock` 和 `requirements.txt`**](https://docs.astral.sh/uv/concepts/projects/sync/#exporting-the-lockfile)

## 项目管理
```shell
# 在当前文件夹下新建项目，项目名就是当前的文件夹名
uv init
# 新建项目（新建文件夹，然后在文件夹下创建项目文件，项目下有 `main.py`）
uv init demo-app
# 新建项目(类似上面，只不过 `main.py` 没了，结构成了下面这样)
uv init --package demo-pkg
demo-app/
├── README.md
├── .python-version
├── pyproject.toml
└── src
    └── demo_app
        └── __init__.py
```

项目内会包含几个文件
- `.python-version` 前面已经说过了
- `pyproject.toml` 为项目信息描述文件
- `uv.lock` 刚生成时没有，但安装依赖后就会有。通常来说不需要太关注 `uv.lock`，它会被自动创建和更新。

**`pyproject.toml`**
一个常规的配置如下，它只说明了项目信息、依赖、工具参数。
```toml
[project]
name = "python-scripts"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "aiofiles==24.1.0",
    "alibabacloud-dysmsapi20170525==2.0.24",
    "alibabacloud-tea-openapi==0.3.12",
    "aliyun-python-sdk-alidns==3.0.7",
    "aliyun-python-sdk-core==2.15.0"
]

[[tool.uv.index]]
url = "https://mirrors.aliyun.com/pypi/simple/"
```

更多配置参见[手册](https://docs.astral.sh/uv/concepts/projects/config/)，有一点值得注意的是它可以定义一个 `entrypoint`，可以通过 `uv run` 来执行。
例如有了如下定义，`uv run hello` 就会执行 `example:hello`
```toml
[project.scripts]
hello = "example:hello"
```

> 有关 `uv index` 的更多配置，参考[手册](https://docs.astral.sh/uv/concepts/indexes/)

## `uv run`
`uv run` 就是一个增强版的 python 命令。
- `uv run main.py`
    - 如果当前目录不是 uv 项目，则直接用 `uv` 生效的环境运行 `main.py`
    - 如果当前目录是 uv 项目，则会自动安装依赖然后运行 `main.py`
- `uv run --with requests demo.py`
    - 这是声明运行 `demo.py` 时临时安装 `requests` 依赖。
    > 该临时依赖在命令执行完毕后会自动清理

**创建独立脚本**
`uv run` 一个很强的功能是可以支持在单个脚本中声明依赖、python 版本等，如下。
```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# [[tool.uv.index]]
# url = "https://example.com/simple"
# ///

import requests
from rich.pretty import pprint

resp = requests.get("https://peps.python.org/api/peps.json")
data = resp.json()
pprint([(k, v["title"]) for k, v in data.items()][:10])
```

## `uv tool` 与 `uvx`
 `uv tool` 用来执行之前通过 `python install` 安装的工具。不同的是，`python install` 后是长久地安装工具（会安装后加入 PATH），而 `uv tool` 把工具安装到 `uv` 缓存中，不会对宿主机产生影响。
 这在只需要执行一两次某些工具时非常有用。
 `uvx` 只是 `uv tool run` 命令的别名。

```shell
# 临时执行 ruff 命令
uvx ruff
# 如下等效
uv tool run ruff
# 临时执行兼容 Python3.10 的 ruff
uvx --python 3.10 ruff
# 如果需要经常执行 ruff，也可以安装
uv tool install ruff
# 还可以升级 ruff
uv tool upgrade ruff
```

## 实践

### 新项目如何用 `uv` 管理
```shell
# 创建项目
uv init project-name
# 安装依赖（使用国内源）
uv add requests --default-index https://mirrors.aliyun.com/pypi/simple/
# 运行某个脚本
uv run xxx.py
# 锁定版本（提交项目时使用）
uv lock
# 同步依赖（项目拉下来时使用）
uv sync
```

### 老项目如何引入 `uv`
```shell
# 初始化项目
uv init
# 安装依赖
uv add -r requirements.txt --default-index https://mirrors.aliyun.com/pypi/simple/
# 后面的一样
```
