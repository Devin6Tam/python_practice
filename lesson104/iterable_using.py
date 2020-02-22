#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/19 22:56
# @Author  : tanxw

from collections.abc import Iterable

class MyList(object):
    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    def __iter__(self):
        """返回一个迭代器"""
        myiterator = MyIterator(self)
        return myiterator


class MyIterator(object):
    """自定义供上面的可迭代对象使用的一个迭代器"""

    def __init__(self, mylist):
        self.mylist = mylist
        # 去记录当前位置的变量
        self.current = 0

    def __next__(self):
        if self.current < len(self.mylist.container):
            item = self.mylist.container[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)

for i in mylist:
    print(i)

print(mylist.container)
print(isinstance(mylist, Iterable))

# 可迭代对象: 可以使用for..in..这样的语句读取数据功能我们使用的对象
# 本质: 提供一个帮助我们记录读取数据的中间"人"

# 可迭代对象通过__iter__方法 提供一个迭代器
# 一个具备了 __iter__方法的对象,就是一个可迭代对象
