"""
    Python中的字符串常用算法
"""

s = '12345'


# 字符串逆序
def reverse(s):
    i = len(s) - 1
    reverse_s = ''
    while i >= 0:
        reverse_s += s[i]
        i -= 1
    return reverse_s


print(reverse(s))