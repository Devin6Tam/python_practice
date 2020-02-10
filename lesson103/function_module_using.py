#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 14:32
# @Author  : tanxw
# @Desc    : 函数的模块使用

name = "打印测试"

def print_line(char, times):
    print(char * times)

def print_lines(char, times):
    for i in range(5):
        print_line(char, times)