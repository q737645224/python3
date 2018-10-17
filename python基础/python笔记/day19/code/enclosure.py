# enclosure.py


# 此示例示意私有属性和私有方法
class A:
    def __init__(self):
        self.__p1 = 100  # 私有属性

    def show_A(self):
        print('self.__p1: ', self.__p1)
        self.__m1()  # 调用自己的方法

    def __m1(self):  # 私有方法
        print("__m1(self)方法被调用")


a = A()
a.show_A()  # a.__p1: 100
# print(a.__p1)  # 出错,在类外部不能访问a的私有属性__p1
# a.__m1()  # 出错,不能调用私有方法


class B(A):
    pass


b = B()
# print(b.__p1)  # 出错, 子类对象不能访问父类中的私有成员
# b.__m1()  # 出错

