#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 17:33
# @Author  : tanxw
# @Desc    : 练习

"""
1、设计一个程序，要求能输入一个值，然后赋值给age变量，判断age的大小，
如果大于等于18，则打印"已成年"，否则打印"未成年"。

2、编写代码，1-7七个数字，分别代表周一到周日，如果输入的数字是1-5之间，输出“工作日”
，如果输入的数字是6或7，输出“周末”，否则提示“输入错误”。
"""

age = int(input("请输入你的年龄："))
if age > 18:
    print("已成年")
else:
    print("未成年")

num = int(input("请输入[1-7]区间的数字："))
if num >= 1 & num <= 5:
    print("工作日")
elif num == 6 or num == 7:
    print("周末")
else:
    print("输入错误")