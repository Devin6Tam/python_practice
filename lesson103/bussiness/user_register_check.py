#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/22 12:03
# @Author  : tanxw

from lesson103.exception.custom_exception import *

def checkUserRegister(name, pwd):
    """判断用户名和密码是否符合规范"""
    # 	1. 用户名长度在3-8个字符
    if len(name) < 3 or len(name) > 8:
        raise NameIsError("用户名的长度应该是在3-8个字符之间")

    # 2.用户名中只能出现英文字母或数字
    if not name.isalnum(): # 满足标识符 字母 数字 下划线
        raise NameIsError("用户名中只能出现英文字母和数字")

    # 3. 密码长度必须是6位
    if len(pwd) != 6:
        raise PwdIsError("密码长度必须是6位")

    # 	4. 密码必须由纯数字组成
    if not pwd.isdigit():
        raise PwdIsError("密码必须由纯数字组成")


__all__ = ["i", "a"]
# 全局变量
i = 'jack_111'
a = "hello, function"

# 来判断运行环境是否是自己的环境
if __name__ == "__main__":
    # 测试代码, 其他的代码
    print("这是一段测试代嘛 里面有什么东西  你可以去用")
    print(__name__)

# 这样一个设置,,就可以过滤掉一些我们对外提供的资源(代码)
