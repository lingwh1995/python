"""
    python中的关键字
"""

# 导入keyword模块
import keyword

# 打印所有关键字
print(keyword.kwlist)

"""
    Python中所有的关键字如下:
    [
        'False', 'None', 'True', 'and', 'as', 
        'assert', 'async', 'await', 'break', 'class', 
        'continue', 'def', 'del', 'elif', 'else', 
        'except', 'finally', 'for', 'from', 'global', 
        'if', 'import', 'in', 'is', 'lambda', 
        'nonlocal', 'not', 'or', 'pass', 'raise', 
        'return', 'try', 'while', 'with', 'yield'
    ]
    
    在定义标识符时,不要使用 关键字 做为标识符名,会报错
"""