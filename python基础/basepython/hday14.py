#hday14.py
# 方法一：
# def get_score():
#     score = int(input("输入学生的成绩："))
#     if 0 <= n <= 100:
#         return score
#     else:
#         return 0
# try:
#     score = get_score()
# except ValueError:
#     score = 0
# print("学生的成绩是：", score)
# 方法二：


# import logging
# def get_score():
#     try:  #在合适的层数使用try，减多少次使用的麻烦
#         score = int(input("成绩"))
#     except Exception as e:
#         # logging.exception(e)
#         return 0
#     if 0 <= score <= 100:
#         return score
#     else:
#         return 0
# score = get_score()
# print("学生的成绩是：", score)

# 写一个函数 get_age()用来获取一个人的年龄信息
#   此函数规定用户只能输入1~140之间的整数,如果用户输入其它的数则直接触发ValueError类型的错误通知
#      如果用户输入的年龄大于140,则触发
#        ValueError("年龄超出了正常值")
#      如果用户输入的年龄小于1,则触发
#        ValueError("年龄太小...")
#   def get_age():
#       ...
#   try:
#       age = get_age()
#       print("用户输入的年龄是:", age)
#   except ValueError as err:
#       print('用户输入的不是1~140的整数,获取年龄失败')
#       print("原因是:", err)

# import logging
# def get_age():
#     age = float(input("输入用户的年龄"))
#     if age > 140:
#         raise ValueError("年龄超出正常值")
#     elif age < 1:
#         raise ValueError("年龄太小")
#     else:
#         return age

# try:
#     age = get_age()
#     print("年龄是：", age)
# except ValueError as err:
#     logging.exception(e)
#     print("用户输入的不是１～１４０的整数，年龄获取失败")
#     print("原因是：", err)


# def get_score():
#     s = int(input("输入的学生成绩（１～１００）："))
#     assert 0 <= s <= 100, '成绩超出范围'
#     return s
# try:
#     score = get_score()
#     print("学生成绩为：", score)
# except ValueError as err:
#     print("用户输入数字不能转换为整数...")
# except AssertionError:

 # 一个球从100米高空落下,每次落地后反弹高度是原高度的一半,再落下,
 #     1) 写程序算出皮球在第10次落地后反弹高度是多高?
 #     2) 打印出球共经过多少米的路程 
# def math(n):
#     i = 1
#     sums = 0
#     stare = 100
#     while i <= n:   
#         s1 = stare
#         stare *= 1/2
#         s2 = stare
#         sums  += s1 + s2
#         i += 1
#     return (stare, sums)
# a = math(1)
# print("高为%d,经过%d" %(a[0], a[1]))


# a = 100
# i = 1
# j = int(input())
# while  True:
#     if i == j:
#         break
#     a = a * 1/2
#     i += 1
# print(a)


# 2. 分解质因数, 输入一个正整数,分解质因数,
#     如:
#       输入: 90
#     则打印:
#       '90=2*3*3*5'
#       (质因数是指最小能被原数整除的素数(不包括1))
# def is_prime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True
# L = []  #此列表用存储素数（质因数）
# n = int(input("请输入一个正整数："))
# #判断如果n不为一则找质因数
# while n != 1:
#     for i in range(2, n + 1): 
#     #依次让n厨艺i，如果整数则i为质因数
#         if n % i ==0 and is_prime(i):
#             L.append(i)
#             n = int(n / i)
#             break #查找当一个质因数结束
# print(L)


L = []
def prime(n):
    if n == 1:
        return False
    while i ** 2 <= n:
        if n % i == 0:
            return False
    return True
n = int(input())
while n != 1:
    for i in range(2, n + 1):
        if n % i == 0 and prime(i):
            L.append(i)
            n = int(n / i)
            break
print(L)

