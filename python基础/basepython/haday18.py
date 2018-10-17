#haday18.py
# class Human:
#     total_count = 0
#     def __init__(self, n):
#         self.name = n
#         self.__class__.total_count += 1
#         print(self.name, "创建")

#     def __del__(self):
#         print(self.name, "销毁")
#         self.__class__.total_count -= 1

# L = []
# L.append(Human("张飞"))
# L.append(Human("关羽"))


# 类方法@classmethod

# class A:
#     v = 0 #类变量（类属性）

#     @classmethod
#     def get_v(cls):
#         return cls.v   #用cls 访问类变量v

#     @classmethod
#     def set_v(cls, a):
#         cls.v = a
# print("A.v=", A.get_v())


# 用类来描述一个学生的信息(可以修改之前写的Student类)
#     class Student:
#          .... 此处自己实现

#     学生信息有:
#        姓名, 年龄, 成绩

#     将一些学生的对象存于列表中,可以任意添加和删除学生信息
#       1) 打印出学生的个数
#       2) 打印出所有学生的平均成绩
#       3) 打印出所有学生的平均年龄

# class Student:
#     __slots__['n', 'a', 's']
#     total_count = 0
#     def __inif__(self, n , a, s = 0):
#         self.name = n
#         self.age = a 
#         self.score = s
#         total_count += 1
#     def del_stdent(self):
#         del self 
#     L = []
#     def add_student(L):
#         L.append(student('小张', 20, 100))

#     def del_student():
#         del cls.L[0]
    
# 练习:
#   写一个类Bicycle类 ,有 run方法.调用时显示骑行里程km
#     class Bicycle:
#         def run(self, km):
#             print('自行车骑行了', km, '公里')
#   再写一个类EBicycle(电动自行车类), 在Bicycle类的基础上添加了电池电量 volume 属性, 有两个方法:
#      1. fill_charge(self, vol)  用来充电, vol为电量
#      2. run(self, km) 方法每骑行10km消耗电量1度,同时显示当前电量,当电量耗尽时调用 父类的run方法继续骑行

#     b = EBicycle(5)  # 新买的电动有内有5度电
#     b.run(10)  # 电动骑行了10km还剩 4 度电
#     b.run(100)  #电动骑行了40km,还剩0度电,其余60用脚登骑行
#     b.fill_charge(10)  # 又充了10度电
#     b.run(50)  # 骑行了50公里剩5度电


class Bicycle:
    def __init__(self, km):
        self.km = km
    def run(self, km):
        print("自行车骑了", km, '公里')

class EBicycle(Bicycle):
    def __init__(self, volume):
        super(Bicycle, self).__init__()
        self.volume = volume
        print("新买的电池内有５度电")

    def fill_charge(self, vol):
        self.volume += vol
        print("又冲了５度电")

    def run(self, km):
        if km/10 < self.volume:
            self.volume -= km / 10
            print("自行车骑了", km, '公里', "还剩", self.volume, "度电")
        else:
            s = km - self.volume * 10
            self.volume = 0
            print("自行车骑了", km, '公里', "还剩", self.volume, "度电", "剩余%d公里用脚蹬骑行" % s)


b = EBicycle(5)  # 新买的电动有内有5度电
b.run(10)  # 电动骑行了10km还剩 4 度电
b.run(100)  #电动骑行了40km,还剩0度电,其余60用脚登骑行
b.fill_charge(10)  # 又充了10度电
b.run(50)  # 骑行了50公里剩5度电

