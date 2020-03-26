FROM centos:7
MAINTAINER txtxw

# 更新镜像源，国内加速下载
RUN yum install -y epel-release && \
    yum makecache && \
    yum -y install gcc gcc-c++ make patch gdbm-devel openssl-devel \
        sqlite-devel readline-devel zlib-devel bzip2-devel pcre-devel gd-devel \
        ncurses xz libffi-devel iproute net-tools telnet wget curl

COPY requirements.txt  $HOME/requirements.txt

# pyenv环境配置
RUN yum -y install git && \
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile && \
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile && \
    source ~/.bash_profile && \
    v=3.7.7;wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P $(pyenv root)/cache/;pyenv install $v && \
    pyenv global $v
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

RUN source ~/.bash_profile  && \
    v=3.7.7 && \
    wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P $(pyenv root)/cache/ && \
    pyenv install $v && \
    pyenv global $v


# pip环境配置及依赖库安装
RUN mkdir ~/.pip && \
    echo '[global]' >> ~/.pip/pip.conf && \
    echo 'index-url=https://mirrors.aliyun.com/pypi/simple/' >> ~/.pip/pip.conf && \
    echo 'trusted-host=mirrors.aliyun.com' >> ~/.pip/pip.conf && \
    $HOME/.pyenv/shims/pip install --upgrade pip && \
    $HOME/.pyenv/shims/pip install -r requirements.txt

# 安装uwsgi依赖库 - 一般windows环境开发不涉及
RUN $HOME/.pyenv/shims/pip install uwsgi

# 安装nginx服务 使用搜狐镜像源
RUN wget http://mirrors.sohu.com/nginx/nginx-1.17.9.tar.gz && \
    tar zxf nginx-1.17.9.tar.gz && \
    cd nginx-1.17.9 && \
    ./configure --prefix=/usr/local/nginx \
    --with-http_ssl_module \
    --with-http_stub_status_module && \
    make -j 4 && make install && \
    rm -rf /usr/local/nginx/html/* && \
    echo "ok" >> /usr/local/nginx/html/status.html && \
    cd / && rm -rf nginx-1.17.9* && \
    ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 创建目录
RUN mkdir -p /python/web_station/log

# 拷贝项目
COPY nginx.conf /usr/local/nginx/conf/nginx.conf
COPY site_demo-1.0.tar.gz /python/web_station

RUN cd /python/web_station && \
    tar -xvf site_demo-1.0.tar.gz && \
    mv site_demo-1.0 site_demo

#工作目录
WORKDIR /python/web_station/site_demo


RUN sed -i 's/\r//' start.sh && \
    sed -i 's/\r//' stop.sh

# 生成数据迁移文件，创建表
#RUN $HOME/.pyenv/shims/python3.7 manage.py makemigrations && \
#    $HOME/.pyenv/shims/python3.7 manage.py migrate

# 暴露端口
EXPOSE 80
EXPOSE 8000

RUN pwd && \
    ls -a

# 执行脚本，运行服务
RUN /bin/bash start.sh
#ENTRYPOINT ["/bin/bash","start.sh"]

