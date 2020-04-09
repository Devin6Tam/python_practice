#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/31 2:18
# @Author  : tanxw

import re

ret = re.match(r'[^a-c]', 'bc\n\bb\nddd')
if ret:
    print(ret.group())
else:
    print('没有匹配结果')