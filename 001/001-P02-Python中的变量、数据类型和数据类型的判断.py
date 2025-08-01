"""
    Python中的变量、数据类型和数据类型的判断
"""

# 1.定义变量和使用变量
# 格式: 变量名 = 值
# 使用: 变量名
#
# 2.变量的类型
# 不可变类型:
#     基础数据类型:
#         int 整数类型
#             1, 2 ,3,100,55,23466
#         float 浮点类型(小数,实数)
#             1.0  3.14  23423.4234234
#         str   字符串类型
#             ''	空字符串
#             ' ' 包含一个空格的字符串
#             ' 艺术硕士 '
#             "" 空字符串
#             " " 包含一个空格的字符串
#             " asd fdfwf  "
#             ''' asdf ''' (特殊的字符串定义格式第一种)
#             """ asdf """ (特殊的字符串定义格式第二种)
#
#         bool  布尔类型
#             True
#             False
#
#         tuple 元组
#
# 可变类型:
#     list
#     dict
#     set
#
# 自定义类型：
#     class
# 判断变量类型:
#   type(变量)

# 定义变量
a = 1
b = 3.14
c = 'Hello Python!'
d = "Python 程序员!"
# 特殊的字符串定义格式第一种
e = ''' 三个单引号包裹 '''
# 特殊的字符串定义格式第二种
f = """ 三个双引号包裹 """
g = True

# 打印变量
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# 使用type()判断变量类型
print(type(1))
print(type(a))
print(type(3.14))
print(type(b))
print(type('Hello Python!'))
print(type(c))
print(type("Python 程序员!"))
print(type(d))
print(type(''' 三个单引号包裹 '''))
print(type(e))
print(type(""" 三个双引号包裹 """))
print(type(f))
print(type(True))
print(type(g))