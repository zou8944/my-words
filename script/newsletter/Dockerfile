FROM registry.cn-beijing.aliyuncs.com/ergedd/python:3.10-slim-bookworm

# 安装必要的系统依赖
RUN sed -i 's|http://deb.debian.org|http://mirrors.aliyun.com|g' /etc/apt/sources.list.d/debian.sources; \
  sed -i 's|http://security.debian.org|http://mirrors.aliyun.com|g' /etc/apt/sources.list.d/debian.sources; \
  apt-get update && apt-get install -y curl build-essential libpq-dev tzdata && \
  ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
  echo "Asia/Shanghai" > /etc/timezone && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 复制依赖文件
COPY pyproject.toml uv.lock /app/

# 安装 uv 和 Python 依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple uv
RUN uv venv && uv sync

# 复制源代码
COPY . .

# 创建日志目录
RUN mkdir -p /app/logs

# 设置环境变量
ENV PYTHONPATH=/app
ENV TZ=Asia/Shanghai

# 运行定时任务
CMD ["uv", "run", "python", "main.py"]
