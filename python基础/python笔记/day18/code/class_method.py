# class_method.py


# 此示例示意类方法的使用
class A:
    v = 0

    @classmethod
    def get_v(cls):  # cls 用来绑定调用此方法的类
        return cls.v  # 访问类变量

    @classmethod
    def set_v(cls, value):
        cls.v = value


print(A.get_v())  # 0
A.set_v(100)
print(A.get_v())  # 100
a1 = A()  # 创建实例
print("a1.get_v() =", a1.get_v())  # 100
a1.set_v(200)
print("a1.get_v() =", a1.get_v())  # 200
print('A.get_v() =', A.get_v())





