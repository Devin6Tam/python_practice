#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/20 12:08
# @Author  : tanxw
# @Desc    : 使用gevent库实现协程

from gevent import monkey
import gevent
import random
import time

# 有耗时操作的时候
monkey.patch_all()

def func1():
    print("func1 running")
    gevent.sleep(2)  # 内部函数实现io操作
    print("switch func1")


def func2():
    print("func2 running")
    gevent.sleep(1)
    print("switch func2")


def func3():
    print("func3  running")
    gevent.sleep(0.5)
    print("func3 done..")


def work(name):
    for i in range(10):
        print(name, i)
        time.sleep(random.random())


if __name__ == '__main1__':
    gevent.joinall([gevent.spawn(func1),
                    gevent.spawn(func2),
                    gevent.spawn(func3),
                    ])


gevent.joinall([
    gevent.spawn(work, 'work1'),
    gevent.spawn(work, 'work2')
])


"""
1. 进程是资源分配的单位
2. 线程是操作系统调度的单位
3. 进程切换消耗的资源最大,效率低
4. 线程切换消耗的资源一般,效率一般
5. 协程切换认为资源很小,效率很高
6. 多进程,多线程根据cpu核数不一样可能是并行的,但是协程是在一个线程中,所以是并发
"""