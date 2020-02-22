#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 15:33
# @Author  : tanxw
# @Desc    ： 线程使用

from threading import Thread
import multiprocessing
import threading
import time

g_num = 0
# 创建互斥锁
# 锁的默认情况下是没有上锁的
mutex = threading.Lock()

def work1(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release() # 解锁

    print("在work1中, g_num的值为%d" % g_num)


def work2(num):
    global g_num
    for i in range(num):
        mutex.acquire()  # 上锁
        g_num += 1
        mutex.release()  # 解锁

    print("在work2中, g_num的值为 %d" % g_num)


print('线程创建之前,g_num的值为', g_num)

t1 = Thread(target=work1, args=(100000,))
t1.start()

t2 = Thread(target=work2, args=(100000,))
t2.start()

while len(threading.enumerate()) != 1:
    time.sleep(1)

print("两个线程对同一个全局变量操作的结果为", g_num)


# 多个线程对同一个全局变量进行操作,会出现资源竞争的问题,从而导致数据结果不正确----即线程非安全