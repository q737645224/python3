# override.py


# 此示例示意用super函数返回的对象调用父类的覆盖方法
class A:
    def works(self):
        print("A.works被调用")

class B(A):
    ''' B类继承自A类'''
    def works(self):
        print("B.works被调用")

    def super_work(self):
        self.works()  # B.works被调用
        super(B, self).works()  # A.works被调用
        super().works()  # A.works被调用


b = B()
# b.works()  # B.works被调用
# super(B, b).works()  # A.works被调用
b.super_work()  # ...
# super().works() # 出错,只能在方法内调用



