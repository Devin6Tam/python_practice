#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 17:16
# @Author  : tanxw
# @Desc    : 死锁

import threading
import time


class ThreadDemo1(threading.Thread):

    def run(self):
        # 对mutexA上锁
        mutexA.acquire()
        print(self.name + "开始执行")
        time.sleep(1)  # 此时线程会被阻塞

        mutexB.acquire()
        print(self.name + '结束执行')
        mutexB.release()

        mutexA.release()


class ThreadDemo2(threading.Thread):

    def run(self):
        # 对mutexB上锁
        mutexB.acquire()
        print(self.name + "开始执行")
        time.sleep(1)  # 此时线程会被阻塞

        mutexA.acquire()
        print(self.name + '结束执行')
        mutexA.release()

        mutexB.release()


mutexA = threading.Lock()
mutexB = threading.Lock()


if __name__ == '__main__':
    t1 = ThreadDemo1()
    t2 = ThreadDemo2()
    t1.start()
    t2.start()