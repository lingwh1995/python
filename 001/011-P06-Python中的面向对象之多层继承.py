"""
    Python中的面向对象之多层继承
"""


"""
    多层继承和多层继承的初始化
"""


class Cat:
    def __init__(self):
        print('爷爷类init()...')

    def sleep(self):
        print('爷爷类 play...')


class BlueCat(Cat):
    def __init__(self):
        # 调用爷爷类__init__方法
        Cat.__init__(self)
        print('父类蓝猫init()...')

    def eat(self):
        print('父类蓝猫 eat...')


class UKBlueCat(BlueCat):
    def __init__(self):
        # 调用父类__init__方法
        BlueCat.__init__(self)
        print('子类英国蓝猫init()...')

    def play(self):
        print('子类英国蓝猫 play...')


cat = UKBlueCat()
cat.sleep()
cat.eat()
cat.play()
