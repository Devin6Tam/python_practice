#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 14:02
# @Author  : tanxw
# @Desc    : 函数使用

# 从当前目录导入模块
from . import function_module_using
# 从指定目录导入模块
# from lesson103 import function_module_using

"""
def 函数名():
    函数封装的代码
    ...
"""

# 1. 函数定义及使用
def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")

# 单步执行F7是进入到函数内部去执行
say_hello()
# if __name__ == '__main__':
#     say_hello()

# 2. 两数相加
def num_plus():
    num1 = 10
    num2 = 5
    ret = num1 + num2
    print("%d + %d = %d" % (num1, num2, ret))

num_plus()

# 3. 函数带参数使用
# 函数的参数,增加函数的通用性.
# 形式参数,用来接收参数.
# 函数的参数在函数的内部当做变量使用
def num_plus_c(num1, num2):
    ret = num1 + num2
    print("num_plus_c")
    print("%d + %d = %d" % (num1, num2, ret))

num_plus_c(10, 15)

# 4. 函数嵌套使用

def num_plus_d(num1, num2):
    num_plus_c(num1, num2)
    print("num_plus_d")
    return num1 + num2

print(num_plus_d(100, 125))

print(function_module_using.name)
print(function_module_using.print_lines("-", 30))
