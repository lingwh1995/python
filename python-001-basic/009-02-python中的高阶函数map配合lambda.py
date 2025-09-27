"""
    python中的高阶函数map配合lambda
"""

"""
    map函数作用: 对参数列表中的元素做一个映射
"""

l = [1, 2, 3, 4]
print(f'初始的list: {l}')


def double(i):
    return i * 2


# 使用map函数对list中每一个元素进行映射
m_o = map(double, l)
# 注意:经过map映射的list是一个object对象
print(f'经过map映射的list(未进行数据类型转换前): {m_o}')
# 将object对象转为list对象
m_l = list(m_o)
print(f'经过map映射的list(进行数据类型转换后): {m_l}')
print('------------------------------')

# 注意:经过map映射的list虽然不能直接打印出来,但是可以直接使用for循环进行遍历,因为遍历的时候,解释器自动对数据类型做了转换
for o in map(double, l):
    print(o)
print('------------------------------')

# map()和lambda配合使用
l_m_o = map(lambda x: x * 10, l)
l_m_l = list(l_m_o)
print(f'map()和lambda配合使用: {l_m_l}')
print('------------------------------')


# map()实现原理: 自己定义一个map()函数
def my_map(fun, source):
    # 定义一个新的列表,用于保存计算后的结果
    result = []
    for s in source:
        result.append(fun(s))
    return result


# 测试自己定义的map()
m_m_l = list(my_map(double, l))
print(m_m_l)
