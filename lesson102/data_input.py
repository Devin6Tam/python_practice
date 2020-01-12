#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 17:46
# @Author  : tanxw
# @Desc    : 数据输入

"""
两种格式
-----------------------------------------
▲语法格式:
格式一: input()  # 不常用
格式二: input(“提示信息”)

▲语法格式:
格式: 变量 = input(......)
"""
# print() # 输出打印 输入 input()

# 输入东西给程序使用
# input()

# 使用input得到的数据都是str字符串类型
# name = input("请您输入一个名字:")
# print(name)

# 计算两个数的和 用户去输入
a = input("请输入第一个数字")
b = input("请输入第二数字")
c = a + b
print(type(c))
print(c)

# print(int(a) + int(b))
# print(float(a) + float(b))
# 非零为True,True的值为1
# a,b 为字符串，怎么求和都为2
print(bool(a) + bool(b))

