# del_method.py


# 此示例示意析构方法的用法
class Car:
    def __init__(self, name):
        self.name = name
        print("汽车", name, '被创建')

    def __del__(self):
        '''析构方法,此方法会在对象销毁时自动被调用'''
        print('汽车', self.name, '被销毁')


c1 = Car('BYD E6')
c2 = c1
del c1  # 此时是删除c1变量,同时解除c1绑定的对象的引用

input("请按回车键结束程序的执行!")

