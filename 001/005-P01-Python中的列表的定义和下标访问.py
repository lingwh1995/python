"""
    Python中的列表的定义和下标访问
"""

"""
    元组:不可变类型
    格式:使用中括号括起来的就是列表
"""

# 定义一个空的列表
list1 = []

print(list1)
print(type(list1))
print('------------------------------')

# 定义一个具有一个元素的列表,必须加逗号
list2 = [1, ]
# list2 = [1]
print(list2)
print('------------------------------')

# 定义一个具有多个元素的列表,必须加逗号
list3 = [1, 2, 3]
print(list3)
# 下标访问
print(list3[0])
print(list3[1])
print(list3[2])
print('------------------------------')

# 使用[]定义list和使用list()方法定义list
list4 = ['h', 'e', 'l', 'l', 'o']
list5 = list('hello')
print(list4)
print(list5)