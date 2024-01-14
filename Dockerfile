# 使用 Python 镜像作为基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装所需的依赖
RUN pip install --no-cache-dir flask

# 声明启动时执行的命令
CMD ["python", "main.py"]