#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 9:05
# @Author  : tanxw
# @Desc    : 字典的其他应用场景

card_list = [
    {'name': "马化腾",
     'qq': 100,
     'phone': 1234567},
    {'name': "张小龙",
     'qq': 100100,
     'phone': 1513132157}
]
find_name = "小龙"
for card_info in card_list:
    print(card_info)
    if card_info['name'].__contains__(find_name):
        print("找到了%s" % find_name)
        break
    else:
        print("没有找到")
print("循环结束")



# 全局字典 sys.modules
import sys
print(sys.modules.keys())
print(sys.modules.values())
print(sys.modules['os'])

# 实现导入模块的过滤
d = sys.modules.copy()
import copy, string
print(zip(set(sys.modules) - set(d)))