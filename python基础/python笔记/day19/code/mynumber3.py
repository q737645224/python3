# mynumber3.py

# 此示例示意数据转换构造函数的重写方法
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        return 'MyNumber(%d)' % self.data

    def __int__(self):
        return self.data


n1 = MyNumber(100)
x = int(n1)  # 转为整数?
print(x)

print(bool(n1))  # True
n2 = MyNumber(0)
print(bool(n2))  # ????
