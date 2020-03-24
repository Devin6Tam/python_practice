FROM centos:7
MAINTAINER txtxw
RUN mkdir -p /python/web_station/{log,site-demo}
WORKDIR /python/web_station/

RUN yum install -y epel-release && \
    yum makecache && \
    yum -y install gcc gcc-c++ make patch gdbm-devel openssl-devel \
        sqlite-devel readline-devel zlib-devel bzip2-devel pcre-devel gd-devel \
        ncurses xz libffi-devel iproute net-tools telnet wget curl

RUN yum -y install git && \
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile && \
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile && \
    source ~/.bash_profile  && \
    v=3.7.7;wget http://mirrors.sohu.com/python/$v/Python-$v.tar.xz -P $(pyenv root)/cache/;pyenv install $v && \
    pyenv global $v

RUN mkdir ~/.pip && \
    echo '[global]' >> ~/.pip/pip.conf && \
    echo 'index-url=https://mirrors.aliyun.com/pypi/simple/' >> ~/.pip/pip.conf && \
    echo 'trusted-host=mirrors.aliyun.com' >> ~/.pip/pip.conf && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

RUN wget http://nginx.org/download/nginx-1.17.9.tar.gz && \
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


COPY uwsgi.ini /python/web_station/uwsgi.ini
COPY nginx.conf /usr/local/nginx/conf/nginx.conf
COPY * /python/web_station/site-demo

RUN python /python/web_station/site-demo/manage.py makemigrations && \
    python /python/web_station/site-demo/manage.py migrate


EXPOSE 8000
ENTRYPOINT uwsgi --ini /python/web_station/uwsgi.ini & /usr/local/nginx/sbin/nginx

