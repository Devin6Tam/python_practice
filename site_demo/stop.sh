#!/bin/bash

kill -9 $(ps -ef | grep uwsgi | awk '{print $2}')
/usr/local/nginx/sbin/nginx -s stop