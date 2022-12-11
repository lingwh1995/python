# Python中的面向之私有属性和私有方法


print('Python中的面向之私有属性和私有方法')


'''
    私有属性
'''
# 属性name和age是共有的
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '查看类的公有属性:' + self.name + str(self.age)


person1 = Person1('张三',25)
print(person1.name)
print(person1.age)
print(person1)
print('----------------------------------')


# 属性name和age是私有的,只有在类的 内容才能被访问
class Person2:
    def __init__(self, name, age):
        # 私有属性的定义,在属性的标识符前面加上 __
        self.__name = name
        self.__age = age

    # get()和set()方法
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age


    def __str__(self):
        # 注意:在类内容使用私有属性的时候标识符前面也要加__
        return '查看类的私有有属性:' + self.__name + str(self.__age)


person2 = Person2('李四',25)
# 外部访问类内部私有的属性会直接报错
# print(person2.name)
# print(person2.age)
# print(person2.__name)
# print(person2.__age)

# 如果想要强制访问该属性,则使用如下方式,格式是: _类名__属性名,但是一般都要使用 get_属性名() 和 set_属性名() 访问
print(person2._Person2__name)
print(person2._Person2__age)

# 使用get_属性名 和 set_属性名访问
person2.set_name('xxxx')
person2.set_age(88)
print(person2.get_name())
print(person2.get_age())
print(person2)
print('----------------------------------')

'''
    私有方法
'''
class Thunder:
    def add_task(self):
        print('创建任务...')


    # 定义一个私有方法,外部不能直接调用,但是内部可以直接调用
    def __get_resource(self):
        print('获取资源...')

    def download(self):
        self.__get_resource()
        print('下载资源...')

thunder = Thunder()
thunder.add_task()
thunder.download()