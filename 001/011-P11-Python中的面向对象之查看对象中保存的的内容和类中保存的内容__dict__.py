# Python中的面向对象之查看对象中保存的的内容和类中保存的内容__dict__


print('Python中的面向对象之查看对象中保存的的内容和类中保存的内容__dict__')

'''
    __dict__中存储着对象中保存的的内容和类中保存的内存
'''
class Cat:
    # 定义一个类属性
    name = '猫咪'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


tom = Cat('tom')
jack = Cat('jack')

print(Cat.__dict__)
print(tom.__dict__)
print(jack.__dict__)
