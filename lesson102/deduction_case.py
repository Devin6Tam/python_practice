#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 11:35
# @Author  : tanxw
# @Desc    : 推导式使用案例

ret = [(x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8]
print(ret)


# 元组推导结果，与下雷同；
ret_str = ""
for x in range(10):
    if x % 2 == 1:
        if x > 3:
            ret_str += ("(%d," % x)
            for y in range(10):
                if y > 7:
                    if y != 8:
                        ret_str += ("%d)\t" % y)
print(ret_str)
