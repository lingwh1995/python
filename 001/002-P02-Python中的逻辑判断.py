"""
    Python中的逻辑判断
"""


def is_adult(age):
    print(f'用户输入的年龄:{age}')
    if age >= 18:
        print("成年人......")
    else:
        print("未成年人......")


userAge = int(input('请输入年龄:'))
is_adult(userAge)


