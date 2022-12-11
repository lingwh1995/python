# Python中的高阶函数filter配合lambda

print('Python中的高阶函数filter配合lambda')

'''
    filter函数作用: 会对参数序列中的元素过滤,返回一个filter对象,如果要转换为list,可以使用list()进行转换
        接收两个参数,第一个为函数,第二个为参数序列(实际上就是一个容器:list),序列中的每个元素作为参数传递给函数进行判断,然后返回True或者False,最后将返回True的元素放到新列表中  
'''

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 获取偶数
def get_even(i):
    return i % 2 == 0


l2_o = filter(get_even, l1)
l2 = list(l2_o)
print(l2)
