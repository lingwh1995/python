# Python中的引用

print('Python中的引用')

a = 100
b = a
print(f'100的引用: {id(100)}')
print(f'a的引用:   {id(a)}')
print(f'b的引用:   {id(b)}')
print('------------------------')
a = 200
print(f'200的引用: {id(200)}')
print(f'a的引用:   {id(a)}')
print(f'b的引用:   {id(b)}')
print('------------------------')
b = a
print(f'b的引用:   {id(b)}')
