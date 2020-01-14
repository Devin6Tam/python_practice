#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 23:23
# @Author  : tanxw
# @Desc    : 循环加法

"""
案例: 数字累计求和
范围: 100以内所有数字(包含一百)
"""

"""
分析:
范围1-100 
a = a + b
使用循环来进行反复求和操作
"""
a = 0
b = 1
while b <= 100:
    a += b
    b += 1
print("1到100的累加求和结果是:%s" % a)