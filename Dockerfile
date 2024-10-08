# 使用 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录下的所有文件到工作目录
COPY . /app

# 安装所需的依赖
RUN pip install --no-cache-dir flask gunicorn

# 设置环境变量，指定 Flask 应用入口文件
ENV FLASK_APP=app.py

EXPOSE 5500

# 声明启动时执行的命令
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5500", "app:app"]
