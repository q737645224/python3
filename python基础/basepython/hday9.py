#hday9.py
# １．写一个函数minmax(a, b, c)  有三个参数，这回这三个参数中的最小值和最大值，
# 　　　　要求，形成元组，最小值在前，最大值在后
# def getminmax(a, b, c):
   
#     d = (min(a, b, c),max(a, b, c))
#     return d   #返回多个值，大个包（列表，元组）
# t = getminmax(11, 33, 22)
# print(t)  # (11, 33)  # <<< 打印元组
# print("最小值:%d,最大值：%d" %(t[0], t[1]))
# print("最小数：%d，　最大值：%d" % t)


# ２．写一个函数 myadd, 此函数可以计算两个数的和,也可以
# 　　　计算三个数的和

# def myadd(a,b,c=0):
#     a = a + b +c
#     return a
# print(myadd(1,2))
# print(myadd(1,2,4))

# 写一个函数，print_odd, 此函数可以传递一个实参，也可以传递
# 两个实参，当传递一个实参时代表结束值当传递两个实参时，第一个实参
# 代表起始值，第二个实参代表结束值打印出以此区间内的全部奇数，
# 不包含结束数:

# def print_odd(a, b=0):
#     for i in range(a,b):
#         if i % 2 != 0:
#             print(i, end="")
# print_odd(10)
# print_odd(11, 20)


# 写一个myrange函数：
# 　　此函数用给定的参数，返回一个存有对应整数的列表
# 如：
# 　　　def myrange(start,stop=None,step=1):
#     ...
#     L = myrange(s)

# def myrange(start, stop=None, step=1):
    
#     L = list()
#     if stop is none:
#         i = 0
#         while i < start:
#             L = L.append(i)
#             i = i + step
#         return L
#     else :
#         i = start
#         while i < stop:
#             L = L.append(i)
#             i = i + step
    



# def myrange(start, stop=None, step=1):
#     L = []
#     if stop is None:
#         stop = start
#         start = 0
#         #print("开始值：", start,　"终止值", "步长"，　step)
#         i =start
#         while i < stop:
#             L.append(i)
#             i += step
        
#     else:
#         if step > 0:
#             i =start
#             while i < stop:
#                 L.append(i)
#                 i += step
#         else:
#             i =start
#             while i > stop:
#                 L.append(i)
#                 i += step
#     return L


# l =myrange(10)
# print(l)

# 写一个函数, mysum可以传入任意个实参的数字,返回所有实参的和

#   def mysum(*args):

# def mysum(*args):
#     sums = 0
#     for i in args:
#         sums += i
#     return sums
# print(mysum(1, 2, 3, 4, 5, 6))

# def mysum(*args):
#     return sum(args)


# 写一个函数，mymax类似于 内键的函数max
# 详见:
#   >>> help(max)
# 仿造 max 写一个mymax函数，功能与max完全相同

# def mymax(arg1, arg2, *args):
#     if arg1 > arg2 :
#         maxs = arg1
#     else:
#         maxs = arg2
#     for i in args:
#         if maxs < i:
#             maxs = i
#     return maxs


# 1.
# def mymax(arg1, *args):
#     if not args: #元组为空，只是a绑定一个可迭代对象
#         zuida = arg1[0] #先假设第一个数最大
#         for x in arg1:
#             if x > zuida:
#                 zuida = x
#             return zuida
#     else:
#         zuida = arg1
#         for i in args:
#             if zuida < i:
#                 zuida = i
#         return zuida

# 2.
# def mymax(arg1, *args):
#     if not args: #元组为空，只是a绑定一个可迭代对象
#         zuida = arg1[0] #先假设第一个数最大
#         for x in arg1:
#             if x > zuida:
#                 zuida = x
#     else:
#         zuida = arg1
#         for i in args:
#             if zuida < i:
#                 zuida = i
#     return zuida

# 3.
# def mymax(a,*args):
#     if not args:
#         return max(a)
#     else:
#         return max(a,max(args))
#         #return max(a, *args)

# print(mymax(1,2,3))   
# print(mymax(1, 2, 3, 51, 6, 7))
# print(mymax([1,2,3,5]))  


# # 查看 >>>help(print)猜想print函烽的参数列表 是如何定义的?
# def myprint(*args, sep=" ", end= "\n"):
#     pass

# 练习：
#     １．写一个函数mysum(n),此函数用来计算１＋２＋３＋４＋...
#     　　　＋n的二和。

# def mysum(n):
#     sums = 0
#     for i in rang(1,n+1):
#         sums += i
#     return sums

# 2.实现带有界面的学生信息管理系统
# 　操作界面：
#     ＋－－－－－－－－－－－－－－－－－－－－－－＋
#     ｜１）添加学生信息　　　　　　　　　　　　　　　　　　　　　　　｜
#     ｜２）显示学生信息　　　　　　　　　　　　　　　　　　　　　　　｜
#     ｜３）删除学生信息　　　　　　　　　　　　　　　　　　　　　　　｜
#     ｜４）修改学生信息　　　　　　　　　　　　　　　　　　　　　　　｜
#     ｜５）q退出　　　　　　　　　　　　　　　　　　　　　　　　　　　　　｜
# 　　　　＋－－－－－－－－－－－－－－－－－－－－－－＋
# 选择：１
# 修改之前学生信息管程序，学生信息依旧为：
#     姓名，年龄，成绩
# 要求：每个功能写一个函数与之相对应

def input_student():
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

def get_student():
    L = input_student()
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

def Pop_student(valus):
    for i in L:
        n = i["name"]
        if valus == n:
            L.remove(i)

def repair_student(valus):  #修改学生信息
    for i in L:             #遍历Ｌ
        n = i["name"]
        if valus == n:
            print("输入修改的信息：\n")
            name = input("请输入姓名：")
            age = input("请输入年龄：")
            score = input("请输入成绩：")
            i["name"] = name
            i["age"] = age
            i["score"] = score
            print("修改成功")
            break
    else:
        print("你输入的姓名不在！")

L = []
# def infomation_mutual():
print("""
    +------------------------------------+ 
    |１）添加学生信息                     |   
    |２）显示学生信息                     |
    |３）删除学生信息                     |
    |４）修改学生信息                     |   
    |５）q退出　　　　　　                |
　　+------------------------------------+
""")
while True:
    i = input("请选择：")
    if i == "1":
        input_student()
    elif i == "2":
        output_student(L) 
    elif i == "3":
        name = input("删信息人的姓名：")
        Pop_student(name)
    elif i == "4":
        name = input("请输入要修改人的姓名：")
        repair_student(name)
    elif i == "q":
        break



