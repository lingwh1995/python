"""
    pydoc
"""

import pydoc


# 最简单的函数,没有返回值的函数返回值为None
def fun_1():
    print("Hello first python function!")


# 有参数的函数
def fun_2(name):
    print("接收到name的值: " + name)


# 有返回值的函数,返回值为c
def fun_3(a, b):
    c = a + b
    return c


print(fun_1())
fun_2('zhangsan')
print(fun_3(4, 5))

"""
    使用pydoc.help(函数名查看函数具体描述)
"""
pydoc.help(print)
