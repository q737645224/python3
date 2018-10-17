# 2. 写一个生成器函数，生成斐波那契数列的前n个数
#    1 1 2 3 5 8 13
#     def fibonacci(n):
#         ...
#         yield...
#   1) 输出前20个数:
#     for x in fibonacci(20):
#         print(x)
#   2) 打印前40个数的和:
#      print(sum(fibonacci(40)))


# 方法1
# def fibonacci(n):
#     L = [0, 1]
#     while len(L) <= n + 1:
#         yield L[-1]
#         L.append(L[-1] + L[-2])

def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        # 在此处生成返回一个斐波那契数
        yield b  # b则是要生成的数
        # 准备下次要生成的数
        a, b = b, a + b
        count += 1


# 1) 输出前20个数:
for x in fibonacci(20):
    print(x)

# 2) 打印前40个数的和:
print(sum(fibonacci(40)))




