# 练习:
#   写一个生成器函数 myeven(start, stop)
#   此函数用来生成从 start开始到stop结束(不包含)区间内的一系列偶数
#   def myeven(start, stop):
#       ....

#   evens = list(myeven(10, 20))
#   print(evens)  # [10, 12, 14, 16, 18]
#   for x in myeven(21, 30):
#       print(x)  # 22, 24, 26, 28

#   L = [x**2 for x in myeven(3, 10)]
#   print(L)  # 16 36 64


def myeven(start, stop):
    # L = [x for x in range(start, stop) if x % 2 == 0]
    # return L
    x = start
    while x < stop:
        if x % 2 == 0:
            yield x
        x += 1


evens = list(myeven(10, 20))
print(evens)  # [10, 12, 14, 16, 18]
for x in myeven(21, 300000000000000000000000000000):
    print(x)  # 22, 24, 26, 28

L = [x**2 for x in myeven(3, 10)]
print(L)  # 16 36 64
