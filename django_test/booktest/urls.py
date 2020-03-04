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
    url(r'^detail/(?P<id>[0-9]+)/$', views.detail1, name='detail1'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit, name='edit'),
    # 正则表达式非命名组, 通过位置参数传递给视图
    url(r'^delete/([0-9]+)/$', views.delete, name='delete'),
    # 正则表达式命名组,通过关键字参数传递给视图
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete1, name='delete1'),

    url(r'^list/([0-9]+)/$', views.list, name='list'),
    url(r'^list1/(?P<pIndex>[0-9]+)/(?P<pSize>[0-9]+)/$', views.list1, name='list1'),

    # 上传页面
    url(r'^to_upload/$', views.to_upload, name='to_upload'),

    # 上传图片
    url(r'^upload$', views.upload, name='upload'),
]
