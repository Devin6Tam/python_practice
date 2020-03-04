#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 12:48
# @Author  : tanxw
# @Desc    : 装饰器使用

"""
功能介绍
1.引入日志
2.函数执行时间统计
3.执行函数前预备处理
4.执行函数后清理功能
5.权限校验等场景
6.缓存

示例使用说明：
def aaaaa(fn):
    def bbbbb():   # 这里可以带参数 def bbbbb(a,b)
        return fn的结果进行处理
    return bbbbb
"""


# 定义函数：完成包裹数据
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

# 定义函数：完成包裹数据
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makeBold
def test1():
    return "hello world-1"

@makeItalic
def test2():
    return "hello world-2"

@makeBold
@makeItalic
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())


# 无参数装饰
# from time import ctime, sleep
#
# def timefun(func):
#     def wrapped_func():
#         print("%s called at %s" % (func.__name__, ctime()))
#         func()
#     return wrapped_func
#
# @timefun
# def foo():
#     print("I am foo")
#
# foo()
# sleep(2)
# foo()

# 有参数装饰
# from time import ctime, sleep
#
# def timefun(func):
#     def wrapped_func(a, b):
#         print("%s called at %s" % (func.__name__, ctime()))
#         print(a, b)
#         func(a, b)
#     return wrapped_func
#
# @timefun
# def foo(a, b):
#     print(a+b)
#
# foo(10, 20)
# sleep(2)
# foo(20, 30)


# 带不定长参数的装饰函数
# from time import ctime, sleep
#
# def timefun(func):
#     def wrapped_func(a, b, c, d):
#         print("%s called at %s" % (func.__name__, ctime()))
#         return func(a, b, c, d)
#     return wrapped_func
#
# @timefun
# def foo(a, b, c, d):
#     print(a+b+c+d)
#
# @timefun
# def getInfo(a, b, c, d):
#     return '----hahah---'
#
# foo(10, 20, 30, 40)
# sleep(2)
# foo(20, 30, 50, 70)
# print(getInfo(20, 30, 50, 70))

from time import ctime, sleep

def timefun_arg(pre="hello"):
    def timefun(func):
        # 在函数的内部再定义一个函数,并且这个函数用到了外部函数的局部变量,那么将这个函数以及用到的一些变量
        # 称之为闭包
        def wrapped_func():
            print("%s called at %s %s" % (func.__name__, ctime(), pre))
            return func()
        #闭包结果
        return wrapped_func
    return timefun

@timefun_arg("practice101")
def foo():
    print("I am foo")

@timefun_arg("practice102")
def too():
    print("I am too")


foo()
sleep(2)
foo()

too()
sleep(2)
too()


# 如何对有用不定长参数的函数进行装饰
# def a(c):
#     def b(*args, **kwargs):
#         print("这里是中华人民共和国的:", end="")
#         c(*args, **kwargs) # 原demo1()
#         print("hello,武汉加油")
#     return b # c()

# # 对带有返回值的参数进行装饰
def a(c):
    def b(*args, **kwargs):
        # print("这里是中华人民共和国的:",end="")
        return c(*args, **kwargs) # 原demo1()
        # print("hello,武汉加油")
    return b # c()

@a
def demo1(name):
    print("湖南省的%s" % name)
    return "hello,热干面加油"


test1 = demo1("岳阳市")
print(test1)