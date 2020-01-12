#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/11 18:47
# @Author  : tanxw

name = input("请输入姓名")
sex = input("请输入性别")
age = input("请输入年龄")
unit = input("请输入单位")
phone = input("请输入联系方式")


print("姓名：%s,性别：%s,年龄：%d,单位：%s,联系方式：%11d" % (name, sex, int(age), unit, int(phone)))