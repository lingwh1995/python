"""
    Python中的换行和for-in-else、while-else
"""


# python换行,使用end进行换行
def fun_1():
    a = 10
    b = 20
    print('a + b = %d' % (a+b), end="  ")
    print('hello')
    print('python')
    print('-------------------------')


# 打印99乘法表
def nine_nine_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print('%d*%d=%d' % (j, i, j*i), end='  ')
        print()
    print('-------------------------')


# for-in-else
def for_in_else_test():
    for i in range(10):
        print(i)
    else:
        print('for-in over')
    print('-------------------------')


# while-else,循环可以执行完的情况,else中代码可以执行
def while_else_test_1():
    i = 0
    while i < 5:
        print(i)
        i += 1
    else:
        print('while over')
    print('-------------------------')


# while-else,循环不能执行完的情况,else中代码不会执行
def while_else_test_2():
    i = 0
    while i < 5:
        i += 1
        if i == 3:
            print('找到3了......')
            break
    else:
        print('while over')
    print('-------------------------')


fun_1()
nine_nine_table()
for_in_else_test()
while_else_test_1()
while_else_test_2()
