
# 此示例示意比较运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __eq__(self, rhs):
        return self.data == rhs.data

    def __gt__(self, rhs):
        return self.data > rhs.data


L1 = MyList([1, 2, 3])
L2 = MyList([1, 2, 3])

print(L1 == L2)  # True

print(L1 > L2)  # False



