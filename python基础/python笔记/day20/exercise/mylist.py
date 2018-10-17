# 练习:
#   1. 实现两个自定义的列表相加
#   class MyList:
#       ....  此处自己实现
#   L1 = MyList([1, 2, 3])
#   L2 = MyList(range(4, 7))
#   L3 = L1 + L2
#   print(L3)  # MyList([1, 2, 3, 4, 5, 6])
#   L4 = L2 + L1
#   print(L4)  # MyList([4, 5, 6, 1, 2, 3])
#   L5 = L1 * 2
#   print(L5)  # MyList([1, 2, 3, 1, 2, 3])

class MyList:
    def __init__(self, iterable):
        '''在初始化方法内为每个对象都创建一个data属性
        data 用来绑定每个对象自己的列表'''
        self.data = list(iterable)
        # self.data = [x for x in iterable]  # 等同于上句

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __add__(self, rhs):
        return MyList(self.data + rhs.data)

    def __mul__(self, rhs):
        return MyList(self.data * rhs)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
L3 = L1 + L2
print(L3)  # MyList([1, 2, 3, 4, 5, 6])
L4 = L2 + L1
print(L4)  # MyList([4, 5, 6, 1, 2, 3])
L5 = L1 * 2
print(L5)  # MyList([1, 2, 3, 1, 2, 3])



