#hday13.py
#此示例示意自定义模块
# def myfac(n):
#     print("正在计算%的阶乘..." % n)
# def mysum(x):
#     print("正在计算%的和..." % x)

# #此列表限定
# def f1():
#     pass
# def f2():
#     pass
# def f3():
#     pass
# var1 = 100
# var2 = 200 

# from random import *
# # L = [1, 2, 3, 4, 5, 9]
# # print(shuffle(L))
# import math

# x = math.floor(uniform(1,100))
# i = 0
# while True:
#     i += 1
#     y = int(input("请输入数字！"))
#     if x == y:
#         print("你猜了%d次，猜对了" % i)
#         break
#     elif y > x :
#         print("你猜大了" )
#     elif y < x :
#         print("你猜小了")
#     print(i)

# def show_menu():
#     print("１）魂斗罗")
#     print("２）坦克大战")

# 1. 模拟斗地主发牌,扑克牌共54张
#     黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'), 红桃('\u2666')
#     A2-10JQK
#     大王、小王
#     三个人玩，每人发17张牌，底牌留三张
#     输入回车, 打印出第1个人的17张牌
#     输入回车, 打印出第2个人的17张牌
#     输入回车, 打印出第3个人的17张牌
#     输入回车, 打印三张底牌

# import random
# def puk():
#     L = ['\u2660','\u2663','\u2665','\u2666']
#     L2 =[str(x) for x in range(2,11)]
#     L2.extend(['A','J','Q','K'])
#     L3 = [i +" "+ j for i in L for j in L2]
#     L3.extend(["大王","小王"])
#     L4=random.sample(L3,17)
#     print(L4)
#     # print(L3)
#     for i in L4:
#         L3.remove(i)
#     L5=random.sample(L3,17)
#     print(L5)
#     # print(L3)
#     for i in L5:
#         L3.remove(i)
#     L6 = random.sample(L3,17)
#     print(L6)
#     for i in L6:
#         L3.remove(i)
#     print(L3)
# puk()


# def puk():
#     L = ['\u2660','\u2663','\u2665','\u2666']
#     L2 =[str(x) for x in range(2,11)]
#     L2.extend(['A','J','Q','K'])
#     L3 = [i +" "+ j for i in L for j in L2]
#     L3.extend(["大王","小王"])
#     random.shuffle(L3)　　＃洗牌
    




# 2.打印 九九乘法表：
#   1x1=1
#   1x2=2 2x2=4
#   1x3=3 2x3=6 3x3=9
#   ....
#   1x9=9 ...................9x9=81

# def fab(n):
#     for i in range(1,n +1):
#         s =i * n
#         print("%dx%d=%d" %(i,n,s),end=" ")
#         if i == n:
#             print("\n")
# def diao(j):
#     i = 1
#     while i <= j:
#         fab(i)
#         i += 1
# diao(7)



# def diao(j):
#     i =1
#     def fab(n):
#         print("%dx%d" %(i,n),end=" ")
#         if i == n:
#             print("\n")
#     return fab()

# for Line in range(1, 10): #line代表行数
#     for col in range(1,Line + 1):
#         print("%dx%d=%d" %(col, Line, col * Line), end=" ")
#     print("\n")

