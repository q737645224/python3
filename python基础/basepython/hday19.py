# hday19.py
# 1. 修改原有的学生信息管理系统, 将学生对象的,全部属性 
#   都变为私有属性,不让外部直接访问来实现封装








 # 2.写一个实现迭代器协议的类，让此类可以生成从b开始的n个素数
  class primr:
    def __init__(self,b,n):
        ...
    def __iter__(self):
        ...
    L = [x for  x in Prime(10,4)] 
    print(L) # L = [11,13,17,19]

class primr():
    def __init__(self):
        self.b, self.n = b, n
    def __iter__(self):
        return self
    def __next__(self):
        if k > n:
            raise StopIteration
        elif:
            if b <= 2:
                break
            elif:
                j = 1
                while j**2 <= i:
                    if i % j == 0:
                        break
                    j += 1
            if j**2 > i:
                return i
s = primr(10,4)
t = 0
while t < n:
    if b <= 2:
        break
    elif:
        j = 1
        while j**2 <= i:
            if i % j == 0:
                break
            j += 1
    if j**2 > i:
        t += 1
        return i



class Prime:
    def __init__(self,b, n):
        self.begin = b
        self.count = n

    def __iter__(self):
        self.cur_