"""
    Python中的三目运算
"""


# 使用三目运算符判断奇偶数
def fun():
    while True:
        # Python中没有直接的三目运算，可以使用if else实现
        n = int(input('请输入一个数字:'))

        s = '偶数' if n % 2 == 0 else '奇数'
        print(s)


fun()