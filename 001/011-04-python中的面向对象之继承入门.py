"""
    python中的面向对象之继承入门
"""


"""
    子类只能调用父类的公有方法,不能调用子类的私有方法
"""


# 父类
class Phone:
    # 创建一个共有方法
    def call(self):
        print('(父类)打电话...')

    # 创建一个私有方法
    def __slide(self):
        print()


# 子类 注意: 子类只能继承父类的共有方法,不能继承父类的私有方法
class IPhone(Phone):
    def play_music(self):
        print('(子类)播放音乐...')


iphone = IPhone()
# 调用父类公有方法
iphone.call()
# 调用子类公有方法
iphone.play_music()

# 调用父类私有方法,会直接报错: AttributeError: 'IPhone' object has no attribute '__slide'
# iphone.__slide()