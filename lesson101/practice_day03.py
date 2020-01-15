#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 17:51
# @Author  : tanxw

"""
6、编写代码设计简易计算器，用户通过3次输入，可以进行两个整数的加减乘除运算并输出结果。

7、闰年判断程序: if判断、格式化输出、运算符
要求:
输入一个有效的年份，判断是不是闰年；
如果是闰年，则打印“***年是闰年”；否则打印“***年不是闰年”；
如输入"2017"，将打印“2017年不是闰年”
"""

num_a = int(input("请输入一个整数："))
operator = input("请输入一个运算符：")
num_b = int(input("请输入一个整数："))

if operator == "+":
    print("%d%s%d=%d" % (num_a, operator, num_b, num_a + num_b))
elif operator == "-":
    print("%d%s%d=%d" % (num_a, operator, num_b, num_a - num_b))
elif operator == "*":
    print("%d%s%d=%d" % (num_a, operator, num_b, num_a * num_b))
elif operator == "/":
    if num_b == 0:
        print("被除数不能为0")
    else:
        print("%d%s%d=%d" % (num_a, operator, num_b, num_a / num_b))
else:
    print("输入运算符错误！")

year = int(input("请输入一个有效的年份:"))

if (year % 4 == 0 & year % 100 != 0) or year % 400 == 0:
    print("%d是润年" % year)
else:
    print("%d不是润年" % year)
