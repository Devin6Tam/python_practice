#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 10:23
# @Author  : tanxw
# @Desc    : 条件判断使用

"""
if 条件:
    满足条件True,执行这里的代码
else: # 否则
    不满足条件False, 执行这里面的代码

两个数字,, 比较他的大小判断if,,打印出较大的那个数字
a = 5
b = 6
if a > b: # 如果 a 大于 b
    print(a) # 打印a
else: # 否则 a 小于等于 b
    print(b) # 打印b
"""


a = 10
b = 20
if a > b:
    print("a大于b")
elif a < b:
    print("a小于b")
else:
    print("a等于b")


"""
& | and  且
or  或
not 非
"""
if a > 0 & a > b:
    print("a大于0且大于b")
else:
    print("条件不成立")
if b > 0 or a > b:
    print("b大于0或a大于b")
else:
    print("条件不成立")

