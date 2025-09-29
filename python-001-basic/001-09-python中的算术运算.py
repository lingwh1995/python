"""
    python中的算术运算
"""

# 加法
print(1 + 2)
print('1+2 = %d' % (1 + 2))
print('1'+'2')
print("'1'+'2' = %s" % ('1' + '2'))
print('a'+'a')
print("'a'+'a' = %s" % ('a' + 'a'))
# 错误运算: NameError: name 'a' is not defined
# print(a+a)
# 错误运算: TypeError: can only concatenate str (not "int") to str
# print('1'+2)


# 乘法
print(2 * 3)
print('2 * 3 = %d' % (2 * 3))
print('a' * 3)
print("'a'* 3 = %s" % ('a' * 3))
# 错误运算: NameError: name 'a' is not defined
# print(a*3)


# 普通除法
print(4 / 2)
print('4/2= %d' % (4 / 2))
print(10 / 3)
print('10/3= %f' % (10 / 3))

# 取整除法(地板除)
print(4 // 2)
print(10 // 3)


# 取余(取模)
print(4 % 2)
print(10 % 3)


# 乘方
# 2的2次方
print(2 ** 2)
print('2 ** 2 = %d' % (2 ** 2))
# 2的3次方
print(2 ** 3)
print('2 ** 3 = %d' % (2 ** 3))
# 2的4次方
print(2 ** 4)
print('2 ** 4 = %d' % (2 ** 4))