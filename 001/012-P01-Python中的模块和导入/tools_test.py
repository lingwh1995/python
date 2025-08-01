"""
    Python工具类的导入
"""


# 导入方式1
import tools_1

# 导入方式1+别名: 可以为导入的模块起一个别名
import tools_1 as t1

# 导入方式2: 导入指定模块中的指定成员,相当于将指定模块中的成员(属性和方法)复制一份到当前文件
from tools_2 import Tool

# 导入方式2+别名: 导入指定模块中的指定成员,相当于将指定模块中的成员复制一份到当前文件,并且为导入的模块起一个别名
from tools_2 import Tool as t3

# 导入方式2+*: 导入该模块中全部成员(所有属性和方法),相当于将指定模块中的所有成员复制一份到当前文件
from tools_3 import *

'''
    import导入 和 from-import的区别:
        1.import: 拿到了模块对象的引用地址,通过这个地址来使用模块中的成员,from-import: 将被导入的成员复制一份到本地,所以可以直接访问该成员
        2.import方式导入没有任何限制,from-import导入有些成员是不能被导入的(有权限限制),好处是更加安全
    导入包时查找顺序:
        1.当前程序所在目录
        2.当前程序所在的工程的根目录
        3.环境变量中配置的PYTHONPATH
        4.系统目录
        5.site_packages 第三方模块的安装目录
'''

# 测试import和from-import的区别
# import导入
import tools_4 as t4
# from-import导入
from tools_4 import *


# 导入方式1
def test_import_1():
    # 测试普通函数
    print('导入方式1:', tools_1.add(1, 2))

    # 测试类中的方法
    print('导入方式1:',tools_1.Tool.sub(10, 5))
    print('-------------------------------')


# 导入方式1+别名: 可以为导入的模块起一个别名
def test_import_1_alias():
    # 测试普通函数
    print('导入方式1+别名:', t1.add(1, 2))

    # 测试类中的方法
    print('导入方式1+别名:', t1.Tool.sub(10, 5))
    print('-------------------------------')


# 导入方式2: 导入指定模块中的指定成员,相当于将指定模块中的成员(属性和方法)复制一份到当前文件
def test_import_2():
    # 测试类中的方法
    print('导入方式2:', Tool.sub(10, 5))
    print('-------------------------------')


# 导入方式2+别名: 导入指定模块中的指定成员,相当于将指定模块中的成员复制一份到当前文件,并且为导入的模块起一个别名
def test_import_2_alias():
    print('导入方式2+别名:', t3.sub(10, 5))
    print('-------------------------------')


# 导入方式2+*: 导入该模块中全部成员(所有属性和方法)
def test_import_2_all():
    print('n = %d' % n)
    print('导入方式2+*:', t3.sub(10, 5))
    print('-------------------------------')


# 测试import和from-import的区别
def test_import_and_from_import():
    print('import导入方式:')
    print('x = %d' % t4.x)
    print('_y = %d' % t4._y)
    print('__z = %d', t4.__z)
    print('from_import导入方式:')
    print('x = %d' % x)
    # 放开注释会报错,可以看到from_import导入方式不支持导入私有属性
    # print('_y = %d' % _y)
    # print('__z = %d', __z)
    print('-------------------------------')


# 测试导入方式1
test_import_1()

# 测试导入方式1+别名
test_import_1_alias()

# 测试导入方式2
test_import_2()

# 测试导入方式2+别名
test_import_2_alias()

# 测试导入方式2+*
test_import_2_all()

# 测试import和from-import的区别
test_import_and_from_import()