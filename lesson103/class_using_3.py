#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 21:38
# @Author  : tanxw
# @Desc    : 类的继承使用，重写，多态

class A:
    def test(self):
        print("test")


class B:
    def demo(self):
        print("demo")


class C(A, B):
    pass


c = C()
c.demo()
c.test()
print(C.__mro__)  # 确定C类对象的调用顺序

