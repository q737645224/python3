
# 练习:
#   写一个Student类
#     1) 为该类添加初始化方法, 实现在创建对象时自动设置
#       '姓名','年龄', '成绩' 属性
#     2) 添加set_score方法能修改成绩信息
#     3) 添加show_info方法打印学生对象的信息

#   如:
#     class Student:
#         def __init__(...):
#             ...
#         ...

#     s1 = Student('小王', 15, 59)
#     s1.show_info()  # 小王 今年 17 岁, 成绩是: 59
#     s1.set_score(80)
#     s1.show_info()  # 小王 今年 17 岁, 成绩是: 80


class Student:
    def __init__(self, n, a, s):
        self.name, self.age, self.score = n, a, s

    def show_info(self):
        print(self.name, '今年',
              self.age, '岁, 成绩是:',
              self.score)

    def set_score(self, s):
        assert 0 <= s <= 100, '参数错误'
        self.score = s


s1 = Student('小王', 15, 59)
s1.show_info()  # 小王 今年 17 岁, 成绩是: 59
s1.set_score(80)  # s1.score = 80
s1.show_info()  # 小王 今年 17 岁, 成绩是: 80

