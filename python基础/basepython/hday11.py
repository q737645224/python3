#hday11.py
# 1. 用map函数求:
#     1**3 + 2**3 + 3 ** 3 + .... 9**3 的和
# def power1(x):
#     return x * 3
# L = [x for x in map(power1, range(1, 10))]
# print(sum(L))

# 2.求 1**9 + 2**8 + 3**7 + ...... 9**1
# def power2(x,y):
#     return x ** y
# print(map(power2,range(1,10),range(9,0,-1)))
# s = sum([x for x in map(power2, range(1, 10), \
#     range(9, 0, -1))])
# print(s)

# for x in map(lambda x : x ** 2, range(1,10)):
#     s += x 
# print(s)

# print(sum(map(lambda x : x **2, range(1,10))))
# print(sum(map(pow, range(1,10), range(9,0,-1))))

# for i in map(pow,
#     [1, 2, 3, 4],
#     (4, 3, 2, 1),
#     range(5, 500)):
#     print(i)

 # 1. 将 1 ～　２０　的偶数用filter生成可迭代对象后
 #   将可迭代对象生成的数放入到列表L中
# def isd(x):
#     return x % 2 == 0

# L = [i for i in filter(isd, range(1,21))]
# print(L)

# L = [i for i in filter(lambda x :x % 2 == 0, range(1,21))]
# print(L)

# L =list()  等同于　L　=　[]

# 2. 写一个函数is_prime(x) 判断x是否是素数
#     用filter函数打印出: 1 ~ 100之间的全部素数

# def isPrime(n): 
#     if n <= 1: 
#         return False
#     i = 2
#     while i*i <= n: 
#         if n % i == 0: 
#           return False
#         i += 1
#     return True

# def isprime(x):
#     if x < 2:
#         return False
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return


# for i in filter(isPrime, range(1, 101)):      
#     print(i, end=" ")

# L = list(filter(isPrime, range(1, 101)))
# print(L)

# 练习:
# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据为字符串的反序:
#            'moT'   yrreJ    ekipS    ekyT
#   结果:
#     ['Spike', 'Tyke', 'Tom', 'Jerry']

# L = sorted(names,key = len)
# def reverse1(x):
#     i = " "
#     i = x[::-1]
#     return i

# names = ['Tom', 'Jerry', 'Spike', 'Tyke']
# L = sorted(names, key = reverse1)
# print(L)

# 

# 练习:
#   写函数 mysum(n)用递归方式实现求和
#     def mysum(n):
#         # 用递归方式求和
#         ...

#     print(mysum(100))  # 5050

# def mysum(n):
    # if n == 1:
#         return 1
#     return n + mysum(n - 1)

# print(mysum(100))


 # 1. 给出一个整数n,写一个函数myfac来计算n!(n的阶乘)
 #    n! = 1 * 2 * 3 * 4 * ..... * n
# 1.
# def myfac(n):
#     s = 1
#     for i in range(1, n + 1):
#         s *= i
#     return


# 2.
# def myfac(n):
#     #用递归来实现
#     #　5! = 5 * 4!
#     # 5! = 5 * 4* 3!
#     # 5! = 5 * 4 * 3 *2!
#     # 5! = 5 * 4 * 3 * 2 * 1!
#     # 5! = 5 * 4 * 3 * 2
#     # 5! = 5 * 4 * 6
#     # 5! = 5 * 24
#     # 5! = 120
    # if n == 1:
    #     return 1
#     #如果n不是１，则地推到下一级求解
    # return n * myfac(n - 1)

# print(myfac(10))

# def pown(y):
#     def fn(x):
#         return x ** y
#     return fn
# l = pown(4)
# print(l(2))

# 写出１～２０的阶乘
# def sum_factorial(n):
#     s = 0
#     for i in range(1, n +1):
#         s += s * i  # s += n!
#         return s
# def sum_factorial(n):
#     s = 0 
#     for i in range(1, n+1):
#         s += myfac(i)
#     return s






# 1.　已知五位朋友在一起
#     第五位朋友比第四位朋友大2岁
#     第四位朋友比第三位朋友大2岁
#     第三位朋友比第二位朋友大2岁
#     第二位朋友比第一位朋友大2岁
#     第一位朋友说它10岁
#     写程序打印出第五位朋友　和第三位朋友　的年龄
# def mage(n):
#     if n == 1:
#         return 10
#     return mage(n -1 ) + 2
# print(mage(5))
# print(mage(3))


