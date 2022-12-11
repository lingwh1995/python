# Python中的文件IO操作

print('Python中的文件IO操作')
'''
    读取文件
        read(): 一次性读取全部文件(不适合大文件)
        read(n): 每次读取n个字节,一般指定1024、2048、4096
        readlines(): 一次性读取全部文件,并且将结果封装到list中,list中每一个元素都是一行
    写入文件
        参考读取文件    
'''


# 读取文件全部内容+按字节读取
def read_1():
    # 打开一个文件
    file = open('a.txt', 'rt')
    # 读取全部内容
    # content = file.read()
    # 读取一个字节
    # content = file.read(1)
    # 读取六个字节
    # content = file.read(6)
    # 按字节读取全部内容
    while True:
        content = file.read(1)
        if content == '':
            break
        print(content)
    file.close()


# 读取文件全部内容+按二进制读取+写入
def read_2():
    # 打开一个文件
    file_r = open('a.txt', 'rb')
    file_w = open('b.txt', 'wb')
    # 按字节读取全部内容
    while True:
        content = file_r.read(6)
        # 判断二进制读取是否读取到空值,要使用 b''来判断
        if content == b'':
            break
        print(content)
        file_w.write(content)
    file_r.close()
    file_w.close()


# 按行读取
def read_3():
    file = open('a.txt', 'rt')
    # 每次读取一行
    # content = file.readline()
    # 每次读取多行
    # contents = file.readlines()
    # for content in contents:
    #     print(content, end='')
    # 按行读取全部内容
    while True:
        content = file.readline()
        if content == '':
            break
        print(content, end='')
    file.close()


# read_1()
read_2()
# read_3()