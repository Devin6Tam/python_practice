#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 11:55
# @Author  : tanxw
# @Desc    : 用列表实现 堆栈和队列

"""
堆栈和队列是数据结构中常用的数据结构，使用列表的append(),pop()
方法可以模拟这俩种数据结构；

1.堆栈是指最先进入堆栈的元素最后才输出，符合“后进先出”的原则。
2.队列是指最先进入队列的元素最早输出，符合“先进先出”的原则
"""
list = ["apple", "banana", "grape", "peach", "orange", "pear"]
list.append("kiwi")
print(list)
print("堆栈实现1-弹出的元素：%s" % list.pop())
print(list)


print("队列实现2-弹出的元素：%s" % list.pop(0))
print(list)


