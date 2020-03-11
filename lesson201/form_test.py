#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 14:30
# @Author  : tanxw
from django import forms

f = forms.EmailField()
f.clean('foo@example.com')
print(f)
f.clean('invalid email address')
