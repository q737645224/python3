
# 此示例示意 索引/切片 运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __getitem__(self, i):
        print("索引i的值是:", i)
        return self.data[i]

    def __setitem__(self, i, v):
        print("__setitem__被调用, i=", i, 'v=', v)
        self.data[i] = v

    def __delitem__(self, i):
        del self.data[i]


L1 = MyList([1, -2, 3, -4, 5])
v = L1[2]  # v = 3
print(v)  # 3
L1[1] = 2
print(L1)  # MyList([1, 2, 3, -4, 5])
del L1[3]
print(L1)  # MyList([1, 2, 3, 5])






