# 3. 写一个类Fibonacci 实现迭代器协议 ,此类的对象可以作为可迭代对象生成相应的斐波那契数
#    1 1 2 3 5
#   class Fibonacci:
#       def __init__(self, n)  # n代表数据的个数
#           ...
#       ...
#   实现如下操作:
#     for x in Fibonacci(10):
#         print(x)  # 1 1 3 5 8 ....
#     L = [x for x in Fibonacii(50)]
#     print(L)
#     F = fibonicci(30)
#     print(sum(F))  


class Fibonacci:
    def __init__(self, n):  # n代表数据的个数
        self.__count = n

    def __iter__(self):
        self.cur = 0  # 当前已生成的个数
        self.a = 0
        self.b = 1  # 当前的第一个斐波那契数
        return self

    def __next__(self):
        if self.cur >= self.__count:  # 不需要再生成
            raise StopIteration
        self.cur += 1  # 已生成的个数加1
        v = self.b  # 绑定当前的数,待返回
        # 计算下一个数,待下次返回
        self.a, self.b = self.b, self.a + self.b
        return v  # 把当前值返回


for x in Fibonacci(10):
    print(x)  # 1 1 3 5 8 ....
L = [x for x in Fibonacci(50)]
print(L)
F = Fibonacci(30)
print(sum(F))

