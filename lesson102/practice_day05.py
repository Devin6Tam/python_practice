#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 0:17
# @Author  : tanxw

"""
3、求 1+2!+3!+...+20! 的和。

4、本金10000元存入银行，年利率是千分之三。
每过1年，将本金和利息相加作为新的本金。
计算5年后，获得的本金是多少？
"""

num = 20
i = num
ret = 1
while i >= 1:
    ret *= i
    i -= 1
print("%d的阶乘为:%d" % (num, ret))

repay_amount = 10000
year = 1
while year <= 5:
    repay_amount *= (1 + 0.003)
    year += 1

print("5年后,回款本息为：%d" % repay_amount)

