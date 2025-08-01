"""
    Python中的字符串常用方法
"""

"""
    find()和index()方法的区别:
        find()方法找不到返回-1，index()方法找不到会报异常
    find()、index和rfind()、rindex()方法区别:
        1.find()、index:从左向右找，rfind()、rindex(): 从右向左找      
        2.find()和rfind()、index()和rindex()方法返回的结果是一样的,只不过是开始查找方向不同
"""

# 定义字符串的几种方式
s1 = 'pythonpython'
s2 = 'p\tython,python,python,pytho n'
s3 = 'pyth\non'
s4 = 'a.txt'
list1 = ['AAA', 'BBB', 'CCC']
s5 = 'pythonpython pythonpython'
s6 = 'python'
s7 = '     python     '


# find()方法: 查询字符或子串在字符串中的索引位置
def test_find_1(target):
    print('%s的索引位置: %d' % (target, s1.find(target)))


# find()方法: 查询字符或子串在字符串中的索引位置
def test_find_2(target, start, end):
    print('%s的索引位置: %d' % (target, s1.find(target, start, end)))


# index()方法: 查询字符或子串在字符串中的索引位置
def test_index_1(target):
    print('%s的索引位置: %d' % (target, s1.index(target)))


# index()方法: 查询字符或子串在字符串中的索引位置
def test_index_2(target, start, end):
    print('%s的索引位置: %d' % (target, s1.index(target, start, end)))


# rfind()方法: 查询字符或子串在字符串中的索引位置
def test_rfind_1(target):
    print('%s的索引位置: %d' % (target, s1.rfind(target)))


# rfind()方法: 查询字符或子串在字符串中的索引位置
def test_rfind_2(target, start, end):
    print('%s的索引位置: %d' % (target, s1.rfind(target, start, end)))


# rindex()方法: 查询字符或子串在字符串中的索引位置
def test_rindex_1(target):
    print('%s的索引位置: %d' % (target, s1.rindex(target)))


# rindex()方法: 查询字符或子串在字符串中的索引位置
def test_rindex_2(target, start, end):
    print('%s的索引位置: %d' % (target, s1.rindex(target, start, end)))


# replace()方法: 全部替换字符或子串
def test_replace_1(old, new):
    result = s1.replace(old, new)
    print('替换后原字符串: %s' % s1)
    print('替换后新字符串: %s' % result)


# replace()方法: 替换指定个数的字符或子串
def test_replace_2(old, new, count):
    result = s1.replace(old, new, count)
    print('替换后原字符串: %s' % s1)
    print('替换后新字符串: %s' % result)


# count()方法: 统计字符/子串在字符串中出现的次数
def test_count_1(target):
    count = s1.count(target)
    print('字符/子串%s在字符串%s中出现的次数: %d' % (target, s1, count))


# count()方法: 统计字符/子串在字符串某部分中出现的次数
def test_count_2(target, start, end):
    count = s1.count(target, start, end)
    print('字符/子串%s在字符串%s中出现的次数: %d' % (target, s1, count))


# split()方法: 分割字符串
def test_split_1(source, separation):
    source_list = source.split(separation)
    print(source_list)


# split()方法: 分割字符串,max_split_times:最大分割次数
def test_split_2(separation, max_split_times):
    s2_list = s2.split(separation, max_split_times)
    print(s2_list)


# split()方法: 分割字符串,使用任意空格作为分隔符分割,不用写任何参数
def test_split_3():
    s2_list = s2.split()
    print(s2_list)


# splitlines()方法: 分割字符串,等同于 s.split('\n')
def test_splitlines():
    s3_list = s3.splitlines()
    print(s3_list)
    print(type(s3_list))


# partition()方法: 分割字符串,1.会保留分割符 2.只会把字符串分割成三段 3.返回值为tuple
# 最佳应用场景: 分割文件名,如 a.txt
def test_partition(source, separation):
    source_tuple = source.partition(separation)
    print(source_tuple)
    print(type(source_tuple))


# join()方法: 遍历字符串中每一个字符/列表(list)中每一个元素,然后使用分隔符连接起来
def test_join(source, separation):
    source_str = separation.join(source)
    print(source_str)
    print(type(source_str))


# startswith()方法: 遍历字符串是否以prefix开始
def test_startswith(prefix):
    is_startswith = s1.startswith(prefix)
    print(is_startswith)


# sufix()方法: 遍历字符串是否以sufix结束
def test_endswith(sufix):
    is_endswith = s1.endswith(sufix)
    print(is_endswith)


