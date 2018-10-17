#day10.py
# 写一个计算公式的解释执行器
#     已知有如下一些函数：
#         def myadd(x, y):
#             return x + y
#         def mysub(x, y):
#             return x - y
#         def mymul(x, y):
#             return x * y
#     写一个函数，传入字符串，返回相应的函数
#         def get_op(s):
#             # 此函数根据字符串来返回相应的函数.
#             # 如果传入字符串"加" 则返回myadd函数
#             # ....        '乘',则返回mymul函数
#             ... 此处自己实现 
# 主程序如下:
# while True:
#     s = input("请输入计算公式: ")# 10 加 20
#     L = s.split()
#     a = int(L[0])
#     b = int(L[2])
#     fn = get_op(L[1])
#     print("结果是:", fn(a, b))  # 30

def myadd(x, y):
    return x + y
def mysub(x, y):
    return x - y
def mymul(x, y):
    return x * y

# def get_op():
#     n = input("请输入：")
#     if n == "加":
#         return myadd
#     elif n == "减":
#         return mysub
#     elif n == "乘":
#         return mymul
# x=int(input("请输数值："))
# y = int(input("请输入数值："))
# fx = get_op()
# print(fx(x,y))


# def get_op(op):
#     if op == "加" or op == +:
#         return myadd
#     elif op == "减" or op ==　"-"  :
#         return mysub
#     elif op == "乘"　or op == "*":
#         return mymul
# def main():
#     while True:
#         s = input("请输入计算公式: ")# 10 加 20
#         L = s.split()
#         a = int(L[0])
#         b = int(L[2])
#         fn = get_op(L[1])
#         print("结果是:", fn(a, b))  # 30

# 1. 写一个lambda 表达式，判断这个数的2次方+1是否能被5整除,如果
#    能被整除返回True, 否则返回False
#      例:
#         fa = lambda x: .....
#         print(fa(2))  # True
#         print(fa(4))  # False

# fa = lambda x: (x ** 2 + 1) % 5 == 0
# print(fa(2))
# print(fa(4))


# 写一个lambda表达式，求两个变量的最大值
#      例如:
#         def mymax(x, y):
#            ...
#         mymax = lambda ...
#         print(mymax(100, 200))  # 200

# mymax = lambda x, y : x if x > y else y 
# print(mymax(1,2))

# 看懂给下面程序在做什么？
# def fx(f, x, y):
#     print(f(x, y))
# fx((lambda a, b: a + b), 100, 200)
# fx((lambda x, y: x ** y), 3, 4)

# 1. 给出一个整数n,写一个函数myfac来计算n!(n的阶乘)
#     n! = 1 * 2 * 3 * 4 * ..... * n
#     如:
#       print(myfac(5))  # 120

# def myfac(n):
#     sums = 1
#     for i in range(1,n + 1):
#         sums = sums * i
#     return sums
# print(myfac(5))


# 2. 给出一个整数n,写一个函数计算myfn(n):
#       1 + 2**2 + 3**3 + .... + n**n的和
#     如:
#       print(myfn(10)) # ???

# def myfn(n):
#     sums = 0
#     for i in range(1, n):
#         sums += i**i
#     return sums
# print(myfn(10))

# 3. 完全数:
#      1 + 2 + 3 = 6 (6为完全数)
#      1,2,3都为6的因数(因数是能被一个数x整除的整数为y,则y为x的因数)
#      1 x 6 = 6
#      2 x 3 = 6
#      完全数是指除自身以外的所有因数相加之和等于自身的数
#      求 4~5个完全数并打印出来
#      答案:
#        6
#        28
#        496
#        ......

# def wsum(times):
#     count = 0
#     i = 3
#     while True:
#         l = []
#         for j in range(1,i):
#             if i % j == 0:
#                 l.append(j)
#             # print(j)
#         if sum(l) == i:
#             print(i)
#             count += 1
#         if count == times:
#             break
#         i += 1
# wsum(5)



#杨辉三角
def get_next_line(L):
    line = [1]  #最左侧的
    #计算中间的数字
    for i in range(len(L)): #i绑定Ｌ的索引
        # line.append(L[i] + L[i + 1])
    #在最后放入一个１
        line.append(1)
    return line

def get_yh_list(n):
    L = []
    line = [1] #当前第一行
    for  _ in range(n):
        L.append(line)
        line = get_next_line(line)
    return L

def list_to_string(L):
    L2 =[str(x) for x in L]
    return ' '.join(L2)

l = get_yh_list(6)
l2 = list_to_string(l)
charmax = len(l2(-1))
for i in l2:
    print(i.center(charmax))


