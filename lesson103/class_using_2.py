#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 10:42
# @Author  : tanxw
# @Desc    : 类的继承使用，重写，多态

class Animal:
    """
        :param name 名称
        :param age 年龄
        :param sex 性别
        :param body_length 体长
        :param weight 体重
        :param foot 是否有脚
        :param mouth
    """

    def __init__(self):
        print("初始化对象...")
        # 私有属性，无法为子类所调用
        self.__xuhao = "12345678"

    def eat(self):
        print("我会吃")
    def drink(self):
        print("我会喝")
    def sleep(self):
        print("我会睡")

    def __test(self):
        print("私有方法无法被子类所调用")

    def test(self):
        print("公有方法调用私有方法，可以为子类调用")
        self.__test()

    def __del__(self):
        print("%s 对象已经销毁..." % self.name)

class Dog(Animal):
    def game(self):
        print("%s 快乐的玩耍" % self.name)

    def bark(self):
        print('我会叫')

    def demo(self):
        self.game()
        # self.__test()

    # 重写父类方法，并且扩展使用
    def sleep(self):
        super().sleep()
        print("随时倒地睡觉")

class Cat(Animal):
    def bark(self):
        print('我会叫')

    def jump(self):
        print('我会跳')

    # 重写父类方法，并且扩展使用
    def sleep(self):
        super().sleep()
        print("我是晚上睡觉")


class Bird(Animal):
    count = 0
    def bark(self):
        print('我会叫')

    def fly(self):
        print('我会飞')

    def sing(self):
        print("我会唱歌")

    # 静态方法
    @staticmethod
    def happy():
        """
        静态方法: 不需要访问实例属性,类属性,也不需要调用类方法,实例方法
        """
        print("我很高兴")

    # 静态方法
    @classmethod
    def show_tool_count(cls):
        """显示工具对象的总数"""
        print("工具对象的总数: %d" % cls.count)


wangcai = Dog()
wangcai.name = "旺财"
wangcai.eat()
wangcai.drink()
wangcai.bark()
wangcai.sleep()
wangcai.demo()

parrot = Bird()
parrot.name = "鹦鹉"
parrot.test()
parrot.eat()
parrot.drink()
parrot.bark()
parrot.sleep()
parrot.fly()
parrot.sing()

Bird.happy()
Bird.show_tool_count()
