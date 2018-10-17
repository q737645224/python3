# filter.py


# 写一个函数判断x是否为奇数，奇数返回True,偶数返回False
def is_odd(x):
    if x % 2 == 1:
        return True
    return False


# 生成1~10以内奇数的列表  # [1, 3, 5, 7, 9]
for x in filter(is_odd, range(1, 10)):
    print(x)

L = [x for x in filter(is_odd, range(1, 10))]

print(L)  # [1, 3, 5, 7, 9]


