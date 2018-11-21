FROM python:3.7.1

MAINTAINER hanmeng hanmeng@bupt.edu.cn

COPY . /app

WORKDIR /app

ENTRYPOINT ["python", "./execution_exe.py"]

