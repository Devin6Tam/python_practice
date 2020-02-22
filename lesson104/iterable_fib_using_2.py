#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 23:24
# @Author  : tanxw
# @Desc    : 生成器

def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1+num2
        current += 1
        yield num
    return 'done'

size = 100
F = fib(size)

for k in range(1, 101):
    print(next(F))

# 遍历超出100之后，打印就报错

"""
使用了yield关键字的函数就不是函数,而是生成器
作用:
1. 保存当前的运行状态(断点执行)
2. 将后面的值作为返回值返回, 可以理解为和return作用一样
"""