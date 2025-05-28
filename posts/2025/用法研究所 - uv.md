---
created_at: 2025-05-27 12:00:00
updated_at: 2025-05-27 12:00:00
title: 用法研究所 - uv
slug: usage-research-uv
categories:
  - 工具
tags:
  - "#uv"
  - "#工具"
  - "#Python"
---
## What and Why
`uv` 是由 [Astral](https://astral.sh/) 开发的 Python 工具。在一定程度上是可以取代 `pip`、`poetry`、`pyenv`、`twine`、`virtualenv` 等工具，主要用于做 Python 依赖管理和 Python 版本管理。通过 uv 命令可以完成从运行单个 Python 脚本、项目依赖管理（依赖声明和版本锁定）、虚拟环境管理等几乎所有维护 Python 项目需要的功能。
之前的工具都只负责部分功能，如 `pyenv` 负责系统上的 Python 版本管理；`virtualenv` 负责虚拟 Python 环境的创建；`pip` 负责依赖管理；`uv` 实现了所有这些功能。当然 `poetry` 也实现了这些功能，但 `uv` 说它比 `poetry` 更快。

> **为什么 uv 更快？**
用 Rust 重写了包解析器；在包管理上完全脱离 Python 本身工具链，甚至不会启动 Python，在 Rust 层面处理问题；用了 Rust 相比 Python 就有了并发优势（Python 有 GIL 限制）。相比之下，像 `poetry` 这样的工具仍基于 Python 运行，受限于解释器启动时间、单线程执行等因素，会比较慢。

> **注意事项**
`uv` 并不等同于 `pyenv`（用于管理系统中的多个 Python 版本）或 `twine`（用于将包发布到 PyPI），这些功能目前还不在 uv 的职责范围内。`uv` 只能管理通过 `uv run` 运行时使用的 Python 版本。
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
# 在当前目录下创建 .python-version 并将 3.12 写入其中
uv python pin 3.12
# 展示当前 pin 的 Python 版本
uv python pin

# 使用 uv python find 规则找到的 Python 版本创建虚拟环境
uv venv

# 以当前版本的 Python 运行 main.py
uv run main.py
```

**确定 Python 版本 [ref](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version)**
我们用 uv run 运行脚本时，使用 uv add 安装依赖时，都需要用到 Python 环境，uv 按照如下规则确定使用哪个版本的 Python 环境。
- 当前目录下的 .python-version 文件指定的版本
- 父目录（不超过当前项目目录）下的 .python-version 文件指定的版本
- 用户目录下的 .python-version 文件指定的版本
- 如果都没有，则不指定，使用当前系统中生效的 Python 版本

**发现 Python 版本 [ref](https://docs.astral.sh/uv/concepts/python-versions/#discovery-of-python-versions)**
在确定了 Python 版本后，uv 按照如下规则搜索符合版本的执行环境
- 首先尝试虚拟环境的发现规则
    - 优先尝试 VIRTUAL_ENV 变量指定的虚拟环境
    - 其次尝试 CONDA_PREFIX 指定的虚拟环境
    - 最后尝试当前目录下的 .venv 或父目录下的 .venv 环境
- 然后尝试自己的发现规则
    - 首先搜索 uv 自己的 Python 安装目录下的版本
    - 其次检查系统中符合要求的 Python 版本

uv python find 得到的结果就是按照上述规则找到的第一个符合要求的 Python 版本路径。如果我们使用 uv python pin 改变当前目录下的 .python-version 文件所记录的版本，会发现 uv python find 得到的结果已经更新了。**你可能会有疑问，之前创建的 venv 还是旧版本，uv run 会发生什么，答案是执行 uv run 时，uv 会将就得 venv 移除，创建符合新版本的 venv**。下面的例子有展示
```shell
# 固定 3.10 版本
zouguodong@MacBook-Pro-2 demo % uv python pin 3.10
Pinned `.python-version` to `3.10`

# 创建 3.10 版本的虚拟环境
zouguodong@MacBook-Pro-2 demo % uv venv
Using CPython 3.10.0 interpreter at: /Users/zouguodong/.pyenv/versions/3.10.0/bin/python3.10
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate

# 查看 uv python find 生效的是 3.10 版本
zouguodong@MacBook-Pro-2 demo % uv python find
/Users/zouguodong/.pyenv/versions/3.10.0/bin/python3.10

# 查看 uv run 运行的也是 3.10 版本
zouguodong@MacBook-Pro-2 demo % uv run -- python --version;
Python 3.10.0

# 重新固定为 3.12 版本
zouguodong@MacBook-Pro-2 demo % uv python pin 3.12
Updated `.python-version` from `3.10` -> `3.12`

# 查看 uv python find 生效的事 3.12 版本
zouguodong@MacBook-Pro-2 demo % uv python find
/opt/homebrew/opt/python@3.12/bin/python3.12

# uv run 自动重建了新的虚拟环境，
zouguodong@MacBook-Pro-2 demo % uv run -- python --version;
Using CPython 3.12.10 interpreter at: /opt/homebrew/opt/python@3.12/bin/python3.12
Removed virtual environment at: .venv
Creating virtual environment at: .venv
Python 3.12.10
```

**pyproject.toml 的 requires-python 的作用**
.python-version 约束了当前文件夹下的固定的 Python 版本，而 pyproject.toml 下的 requires-python 约束了当前项目(其实也是当前文件夹)的 Python 版本。我们应该保持二者兼容，当不兼容时，执行 uv sync 或 uv run 等命令时会报错，如下
```shell
$ uv run -- python -c "import sys; print(sys.executable)";
Using CPython 3.10.0 interpreter at: /Users/zouguodong/.pyenv/versions/3.10.0/bin/python3.10
error: The Python request from `.python-version` resolved to Python 3.10.0, which is incompatible with the project's Python requirement: `>3.10`. Use `uv python pin` to update the `.python-version` file to a compatible version.
```
## 依赖管理


## 项目管理

## uv run

## uv tool 与 uvx

## 实践
### 新项目如何用 uv 管理

### 老项目如何引入 uv

## 自问自答
- uv add 安装的依赖位置在哪里？
- 一个 uv 项目中同时存在 requirements.txt 和 pyproject.toml 是最佳实践吗？