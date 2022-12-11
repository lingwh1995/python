# Python通过key和get访问字典数据

print('Python通过key和get访问字典数据')

'''
    1.使用 []+ key 访问字典
    2.使用get()访问字典
'''

# 定义一个标准的字典
d1 = {'one': '周一', 'two': '周二', 'three': '周三'}
print(d1)

# 通过 []+key 访问字典中元素
print(d1['one'])
# 如果使用了不存在的key,则会报错:KeyError: 'x'
# print(d3['x'])

# 通过get()访问字典中元素
print(d1.get('one'))
# 如果使用了不存在的key,会返回None,但是不会报错
print(d1.get('x'))