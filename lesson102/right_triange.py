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