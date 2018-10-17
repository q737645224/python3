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
b.works()  # 调用哪儿个方法?

# a = A()
# a.works()  # A.works被调用

