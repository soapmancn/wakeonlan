# 使用 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装所需的依赖
RUN pip install --no-cache-dir flask

# 设置环境变量，指定 Flask 应用入口文件
ENV FLASK_APP=app.py

# 声明启动时执行的命令
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--without-threads"]
