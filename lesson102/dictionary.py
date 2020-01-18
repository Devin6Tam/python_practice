#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/17 12:09
# @Author  : tanxw
# @Desc    : 字典定义及使用

# 字典是一个无序的对象集合,
# 索引值 是 键(key).`

triangle = {
    'name': 'twinkle',
    'age': 31,
    'gender': True,
    'height': 1.68,
    1: 'laowang',
    (1, 2): 'laowang',
}


triangle_dict = {
    'name': '帅帅',
    'age': 31,
}

# 取值
print(triangle['name'])
# 在取值的时候,指定的key不存在, 程序会报错
# print(triangle['name1'])

# 增加/修改
triangle['name'] = '7-11'


triangle.update(triangle_dict)
print(triangle)

triangle.popitem()
triangle.pop('name')

print(triangle)
