# closure.py


# 闭包示例:
def make_power(y):
    def fn(arg):
        return arg ** y
    return fn


pow2 = make_power(2)  # 请问pow2绑定的是什么？
print('5的平方是:', pow2(5))  

# 求1**2 + 2 ** 2 + 3 ** 2 + .... 100 ** 2
print(sum(map(lambda x: x ** 2, range(1, 101))))
print(sum(map(make_power(2), range(1, 101))))

print("1 ** 3 + 2**3 + ...... + 100 ** 3=")
print(sum(map(lambda x: x ** 3, range(1, 101))))
print(sum(map(make_power(3), range(1, 101))))
# print(sum(map(lambda x: x ** 3, range(1, 101))))
