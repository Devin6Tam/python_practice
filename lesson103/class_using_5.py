#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/15 21:58
# @Author  : tanxw
# @Desc    : 示例

class Game(object):

    # 记录游戏的最高分
    top_score = 0

    def __init__(self, name):
        self.name = name

    def start_game(self):
        print("[%s] 开始游戏" % self.name)
        print("经过一番大战, 游戏结束")
        Game.top_score = 900

    @staticmethod
    def show_help():
        print("帮助信息: 植物大战僵尸")

    @classmethod
    def show_top_score(cls):
        print("游戏的最高分数为: %d " % cls.top_score)

    def __del__(self):
        print("已退出游戏")


# 查看游戏的帮助信息
Game.show_help()

# 显示游戏的最高分
Game.show_top_score()

# 创建玩家
game = Game('kiki')

# 开始游戏
game.start_game()

# 游戏结束, 显示游戏最高分
Game.show_top_score()

