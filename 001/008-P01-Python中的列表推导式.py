# Python中的列表推导式

print('Python中的列表推导式')

# 创建一个具有一百个数字(0到99)的列表方式1:使用循环创建
l1 = []
for i in range(100):
    l1.append(i)
print(l1)
print("---------------------------")

# 创建一个具有一百个数字(0到99)的列表方式2:使用列表推导式
l2 = [i for i in range(100)]
print(l2)
print("---------------------------")

# 创建一个具有50个数字(0到99之间的偶数)的列表方式
l3 = [i for i in range(100) if i % 2 == 0]
print(l3)
print("---------------------------")

# 创建一个具有10个元组的列表方式
l5 = [(i, i) for i in range(10)]
print(l5)
print("---------------------------")

# 在列表推导式中使用双重循环
l6 = [(x, y) for x in range(10) for y in range(3)]
print(l6)
