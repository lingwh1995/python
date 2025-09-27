"""
    python中的字符串和下标
"""

# 定义字符串的几种方式
a = '12345'
b = "12345"
c = '''12345'''
d = """12345"""

print(a)
print(b)
print(c)
print(d)

# 字符串的下标,使用下标访问字符串中每一个字符
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# 打印不存在的字串会报错,IndexError: string index out of ranget):
# print(a[5])

s = '12345'


# 遍历字符串,for-in遍历
def loop_print_str_1():
    for i in s:
        print(i)
    print('-----------------')


# 遍历字符串,for-in+range()+len()遍历
def loop_print_str_2():
    for i in range(len(s)):
        print(s[i])
    print('-----------------')


# 遍历字符串,while+len()遍历
def loop_print_str_3():
    i = 0
    while i < len(s):
        print(a[i])
        i += 1
    print('-----------------')


loop_print_str_1()
loop_print_str_2()
loop_print_str_3()

# len()函数
print('字符串s的长度: %d' % len(s))