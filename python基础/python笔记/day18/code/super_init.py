# super_init.py

# 此示例示意 用super函数显示调用基类__init__初始化方法
class Human:
    def __init__(self, n, a):
        self.name, self.age = n, a
        print("Human的__init__方法被调用")

    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)


class Student(Human):
    def __init__(self, n, a, s=0):
        super().__init__(n, a)  # 显式调用父类的初始化方法
        self.score = s  # 添加成绩属性
        print("Student类的__init__方法被调用")

    def infos(self):
        super().infos()  # 调用父类的方法
        print("成绩:", self.score)


s1 = Student('小张', 20, 100)
s1.infos()

