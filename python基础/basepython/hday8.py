#hday8.py
# s1= {'曹操', '刘备', '孙权'}
# s2 = {'曹操', '孙权', '张飞', '关羽'}
# print(s1 & s2)
# print(s1 - s2)
# print(s2 - s1)
# s = "张飞"in s1
# print("张飞是经理吗？\n", s)

# print((s1 - s2) | (s2 - s1))
# print([(s1 - s2) | (s2 - s1) | (s1 & s2)])

# print(s1 ^ s2 )
# print(s1 | s2)


# def myadd(x, y):
#     print(x+y)
#     return()

# myadd(3, 4)
# myadd("abc", "123")


# def mysum(x):
#     sums = 0
#     for i in range(1, x + 1):
#         sums = sums + i
#     print(sums)
# n = int(input("请输入要求和的数："))
# mysum(n)


# def print_even(n):
#     for x in range(1, n + 1):
#         if x % 2 == 0:
#             print(x)

# print_even(8)


# def input_number():
#     L = list()
#     while True:
#         l = int(input())
#         if l < 0:
#              break
#             # return L
#         else:
#             L.append(l)
#     print(L)
#     print("用户输入的最大数是：", max(L))
#     print('用户输入的最小数是：', min(L))
#     print('用户输的这些数的和是：', sum(L))

# input_number()

# def print_odd(begin, end):
#     for x in range(begin, end):
#         if x % 2 == 1:
#             print(x)
# print_odd(1,10)
# print_odd(10, 20)

# def mymax(a, b):
#     if a > b:
#         return a
#     return b


# def sum3(a, b, c):
#     print(a + b + c)
# def pow3(x):
#     return x * 3
# sum3(pow3(1), pow3(2), pow3(3))
# pow3(sum3(1, 2, 3))
# 
# def fun(n):
#     i = 1
#     sums = 0
#     while i <= n:
#         sums += 1/i
#         i += 1
#     return sums

# print(fun(3))
# print(fun(10))



# def fun2(n):
#     i = 1
#     sums = 0
#     while i <= n:
#         sums += 1/i* (i - 1)
#         i += 1
#     return sums

# print(fun(3))
# print(fun(10))


# def fun(n):
#     l=(1/x for x in range(n))
#     return sum(l)
# fun(3)


# 1.写一个函数 get_chinese_char_count(x),
# 此函数实现的功能是从一个给定的字符串中返回中文字符的个数
#     def get_chinese_char_count(x):
#         ...


#     s = input("请输入中英文混合的字符串：")   #hello中国
#     print('你输入的中文的字符个数是：')
#     get_chinese_char_count(s)  #2

# def get_chinese_char_count():
#     times = 0
#     s = input("请输入中英文混合的字符串：")
#     for i in s:
#         if ord(i) > 127:
#             times += 1
#     print('你输入的中文的字符个数是：', times)

# get_chinese_char_count()


# 2.写一个函数isprime(x)
#   判断x是否为素数，如果为素数，返回true，否则返回False
#     如：
#      print(isprime(5)) #true
#      print(isprime(6)) #False
1.
def isprime(x):
    if x < 2:
        return false
    for i in range(2,x):
        if x % i == 0: #如果整除则不是素数
            print("false")
            return False
    return True
2.
def isPrime(n): 
  if n <= 1: 
    return False
  i = 2
  while i*i <= n: 
    if n % i == 0: 
      return False
    i += 1
  return True

# # 3.写一个函数prime_m2n(m,n)返回从m开始，到n结束范围内的素数，
#    回这些素数的列表，并打印。
# 如：
#   L = prime_m2n(10,20)
# print(L) #[11,13,17,19]

# def prime_m2n(m, n):
#     L = []
#     for i in range(m, n):
#         b = isPrime(i)  #if isprime(x): 
#         if b == True:     # L.append(x)
#             L.append(i)
#     print(L)              #return L

# prime_m2n(10,20)

# 4.写一个函数primes(n) 返回指定范围内n(不包括n)的全部素数的列表
# ，并打印这些列表
#   如：
#     L = primes(10)
#     print(L) #[2,3,5,7]
#     1）打印100以内全部素数的和
#     2）打印200以内全部素数的和

def prime(n):
    L = []
    for i in range(n):
        b = isPrime(i)
        if b == True:
            L.append(i)
    print(sum(L))

prime(100)


# 5.改写之前的学生信息管理程序
#     改为两个函数:
    
#       def input_student():
#            ....

#       def output_student(lst):
#            ...

#     １．input_student()用于从键盘读取学生数据，形成列表并
#       返回列表

#     2.output_student(lst)此函数传入一个列表lst,
#        字典的列表
#     此函数把lst的内容以表格形式打印出来
#       测试代码：
#         L = input_student()
#         print(L)
#         putput_student(L) #打印表格

def input_student():
    L = []
    while True:
        name = input("请输入姓名：")
        if not name:
            break
        age = input("请输入年龄：")
        while not age :
            age = iput("请输入年龄：")
        score = input("请输入成绩：")
        while not score :
            score = input("请输入成绩：")
        d = {}
        d["name"] = name
        d["age"] = age
        d["score"] = score
        L.append(d)
    return L

def output_student(l):
    print("+" + "-"* 12 + \
        "+" + "-" * 10 + \
        "+" + "-" * 9 + "+")
    print("|", "name".center(10), \
        "|", "age".center(8), "|", \
        "score".center(6), "|" )
    print("+" + "-"* 12 + "+" +\
     "-" * 10 + "+" + "-" * 9 + "+")
    for i in l:
        n = i["name"]
        a = i["age"]
        s = i["score"]
    print("|", \
        n.center(10), "|",\
        a.center(8), "|", \
        s.center(6), "|" )
    #print("|"%s"|"%s"|"%s"|")
    print("+" + "-"* 12 + \
        "+" + "-" * 10 + \
        "+" + "-" * 9 + "+")

L = input_student()
print(L)
output_student(L)
