#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/9 17:50
# @Author  : tanxw
# @Desc    : 抽象类，接口类概念的使用

from abc import ABCMeta, abstractmethod
# 抽象类 接口类  规范和约束  metaclass指定的是一个元类
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self):
        pass  # 抽象方法

class Alipay(Payment):
    def pay(self, money):
         print('使用支付宝支付了%s元' % money)

class QQpay(Payment):
    def pay(self, money):
        print('使用qq支付了%s元' % money)

class Wechatpay(Payment):
    def pay(self,money):
        print('使用微信支付了%s元'%money)

def pay(a,money):
    a.pay(money)

qqpay = QQpay()
alipay = Alipay()

pay(qqpay, '￥100.00')
pay(alipay, '￥110.00')

wechatpay = Wechatpay()
wechatpay.pay('￥120.00')
pay(wechatpay, '￥120.00')

"""
抽象类和接口类做的事情 ：建立规范
制定一个类的metaclass是ABCMeta，
那么这个类就变成了一个抽象类(接口类)
"""