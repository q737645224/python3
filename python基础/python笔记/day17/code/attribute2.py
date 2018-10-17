# attribute.py


# 此示例示意属性的用法
class Dog:
    def eat(self, food):
        # print("小狗正在吃:", food)
        print(self.color, '的', self.kinds, '正在吃', food)
        # 让调用此方法的对象添加一个last_food属性用来记住吃的信息
        self.last_food = food

dog1 = Dog()
dog1.kinds = '京巴'  # 为dog1对象添加kinds属性,绑定为'京巴'
dog1.color = '白色'  # dog1添加属性 为'白色'

dog2 = Dog()
dog2.kinds = '哈士奇'
dog2.color = '黑白相间'

dog1.eat('骨头')
dog2.eat('窝头')
print("dog1上次吃的是:", dog1.last_food)
print("dog2上次吃的是:", dog2.last_food)






