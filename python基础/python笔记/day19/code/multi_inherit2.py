# multi_inherit2.py


# 此示例示意多继承名字冲突问题
# 小张写了一个类A
class A:
    def m(self):
        print('A.m()被调用')


# 小李写了一个类B
class B:
    def m(self):
        print('B.m()被调用')


# 小王感觉小张和小李写的两个类自己可以用
class AB(A, B):
    pass


ab = AB()
ab.m()  #  请问会发生什么?


