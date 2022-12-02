# Python中的循环

print('Python中的循环')


# for循环遍历字符串
def loop_for_in_1():
    for i in 'abcde':
        print(i)
    print('-------------------------')


# for-in + range打印0~9之间的数字
def loop_for_in_2():
    for i in range(10):
        print(i)
    print('-------------------------')


# for-in + range打印2~9之间的数字
def loop_for_in_3():
    for i in range(2, 10):
        print(i)
    print('-------------------------')


# for-in + range打印2~9之间的数字,并且步长为2
def loop_for_in_4():
    for i in range(2, 10, 2):
        print(i)
    print('-------------------------')


# while循环打印1到9之间的数字,步长为1
def loop_while_1():
    i = 0
    while i < 10:
        print(i)
        i += 1
    print('-------------------------')


# while循环打印1到9之间的数字,步长为2
def loop_while_2():
    i = 0
    while i < 10:
        print(i)
        i += 2
    print('-------------------------')


loop_for_in_1()
loop_for_in_2()
loop_for_in_3()
loop_for_in_4()
loop_while_1()
loop_while_2()