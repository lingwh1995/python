"""
    python中的面向对象、魔法方法和self对象
"""

"""
    面向对象入门
"""


# 经典类1
class Dog:
    def eat(self):
        print('dog eat...')

    def drink(self):
        print('dog drink...')


# 经典类2
class Cat():
    def eat(self):
        print('cat eat...')

    def drink(self):
        print('cat drink...')


# 新式类
class Person(object):
    def eat(self):
        print('person eat...')

    def drink(self):
        print('person drink...')


# 创建对象
dog = Dog()
dog.eat()
dog.drink()

cat = Cat()
cat.eat()
cat.drink()

person = Person()
person.eat()
person.drink()
print('-------------------------------------------------')

"""
    动态绑定方属性
"""


class Sheep:
    def eat(self):
        print(self.name, 'person eat...')

    def drink(self):
        print(self.name, 'person drink...')


# 注意:动态绑定属性只能为每一个具体的对象绑定,并不是绑定到这个类上了
sheep1 = Sheep()
sheep1.name = 'duoli'
sheep1.eat()
sheep1.drink()

sheep2 = Sheep()
# 下面代码会报错: 原因是没有给属性name赋值
# sheep2.drink()
print('-------------------------------------------------')

"""
    1.使用__init__ + self绑定方属性
        __init__: 会在创建对象时自动调用
        self: 这个参数调用方法时不用传递,解释器会自动填充这个参数
    2.使用__str__ + str()格式化输出对象
        类似于java中toString()方法,但是必须返回一个字符串类型的数据
    3.self对象可以理解为java中的this,用来代指当前类本身    
"""


class Pig(object):
    # 初始化方法
    def __init__(self, name, age):
        print('__init__执行了')
        # 绑定属性
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, 'person eat...')

    def drink(self):
        print(self.name, 'person drink...')

    # 格式化输出方法
    def __str__(self):
        # print(f'pig的name是:{self.name},pig的age是:{self.age}')
        return 'name:' + str(self.name) + ',age:' + str(self.age)

    # 删除对象时回收资源时会自动调用该方法
    def __del__(self):
        print('over...')

# __init__ + self
pig1 = Pig('佩奇', 5)
print(pig1.name, pig1.age)
pig1.eat()
pig1.drink()

pig2 = Pig('乔治', 10)
print(pig2.name, pig2.age)
pig2.eat()
pig2.drink()

# __str__
print(pig1)
print(pig2)

# __del__ ,del关键字用于手动释放资源
del pig1
