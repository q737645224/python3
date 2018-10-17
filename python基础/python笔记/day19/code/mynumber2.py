# mynumber.py


# 此示例示意通过重写 repr 和 str方法改变转为字符串的规则
class MyNumber:
    def __init__(self, value):
        '构造函数,初始化MyNumber对象'
        self.data = value

    # def __str__(self):
    #     '''转换为普通人识别的字符串'''
    #     # print("__str__方法被调用!")
    #     return "自定义数字类型对象: %d" % self.data

    def __repr__(self):
        '''转换为eval能够识别的字符串'''
        return 'MyNumber(%d)' % self.data


n1 = MyNumber(100)
n2 = MyNumber(200)
print('repr(n1) ====>', repr(n1))
print('str(n2)  ====>', str(n2))


