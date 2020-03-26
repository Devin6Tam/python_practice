#!/bin/bash

source ~/.bash_profile
$HOME/.pyenv/shims/uwsgi --ini uwsgi.ini & /usr/local/nginx/sbin/nginx