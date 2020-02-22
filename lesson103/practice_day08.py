#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 11:47
# @Author  : tanxw
# @Desc    : 用户登录信息校验

from lesson103.exception.custom_exception import *
# from lesson103.bussiness.user_register_check import *
from lesson103.bussiness.user_register_check import checkUserRegister
"""
案例:
    用户登录信息校验
要求:
	用户输入用户名, 密码后对信息进行校验
	1. 用户名长度在3-8个字符
	2. 用户名中只能出现英文字母和数字
	3. 密码长度必须是6位
	4. 密码必须由纯数字组成

"""
# 拿到用户的信息
# print(i, a)
name = input("请输入您的用户名:")
pwd = input("请输入您的密码:")
# 1.抽离出差来，放在独立的包中，作为模块使用
# 自定义异常
# class NameIsError(Exception):
#     pass
#
#
# class PwdIsError(Exception):
#     pass

# 2.抽离出差来，放在独立的包中，作为模块使用
# 检测注册账号跟密码是否符合规范
# def checkUserRegister(name, pwd):
#     """判断用户名和密码是否符合规范"""
#     # 	1. 用户名长度在3-8个字符
#     if len(name) < 3 or len(name) > 8:
#         raise NameIsError("用户名的长度应该是在3-8个字符之间")
#
#     # 2.用户名中只能出现英文字母或数字
#     if not name.isalnum(): # 满足标识符 字母 数字 下划线
#         raise NameIsError("用户名中只能出现英文字母和数字")
#
#     # 3. 密码长度必须是6位
#     if len(pwd) != 6:
#         raise PwdIsError("密码长度必须是6位")
#
#     # 	4. 密码必须由纯数字组成
#     if not pwd.isdigit():
#         raise PwdIsError("密码必须由纯数字组成")


# 拦截异常
try:
    checkUserRegister(name, pwd)
except NameIsError as e:
    print(e)
except PwdIsError as e:
    print(e)