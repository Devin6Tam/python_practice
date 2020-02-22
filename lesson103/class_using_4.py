#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 22:28
# @Author  : tanxw
# @Desc    : 类的继承使用，重写，多态


class Tools(object):

    # 定义类属性,记录工具对象的总数
    count = 0

    def __init__(self, name):
        self.count = 5
        self.name = name

        # 针对类属性做 +1 操作
        Tools.count += 1

    @classmethod
    def show_tool_count(cls):
        """显示工具对象的总数"""
        print("工具对象的总数: %d" % cls.count)

    @staticmethod
    def desc():
        """
        静态方法: 不需要访问实例属性,类属性,也不需要调用类方法,实例方法
        """
        print("打印描述")


# 创建工具对象
tool1 = Tools('剪刀')
tool2 = Tools('斧头')
tool3 = Tools('锤子')

# 实例属性
print("使用这个类创建了%d个工具对象" % tool1.count)
# 类属性
print("使用这个类创建了%d个工具对象" % Tools.count)

Tools.show_tool_count()
Tools.desc()
