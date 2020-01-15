#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 0:33
# @Author  : tanxw

a = [[1, 2, 3, 4], [1, 3, 5, 7], [2, 4, 6, 8]]
b = ["a", "b", "c", "d", "e", "f", "g"]

# 1. 列表的增加方法
# l.insert(索引值, 数据)
# 在指定的位置插入数据
a.insert(1, [3, 6, 9, 12])
# 在列表的末尾添加数据
# a.append("我爱中国")
# extend方法能够的数据为 可以使用for 循环遍历的数据
a.extend(b)

for c in a:
    print(c)

# 2.列表的修改
# 列表[索引] = 数据
# l[2] = 11  # 修改指定位置的数据

# 3. 列表的删除
# l.remove(数据)
# l.remove("python")  # 删除第一个出现的数据
# l.pop(4)  # 删除指定索引的数据
# l.pop()  # 删除列表末尾的数据
# l.clear()  # 清空列表
# del l[2]  # 删除指定位置的数据

# 4.列表的统计
print(len(a))  # 统计列表的长度,列表中有多少条数据
print(a.count('a'))  # 统计数据在列表中出现的次数

# 5. 列表的排序
# l.sort()  # 升序排序
# l.sort(reverse=True)  # 降序排序
# l.reverse()  # 列表的反转
#
print(a.index("a"))  # 查找的数据在列表中第一次出现的索引
print("g" not in a)  # 数据不在列表中