# 4. 编写函数 fn(n) 此函数返回下列级数的和:
#     fn(n) = 1/(1*2) + 1/(2*3) + .... 
#     + 1/(n*(n-1)) 的和

#   print(fn(100))


def fn(n):
    Sn = 0
    for i in range(2, n + 1):
        Sn += 1 / ((i - 1) * i)
    return Sn


print(fn(100))

