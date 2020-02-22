#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 12:01
# @Author  : tanxw
# @Desc    : 简单协程与greenlet协程使用

import time
from greenlet import greenlet

def work1():
    while True:
        print("work1")
        yield
        time.sleep(0.5)


def work2():
    while True:
        print("work2")
        yield
        time.sleep(0.5)


def main():
    w1 = work1()
    w2 = work2()
    while True:
        next(w1)
        next(w2)


if __name__ == '__main1__':
    main()


def work3():
    while True:
        print("work3")
        g4.switch()
        time.sleep(0.5)


def work4():
    while True:
        print("work4")
        g3.switch()
        time.sleep(0.5)


g3 = greenlet(work3)
g4 = greenlet(work4)

g3.switch()
