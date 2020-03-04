#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 11:01
# @Author  : tanxw
# @Desc    : 中间件使用 - 系统异常定义

from django.http import HttpResponse

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

class SystemException(MiddlewareMixin):
    def process_exception(request, response, exception):
        return HttpResponse('中间件已捕捉异常：' + str(exception))