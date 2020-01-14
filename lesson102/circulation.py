#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 23:29
# @Author  : tanxw
# @Desc    : 循环使用介绍

"""
第一种循环，需要人工干预break，适用于轮询;
第二、三种循环，执行完成后直接退出
"""


i = 1
while True:
    if i < 10:
        print("我开始吃第%d碗饭" % i)
    else:
        break
    i += 1

j = 1
while j < 10:
    print("剩下%d碗饭" % (9 - j))
    j += 1

for k in range(1, 10):
    print("")
