#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 17:15
# @Author  : tanxw
# @Desc    : 进程-队列使用

from multiprocessing import Queue

q = Queue(3)
q.put("消息1")
q.put("消息2")
print(q.full())
q.put("消息3")
print(q.full())

try:
    # 使用捕获异常的语法原因是,下面两种方式都会抛出异常,第一个是等待两秒抛出异常,第二个是立刻抛出异常
    # q.put("消息4")
    q.put("消息4", True, 2)
except:
    print("消息队列已满，现有消息数量：", q.qsize())

# 存放消息,先判断是否满了,如果没满,再写入
if not q.full():
    q.put_nowait('消息4')

# 读取消息,先判断消息队列是否为空,再读取
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
