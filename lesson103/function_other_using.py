#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 22:12
# @Author  : tanxw
# @Desc    : 函数其他使用

# 1. 实例
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line


if __name__ == "__main__":
    line1 = line_conf(2, 3)
    line2 = line_conf(1, 1)
    print(line1(5))
    print(line2(5))

# 2. 修改函数外部变量的值
"""
global与nonlocal使用区别
global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量。
nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量，如果上一级函数中不存在该局部变量，
nonlocal位置会发生错误（最上层的函数使用nonlocal修饰变量必定会报错）。
"""
def count(start=0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr


c1 = count()
print(c1())
print(c1())

# 3. 匿名函数
# lambda 参数列表: return [表达式] 变量
ret = lambda x, y: x + y

print(ret(1, 19))

infos = [{'name': 'wang', 'age': 20},
         {'name': 'xiaoming', 'age': 15},
         {'name': 'zhang', 'age': 22}]
"""
list sort 参数使用说明
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认)
"""
infos.sort(key=lambda a: a['age'], reverse=True)
print(infos)


def demo(a, b, func):
    ret = func(a, b)
    return ret


num = demo(5, 10, lambda x, y: x+y)
print(num)


"""
演示文档注释使用
"""

def say():
    """打印hello 武汉加油"""
    print("hello 武汉加油")


def sum_1_100():
    """完成1到100的累加求和"""
    i = 1
    sum = 0
    while i <=100:
        sum = sum + 1
        i += 1
    print("1到100的求和结果是:%d" %sum)

# 按住ctrl 键
say()
sum_1_100()