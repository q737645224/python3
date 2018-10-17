# 练习:
#   自己写一个'人'类: Human
#   class Human:
#       def set_info(self, name, age, address='未知'):
#           '''此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性'''
#           ...  # << 此处自己实现
#       def show_info(self):
#           '''显示此人的全部信息'''
#           ... # 此处自己实现
#   如:
#     h1 = Human()
#     h1.set_info('小张', 20, '北京市朝阳区')
#     h2 = Human()
#     h2.set_info('小李', 18)
#     h1.show_info()  # 小张今年 20 岁,家庭住址:北京市朝阳区
#     h2.show_info()  # 小李今年 18 岁,家庭住址:末知


class Human:
    def set_info(self, name, age, address='未知'):
        '''此方法用来给人对象添加'姓名', '年龄', '家庭住址'三个属性'''
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        '''显示此人的全部信息'''
        print(self.name, '今年',
              self.age, '岁,家庭住址:',
              self.address)


h1 = Human()
h1.set_info('小张', 20, '北京市朝阳区')
h2 = Human()
h2.set_info('小李', 18)
h1.show_info()  # 小张今年 20 岁,家庭住址:北京市朝阳区
h2.show_info()  # 小李今年 18 岁,家庭住址:末知






