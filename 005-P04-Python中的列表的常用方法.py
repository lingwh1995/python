# Python中的列表的常用方法

print('Python中的列表的常用方法')

# 对列表进行排序,从小到大
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print('初始列表: %s' % list1)

# append():给列表尾部追加一个元素
list1.append(9)
print('append(): %s' % list1)

# insert(): 在指定的索引位置插入元素
list1.insert(0, 'a')
# 如果索引的值超过了列表的长度,则会添加到列表尾部
list1.insert(50, 'b')
print('insert(): %s' % list1)

# 扩展列表,给列表中添加一个新的列表
list2 = ['a', 'b', 'c']
list1.extend(list2)
print('extend(): %s' % list1)

# 倒转列表
list1.reverse()
print('reverse(): %s' % list1)

# 统计某个元素在列表中出现的次数
i = list1.count('a')
print('count(): %d' % i)

# 查询某个元素在列表中的索引
j = list1.index(2)
print('index(): %d' % j)
# 如果列表中不包含这个元素,但是调用了index()方法,则会报错: ValueError: 'j' is not in list
# j = list1.index('j')

# in判断某个元素是否在list中:在的话返回True
is_exist1 = 111 in list1
print('in: %d' % is_exist1)
# not in判断某个元素是否在list中:不在的话返回True
is_exist2 = 'x' not in list1
print('not in: %d' % is_exist2)

'''
    删除元素
    注意: 使用列表时,不要在循环遍历时删除元素
'''
list2 = [1, 1, 2, 2, 3, 3, 1, 2, 3]
print('list2: %s' % list2)
# 删除元素,如果有多个重复的元素,只会删除第一个
list2.remove(1)
print('remove(): %s' % list2)
# 不填写参数: 删除最后一个元素,类似于弹出栈顶元素
list2.pop()
print('pop(): %s' % list2)
# 填写参数: 删除指定索引的元素,如下:删除索引为3的元素
list2.pop(3)
print('pop(): %s' % list2)
# del: 删除指定索引的元素
del list2[0]
print('del: %s' % list2)
# del: 将整个列表删除
del list2
# 放开下面一行代码的注释会导致往后面的代码无法执行,所以这里注释掉了
# print('del: %s' % list2)

# clear(): 清空列表中所有元素,但是并不删除列表
list3 = [1, 2, 3, 4, 5, 6, 7, 8]
print('初始列表: %s' % list3)
list3.clear()
print('clear(): %s' % list3)


# 注意: 使用列表时,不要在循环遍历时删除元素,下面的示例无法实现删除list4中所有元素
list4 = [1, 2, 3, 4, 5]
for i in list4:
    list4.remove(i)
print(list4)

