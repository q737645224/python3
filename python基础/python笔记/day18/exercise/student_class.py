# 练习:
#   用类来描述一个学生的信息(可以修改之前写的Student类)
#     class Student:
#          .... 此处自己实现

#     学生信息有:
#        姓名, 年龄, 成绩

#     将一些学生的对象存于列表中,可以任意添加和删除学生信息
#       1) 打印出学生的个数
#       2) 打印出所有学生的平均成绩
#       3) 打印出所有学生的平均年龄


class Student:
    docs = []  # 用来存储所有学生信息(类变量)

    def __init__(self, n, a, s):
        self.name, self.age, self.score = n, a, s

    @classmethod
    def add_student(cls):
        s = Student('小张', 20, 100)
        cls.docs.append(s)
        s = Student('小李', 18, 98)
        cls.docs.append(s)

    @classmethod
    def get_student_count(cls):
        return len(cls.docs)

    @classmethod
    def get_avg_score(cls):
        ''' 获取所有学生的平均成绩'''
        total = 0.0
        for s in cls.docs:
            total += s.score
        return total / len(cls.docs)

Student.add_student()  # 添加学生
print('当前有%d个学生' % Student.get_student_count())
print('当前学生的平均成绩是:', Student.get_avg_score())
