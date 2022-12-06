# Python中字典的增删改查

print('Python中字典的增删改查')

# 定义一个空的字典
d = {'a': 1, 'b': 2, 'c': 3}
print(d)
'''
    1.如果key存在就是添加数据,如果key不存在就是修改数据
    2.key不能修改,值是可以修改
'''
# 增加元素
d['d'] = 4
print(d)
# 修改元素
d['d'] = 'd'
print(d)
# 查询元素
print(d['a'])
print(d.get('a'))
print(d)
# 删除任意位置键值对
d.pop('a')
print(d)
# 删除字典中最后一对元素,或者说删除字典尾部元素
d.popitem()
print(d)
# 清空字典
d.clear()
print(d)

d1 = {'a': 1, 'b': 2, 'c': 3}
print(d1)
# 删除整个字典,删除后再打印会报错: NameError: name 'd1' is not defined
del d1
# print(d1)

