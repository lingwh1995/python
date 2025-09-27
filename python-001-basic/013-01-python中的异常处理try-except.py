"""
    python中的异常处理try-except
"""


s = 'hello'

# 捕获一个异常
try:
    s.index('x')
except Exception as e:
    print('查找的字串不存在...', e)
finally:
    print('finally...')
print('---------------------------')


# 捕获多个异常
try:
    1/0
    s.index('x')
except (ZeroDivisionError, NameError) as e:
    print('查找的字串不存在...', e)
finally:
    print('finally...')
print('---------------------------')


# 捕获一个异常
try:
    print('hello python')
except Exception as e:
    print('发生异常时执行...', e)
else:
    print('没有发生异常时执行...')
finally:
    print('finally...')
