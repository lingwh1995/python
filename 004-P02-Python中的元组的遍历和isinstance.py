# Python中的元组(tuple)的遍历

print('Python中的元组(tuple)的遍历')

'''
    元组的遍历 + 判断一个对象是不是元组
'''
t1 = ('a', 'b', 'c')
# for循环遍历
for i in t1:
    print(i)

print('------------')
# for循环配合下标遍历
for i in range(len(t1)):
    print(t1[i])

print('------------')
# while循环配合下标遍历
j = 0
while j < len(t1):
    print(t1[j])
    j = j+1

print('------------')
# 循环遍历嵌套元组
t2 = ('a', 'b', 'c', ('1', '2', '3'))
for i in t2:
# 判断元素是不是元组,isinstance(object, type)
    if isinstance(i, tuple):
        for j in i:
            print(j)
    else:
        print(i)