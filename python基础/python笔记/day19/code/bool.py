# bool.py


# 此示例示意bool(x) 函数的重写
class MyList:
    '自定义类型的列表，用来保存数据，内部用一个列表来存储数据'
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __len__(self):
        '''返回长度'''
        print("__len__方法被调用")
        return len(self.data)

    def __bool__(self):
        print("__bool__方法调用")
        for x in self.data:
            if not x:
                return False
        return True
        # return False  # <<=== 所有对象都为False


myl = MyList([0, -1, 2, -3])
# myl = MyList()
print(myl)
print(bool(myl))
if myl:
    print("myl为真值")
else:
    print('myl为假值')








