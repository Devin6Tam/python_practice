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
    'age': 33,
}

# 统计键值对的数量
print(len(triangle))

# 取值
print(triangle['name'])
# 在取值的时候,指定的key不存在, 程序会报错
# print(triangle['name1'])

# 增加/修改  如果key存在，就更新键值对，如果key不存在，就新增键值对
triangle['name'] = '7-11'

# 如果合并的字典中有重复的key, 会覆盖原有的键
triangle.update(triangle_dict)
print(triangle)

# 删减项
# popitem 单独使用，默认删除字典中最后一项
triangle.popitem()
triangle.pop('name')

print(triangle)

# 清空字典
triangle_dict.clear()
print(triangle_dict)

# 迭代遍历字典
for k in triangle:
    print("%s-%s" % (k, triangle[k]))

for k, v in triangle.items():
    print(k, v)


print(triangle.items())
x, y = (1, 2)
