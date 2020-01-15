#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 0:58
# @Author  : tanxw

abc = [4, 2, 1, 3, 5, 0, 8, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# for i, x in enumerate(abc):
#     if x == 1:
#         print(i, x)

# tt = (1, 2)
# x, y = tt
# print(x)
# print(y)

# 列表推导式
# [表达式 for 变量 in 集合]   [表达式 for 变量 in 集合 if 条件]
# ret = [i for i in range(10) if i % 2 == 0]
# print(ret)

# 获取固定值，索引
res = [(i, x) for i, x in enumerate(abc) if x == 5]
print(res)