#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 20:59
# @Author  : tanxw

from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页的处理方法
    url(r'^$', views.index),

    # 书籍视图，路径可以加book,如访问详情页 book/detail/1,方法 get_book_detail
    url(r'^add/$', views.add, name='add'),
    # 详情页
    url(r'^detail/([0-9]+)/$', views.detail, name='detail'),
    url(r'^edit/([0-9]+)/$', views.edit, name='edit'),
    url(r'^delete/([0-9]+)/$', views.delete, name='delete'),

]
