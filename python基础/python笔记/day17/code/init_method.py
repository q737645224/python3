# init_method.py

class Car:
    '''定义一个汽车类'''
    def __init__(self, c, b, m):
        self.color = c  # 颜色
        self.brand = b  # 品牌
        self.model = m  # 型号
        print("__init__方法被调用")

    def run(self, speed):
        print(self.color, '的', self.brand,
              self.model, '正在以',
              speed, '公里/小时的速度行驶')


a4 = Car('红色', '奥迪', 'A4')  # 调用构造函数
a4.run(299)

s3 = Car('蓝色', 'TESLA', 'Model S')
s3.run(270)


# print(a4.color)
