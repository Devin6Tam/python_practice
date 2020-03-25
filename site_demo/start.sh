#!/bin/bash

$HOME/.pyenv/shims/uwsgi --ini site_demo/uwsgi.ini & /usr/local/nginx/sbin/nginx