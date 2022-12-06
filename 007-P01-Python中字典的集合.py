# Python中字典的集合

print('Python中字典的集合')

'''
    集合中不能保存重复的元素
'''

# 定义一个空的字典,注意:定义空的集合用 s = set()
d = {}
print(d)
print(type(d))

# 定义一个空的集合
s = set()
print(s)
print(type(s))

s1 = {1, 2, 3, 4, 5, 6, 7, 7, 7}
print(s1)

# 集合不支持通过下标访问,如果访问的话,会报错: TypeError: 'set' object is not subscriptable
# print(s1[0])

# 遍历set
for s in s1:
    print(s)



