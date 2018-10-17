# 2. 写一个函数is_prime(x) 判断x是否是素数
#   用filter函数打印出: 20 ~ 30之间的全部素数


def is_prime(x):
    if x < 2:
        return False
    # 排序法
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for x in filter(is_prime, range(20, 30)):
    print(x)



