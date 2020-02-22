#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/18 16:10
# @Author  : tanxw
# @Desc    : 线程使用

import threading
import time

class TestThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = '线程' + self.name + "-" + str(i)
            print(msg)

def test():
    for i in range(5):
        t = TestThread()
        t.start()

# 多线程执行顺序不确定,
# start方法是以多任务的形式运行
# run方法以普通函数方式运行
# 都能启动程序
if __name__ == '__main__':
    test()
