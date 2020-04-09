#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 22:48
# @Author  : tanxw
# @Desc    : 使用字典实现switch语句

from __future__ import division

def calcator(x, y, operator):
    result = {
        "+": x + y,
        "-": x - y,
        "*": x * y,
        "/": x / y
    }
    print(result.get(operator))
    return result.get(operator)

if __name__ == '__main__':
    calcator(10, 18, '*')