# recursion_fac.py

# n! = 1 * 2 * 3 * 4 * ..... * n
# n! = n * (n-1) * (n-2) * ..... 3 * 2 * 1
# 100! = 100 * 99 * 98 * .....  3 * 2 * 1

def fac(n):
    # 此函数用递归的方式实现阶乘
    if n == 1:  # 1! 直接返回1
        return 1
    return n * fac(n - 1)


print(fac(5))  # 120
