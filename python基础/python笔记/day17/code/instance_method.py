# instance_method.py


# 此示例示意实例方法的创建和调用
class Dog:
    '''这是一种小动物的定义
    此类动物有吃(eat)的行为:

    '''
    def eat(self, food):
        '''此方法用来描述小狗吃的行为'''
        print("小狗正在吃:", food)

    def sleep(self, hour):
        print("小狗睡了%d小时" % hour)

    def play(self, obj):
        print("小狗正在玩:", obj)


dog1 = Dog()  # 调用构造函数创建一个实例对象 再用dog1变量绑定
dog1.eat('骨头')
dog1.sleep(1)
dog1.play('球')


dog2 = Dog()  # 创建另一个实例对象
dog2.eat('包子')
dog2.sleep(3)
dog2.play('飞盘')












