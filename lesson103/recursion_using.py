#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 10:10
# @Author  : tanxw
# @Desc    : 递归使用

def print_info(name, gender=True):

    gender_text = get_gender_text(gender)

    print("%s is %s!" % (name, gender_text))


def print_info(name, title, gender=True):

    gender_text = get_gender_text(gender)

    print("%s%s is %s!" % (name, title, gender_text))

def get_gender_text(gender=True):
    gender_text = "boy"

    if not gender:
        gender_text = "girl"
    return gender_text

# 函数没法呈现多态
# print_info("shuaishuai", gender=False)
print_info("shuaishuai", " commissary", gender=False)


# 多个参数
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="张三", age=18, gender=True)

nums = (1, 2, 3)
card_dict = {'name': 'yaoming', 'age': 18}

demo(1, nums, card_dict)
demo(1, *nums, **card_dict)


def sum_nums(*args):
    ret = 0
    for i in args:
        ret += i
    return ret


# print(sum_nums(1, 2, 3, 4, 54, 5))
s = sum_nums(1, 2, 3, 4, 54, 5)
print(s)

# 递归打印
def print_nums(num):
    # 控制递归出口，以免死循环
    if num == 0:
        return
    print(num)
    print_nums(num-1)

print_nums(100)


# 递归求和
def add_nums(num):
    # 控制递归出口，以免死循环
    if num == 1:
        return 1
    temp = add_nums(num - 1)
    return num + temp

print(add_nums(100))