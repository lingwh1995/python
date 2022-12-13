# python工具类

# 如果要使得from-import也能访问到_y这个属性,需要使用__all__来改变私有属性可见性
# __all__ = ['_y']
# 定义一个共有变量
x = 10

# 定义一个私有变量(文件中的私有变量通常在标识符前面加一个_)
_y = 20

# 定义一个私有变量(类中的私有变量通常在标识符前面加两个_)
__z = 30

