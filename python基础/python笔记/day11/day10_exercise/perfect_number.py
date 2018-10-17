# 3. 完全数:
#    1 + 2 + 3 = 6 (6为完全数)
#    1,2,3都为6的因数(因数是能被一个数x整除的整数为y,则y为x的因数)
#    1 x 6 = 6
#    2 x 3 = 6
#    完全数是指除自身以外的所有因数相加之和等于自身的数
#    求 4~5个完全数并打印出来
#    答案:
#      6
#      28
#      496
#      ......

def is_perfect_number(n):
    # 此函数判断n是否是完全数，
    # 如果是则返回True,否则返回False
    L = []  # 此列表用于存放　所有的因数
    for x in range(1, n):
        if n % x == 0:  # 整除了．则说明x为n的因数
            L.append(x)
    return sum(L) == n  # 如果因数之和等于n则返回True


def print_number():  # 此函数用于打印所有的完全数
    i = 1
    while True:
        if is_perfect_number(i):
            print(i)  # 打印这个完全数
        i += 1


print_number()  # 开始计算

