"""
    python中的面向对象之__dict__
"""

"""
    实例方法、实例属性、类属性
"""


class Cat:
    # 定义一个类属性
    name = '猫咪'

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


tom = Cat('tom')
# 调用实例属性
print(tom.name)
# 调用实例方法方式1
tom.show()
# 调用实例方法方式2
# 调用过程: 从Cat.__dict__中获取类中保存的信息 -> 找到方法名 -> 传递一个实例参数进行方法调用
Cat.show(tom)

# 调用类属性
print(Cat.name)
print('------------------------------------------')

'''
    类方法和静态方法用途和区别?
        用途: 这两种方法适合于写工具类
        区别: 
            1.当不需要使用类中的实例属性时,使用@staticmethod修饰,当需要使用类中的实例属性时,使用@classmethod修饰
            2.类方法常用于模拟java构造函数
        
'''


class MyMath:
    num = 1000

    @classmethod
    def get(cls):
        print(cls.num)

    @classmethod
    def add(cls, a, b):
        return a + b

    @staticmethod
    def show():
        print('I am static method...')


MyMath.get()
print(MyMath.add(10, 20))
MyMath.show()
