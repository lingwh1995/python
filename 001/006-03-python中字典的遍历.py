"""
    python中字典的遍历
"""

# 定义一个空的字典
ed = {}
print(ed)
print(type(ed))

# 定义一个标准的字典
d = {'one': '周一', 'two': '周二', 'three': '周三'}
print(d)

# 方式一:使用for-in遍历
for k in d:
    print('%s->%s' % (k, d[k]))
    print(f'{k} -> {d[k]}')

print('------------------')

# 方式二:使用keys()方法遍历
print(d.keys())
for k in d.keys():
    print(f'{k} -> {d[k]}')

print('------------------')

# 方式三:使用values()方法遍历，但是只能获取到字典中所有的值，不能获取到键
print(d.values())
for v in d.values():
    print(f'{v}')

print('------------------')

# 方式四:打印items
print(d.items())
for item in d.items():
    print(f'{item[0]} -> {item[1]}')

for k, v in d.items():
    print(f'{k} -> {v}')

# 解包
a, b, c, e, f = 1, 2, 3, 4, 5
print(f'a = {a}')
print(f'b = {b}')

t = (6, 7, 8, 9, 10)
h, i, j, k, l = t
print(f'h = {h}')
print(f'i = {i}')