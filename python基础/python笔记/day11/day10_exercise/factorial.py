

# 练习:
#   1. 给出一个整数n,写一个函数myfac来计算n!(n的阶乘)
#     n! = 1 * 2 * 3 * 4 * ..... * n
#     如:
#       print(myfac(5))  # 120


def myfac(n):
    m = 1
    for x in range(2, n + 1):
        m *= x
    return m

print(myfac(5))  # 120