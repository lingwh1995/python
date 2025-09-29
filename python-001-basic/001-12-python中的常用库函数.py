"""
    python中的常用库函数
"""

# 导入随机数函数
import random

"""
    随机函数
"""
r = random.randint(0, 2)
print(r)

"""
    使用随机函数生成10个0-1之间的随机浮点数
"""
for i in range(10):
    print(random.random())

"""
    使用随机函数生成10个0-9之间的随机整数，左闭右闭，生成的随机整数范围是[0, 9]
"""
for i in range(10):
    print(random.randint(0, 9))

"""
    求最大值和最小值函数
"""
l = [1, 2, 3, 4, 5]
print(max(l))
print(min(l))

