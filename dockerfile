FROM python:3.8

# 维护者信息
LABEL maintainer="uzdz"
LABEL maintainer_email="devmen@163.com"

# 设置工作目录
WORKDIR /app
COPY *.py requirements.txt /app/

# 安装 Python 依赖
RUN pip install -r requirements.txt

# 默认启动参数
ENV BOT_COOKIE=
ENV BOT_EXCLUDE_DATE=
ENV BOT_OS_URLS=
ENV BOT_CYCLE_TIME=
ENV BOT_DING_WEBHOOK=
ENV BOT_LARK_WEBHOOK=

# 添加一个脚本
COPY ["entrypoint.sh", "/app/entrypoint.sh"]
RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/robot.py
RUN chmod +x /app/feishu.py
RUN chmod +x /app/dingding.py

# 使用脚本作为启动命令
ENTRYPOINT ["/app/entrypoint.sh"]