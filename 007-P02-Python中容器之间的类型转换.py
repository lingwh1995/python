# Python中容器之间的类型转换

print('Python中容器之间的类型转换')

'''
    set-list-tuple之间的转换
'''

s = 'hello'
print(s)

# str->list
l = list(s)
print(l)

# list->set 注意:set(集合)是无序的
s1 = set(l)
print(s1)

# str->set
s2 = set(s)
print(s2)

# list->str
print(str(l))