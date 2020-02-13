#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 14:32
# @Author  : tanxw
# @Desc    : 函数的模块使用

import random
# 导入模块，并设置别名
# import reprlib as repb

name = "打印测试"

def print_line(char, times):
    print(char * times)

def print_lines(char, times):
    for i in range(5):
        print_line(char, times)

def get_randow_pass(default= False):
    randow_str = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%$#@?<>"
    if default:
        return "changeit"
    pass_str = ""
    for k in range(1, 12):
        index = random.randint(0, len(randow_str)-1)
        pass_str += randow_str[index]
    print(pass_str)
    return pass_str

get_randow_pass()