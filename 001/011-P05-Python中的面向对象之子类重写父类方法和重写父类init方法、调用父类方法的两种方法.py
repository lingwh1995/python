# Python中的面向对象之子类重写父类方法和重写父类init方法、调用父类方法的两种方法


print('Python中的面向对象之子类重写父类方法和重写父类init方法、调用父类方法的两种方法')


class Cat:
    def __init__(self, name):
        self.name = name
        print('父类init()...')

    def play(self):
        print('父类 play...')


'''
    1.重写父类init()方法
    2.子类重写了父类的init()方法,但是未调用父类init()方法
    3.重写父类非init()方法
'''


class BlueCat(Cat):
    def __init__(self, age):
        self.age = age
        print('子类蓝猫init()...')

    def play(self):
        print('子类蓝猫 play...')


'''
    1.重写父类init()方法
    2.子类重写了父类的init(),并且调用了父类init()方法
    3.重写父类非init()方法,并且重写前调用父类该方法
'''


class MachineCat(Cat):
    def __init__(self, name, age):
        # 调用父类构造方法
        Cat.__init__(self, name)

        self.age = age
        print('子类机器猫init()...')

    def play(self):
        # 调用父类play()方法第一种方式
        # Cat.play(self)
        # 调用父类play()方法第二种方式
        super().play()
        print('子类机器猫 play...')


tom = BlueCat(10)
print(tom.age)
# 调用父类属性会报错
# print(tom.name)
tom.play()
print('---------------------------------')

doraemon = MachineCat('哆啦A梦', 5)
print(doraemon.name)
print(doraemon.age)
doraemon.play()
