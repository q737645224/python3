
# 此示例示意一元运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __neg__(self):
        return MyList((-x for x in self.data))

    def __pos__(self):
        return MyList([abs(x) for x in self.data])


L1 = MyList([1, -2, 3, -4, 5])
L2 = -L1
print(L2)  # MyList([-1, 2, -3, 4, -5])

# 实现用正号运算符返回全部元素为正数的自定义列表
L3 = + L1
print(L3)  # MyList([1, 2, 3, 4, 5])



