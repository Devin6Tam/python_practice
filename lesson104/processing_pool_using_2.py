#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 21:33
# @Author  : tanxw
# @Desc    : 进程池间的通信

from multiprocessing import Manager, Pool
import time, random, os


def write(q):
    print("write 开始启动(%d), 父进程为: %d" % (os.getpid(), os.getppid()))
    for i in '在那遥远的地方的，有位好姑娘':
        q.put(i)


def read(q):
    print("read 开始启动(%d), 父进程为: %d" % (os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print('read从Queue中获取的数据为: %s' % q.get(True))


if __name__ == '__main__':
    print("%s 开始执行" % os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(write, (q,))

    time.sleep(1)  # 先让上边的任务向Queue存入数据,然后再向下边的任务开始读取数据

    po.apply_async(read, (q,))
    po.close()
    po.join()
    print("%s end" % os.getpid())


