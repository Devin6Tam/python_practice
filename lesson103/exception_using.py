#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 10:51
# @Author  : tanxw
# @Desc    : 异常使用

"""
try:
    代码块
except:
    打印异常提示信息
else:
    没有异常会执行的代码
finally:
    不管有无异常，必须要执行的代码，可以在这里执行
"""

try:
    num = int(input("请输入一个整数"))
    print(num)
except:
    print("请输入正确的数字")

try:
    num = int(input("请输入一个整数: "))
    ret = 10 / num
    print(ret)
except ZeroDivisionError:
    print("除零错误")
except ValueError:
    print("请输入整数类型的数据")
except Exception as e:
    print("未知错误 %s" % e)
else:
    print("执行正常")
finally:
    print("执行完成，不确定有没有执行正确")


def demo1():
    return int(input("请输入一个整数: "))


def demo2():
    return demo1()


try:
    print(demo2())
except ValueError:
    print("请输入正确的整数")
except Exception as e:
    print("未知错误 %s" % e)

def input_username():
    username = input("请输入用户名称：")
    if username.isnumeric():
        raise Exception("用户名称需包含字母，数字")
    return username

try:
    username = input_username()
    print(username)
except Exception as e:
    print("发现错误 %s" % e)