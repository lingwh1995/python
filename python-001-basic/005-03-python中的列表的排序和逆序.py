"""
    python中的列表的排序和逆序
"""

# 对列表进行排序,从小到大
list1 = [4, 8, 2, 7, 6, 5, 1]
list1.sort()
print(list1)

print('------------------------------------')
# 对列表进行排序,从大到小
list2 = [4, 8, 2, 7, 6, 5, 1]
list2.sort(reverse=True)
print(list2)

print('------------------------------------')
# 逆序,使用python自带库进行逆序
list3 = [1, 2, 3, 4, 5, 'a']
list3.reverse()
print(list3)

print('------------------------------------')
# 逆序,使用自定义算法进行逆序
list4 = [1, 2, 3, 4, 5, 'b']


def reverse(source):
    i = len(source) - 1
#    r_list = list()
    r_list = []
    while i >= 0:
        r_list.append(source[i])
        i -= 1
    return r_list


print(reverse(list4))