# 字符串转大写
def test_upper():
    upper_s1 = s1.upper()
    print(upper_s1)


# 字符串转小写
def test_lower():
    lower_s1 = s1.lower()
    print(lower_s1)


# 字符串每个单词首字母大写
def test_title():
    title_s5 = s5.title()
    print(title_s5)


# 字符串中第一个单词首字母大写
def test_capitalize():
    capitalize_s5 = s5.capitalize()
    print(capitalize_s5)


# 字符串居中对齐
def test_center_1(width):
    center_s6 = s6.center(width)
    print('|' + center_s6 + '|')


# 字符串居中对齐,并且使用字符填充空白处
def test_center_2(width, fill):
    center_s6 = s6.center(width, fill)
    print('|' + center_s6 + '|')


# 字符串居左对齐
def test_ljust_1(width):
    ljust_s6 = s6.ljust(width)
    print('|' + ljust_s6 + '|')


# 字符串居左对齐，并且使用字符填充空白处
def test_ljust_2(width, fill):
    ljust_s6 = s6.ljust(width, fill)
    print('|' + ljust_s6 + '|')


# 字符串居右对齐
def test_rjust_1(width):
    rjust_s6 = s6.rjust(width)
    print('|' + rjust_s6 + '|')


# 字符串居右对齐，并且使用字符填充空白处
def test_rjust_2(width, fill):
    rjust_s6 = s6.rjust(width, fill)
    print('|' + rjust_s6 + '|')


# 字符串居右对齐，并且使用字符填充空白处
def test_rjust_2(width, fill):
    rjust_s6 = s6.rjust(width, fill)
    print('|' + rjust_s6 + '|')


# 字符串去除两端空白
def test_strip():
    strip_s7 = s7.strip()
    print('|' + strip_s7 + '|')


# 字符串去除左端空白
def test_lstrip():
    lstrip_s7 = s7.lstrip()
    print('|' + lstrip_s7 + '|')


# 字符串去除右端空白
def test_rstrip():
    rstrip_s7 = s7.rstrip()
    print('|' + rstrip_s7 + '|')


"""
    find()方法
"""
# 查询单个字符的索引位置
test_find_1('h')
# 查询子串的索引位置
test_find_1('th')
# 查看不存在的字符的索引位置
test_find_1('j')
# 查询单个字符的索引位置
test_find_1('n')
# 在字符串的某段字串中查询单个字符/子串的索引位置
test_find_2('o', 1, 3)
test_find_2('o', 1, 5)

"""
    index()方法
"""
test_index_1('h')
# test_index_2('o', 1, 3)
test_index_2('o', 1, 5)


"""
    rfind()方法
"""
test_rfind_1('h')
test_rfind_2('h', 1, 5)


"""
    rindex()方法
"""
test_rindex_1('h')
test_index_2('o', 1, 5)


"""
    replace()方法
"""
test_replace_1('h', 'H')
test_replace_1('python', 'PYTHON')
test_replace_2('python', 'PYTHON', 1)

"""
    count()方法
"""
test_count_1('p')
test_count_2('p', 0, 6)


"""
    split()方法
"""
test_split_1(s2, ',')
test_split_2(',', 1)
# 分割符使用后会被删除,所以打印的结果中没有th
test_split_1(s2, 'th')
test_split_1(s2, '\t')
# 按照一个空格分割
test_split_1(s2, ' ')
test_split_3()
# 按行分割
test_split_1(s3, '\n')
test_splitlines()


"""
    partition()方法
"""
test_partition(s1, 'th')
test_partition(s4, '.')


"""
    join()方法
"""
test_join(s1, '-')
test_join(list1, '-')


"""
    startswith()方法
"""
test_startswith('p')
test_startswith('py')


"""
    endswith()方法
"""
test_endswith('n')
test_endswith('on')


"""
    upper()方法
"""
test_upper()

"""
    lower()方法
"""
test_lower()


"""
    title()方法
"""
test_title()


"""
    capitalize()方法
"""
test_capitalize()

"""
    center()方法
"""
test_center_1(20)
test_center_2(20, '*')

"""
    ljust()方法
"""
test_ljust_1(20)
test_ljust_2(20, '*')

"""
    rjust()方法
"""
test_rjust_1(20)
test_rjust_2(20, '*')

"""
    strip()方法
    lstrip()方法
    rstrip()方法
"""
test_strip()
test_lstrip()
test_rstrip()