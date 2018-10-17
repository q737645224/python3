# inherit.py


# 此示例示意单继承的用法:
class Human:  # 人类的共性
    def say(self, what):
        print("say:", what)

    def walk(self, distance):  # 走路
        print("走了", distance, '公里')


class Student(Human):
    def study(self, subject):
        print("正在学习:", subject)


class Teacher(Student):
    '''说话,行走,教学'''
    def teach(self, subject):
        print("正在教:", subject)

h1 = Human()
h1.say('天气晴了')
h1.walk(5)
print('---------------')
s1 = Student()
s1.walk(4)
s1.say('感觉有点累')
s1.study('Python')
print('===============')
t1 = Teacher()
t1.walk(6)
t1.say('吃点啥好呢')
t1.teach('面向对象')
t1.study('转魔方')



