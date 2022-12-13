"""
    判断python中程序的制动执行和被动执行
    name = __main__ :程序主动执行(就是在当前类发起执行的)
    name = execute  :程序被动执行(就是在其他类调用/导入发起执行的)
"""
print('name', __name__)

if __name__ == '__main__':
    print('主动执行......')
else:
    print('被动执行......')