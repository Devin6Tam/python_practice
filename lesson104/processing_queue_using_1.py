#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 21:16
# @Author  : tanxw
# @Desc    : 进程-队列使用实例
from multiprocessing import Queue,Process
import time
import random

def write(q):
    for i in ['a', 'b', 'c']:
        # 往消息队列中放入消息
        print('put %s to queue' % i)
        q.put(i)
        time.sleep(random.random())  # random.random()随机生成0-1之间的小数

def read(q):
    while True:
        if not q.empty():
            # 从消息队列中取值
            value = q.get(True)  # 取值,默认等待
            print("读取消息为", value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    q = Queue()
    # 创建进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动写入消息的进程
    pw.start()
    # 等待写入消息进程执行结束
    pw.join()
    # 启动读取消息的进程
    pr.start()
    # 等待读取消息的进程执行结束
    pr.join()
    print("所有的数据都写入完成,并且读取完成")
