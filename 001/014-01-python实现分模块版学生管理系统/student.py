"""
    学生实体类
"""


class Student:
    def __init__(self, stu_id, stu_name, stu_age):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age

    # 格式化输入
    def __str__(self):
        return '|' + self.stu_id.ljust(5) + self.stu_name.ljust(10) + str(self.stu_age).ljust(3) + '|'


# 防止测试代码在非测试情况下被执行
if __name__ == '__main__':
    student = Student('001', 'zhangsan', 18)
    print(student)
