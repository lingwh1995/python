"""
    Python中的字典的定义、通过key访问和修改数据
"""

"""
    Python中的字典类似于Java中的Map,是一种键值对结构的数据
    定义字典
    d = {}
"""

# 定义一个空的字典
d1 = {}
print(d1)
print(type(d1))

# 定义一个不标准的字典
# 理论上所有不可变的类型都可以作为key,只要是可hash的对象都可以作为key,一般情况下使用字符串类型的数据作为key
d2 = {1: 'one', '2': 'two', 'one': '星期一', 'a': 'b'}
print(d2)

# 定义一个标准的字典
d3 = {'one': '星期一', 'two': '星期二', 'three': '星期三'}
print(d3)

# 通过 []+key 访问字典中元素
print(d3['one'])
print(d3['two'])
print(d3['three'])
# 如果使用了不存在的key,则会报错:KeyError: 'x'
# print(d3['x'])

# 通过 []+key 改变该key所对应的值
d3['one'] = '星期一星期一'
print(d3)