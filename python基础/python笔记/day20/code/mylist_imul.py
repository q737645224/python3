
# 此示例示意返向算述运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __mul__(self, rhs):
        print("__mul__被调用!!!")
        return MyList(self.data * rhs)

    def __rmul__(self, lhs):
        print("__rmul__被调用!!!")
        return MyList(self.data * lhs)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = 2 * L1  # L1.__rmul__(2)
print(L3)

L5 = L1 * 2  # L5 = L1.__mul__(2)
print(L5)  # MyList([1, 2, 3, 1, 2, 3])



