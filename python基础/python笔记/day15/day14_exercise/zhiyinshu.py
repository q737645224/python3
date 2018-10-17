# 2. 分解质因数, 输入一个正整数,分解质因数,
#   如:
#     输入: 90
#   则打印:
#     '90=2*3*3*5'
#     (质因数是指最小能被原数整除的素数(不包括1))


def is_primes(x):
    if x <= 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# def get_zhiyishu(n):
#     '''用循环来实现'''
#     L = []
#     # 如果n不是素数就循环取出一个质因数
#     while not is_primes(n):
#         for i in range(2, n):
#             if n % i == 0:
#                 L.append(i)  # i是质数数
#                 n = int(n / i)  # 转为整数
#                 break
#     else:  # n一定为最后一个质因数
#         L.append(n)
#     return L

def get_zhiyishu(n):
    '''递归方式实现'''
    L = []
    # 如果n已经为素数，终止递归，把L 返回回去
    if is_primes(n):
        L.append(n)
        return L
    for i in range(2, n):
        if n % i == 0:
            L.append(i)  # i是质数数
            n = int(n / i)  # 转为整数
            L += get_zhiyishu(n)
            break  # 此处一定要加break 来终止循环
    return L


n = int(input("请输入一个数: "))
print(n, "的质因数是:", get_zhiyishu(n))


