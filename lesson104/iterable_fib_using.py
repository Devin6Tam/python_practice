#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 23:05
# @Author  : tanxw
# @Desc    : 斐波那契数列迭代器

# 0 1 1 2 3 5 8 13....

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