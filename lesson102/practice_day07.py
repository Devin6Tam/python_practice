#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 21:08
# @Author  : tanxw
# @Desc    : 练习day07

"""1、for循环输出1-100之间的所有质数。"""
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for k in range(1, 100):
    if is_prime(k):
        print(k)


"""
2、从键盘中输入5个学生的名字，存储到列表中，然后打印出每个学生名字中的第2个字母。
"""
def make_stu_list(num):
    student_list = []
    student_index = 0
    while student_index < num:
        name = input("请输入姓名：\n")
        student_list.append(name)
        student_index += 1
    return student_list

def print_message(a):
    students = make_stu_list(a)
    for student in students:
        print("%s的第二个字母为%s" % (student, student[1]))
print_message(5)

"""
3、编程：使用字典来存储一个人的信息（姓名、年龄、学号、
QQ、微信、住址等），这些信息来自键盘的输入。
"""

card_info = {}
name = input("请输入姓名：\n")
card_info["name"] = name
age = int(input("请输入年龄：\n"))
card_info["age"] = age
study_no = input("请输入学号：\n")
card_info["study_no"] = study_no
qq_num = input("请输入QQ：\n")
card_info["qq_num"] = qq_num
wc_num = input("请输入微信：\n")
card_info["wc_num"] = wc_num
addr = input("请输入地址：\n")
card_info["addr"] = addr
print(card_info)


"""
4、有10个球分别为3红、3蓝、4白，球与球之间只有颜色的差别，
现需要将这10个球放入3个盒子，要求每个盒子至少有一个白球，
其余的球全部随机放，要求输出三个盒子里所有球的颜色，请用程序实现。
"""
import random

red_ball = ["红色", "红色", "红色"]
blue_ball = ["蓝色", "蓝色", "蓝色"]
white_ball = ["白色", "白色", "白色", "白色"]

boxes = [[], [], []]

for box in boxes:
    box.append(white_ball.pop())
    # print(box)

# print(boxes)
balls = red_ball+blue_ball+white_ball

for ball in balls:
    box_index = random.randint(0, len(boxes) - 1)
    # print(box_index)
    boxes[box_index].append(ball)

i = 1
for ball2 in boxes:

    print("盒子%s有%d个球" % (i, len(ball2)))
    i += 1
    for ball in ball2:
        print(ball)

"""
5、现有一字符串a = “abcdefg”，将字符串中的元素逐个输出，
并且在输出的时候如果字母是b则显示B。
"""

a = "abcdefg"

for a_str in a:
    if a_str == "b":
        print(a_str.upper())
    else:
        print(a_str)