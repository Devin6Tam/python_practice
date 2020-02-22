#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 23:18
# @Author  : tanxw
# @Desc    : 线程使用

import time
import threading


def sing():
    for i in range(3):
        print("正在唱歌%d" % i)
        time.sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞%d" % i)
        time.sleep(1)

# 单线程，多任务
if __name__ == '__main__1':
    sing()
    dance()

if __name__ == '__main__':

    # 多线程
    # for i in range(1, 5):
    print("开始执行: %s" % time.ctime())
    t = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t.start()
    t2.start()

    # 查看线程数量
    while True:
        length = len(threading.enumerate())
        print("当前运行的线程数量为: %d" % length)
        if length <= 1:
            break

        time.sleep(0.5)
    print('结束: %s' % time.ctime())


