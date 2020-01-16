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


