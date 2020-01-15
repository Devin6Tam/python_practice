#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 17:58
# @Author  : tanxw


"""
1、使用while循环计算1~100的累积和（包含1和100）,但要求跳过所有个位为3的数。
2、从键盘获取一个数字，然后计算它的阶乘，例如输入的是3，
那么即计算3!的结果，并输出
提示：
1！等于 1

2！等于 1*2
3！等于 1*2*3
n！等于 1*2*3*...*n
"""
k = 0
for j in range(1, 101):
    if j % 10 == 3:
        continue
    k += j
print("求和值：%d" % k)

num = int(input("请输入一个整数: "))
i = num
ret = 1
while i >= 1:
    ret *= i
    i -= 1
print("%d的阶乘为:%d" % (num, ret))
