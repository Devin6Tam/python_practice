#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/14 23:15
# @Author  : tanxw
# @Desc    : 直角三角形

"""
打印
*
**
***
****
*****
"""
for i in range(1, 6):
    row_data = ""
    for j in range(1, 6):
        if i >= j:
            row_data += "*"
    print(row_data)


# 4、使用while循环输出如下图形：（必须使用双重while循环实现）
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
h = 5

while h > 0:
    row_data = ""
    k = 1
    while k < 6:
        if k >= h:
            row_data += "* "
        else:
            row_data += " "
        k += 1
    h -= 1
    print(row_data)


