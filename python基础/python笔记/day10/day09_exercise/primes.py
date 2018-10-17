# 1. 写一个函数isprime(x) 判断x是否为素数。如果是
#    素数，返回True,否则返回False

def isprime(x):
    if x < 2:
        return False
    # 用排除法判断x 能否被 2, 3, ... x -1 整除
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


# 2. 写一个函数prime_m2n(m, n) 返回从m开始，到n结束(不包含n)范围内的素数，返回这些素数的列表并打印
#   如:
#     L = prime_m2n(5, 10)
#     print(L)  [5, 7]
def prime_m2n(m, n):
    L = []  # 先准备容器，准备放入数据
    for x in range(m, n):
        if isprime(x):
            L.append(x)
    return L


L = prime_m2n(5, 10)
print(L)  # [5, 7]
# 3. 写一个函数pimes(n) 返回小于n的全部素数的列表,并打印这些素数
#   如:
#     L = primes(10)
#     print(L)  # [2, 3, 5, 7]
#   1) 打印100 以内的全部素数
#   2) 打印200 以内的全部素数的和


def primes(n):
    return prime_m2n(0, n)

L = primes(10)
print(L)  # [2, 3, 5, 7]
#   1) 打印100 以内的全部素数
print(primes(100))

#   2) 打印200 以内的全部素数的和
print(sum(primes(200)))
