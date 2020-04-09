#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 23:37
# @Author  : tanxw
# @Desc    : 序列使用

"""
序列是具有索引和切片能力的集合。
元组、列表和字符串具有通过索引访问某个具体的值，
或通过切片返回一段切片的能力，因此元组、列表和字符串都属于序列
"""

tuple = ("apple", "banana", "orange", "grape")
list = ("apple", "banana", "orange", "grape")
str = "apple"

print(tuple[:3])
print(tuple[3:])
print(tuple[1:-1])
print(tuple[:])

print(list[:3])
print(list[3:])
print(list[1:-1])
print(list[:])


print(str[:3])
print(str[3:])
print(str[1:-1])
print(str[:])
