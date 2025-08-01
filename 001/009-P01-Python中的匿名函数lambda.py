"""
    Python中的匿名函数lambda
"""

print('Python中的匿名函数lambda')

"""
    格式
    lambda [形参1], [形参2], ... : [单行表达式] 或 [函数调用]

    lambda函数和普通函数的区别:
        1. lambda 没有函数名
        2. lambda 函数列表外没有括号
        3. lambda 在函数体中,只能实现简单的表达式或者函数调用
        4. lambda 在函数体中,不能使用return、if、while、for-in都不行,print()可以
            为什么不能使用return?
                lambda表达式默认就会返回计算结果,如果加return则会报语法错误
            为什么不能使用if?
                不支持if,但是支持包含if的三目运算符    
            为什么不能使用while、for-in?
                lambda中有自己的遍历元素的方式,不能使用传统循环遍历元素
        5. lambda 在函数体中,可以使用if实现三目运算符
    作用: 使用高阶函数时使用lambda进行传参    
"""

# 把lambda函数的引用赋给一个变量(不传递参数)
l_func1 = lambda: 1 + 2
print(l_func1)
l_func1()
print('------------------------------')

# 把lambda函数的引用赋给一个变量(传递参数)
l_func2 = lambda x: x * 10
print(l_func2(2))
print('------------------------------')

# 把lambda函数的引用赋给一个变量(传递参数+直接打印)
l_func3 = lambda x: print(x * 10)
l_func3(3)
print('------------------------------')

# 在lambda中使用包含if的三目运算表达式
l_func4 = lambda n: '偶数' if n % 2 == 0 else '奇数'
print(l_func4(1))
print(l_func4(2))
