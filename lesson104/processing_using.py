#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 17:22
# @Author  : tanxw
# @Desc    : 进程使用

import multiprocessing
import time
import os

def run_proc():
    """子进程要执行的代码"""
    while True:
        print('--2--')
        # 打印进程ID
        print("子进程ID：%d" % os.getpid())
        time.sleep(1)


if __name__ == '__main__1':
    p = multiprocessing.Process(target=run_proc)
    p.start()
    print("主进程ID：%d" % os.getpid())
    # while True:
    #     print('--1--')
    #     time.sleep(1)
    print(p.is_alive())
    p.join()
    p.terminate()
    print("结束")


"""
Process([group [, target [, name [, args [, kwargs]]]]])

target：如果传递了函数的引用，可以任务这个子进程就执行这里的代码
args：给target指定的函数传递的参数，以元组的方式传递
kwargs：给target指定的函数传递命名参数
name：给进程设定一个名字，可以不设定
group：指定进程组，大多数情况下用不到


Process创建的实例对象的常用方法：

start()：启动子进程实例（创建子进程）
is_alive()：判断进程子进程是否还在活着
join([timeout])：是否等待子进程执行结束，或等待多少秒
terminate()：不管任务是否完成，立即终止子进程
"""


def run_proc2(name, age, **kwargs):
    """子进程要执行的代码"""
    for i in range(10):
        print('在子进程中,name=%s, age=%d, pid=%d' % (name, age, os.getpid()))  # os.getpid()获取当前的进程号
        print(kwargs)
        time.sleep(0.2)


if __name__ == '__main__':
    print("主进程pid=%d" % os.getpid())
    p = multiprocessing.Process(target=run_proc2, args=('test', 20), kwargs={'m': 10})
    p.start()
    # time.sleep(10)
    p.join(10)
    p.terminate()
