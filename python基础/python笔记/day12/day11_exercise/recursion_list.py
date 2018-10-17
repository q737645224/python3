# 2. 已知有列表:
#  L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]
#  1) 写一个函数print_list(lst) 打印出所有元素
#    print(L)  # 打印 3 5 8 10 13 14 ....
#  2) 写一个函数sum_list(lst) 返回这个列表中所有元素的和
#    print(sum_list(L))  # 86
#  注:
#    type(x) 可以返回一个变量的类型
#    如:
#       >>> type(20) is int # True
#       >>> type([1, 2, 3]) is list # True


L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]


# 1) 写一个函数print_list(lst) 打印出所有元素
def print_list(lst):
    for x in lst:
        if type(x) is list:  # 如果x是列表，则再次再印
            print_list(x)
        else:
            print(x)


print_list(L)  # 打印 3 5 8 10 13 14 ....


# 2) 写一个函数sum_list(lst) 返回这个列表中所有元素的和
def sum_list(lst):
    s = 0
    for x in lst:
        if type(x) is list:  # 是列表
            s += sum_list(x)
        else:  # 不是列表
            s += x
    return s


print(sum_list(L))  # 106


