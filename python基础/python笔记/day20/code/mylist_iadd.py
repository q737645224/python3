

# 此示例示意 复合赋值算术运算符的重载 
class MyList:
    def __init__(self, iterable):
        self.data = list(iterable)

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __add__(self, rhs):
        print("__add__方法被调用")
        r = MyList(self.data + rhs.data)
        print("id(r)=", id(r))
        return r

    def __iadd__(self, rhs):
        print("__iadd__方法被调用!!!")
        self.data += rhs.data  # 把 rhs数据加到现有列表中
        return self  # 不创建新对象,把自己返回回去

    def __mul__(self, rhs):
        print("__mul__方法被调用")
        return MyList(self.data * rhs)


L1 = MyList([1, 2, 3])
L2 = MyList(range(4, 7))
print("L1的ID:", id(L1))
L1 += L2  # 效果等同于 L1 = L1 + L2
print("L1 += L2之后的ID", id(L1))






