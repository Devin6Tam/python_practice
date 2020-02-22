#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 8:55
# @Author  : tanxw
# @Desc    : 函数进阶使用

# 1. 无参数无返回值
def show_menu():
    print("*" * 30)
    print("1. 看病")
    print("2. 听诊")
    print("3. 开药")
    print("4. 巡诊")
    print("*" * 30)

show_menu()

# 2. 无参数有返回值
def calc():
    num1 = 10
    num2 = 20
    return num1 + num2

print(calc())


# 3. 有参数有返回值
def calc(num1, num2, operator):
    if operator == "/":
        return num1 / num2
    elif operator == "*":
        return num1 * num2
    elif operator == "+":
        return num1 * num2
    elif operator == "-":
        return num1 * num2
    else:
        return 0

print(calc(25, 25, "*"))

# 4. 函数引用
def test(num):
    print("在函数内部, %d 对应的内存地址是 %d" % (num, id(num)))

    # 定义一个字符串
    ret = "hello"
    print("函数要返回的数据的内存地址是 %d" % id(ret))

    # 将字符串变量返回, 返回的是数据的引用, 而不是数据的本身
    return ret

# 定义一个变量
a = 10

print("变量a保存的数据 内存地址是 %d" % id(a))
# 调用test函数,本质上,传递的是实参保存的数据的引用, 而不是实参保存的数据
# 注意: 如果函数有返回值,但是没有定义变量接收
# 程序不会报错,但是无法获得结果
res = test(a)
print("%s的内存地址是 %d" % (res, id(res)))

# 5.修改全局变量

def test1():
    # 修改全局变量的值 使用关键字global声明就可以
    global a
    a = 20
    print("test1 a=%d" % a)
def test2():
    print("test2 a=%d" % a)

test1()
test2()

# 6. 多个返回值
def test3():
    return 3, 6

c, d = test3()
print("c=%d" % c)
print("d=%d" % d)

# 7. 函数可变参数与不可变参数
def demo1(num, num_list):
    # 这里变量赋值，只影响函数内部
    num = 20
    num_list = [1, 3, 7, 11]
    print(num)
    print(num_list)

num = 16
num_list = [4, 7, 11]
demo1(num, num_list)
print(num)
print(num_list)

def demo2(num_list):
    num_list.extend([7, 9, 17])
    print(num_list)

demo2(num_list)
print(num_list)


# 8. 函数参数+=的结果类似append
def demo3(num, num_list):
    num += num
    num_list += num_list
    print(num)
    print(num_list)

demo3(num, num_list)


# 9. 列举参数应用场景
def demo4(x, y, *args, a=5, b ,**kwargs):
    print("位置参数x,y：", x, y)
    print("默认参数a:", a)
    print("可变参数args:", args)
    print("关键参数b:", b)
    print("字典参数kwargs:", kwargs)

demo4(5, 6,7,8,9,a=10,b=10,name="张三", age=18, gender=True)