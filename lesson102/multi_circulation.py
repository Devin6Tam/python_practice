#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 23:21
# @Author  : tanxw
# @Desc    : 多个循环嵌套使用

j = 1
while j <= 3:
    i = 0
    while i < 3:
        i += 1
    j += 1
print(j)