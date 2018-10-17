
# 此示例示意 in / not in 运算符的重载
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __contains__(self, e):
        return e in self.data

L1 = MyList([1, -2, 3, -4, 5])
print(2 in L1)
print(3 in L1)
print(4 not in L1)
print(5 not in L1)





