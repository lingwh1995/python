"""
    python中的列表的定义和下标访问
"""

# 定义一个具有多个元素的列表,必须加逗号
list1 = [1, 2, '3', (4, 5, 6), [7, 8, 9]]
for i in list1:
    if isinstance(i, tuple) or isinstance(i, list):
        for j in i:
            print(j)
    else:
        print(i)

# 使用list()创建列表对象
# list2 = list()
list2 = list('hello')
print(list2)

# 通过下标访问list中元素
list3 = [1, 2, 3, 4]
print(list3[0])
print(list3[1])
print(list3[2])
print(list3[3])
# 如果越界访问,则会报: IndexError: list index out of range
print(list3[10])