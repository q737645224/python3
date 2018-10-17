
# import sys
# import math

# import tensorflow as tf

# import compare

# 此示例示意 PEP8编码规范
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __getitem__(self, i):
        print("索引i的值是:", i)
        if type(i) is int:
            print("正在进行索引操作")
        elif type(i) is slice:
            print("正在进行切片操作")
            print("起始值是:", i.start)
            print("终止值是:", i.stop)
            print("步长值是:", i.step)
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v=', v)
        self.data[i] = v

    def __delitem__(self, i):
        del self.data[i]


def hello(end='\n'):
    pass

hello(end="#")

L1 = MyList([1, -2, 3, -4, 5])
L2 = L1[::2]
print(L2)






