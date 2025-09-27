"""
    实现学生增删改查逻辑实现
"""

from student import *


class StudentManagerSystem:
    def __init__(self):
        self.students = {}

    # 启动学生管理系统
    def start(self):
        print('系统启动...')
        self.__load()
        while True:
            self.__print_menu();
            operate_id = input('请输入功能编号:')
            n = int(operate_id)
            if n < 0 or n > 5:
                print('暂无此功能...')
            else:
                self.__operate(operate_id)

    # 打印菜单
    def __print_menu(self):
        print('*' * 30)
        print('欢迎使用【学生管理系统】 V1.0')
        print('1.添加学生')
        print('2.删除学生')
        print('3.修改学生')
        print('4.查询学生')
        print('5.显示学生')
        print('0.退出系统')
        print('*' * 30)

    # 选择操作
    def __operate(self, operate_id):
        print('选择了功能:', operate_id)
        # 将功能id和方法对应,封装在字典中,模拟switch-case功能
        method_dict = {
            '1': self.__add,
            '2': self.__remove,
            '3': self.__update,
            '4': self.__get,
            '5': self.__show,
            '0': self.__exit
        }

        # 通过接收id,去字典中查询相关方法,并执行
        method = method_dict[operate_id]

        if operate_id == '2' or operate_id == '3' or operate_id == '4':
            stu_id = input('请输入要操作的学生id:')
            method(stu_id)
        elif operate_id == 0:
            method(0)
        else:
            method()

    # 添加学生
    def __add(self):
        stu_id = input('请输入学生编号:')
        stu_name = input('请输入学生姓名:')
        stu_age = input('请输入学生年龄:')
        self.students[stu_id] = Student(stu_id, stu_name, stu_age)
        self.__show()

    # 删除学生
    def __remove(self, stu_id):
        student = self.__get(stu_id)
        if None == student:
            print('没有查找到id为%s的学生,无法删除' % stu_id)
        else:
            self.students.pop(stu_id)
        self.__show()

    # 修改学生
    def __update(self, stu_id):
        student = self.__get(stu_id)
        if None == student:
            print('没有查找到id为%s的学生,无法修改' % stu_id)
        else:
            stu_name = input('请输入学生姓名:')
            stu_age = input('请输入学生年龄:')
            self.students[stu_id] = Student(stu_id, stu_name, stu_age)
        self.__show()

    # 查询学生
    def __get(self, stu_id):
        student = None
        if stu_id in self.students:
            student = self.students[stu_id]
            print(student)
        return student

    # 显示学生
    def __show(self):
        for k, v in self.students.items():
            print(f'{k}: {v}')

    # 退出系统
    def __exit(self):
        print('退出系统')
        self.__save()
        exit(0)

    # 保存学生数据
    def __save(self):
        file_w = open('mock.db', 'wt')
        for student in self.students.values():
            print(student)
            # 将字符串转换为一个字符串对象
            student_str = student.stu_id + ',' + student.stu_name + ',' + student.stu_age
            file_w.write(student_str)
        file_w.close()

    # 加载学生数据
    def __load(self):
        file_r = None
        try:
            file_r = open('mock.db', 'rt')
        except Exception as e:
            print(e, '文件不存在')
        else:
            students = file_r.readlines()
            for student in students:
                self.students[student.split(',')[0]] = Student(student.split(',')[0], student.split(',')[1],
                                                               student.split(',')[2])
        finally:
            if file_r is not None:
                file_r.close()
