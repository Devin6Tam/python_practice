FROM ubuntu:16.04

MAINTAINER Wilf

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	sqlite3

RUN	python3 -m pip install --upgrade pip && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default

# 创建工作路径
RUN mkdir -p /var/www

COPY site_demo-1.2.tar.gz /var/www

RUN cd /var/www && \
    tar -xvf site_demo-1.2.tar.gz && \
    mv site_demo-1.2 site_demo

# 指定容器启动时执行的命令都在/var/www/site_demo目录下执行
WORKDIR /var/www/site_demo

RUN pip install -r /home/docker/code/app/requirements.txt -i  https://pypi.tuna.tsinghua.edu.cn/simple some-package --no-cache-dir

EXPOSE 80

CMD ["/bin/bash","start.sh"]