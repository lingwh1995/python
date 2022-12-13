# Python中的面向对象之多继承顺序改变mro顺序


print('Python中的面向对象之多继承顺序改变mro顺序')


class Person:
    def __init__(self):
        print("person init ...")


class Father(Person):
    def __init__(self):
        # 调用父类初始化方法
        super().__init__()
        print("father init ...")


# 第一种继承顺序
class Mother(Person):
    def __init__(self):
        # 调用父类初始化方法
        super().__init__()
        print("mother init ...")


# 第二种继承顺序
class Son1(Father, Mother):
    def __init__(self):
        super().__init__()
        print("son init ...")
        # 查看解释器执行继承关系的顺序: __mro__  魔法属性
        print(Son1.__mro__)


class Son2(Mother, Father):
    def __init__(self):
        super().__init__()
        print("son init ...")
        # 查看解释器执行继承关系的顺序: __mro__  魔法属性
        print(Son2.__mro__)


son1 = Son1()
son2 = Son2()