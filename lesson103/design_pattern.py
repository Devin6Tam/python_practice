#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/10 0:41
# @Author  : tanxw
# @Desc    : 设计模式
"""
设计模式的目标是形成典型问题的解决方案，设计出可复用的软件结构。
设计模式与语言无关的，任何语言都可以实现设计模式

设计模式根据使用目的不同而分为创建型模式（Creational Pattern）、
结构型模式（Structural Pattern）、行为型模式（Behavioral Pattern）

创建型模式提出了对象创建的解决方案以及数据封装的方法。
降低了创建对象时代码实现的复杂度，使对象的创建能满足特定的要求。
例如：工厂模式、抽象工厂模式、单例模式、生成器模式等

结构性模式描述了对象之间的体系结构，通过组合、
继承等方式改善体系结构，降低体系结构中组件的依赖性。
例如、适配器模式、桥模式、组合模式、装饰器模式、外观模式等。

行为型模式描述了对象之间的交互和各自的职责，有助于实现程序中对象的通讯和流程的控制
如：迭代器模式、解释器模式、中介者模式、观察者模式等。
"""

#　工厂模式
class FruitFactory:
    def createFruit(self, fruit):
        if fruit == 'apple':
            return Apple()
        elif fruit == 'banana':
            return Banana()

class Fruit:
    def __str__(self):
        return 'fruit'

class Apple(Fruit):
    def __str__(self):
        return 'apple'

class Banana(Fruit):
    def __str__(self):
        return 'Banana'

if __name__ == '__main__':
    factory = FruitFactory()
    print(factory.createFruit('apple'))
    print(factory.createFruit('banana'))