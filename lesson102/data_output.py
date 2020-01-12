#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 17:49
# @Author  : tanxw
# @Desc 数据输出

"""
三个格式，六种占位符
-----------------------------------------
语法格式:
		格式一:
		print(变量)
		格式二:
		print(“格式化字符串” % 变量)
		格式三:
		print(“格式化字符串” %  (变量...))
-----------------------------------------
输出占位符
%s       字符串
%d       整数
%nd      整数,数字设置n个位数,不足前面补空白
%f       浮点数
%0.nf    设置n个小数位数,四舍五入
%%       输出%
"""
print("hello,world")

name = "devintam"
age = 31
height = 1.68
question = "你有对象吗？"
# 示例
# 格式化字符串，如需使用百分比（%）需要转化，如示例2，示例4
# 输出的数据中包变量，需要格式化字符串，示例
# 单变量与多变量使用
print("我的网名是:%s,年龄是:%8d,身高是:%.1f米" % (name, age, height))
print("我的网名是:%s,年龄是:%8d,身高是:%.1f米,我有20%%的体脂" % (name, age, height))
print("我的网名是:%s,年龄是:%8d,身高是:%.1f米,%s" % (name, age, height, question))
print("我有20%的体脂")
print("我的网名是:%s", name)
print("我的网名是:name")