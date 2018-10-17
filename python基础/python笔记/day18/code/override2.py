# override.py


# 此示例示意B类的works方法覆盖A类的works方法
class A:
    def works(self):
        print("A.works被调用")


class B(A):
    ''' B类继承自A类'''
    def works(self):
        print("B.works被调用")


b = B()
b.works()  # B.works被调用
A.works(b)  # 用类名显式调用, A.works被调用




