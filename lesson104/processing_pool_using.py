#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 21:25
# @Author  : tanxw
# @Desc    : 进程池使用

from multiprocessing import Pool
import time, os, random


def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random())
    t_stop = time.time()
    print(msg, '执行完毕, 耗时%.2f' % (t_stop - t_start))


if __name__ == '__main__':
    po = Pool(3)  # 定义一个进程池,最大进程数3
    for i in range(0, 10):
        # 每次循环将会用到空闲出来的子进程调用目标
        po.apply_async(worker, (i,))

    print('start')
    po.close()  # 关闭进程池, 关闭以后不再接收新的请求
    po.join()  # 等待所有的po中的子进程执行完成, 必须放在close之后
    print('end')
