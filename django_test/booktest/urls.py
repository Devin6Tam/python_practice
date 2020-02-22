#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 20:59
# @Author  : tanxw

from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页的处理方法
    url(r'^$', views.index)
]
