#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 22:04
# @Author  : tanxw
# @Desc    : 实例化对象及单例模式

class MusicPlayer(object):
    # 记录单例对象是否被引用
    instance = None
    # 定义类属性记录 是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        print("new方法被执行......")  # 增加功能的操作
        # 判断类属性是否已经被赋值
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # 分配一个内存空间

        # 返回类属性的单例引用
        return cls.instance

    def __init__(self):
        if not MusicPlayer.init_flag:
            print("初始化音乐播放器对象")
            MusicPlayer.init_flag = True

player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)
