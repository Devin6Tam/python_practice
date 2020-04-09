#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/6 19:43
# @Author  : tanxw

import re

# str = 'python0008888ooo'
# print(str[0].upper()+str[1:])
#
# for i in range(3):
#     print(2, end=',')
#
# print(len("hello world"[100:]))
#
# print(int(2.6))
#
# alist=[0, 1, 2]
# for i in alist:
#     print(i+1)
#
#
# print(str.count('o'))
# print(str.find('aa'))
# print(str.index('aa'))

#
# def change(a):
#     a = [3, 4, 5]
#
# def no_change(a):
#     a.append(4)
#
# a = [1, 2, 3]
# change(a)
# print(a)
#
# no_change(a)
# print(a)

# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print Parent.x, Child1.x, Child2.x
# Child1.x = 2
# print Parent.x, Child1.x, Child2.x
# Parent.x = 3
# print Parent.x, Child1.x, Child2.x


# 学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示

# score = 59
# if score >= 90:
#     # 学习成绩>=90分
#     print("A")
# elif score >= 60 & score < 90:
#     # 60 - 89分之间
#     print("B")
# else:
#     #　60分以下
#     print("C")


import re
s = """se234 1987-02-09 07:30:00

1987-02-10 07:25:00"""
data = re.findall("\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", s)
for i in data:
    print(i)

data = re.match(r"(.[0-9]{4})+", s)
print(data)