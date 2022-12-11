# Python中的排序函数sort配合lambda

print('Python中的排序函数sort配合lambda')

l1 = [2, 4, 3, 5, 7, 1, 8, 6, 9, 10]
# 简单使用sort()
l1.sort()
print(l1)
print('------------------------------')

l2 = [{'id': 2, 'name': 'zhangsan'}, {'id': 8, 'name': 'lisi'}, {'id': 5, 'name': 'wangwu'}]
# 使用lambda配合sort()根据id从小到大排序
l2.sort(key=lambda i: i['id'])
print(l2)
# 使用lambda配合sort()根据id从大到小排序
l2.sort(key=lambda i: i['id'], reverse=True)
print(l2)