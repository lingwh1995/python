"""
    python中的面向对象之多继承父类使用super解决父类重复初始化问题、mro魔法属性使用
"""


"""
    多继承V1: 使用   父类.__init__()
        出现了父类Person被多次初始化的问题
"""


class Person:
    def __init__(self):
        print("person init ...")


class Father(Person):
    def __init__(self):
        # 调用父类初始化方法
        Person.__init__(self)
        print("father init ...")


class Mother(Person):
    def __init__(self):
        # 调用父类初始化方法
        Person.__init__(self)
        print("mother init ...")


class Son(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("son init ...")


son = Son()
print('------------------------------------')


"""
    多继承V2: 使用super(当前类, self).__init__()
        解决了父类Person被多次初始化的问题
"""


class Person:
    def __init__(self):
        print("person init ...")


class Father(Person):
    def __init__(self):
        # 调用父类初始化方法
        super(Father, self).__init__()
        print("father init ...")


class Mother(Person):
    def __init__(self):
        # 调用父类初始化方法
        super(Mother, self).__init__()
        print("mother init ...")


class Son(Father, Mother):
    def __init__(self):
        super(Son, self).__init__()
        print("son init ...")
        # 查看解释器执行继承关系的顺序: __mro__  魔法属性
        print(Son.__mro__)


son = Son()
print('------------------------------------')

"""
    多继承V3: 使用super(当前类, self).__init__(构造参数)
        1.解决了父类Person被多次初始化的问题
        2.出现了实例化子类的父类时报错的问题
"""


class Person:
    def __init__(self, name):
        print("person init ...")
        print(f"参数: name={name}")
        self.name = name


class Father(Person):
    def __init__(self, name, age, hobby):
        # 调用父类初始化方法
        super(Father, self).__init__(name, age)
        print("father init ...")
        print(f"参数: name={name}, age={age}, hobby={hobby}")
        self.hobby = hobby


class Mother(Person):
    def __init__(self, name, age):
        # 调用父类初始化方法
        super(Mother, self).__init__(name)
        print("mother init ...")
        print(f"参数: name={name}, age={age}")
        self.age = age


class Son(Father, Mother):
    def __init__(self, name, age, hobby, gender):
        super(Son, self).__init__(name, age, hobby)
        print("son init ...")
        print(f"参数: name={name}, age={age}, hobby={hobby}, gender={gender}")
        self.gender = gender
        # 查看解释器执行继承关系的顺序: __mro__  魔法属性
        print(Son.__mro__)


# 实例化子类正常
son = Son('姓名', '年龄', '爱好', '性别')
# 实例化子类的父类,会报错
# father = Father('姓名', '年龄', '爱好')
print('------------------------------------')

"""
    多继承V4: 使用super(当前类, self).__init__(构造参数)
        1.解决了父类Person被多次初始化的问题
        2.解决了实例化子类的父类时报错的问题
        3.super(当前类,self)的简化写法super()
        
        多继承参数传递
"""


class Person:
    def __init__(self, name):
        print("person init ...")
        self.name = name


class Father(Person):
    def __init__(self, hobby, *args):
        # 调用父类初始化方法
        # super(Father, self).__init__(*args)
        # super()的简化写法
        super().__init__(*args)
        print("father init ...")
        self.hobby = hobby


class Mother(Person):
    def __init__(self, age, *args):
        # 调用父类初始化方法
        # super(Mother, self).__init__(*args)
        # super()的简化写法
        super().__init__(*args)
        print("mother init ...")
        self.age = age


# # 版本1: 最下层的子类使用可变参数传参,需要考虑顺序
# class Son(Father, Mother):
#     def __init__(self, gender, *args):
#         super(Son, self).__init__(*args)
#         print("son init ...")
#         self.gender = gender
#         # 查看解释器执行继承关系的顺序: __mro__  魔法属性
#         print(Son.__mro__)


# 版本2: 最下层的子类使用正常传参,需要考虑顺序,最好使用这个,因为这样外部调用的时候知道应该传递什么参数
class Son(Father, Mother):
    def __init__(self, gender, hobby, age, name):
        # super(Son, self).__init__(hobby, age, name)
        # super()的简化写法
        super().__init__(hobby, age, name)
        print("son init ...")
        self.gender = gender
        # 查看解释器执行继承关系的顺序: __mro__  魔法属性
        print(Son.__mro__)


# 实例化子类正常(使用 正常传参/可变参数 传参)
son = Son('性别', '爱好', '年龄', '姓名')
print(f"子类对象: name={son.name}, age={son.age}, hobby={son.hobby}, gender={son.gender}")
# 实例化子类的父类,不会报错了(使用 正常传参/可变参数 传参)
father = Father('爱好', '姓名')
print(f"子类的父类对象: name={father.name}, hobby={father.hobby}")

print('*********')

# 实例化子类正常(使用 位置参数(关键字参数) 传参,不用考虑参数顺序)
son = Son(age='年龄', gender='性别', hobby='爱好', name='姓名')
print(f"子类对象: name={son.name}, age={son.age}, hobby={son.hobby}, gender={son.gender}")
print('------------------------------------')
