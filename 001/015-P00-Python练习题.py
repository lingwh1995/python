# Python练习题
import functools
import random

print('Python练习题')


# 有四个数字, 1,2,3,4 能组成多少个互不相同且无重复的三位数?各是多少?
def exercise_1():
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                # 判断无重复
                if i != j and j != k and i != j:
                    # 拼接三位数的方法第一种
                    print(f'{i}{j}{k}')
                    # 拼接三位数的方法第二种
                    print(i*100 + j*10 + k)


# 求出100以内所有的素数(只能被1和本身除尽的数)
def exercise_2():
    for i in range(1, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


# 水仙花数: 一个三位数,每一位的立方之和等于其本身 153 = 1 + 125 + 27
def exercise_3():
    for i in range(100, 1000):
        a = i // 100
        b = i % 100 // 10
        c = i % 10
        if (a ** 3) + (b ** 3) + (c ** 3) == i:
            print(i)


# 输入若干数字,求输入的数字中最大值、最小值、平均值、总和,按q退出
def exercise_4():
    nums = []
    while True:
        user_in = input('请输入:')
        if user_in.isdigit():
            nums.append(int(user_in))
        elif user_in == 'q':
                break
        else:
            print('输入的数据不合法')

    nums.sort()
    sum = functools.reduce(lambda a,b: a+b, nums)
    print('最大值:',nums[len(nums)-1])
    print('最小值:',nums[0])
    print('总和:',sum)
    print('平均值:',sum/len(nums))


# 利用随机数获取一个四位的验证码,包含数字和字母
# 然后输入看到的验证码,直到输入正确程序结束,如果输入错误持续输入直到输入正确为止
def exercise_5():
    """
        准备知识:
            0-9: 48-57
            A-Z: 65-90
            a-z: 97-122
    """
    code = ''
    i = 0
    while True:
        n = random.randint(48, 122)
        if n in range(48,58) or n in range(65,91) or n in range(97,123):
            code += chr(n)
            i = i + 1
        if i == 4:
            break
    print('生成的验证码是:', code)
    while True:
        input_code = input('请输入验证码:')
        if code == input_code:
            print('验证成功')
            break


# 循环输入若干次字符,输入q时退出,统计数字、字母、空白、其他字符各有多少(一次只允许输入一个字符)
def exercise_6():
    # 四个元素分别代表: 数字、字母、空白、其他字符
    count_result = [0,0,0,0]
    while True:
        user_input = input('请输入:')
        if user_input == 'q':
            break
        else:
            user_input = user_input[:1]
            if user_input.isdigit():
                count_result[0] += 1
            elif user_input.isalpha():
                count_result[1] += 1
            elif user_input.isspace():
                count_result[2] += 1
            else:
                count_result[3] += 1

    print('digit:',count_result[0])
    print('alpha:',count_result[1])
    print('space:',count_result[2])
    print('other:',count_result[3])


# 输入两个数字a和b,求 n = a + aa + aaa + aaaa 的值
# 例如,输入2,5  求 2 + 22 + 222 + 2222 + 22222 = 24960 此时共有5个数字相加
# 输出格式为: x + xx + xxx + xxxx + xxxxx = n 的格式
def exercise_7():
    user_input = input('请输入:')
    n = user_input.split(',')[0]
    t = int(user_input.split(',')[1])
    total = 0
    expression = ''
    for i in range(1, t+1):
        num_str = n * i
        total += int(num_str)
        if i == t:
            expression += num_str
        else:
            expression += num_str + ' + '
    expression = expression + ' = ' + str(total)
    print('total:', total)
    print('expression:', expression)


# 从姓和名中各取出一个,组成一个随机的姓名
def exercise_8():
    first_names = ['赵','钱','孙','李','周','吴','郑','王']
    last_names = ['强','旭阳','宝','红梅','杰','伟','波','浪']
    first_name = first_names[random.randint(0,len(first_names)-1)]
    last_name = last_names[random.randint(0,len(last_names)-1)]
    print('姓名:', (first_name + last_name))


# 求最小字串
def exercise_9():
    str_list = ['abcdef','abcd','ab','abc']
    str_list.sort(key=lambda l:len(l))
    short_str = str_list[0]
    for i in range(1, len(short_str)+1):
        for s in str_list:
            if short_str[:i] != s[:i]:
                return short_str[:i-1]
    return short_str[:i]


# 按照从高到低顺序统计文本中单词出现的频率
def exercise_10():
    file_r = open('c.txt','rt')
    word_list = file_r.read().split()
    word_set = set(word_list)
    count_dict = {}
    for word in word_set:
        t = word_list.count(word)
        count_dict[word] = t
    # 对字典进行排序
    count_dict = sorted(count_dict.items(), key=lambda w:w[1])
    print(count_dict)


# exercise_1()
# exercise_2()
# exercise_3()
# exercise_4()
# exercise_5()
# exercise_6()
# exercise_7()
# exercise_8()
# print(exercise_9())
exercise_10()
