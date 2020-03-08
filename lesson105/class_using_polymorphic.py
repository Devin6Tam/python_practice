#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 0:35
# @Author  : tanxw
# @Desc    : 面向对象--多态使用

# 一个类继承了其他类的功能, 根据不同的场景, 切换不同的形态, 做到不同的功能, 我们就称之为多态

class Player:
    def play(self):
        print("会打篮球")


class Singer:
    def sing(self):
        print("会唱歌")

# 继承关系
# 多重特征
class Man(Player, Singer):
    def play(self):
        print("我会打篮球")

    def sing(self):
        print("我会唱歌")


class Student:
    def show(self, singer):
        singer.sing()

s1 = Student()
# 第一种情况
singer1 = Singer()
s1.show(singer1)

# 第二种情况
man1 = Man()
s1.show(man1)
man1.play()
