"""
    python石头剪刀布游戏
"""

import random


def game():
    while True:
        # 定义一个变量代表玩家出的，从键盘输入值
        player = int(input('请输入一个状态(石头 0，剪刀 1，布 2):'))

        # 定义一个电脑变量，使用随机数获取状态
        robot = random.randint(0, 2)
        print(robot)
        print('电脑出的是: %d' % robot)

        # 平局
        if player == robot:
            print('平局......')
        # 玩家赢
        elif ((player == 0) and (robot == 1)) or ((player == 1) and (robot == 2)) or ((player == 2) and (robot == 0)):
            print('您赢了......')
        # 电脑赢
        else:
            print('电脑赢......')


game()

