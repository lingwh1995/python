"""
    python中的赋值和复合赋值
"""

# 赋值
a = 10
print('a = %d' % a)

# 一次赋值多个变量
b, s = 20, '我是一个字符串'
print('b = %d' % b)
print('s = %s' % s)

# 复合赋值
a += a
print('a = %d' % a)

b *= b + 10
# b = b * (b + 10)
print('b = %d' % b)
