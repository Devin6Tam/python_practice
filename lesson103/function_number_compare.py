#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 0:08
# @Author  : tanxw
# @Desc    : 使用函数进行数值比较，使用判断语句缩写形式

def comare_two_numbers(num1, num2):
    """俩个数值比较"""
    # 使用判断语句缩写
    # if num1 > num2:
    #     return num1
    # else:
    #     return num2
    return num1 if num1 > num2 else num2


def comare_three_numbers(num1, num2, num3):
    """三个数值比较"""

    #使用判断语句缩写形式
    # if num1 > num2:
    #     if num1 > num3:
    #         return num1
    #     else:
    #         return num3
    # else:
    #     if num2 > num3:
    #         return num2
    #     else:
    #         return num3
    return (num1 if num1 > num2 else num2) if(num1 if num1 > num2 else num2) > num3 else num3

print (comare_three_numbers(1, 9 , 4))
