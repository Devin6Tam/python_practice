#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 22:47
# @Author  : tanxw
# @Desc    : 类方法

class Chinese:
    # 类变量
    country = "中国"

    def __init__(self,name,id_card):
        self.name = name
        self.id_card = id_card

    # 类方法
    @classmethod
    # 演示类方法中调用实例成员
    def show_country(cls):
        # self.show()
        # self.name
        print("我是中国人,我骄傲,我为武汉加油")

    # 实例方法
    def show_(self):
        # 实例方法中调用类变量
        print(Chinese.country)
        print(self.name)
        Chinese.show_country()

man1 = Chinese("小明","654321")
# 类名.类方法名() 推荐使用
# Chinese.show_country()
# 对象名.类方法名()
man1.show_()
Chinese.show_country()
