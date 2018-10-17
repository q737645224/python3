# 2. 给出一个整数n,写一个函数计算myfn(n):
#     1 + 2**2 + 3**3 + .... + n**n的和
#   如:
#     print(myfn(10)) # ???


# def myfn(n):
#     s = 0
#     for i in range(1, n + 1):
#         s += i ** i
#     return s

def myfn(n):
    return sum(map(lambda i: i ** i,
                   range(1, n + 1)
                   )
               )


print(myfn(10))  # 10405071317
