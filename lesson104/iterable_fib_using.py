#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 23:05
# @Author  : tanxw
# @Desc    : 斐波那契数列迭代器

# 0 1 1 2 3 5 8 13....
# 迭代类
class Fib(object):
    def __init__(self, n):
        self.n = n
        # 去记录当前位置的变量
        self.current = 0
        # 第一个数
        self.num1 = 0
        # 第二个数
        self.num2 = 1

    def __iter__(self):
        return FibIterator(self.n)

# 迭代器
class FibIterator(object):
    """斐波那契数列迭代器"""
    def __init__(self, n):
        self.n = n
        # 去记录当前位置的变量
        self.current = 0
        # 第一个数
        self.num1 = 0
        # 第二个数
        self.num2 = 1

    def __next__(self):
        if self.current < self.n:
            num = self.num1
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            self.current += 1
            return num
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    fib = FibIterator(100)
    for num in fib:
        print(num, end=" ")
    print("\n===========================")
    f = Fib(30)
    for num in f:
        print(num, end=" ")


"""
迭代器与生成器的区别
迭代器是一个定义了next方法和iter方法,并且结果返回本身的类。

生成器的基本功能就是用来创建迭代器，形式上类似于普通定义的函数，拥有yield关键字。
yield关键字不同于return，return后会退出相关代码，但yield则会保留退出，下次继续。

生成器能做到迭代器能做的所有事,而且因为自动创建了 iter()和 next()方法,生成器显得特别简洁,而且
生成器也是高效的，使用生成器表达式取代列表解析可以同时节省内存。除了创建和保存程序状态的自动方法,当
发生器终结时,还会自动抛出 StopIteration 异常。


其他知识点：
迭代器 （Iterator）： Python 中 for 循环实际操作的对象
可迭代对象 （Iterable）：可以直接作用于 for 循环的对象
生成器（generator）：迭代器的一种，只能用于迭代操作

string、list、dict、tuple等 都是 iterable（可迭代对象）
占用内存小，高效实用对比： generator > Iterator > Iterable

itertools 是Python的迭代器模块，标准化了一个快速，高效利用内存的核心工具集。
迭代器可分为：无穷迭代器，有穷迭代器，排列组合迭代器
"""