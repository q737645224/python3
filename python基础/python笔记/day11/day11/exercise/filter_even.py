# 1. 将 1 ～　２０　的偶数用filter生成可迭代对象后将可
#    迭代对象生成的数放入到列表L中

def is_even(x):  # 判断x是否是偶数
    if x % 2 == 0:
        return True
    return False


evens = filter(is_even, range(1, 21))
# L = list(evens)
L = [x for x in evens]

print(L)








