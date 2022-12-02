# Python中的数据类型转换
print('Python中的数据类型转换!')

a = '1'
b = '2'
print(a + b)

# 字符串类型的数字->整形数据
int_a = int(a)
int_b = int(b)
print(int_a + int_b)

# 整形数据->字符串类型的数字
str_a = str(int_a)
str_b = str(int_b)
print(str_a + str_b)

# 浮点类型数据->整形数据
print(int(1.1))

# 字符串类型的浮点类型数据->整形数据
print(int(float('1.1')))

# 数字编码->阿拉伯数字/字母
print(chr(48))
print(chr(65))
print(chr(97))

# 阿拉伯数字/字母->数字编码
print(ord('0'))
print(ord('A'))
print(ord('a'))