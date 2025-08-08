"""
    python中的高阶函数reduce配合lambda
"""

import functools
"""
    reduce函数作用: 会对参数序列中的元素进行累计处理,直到处理完参数列表中所有参数
    函数将一个数据集合中所有数据进行下列操作:
        1.用传给reduce中函数function(有两个参数),先对集合中的第1,2个元素进行操作
        2.用得到的结果再与第三个数据用function函数运算,最后得到一个结果
    注意: 这个reduce()函数不能直接使用,需要导入一个functools,使用functools.reduce()进行调用    
"""

l1 = [1, 2, 3, 4, 5]


def add(a, b):
    return a + b


result = functools.reduce(add, l1)
# reduce过程分析: 1+2=3, 3+3=6, 6+4=10, 10+5=15
print(result)
print('------------------------------')

# reduce()和lambda配合拼接字符串
l2 = ['h', 'e', 'l', 'l', 'o']
s1 = functools.reduce(lambda a, b: a + b, l2)
print(s1)

s2 = functools.reduce(lambda a, b: a.upper() + b.upper(), l2)
print(s2)
