#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 16:48
# @Author  : tanxw

tt = (1, 2, 3)

a, b, c = tt
print("a=%d,b=%d,c=%d" % (a, b, c))

# 从元组里头获取n个元素 n > 元组的长度时，默认元组的数据
print(tt[:1])

# 当元组中只有一个值的时候需要加上逗号
ttt = ("a",)

# 取数据在元组中的索引值
print(tt.index(3))

# 元组的统计方法
print(tt.count(3))

# 不能对元组中的数据进行修改, 列表中的可以被修改
bb = [1, 2, 3]
print(tt * 3)
print(bb * 3)

# 列表中的值发生了变化,但是内存中的地址没有变化,说明列表是可变的数据类型
print(id(bb))
bb += bb
print(bb)
print(id(bb))

# 值改变了,内存地址发生了变化,说明元组是不可变的数据类型
print(id(tt))
tt += tt
print(tt)
print(id(tt))


print(id(ttt))





