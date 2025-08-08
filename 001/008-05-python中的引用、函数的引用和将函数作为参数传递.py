"""
    python中的引用、函数的引用和将函数作为参数传递
"""

"""
    引用
"""
a = 100
b = a
print(f'100的引用: {id(100)}')
print(f'a的引用:   {id(a)}')
print(f'b的引用:   {id(b)}')
print('------------------------')
a = 200
print(f'200的引用: {id(200)}')
print(f'a的引用:   {id(a)}')
print(f'b的引用:   {id(b)}')
print('------------------------')
b = a
print(f'b的引用:   {id(b)}')
print('------------------------------------------------')

"""
    函数的引用:python中很特别的一点是可以把函数的引用赋值给另一个变量
"""


def show():
    print('I am show!')


show()

# 把函数show()的引用赋值给另一个变量
show_new = show
show_new()
print(f'show():     {show}')
print(f'show_new(): {show_new}')
print('------------------------------------------------')


def call_function(func):
    func()


call_function(show)
call_function(show_new)
