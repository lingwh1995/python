# Python中的文件操作常用方法

import os

print('Python中的文件操作常用方法')

'''
    操作文件,需要引入os模块
        rename(): 重命名文件或文件夹
        getcwd(): 获取当前工作目录
        listdir(): 获取当前目录下的文件列表
'''
# 重命名文件/文件夹
# os.rename('a.txt', 'a.txt')

# 获取当前工作目录
cwd = os.getcwd()
print(cwd)

# 获取当前目录下的文件列表
file_list = os.listdir('.')
print(file_list)
for file in file_list:
    print(file)