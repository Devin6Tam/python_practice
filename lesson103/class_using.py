#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 0:16
# @Author  : tanxw
# @Desc    : 类的使用

# class 类名:
#     def 方法1(self, 参数列表):
#         pass
#     def 方法2(self, 参数列表):
#         pass
# 对象名 = 类名()

class Cat:
    """定义了一个猫类"""

    def __init__(self):
        print("初始化方法")  # 初始化方法在对象被创建的时候自动调用

    # 下面的方法，初始化需要传入参数才行
    # def __init__(self, name):
    #     print("初始化方法")  # 初始化方法在对象被创建的时候自动调用
    #     # self.name = 'Tom'
    #     # 对属性的设置进行改造
    #     self.name = name

    def __del__(self):
        # 对象销毁之前被自动调用,这个方法跟关键字del没有必然的联系
        print("%s 去了" % self.name)

    # 用于打印对象输出信息
    def __str__(self):  # 必须返回一个字符串
        return '我是小猫%s' % self.name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def drink(self):
        print("%s在喝水" % self.name)

tom = Cat()
tom.name = "Tom"
tom.eat()
tom.drink()
print(tom)


class HouseItem:

    def __init__(self, name, area):
        """
        :param name: 家具名称
        :param area: 占地面积
        """
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.2f平米" % (self.name, self.area)


bed = HouseItem('高露捷', 4)
chest = HouseItem('壁橱', 2)
table = HouseItem('麻将桌', 2.5)

print(bed)
print(chest)
print(table)


class House:

    def __init__(self, house_type, area):
        """
        :param house_type: 户型
        :param area: 总面积
        """
        self.house_type = house_type
        self.area = area

        # 剩余面积, 默认情况下剩余面积就是总面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        return "户型:%s\n总面积:%.2f平米[剩余:%.2f平米]\n家具列表:%s" % (self.house_type,
                                                          self.area,
                                                          self.free_area,
                                                          self.item_list)

    def add_item(self, item):

        print("要添加%s" % item)
        # 如果家具的面积 超过了 剩余面积
        if item.area > self.free_area:
            print("%s 的面积过大, 无法添加" % item.name)
            return

        # 没有超过,添加到列表
        self.item_list.append(item.name)

        # 计算剩余面积
        self.free_area -= item.area


my_home = House('三室两厅', 80)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)