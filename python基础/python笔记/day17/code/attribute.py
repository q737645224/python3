# attribute.py


# 此示例示意属性的用法
class Dog:
    def eat(self, food):
        # print("小狗正在吃:", food)
        print(self.color, '的', self.kinds, '正在吃', food)

dog1 = Dog()
dog1.kinds = '京巴'  # 为dog1对象添加kinds属性,绑定为'京巴'
dog1.color = '白色'  # dog1添加属性 为'白色'
dog1.color = '黄色'  # 改变dog1的color属性
print(dog1.color, "的", dog1.kinds)  # 访问dog1 的属性

dog2 = Dog()
dog2.kinds = '哈士奇'
dog2.color = '黑白相间'
print(dog2.color, '的', dog2.kinds)  # 出错

dog1.eat('骨头')
dog2.eat('窝头')







