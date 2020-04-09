#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 14:50
# @Author  : tanxw
# @Desc    : generator 函数

# yield 的函数是一个生成器，需要通过next()方法来获取值

# 用法： 斐波那契数列

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
# 获取生成器
F = fib(size)

# 遍历从生成器获取每个生成的值
for k in range(1, 101):
    print(next(F))

# yield 与 return 语句的区别
def func(n):
    for i in range(n):
        return i

def func2(n):
    for i in range(n):
        yield i

"""
0  循环直接中断并返回0
<generator object func2 at 0x00000000038316D8>  生成器对象
0  第一个next 生成0
1  第二个next 生成1
"""
print(func(3))
c = func2(3)
print(c)
print(next(c))
print(next(c))


