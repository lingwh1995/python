# Python中的元组(tuple)的定义

print('Python中的元组(tuple)的定义')
'''
    元组:不可变类型
    格式:使用小括号括起来的就是元组
'''


'''
    元组的定义
'''
# 定义一个空的元组
t1 = ()
print(t1)
print(type(t1))

t2 = (1, 2, 3, 4, 5)
print(t2)

t3 = ('1', '2', '3', '4')
print(t3)

# 元组的复杂定义
t4 = (1, 'A', '你好', True)
print(t4)

# 元组中嵌套元组
t5 = (1, 'A', '你好', True, ('hello', 'world'))
print(t5)

# 定义只有一个元素的元组,必须加上逗号,否则会被解析成普通的数字或者字符
t6 = (1,)
print(t6)