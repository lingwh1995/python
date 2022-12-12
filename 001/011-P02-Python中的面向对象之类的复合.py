# Python中的面向对象之类的复合


print('Python中的面向对象之类的复合')


class Dog:
    def eat(self):
        print('狗吃东西...')


class Person:
    # 添加一条狗
    def __init__(self):
        self.dog = None

    def add_dog(self, dog):
        self.dog = dog

    def look_dog(self):
        print('人看狗吃东西')
        self.dog.eat()


dog = Dog()
person = Person()
person.add_dog(dog)
person.look_dog()