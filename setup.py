#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 11:41
# @Author  : tanxw
# @Desc    : 发布模块

from distutils.core import setup

setup(name="lesson103",  # 包名
      version="1.0",  # 版本
      description="python 练习",  # 描述信息
      long_description="python 模块发布练习",  # 完整描述信息
      author="tanxw",  # 作者
      author_email="txtxw@163.com",  # 作者邮箱
      url="https://github.com/Devin6Tam",  # 主页
      py_modules=["lesson103.function_module_using"])
