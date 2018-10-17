#student.py


 # 修改原来的学生信息管理程序,将原来字典来存储学生信息,
 #  现改为用对象来存储学生信息
 #    # file : student.py  
 #    class Student:
 #        def __init__(self, n, a, s):
 #             ....

 #    L = []
 #    # L.append({...}) 改为对象
 #    L.append(Student('xiaozhang', 20, 100))

 #    (要求类Student 要写在模块 student.py中)
class student(object):
    def __init__(self, name, age, score = '未考' ):
        self.name = name
        self.age = age
        self.score = score
    def set_score(self, score):  #设置方法保护内部数据不会轻易被外部调用修改
        if 0<= score <= 100:
            self.__score = score

while True:
        name = input("请输入姓名：")
        if not name:
            break
        try:
            age = int(input("请输入年龄："))
            while not age :
                age =int(input("请输入年龄："))
            score = int(input("请输入成绩："))
            while not score :
                score = int(input("请输入成绩："))
        except:
            continue
        L = []
        L.append(student(name, age, score))
print(L)
print(L[0].name)