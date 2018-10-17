
# 3. 改写之前的学生信息管理程序
#    改为两个函数:
#      1. 写一个函数 input_student() 用于返回学生信息的字典的列表(以前格式一样)
#      2. 写一个函数 output_student(lst)
#        此函数传入一个列表lst,即字典的列表
#        此函数把lst的内容以表格形式打印出来
#     def input_student():
#          ....

#     def output_student(lst):
#          ...

#     L = input_student()  # 获取学生信息的列表
#     output_student(L)  # 把L 以列表的形式打印 


def input_student():
    L = []  # 创建一个容器准备放入
    while True:
        name = input('请输入姓名: ')
        if not name:  # 如果名字为空,结束输入操作
            break
        age = int(input("请输入年龄: "))
        score = int(input("请输入成绩: "))
        d = {}  # 每次都会执行{} 来创建新的字典
        d['name'] = name
        d['age'] = age
        d['score'] = score
        L.append(d)
    return L


def output_student(lst):
    # 打印表格
    print("+---------------+----------+----------+")
    print("|     name      |   age    |   score  |")
    print("+---------------+----------+----------+")
    for d in lst:
        n = d['name'].center(15)
        a = str(d['age']).center(10)
        s = str(d['score']).center(10)
        print("|%s|%s|%s|" % (n, a, s))

    # print("|   xiaozhang   |    20    |   100    |")
    # print("|     xiaoli    |    18    |    98    |")
    print("+---------------+----------+----------+")


L = input_student()  # 获取学生信息的列表
# print(L)
output_student(L)  # 把L 以列表的形式打印 









