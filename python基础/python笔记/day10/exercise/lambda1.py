# 1. 写一个lambda 表达式，判断这个数的2次方+1是否能
#    被5整除，如果能被整除返回True, 否则返回False
#    例:
#       fa = lambda x: .....
#       print(fa(2))  # True
#       print(fa(4))  # False


fa = lambda x: (x ** 2 + 1) % 5 == 0

print(fa(2))  # True
print(fa(4))  # False

