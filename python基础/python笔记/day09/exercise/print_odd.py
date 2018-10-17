# 2. 写一个函数，print_odd, 此函数可以传递一个实参，也可以传递两个实参，当传递一个实参时代表结束值
# 当传递两个实参时，第一个实参代表起始值，第二个实参代表结束值
#    打印出以此区间内的全部奇数，不包含结束数:
# print_odd(10)  # 1 3 5 7 9
# print_odd(11, 20)  # 11 13 15 17 19     


# 方法1
def print_odd(a, b=0):
    if b == 0:
        for x in range(1, a, 2):
            print(x, end=' ')
        else:
            print()
    else:
        if a % 2 == 0:  # 如果是偶数，变为奇数
            a += 1
        for x in range(a, b, 2):
            print(x, end=' ')
        else:
            print()

def print_odd(a, b=None):
    if b is None:
        start = 1
        end = a
    else:
        start = a
        end = b
    # 如果开始的偶数，做校正
    if start % 2 == 0:
        start += 1
    for x in range(start, end, 2):
        print(x, end=' ')
    print()


print_odd(10)  # 1 3 5 7 9
print_odd(11, 20)  # 11 13 15 17 19     
print_odd(10, 20)
print_odd(5, 0)
