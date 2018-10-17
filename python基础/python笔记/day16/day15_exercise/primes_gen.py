# 1. 写一个生成器函数primes生成素数，
# 此生成器函数为 primes(begin, end)
# 如: [x for x in primes(10, 20)] 将得到列表
#    [11, 13, 17, 19]


def is_primes(x):
    '''判断x是否为素数,如果为素数返回True,否则返回False'''
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def primes(begin, end):
    for x in range(begin, end):
        if is_primes(x):  # 如果x为素数,则把x返回给next调用
            yield x


L = [x for x in primes(10, 20)]
print(L)
