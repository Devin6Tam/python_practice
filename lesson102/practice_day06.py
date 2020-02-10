#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 15:43
# @Author  : tanxw
# @Desc    : 练习day06

"""
1、题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各个位上数字的立方和等于该数本身。例如：153是一个”水仙花数"，
因为153=1的三次方＋5的三次方＋3的三次方。
"""
for k in range(100, 1000):
    a = int(k/100)
    b = int(k/10) % 10
    c = k % 10
    ret = a**3 + b**3 + c**3
    if ret == k:
        print("%d是一个水仙花数" % k)


"""2、设计“过7游戏”的程序, 打印出1-100之间除了含7和7的倍数之外的所有数字。"""
for h in range(1, 101):
    if not (h % 10 == 7 or h % 7 == 0):
        print(h)

"""
3、使用while，完成以下图形的输出。（每一行的星星不能用*乘以星星的数量来完成，须使用while嵌套）(较难)
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
row = 1
count = 1  # 表示当前行数应该有多少个*

while row <= 9:

    col = 1
    if row != 1:
        if row < 6:
            count += 2
        else:
            count -= 2

    while col <= count:
        if col == 1:  # 处理*前面的空格
            print(" " * ((9 - count) // 2), end="")
        print("*", end="")
        col += 1

    print("")
    row += 1

"""
4、使用while、if来完成剪刀石头布程序，要求，
当玩家第3次获胜时才退出游戏，否则继续玩。
"""
import random

win_times = 0
while True:
    player = int(input("请输入：剪刀(0) 石头(1) 布(2)"))
    computer = random.randint(0, 2)
    if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player ==2 and computer == 1):
        win_times += 1
        if win_times == 3:
            print("你赢了三次了")
            break
        else:
            print("你赢了这局游戏")
    elif player == computer:
        print("平局，再来一次")
    else:
        print("你输了，不要走，决战到天亮")

"""
6、幸运猜猜猜：游戏随机给出一个0~99（包括0和99）的数字，然后让你猜是什么数字。
你可以随便猜一个数字，游戏会提示太大还是太小，从而缩小结果范围。
经过几次猜测与提示后，最终推出答案。在游戏过程中，记录你最终猜对时所需要的次数，
游戏结束后公布结果。  
说明： 
1~2次猜中，打印你太TM有才了！  
3~6次猜中，打印这么快就猜出来了，很聪明嘛！ 
大于7次猜中，打印猜了半天才猜出来，小同志，尚需努力啊！  
猜测次数最多20次。
"""

gamer = random.randint(0, 99)

guess_times = 0
while guess_times <= 20:
    player = int(input("请输入你猜的数字: "))
    if player > gamer:
        print("数字大了，再来")
        if guess_times > 20:
            print("你都猜了20次了，还没猜中")
            break
        continue
    elif player < gamer:
        print("数字小了，再来")
        if guess_times > 20:
            print("你都猜了20次了，还没猜中")
            break
        continue
    else:
        print("恭喜，猜中了")
        if guess_times < 2:
            print("你太TM有才了！")
        if 3 <= guess_times <= 6:
            print("这么快就猜出来了，很聪明嘛！")
        if guess_times >= 7:
            print("猜了半天才猜出来，小同志，尚需努力啊！")
    guess_times += 1
print("游戏选择数字：%d" % gamer)