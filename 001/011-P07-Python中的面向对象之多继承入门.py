# Python中的面向对象之多继承


print('Python中的面向对象之多继承')


class Father:
    def eat(self):
        print('父亲类 eat...')


class Mother():
    def play(self):
        print('母亲类 play...')


class Son(Father, Mother):
    pass


son = Son()
son.eat()
son.play()