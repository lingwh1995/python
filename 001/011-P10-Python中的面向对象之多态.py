# Python中的面向对象之多态


print('Python中的面向对象之多态')

'''
    多态:父类引用指向子类对象,本质上是调用名称相同的方法,产生了不同的结果
'''


class Animal:
    def eat(self):
        pass


class Duck(Animal):
    def eat(self):
        print('鸭子吃东西...')


class Dog(Animal):
    def eat(self):
        print('狗吃东西...')


duck = Duck()
duck.eat()
dog = Dog()
dog.eat()


class Cat:
    # 定义一个类属性
    name = '猫咪'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


# 调用实例方法
tom = Cat('tom')
print(tom.name)
tom.show()

# 调用类属性
print(Cat.name)
# 调用类方法
Cat.show(tom)
