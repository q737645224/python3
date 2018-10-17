# static_method.py


class A:
    @staticmethod
    def myadd(a, b):
        return a + b


print(A.myadd(100, 200))  # 300
a = A()  # 创建实例
print(a.myadd(300, 400))  # 700

