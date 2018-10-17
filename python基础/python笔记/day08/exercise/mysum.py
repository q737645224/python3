# 2. 写一个函数 mysum, 传入一个参数x代表终止整数，
#    打印出 1 + 2 + 3 + 4 + ..... + x的和
#   def mysum(x):
#       ....

#   mysum(100)  # 5050
#   mysum(4)   # 10


def mysum(x):
    s = 0  # 创建变量用于累加
    for i in range(1, x + 1):
        s += i
    print(s)


mysum(100)  # 5050
print('s =', s)
mysum(4)   # 10