# 2.已知有列表:
#     L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#     1） 写一个函数print_list(lst) 打印出所有元素
#       print(L)  # 打印 3 5 8 10 13 14 ....
#     2）写一个函数sum_list(lst) 返回这个列表中所有元素的和
#       print(sum_list(L))  # 106
#     注:
#       type(x) 可以返回一个变量的类型
#       如:
#         >>> type(20) is int 　　#True
#         >>> type([1, 2, 3]) is list 　#True


def print_list(lst):
    for i in lst:
        if type(i) is list :
            print_list(i)
        else:
           print(i)

L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
print_list(L)

def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is int:
            s += x 
        elif type(x) is list:
            print(x)
            s += sum_list(x)
    return s

# global l
# l = []
# def sum_list(lst):
#     for i in lst:
#         if type(i) is list:
#             sum_list(i)
#         else:
#             l.append(i)
#     return sum(l)

# print(sum_list(L))



# 3. 改写之前的学生信息管理程序
#   　　要求添加四个功能:
#       |５）按学生成绩高-低显示学生信息　|
#     　　|６）按学生成绩低-高显示学生信息　|
#       |７）按学生年龄高-低显示学生信息　|
#       |８）按学生年龄低-高显示学生信息　|



# def input_student():
#     while True:
#         name = input("请输入姓名：")
#         if not name:
#             break
#         age = input("请输入年龄：")
#         while not age :
#             age = input("请输入年龄：")
#         score = input("请输入成绩：")
#         while not score :
#             score = input("请输入成绩：")
#         d = {}
#         d["name"] = name
#         d["age"] = age
#         d["score"] = score
#         L.append(d)
#     return L

# def output_student(l):
#     print("+" + "-"* 12 + \
#         "+" + "-" * 10 + \
#         "+" + "-" * 9 + "+")
#     print("|", "name".center(10), \
#         "|", "age".center(8), "|", \
#         "score".center(6), "|" )
#     print("+" + "-"* 12 + "+" +\
#      "-" * 10 + "+" + "-" * 9 + "+")
#     for i in l:
#         n = i["name"]
#         a = i["age"]
#         s = i["score"]
#         print("|", \
#             n.center(10), "|",\
#             a.center(8), "|", \
#             s.center(6), "|" )
#         #print("|"%s"|"%s"|"%s"|")
#     print("+" + "-"* 12 + \
#         "+" + "-" * 10 + \
#         "+" + "-" * 9 + "+")

# def Pop_student(valus):
#     for i in L:
#         n = i["name"]
#         if valus == n:
#             L.remove(i)

# def repair_student(valus):  #修改学生信息
#     for i in L:             #遍历Ｌ
#         n = i["name"]
#         if valus == n:
#             print("输入修改的信息：\n")
#             name = input("请输入姓名：")
#             age = input("请输入年龄：")
#             score = input("请输入成绩：")
#             i["name"] = name
#             i["age"] = age
#             i["score"] = score
#             print("修改成功")
#             break
#     else:
#         print("你输入的姓名不在！")

# def show_menu():
#     print("""
#     +------------------------------------+ 
#     |１）添加学生信息                     |   
#     |２）显示学生信息                     |
#     |３）删除学生信息                     |
#     |４）修改学生信息                     |   
#     |５）q退出　　　　　　                |
#     |５）按学生成绩高-低显示学生信息　     |
#     |６）按学生成绩低-高显示学生信息　     |
#     |７）按学生年龄高-低显示学生信息　     |
#     |８）按学生年龄低-高显示学生信息　     |
# 　　+------------------------------------+
# """)


# def sorted_gradeh(l):
#     def grades(i):
#         return i["score"]
#     list_ = sorted(l,key=grades, reverse=True)
#     output_student(list_)

# def sorted_gradel(l):
#     def grades(i):
#         return i["score"]

#     list_ = sorted(l,key=grades)
#     output_student(list_)


# def sorted_ageh(a):
#     def ages(i):
#         return i["age"]
#     age_ =sorted(a,key = ages, reverse = True)
#     output_student(age_)

# def sorted_agel(a):
#     def ages(i):
#         return i["age"]
    age_ =sorted(a,key=lambda d: d["age"])
#     output_student(age_)

# def main():
#     show_menu()
#     while True:
#         i = input("请选择：")
#         if i == "q":
#             break
#         elif i == "1":
#             input_student()
#         elif i == "2":
#             output_student(L) 
#         elif i == "3":
#             name = input("删信息人的姓名：")
#             Pop_student(name)
#         elif i == "4":
#             name = input("请输入要修改人的姓名：")
#             repair_student(name)
#         elif i == "5":
#             sorted_gradeh(L)   
#         elif i == "6":
#             sorted_gradel(L)
#         elif i == "7":
#             sorted_ageh(L)
#         elif i == "8":
#             sorted_agel(L)


# L = [] 
# main()