"""
    Python实现学生管理系统
"""


def main():
    while True:
        print('----------------------------------')
        print('1:新增学生信息')
        print('2:删除学生信息')
        print('3:修改学生信息')
        print('4:查询学生信息')
        print('5:显示所有学生信息')
        print('----------------------------------')
        operator_no = int(input('请输入指令编号:'))
        # 新增学生信息
        if 1 == operator_no:
            insert()
        # 删除学生信息
        elif 2 == operator_no:
            delete()
        # 修改学生信息
        elif 3 == operator_no:
            update()
        # 查询学生信息
        elif 4 == operator_no:
            stu_no = input('请输入学生编号:')
            select(stu_no)
        # 显示所有学生信息
        elif 5 == operator_no:
            show()
        else:
            break


stu_infos = []


# 新增学生信息
def insert():
    print('请输入学生信息')
    stu_info = {}
    stu_no = input('请输入学生编号:')
    stu_info['stu_no'] = stu_no
    if select(stu_no) is not None:
        print('已经有该学生信息,请勿重复录入！')
        return
    stu_info['stu_name'] = input('请输入学生姓名:')
    stu_info['stu_age'] = input('请输入学生年龄:')
    stu_info['stu_subject'] = input('请输入学生专业:')
    stu_infos.append(stu_info)
    show()


# 查询学生信息
def select(stu_no):
    for stu_info in stu_infos:
        if stu_no == stu_info['stu_no']:
            print(f"学生编号: {stu_info['stu_no']},学生姓名: {stu_info['stu_name']},"
                  f"学生年龄: {stu_info['stu_age']},学生专业: {stu_info['stu_subject']}")
            return stu_info
        else:
            print('没有查询到该学生信息')
    show()


# 删除学生信息
def delete():
    stu_no = input('请输入学生编号:')
    stu_infos.remove(select(stu_no))
    show()


# 修改学生信息
def update():
    stu_no = input('请输入学生编号:')
    for stu_info in stu_infos:
        if stu_no == stu_info['stu_no']:
            stu_info['stu_name'] = input('请输入学生姓名:')
            stu_info['stu_age'] = input('请输入学生年龄:')
            stu_info['stu_subject'] = input('请输入学生专业:')
        else:
            print('没有查询到该学生信息')


def show():
    print('----------------------------------')
    for stu_info in stu_infos:
        print(f"学生编号: {stu_info['stu_no']},学生姓名: {stu_info['stu_name']},"
              f"学生年龄: {stu_info['stu_age']},学生专业: {stu_info['stu_subject']}")
    print('----------------------------------')


main()
