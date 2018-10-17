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


class Human:
    '''人类,用于描述人的行为和属性'''
    def __init__(self, n, a=1):
        self.name = n  # 姓名
        self.age = a  # 年龄
        self.money = 0  # 钱数
        self.skill = []  # 技能

    def teach(self, other, subject):
        other.skill.append(subject)
        print(self.name, '教',
              other.name, '学', subject)

    def print_info(self):
        print(self.age, '岁的',
              self.name, '有钱',
              self.money, '元,它学会了:',
              self.skill)

    def works(self, money):
        self.money += money
        print(self.name, '上班赚了', money, '元钱')

    def borrow(self, other, money):
        if other.money > money:
            other.money -= money
            self.money += money
            print(self.name, "向", other.name,
                  '成功借了', money, '元钱')
        else:
            print(self.name, '向', other.name, '错钱失败')


zhang3 = Human('张三', 35)
li4 = Human('李四', 8)
# 张三 教 李四 学 python
zhang3.teach(li4, 'Python')
# 李四 教 张三 学 跳皮筋
li4.teach(zhang3, '跳皮筋')
# 张三 上班赚了 1000 元钱
zhang3.works(1000)
# 李四 向 张三 借了 200 元钱
li4.borrow(zhang3, 200)

# 打印张三的信息: 35岁 的 张三 有钱 800元, 它学会跳皮筋
zhang3.print_info()
# 打印李四的信息: 8岁 的 李四 有钱 200元, 它学会python
li4.print_info()






