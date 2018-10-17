# hday17.py
# class  Dog(object):
#     """docstring for  Dog"""
#     def eat(self, food):
#         print("吃东西", food)
#     def sleep(self, hour):
#         print("小时", hour)
#     def play(self, obj):
#         print("玩", obj)

# dog1 = Dog()
# dog2 = Dog()
# dog1.eat("骨头")
# dog2.eat("肉")
# dog1.sleep("2")
# dog2.sleep("4")

# class Dog:
#   def eat(self, food):
#     print(self.color, 'de ', self.kinds, '正在吃', food)
# dog1 = Dog()
# dog1.kinds = '京巴'  #添加实例属性
# dog1.color = '白色'
# dog1.color = '黄色' #修改实例属性的绑定关系

# dog2 = Dog()
# dog2.kinds = '藏獒'
# dog2.color = '棕色'
# print(dog1.color, '的', dog1.kinds)
# print(dog2.color, '的', dog2.kinds)
# dog1.eat("骨头")


# 自己写一个'人'类: Human
#   class Human:
#       def set_info(self, name, age, address='未知'):
          # '''此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性'''
          # ...  # << 此处自己实现
      # def show_info(self):
          # '''显示此人的全部信息'''
          # ... # 此处自己实现




# 写一个Student类
#     1) 为该类添加初始化方法, 实现在创建对象时自动设置
#       '姓名','年龄', '成绩' 属性
#     2) 添加set_score方法能修改成绩信息
#     3) 添加show_info方法打印学生对象的信息

# class student(object):
#     def __init__(self, name, age, score = '未考' ):
#         self.name = name
#         self.age = age
#         self.score = score
#     def set_score(self, score):  #设置方法保护内部数据不会轻易被外部调用修改
#         if 0<= score <= 100:
#             self.__score = score
#     def show_info(self):
#         print(self.name, self.age, self.score)
# L = []
# L.append(student("小明", 20, 60))
# L.append(student("小包", 54))
# L.append(student("效果", 54, 90))
# L[2].set_score(89)
# for o in L:
#     o.show_info()


# 面向对向的综合示例:
#   有两个人(Human):
#     1.
#       姓名: 张三
#       年龄: 35
#     2.
#       姓名: 李四
#       年龄: 8
#     行为:
#       1. 教别人学东西 teach
#       2. 赚钱 works
#       3. 借钱 borrow
#     事情:
#       张三 教 李四 学 python
#       李四 教 张三 学 跳皮筋
#       张三 上班赚了 1000 元钱
#       李四 向 张三 借了 200 元钱
#       打印张三的信息: 35岁 的 张三 有钱 800元, 它学会跳皮筋
#       打印李四的信息: 8岁 的 李四 有钱 200元, 它学会python


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def teach1(self):
#         self.teach1 = python
#     def teach2(self):
#         self.teach2 = "跳皮筋"
#     def works(self, m):
#         self.m = m
#     def borrow(self, m):
#         self.m = m
# h1 = Human("张三", 35)
# h2 = Human("李四", 8)
# h1.teach1()
# h2.teach2()
# h1.works(800)
# h2.borrow(200)


class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.money = 0 #添加
        self.skill = [] #技能
    def teach(self, other, skill):
        print(self.name, '教', other.name, '学', skill)
        other.skill.append(skill)  #让other增加技能
    def works(self, money):
        print(self.name, '上班赚了', money, '元钱')
        self.money += money

    def borrow(self, other, m):
        if other.money:
            print(self.name, '向', other.name, '借', m, '元钱')
            other.money -= m
            self.money += m
        else:
            print(other.name, '没有钱借给', self.name)
    def show_info(self):
        print(self.age, '岁的', self.name, '有钱', 
            self.money, '元，他学会的技能：',
            '、'.join(self.skill))

zhang3 = Human("张三", 35)
li4 = Human('李四', 8)
# 张三 教 李四 学 python
zhang3.teach(li4, 'python')

# 李四 教 张三 学 王者荣耀
li4.teach(zhang3,"王者荣耀")

# 张三 上班赚了 1000 元钱

li4.borrow(zhang3, 200)
# 李四 向 张三 借了 200 元钱
zhang3.works(1000)

li4.borrow(zhang3, 200)

zhang3.show_info()
li4.show_info()