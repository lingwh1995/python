"""
    python中的局部变量和全局变量
"""

"""
    求函数中的最大值和最小值
"""

# 不可变对象
a = 10
b = 20
c = 30
# 可变对象
d = []

# 如果直接修改全局变量的值不影响后续使用
def show1():
    a = 100
    print(a)


# 如果先使用全局变量的值,再使用就会报错,必须保证在修改这个全局变量值之前,没有进行过任何修改
def show2():
    # 会报错: UnboundLocalError
    print(b)
    b = 200
    print(b)


# 使用global关键字修饰才能先使用,再修改
def show3():
    global c
    print(c)
    c = 300
    print(c)


# 不用global关键字修饰才,可以直接先使用再修改
def show4():
    print(d)
    d.append('a')
    print(d)


show1()
# show2()
show3()
show4()