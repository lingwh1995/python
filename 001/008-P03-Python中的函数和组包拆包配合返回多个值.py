"""
    Python中的函数和组包拆包配合返回多个值
"""

"""
    求函数中的最大值和最小值
"""


def max_min():
    a = [1, 2, 3, 4, 5]
    max_num = max(a)
    min_num = min(a)
# 返回多个值,解释器会自动对多个值组包
    return max_num, min_num


b = max_min()
print(b)
print(type(b))
