# 练习:
#   求 100以内有哪儿些整数与自身+1的乘积再对11求余的
#     结果等于8?
#       x * (x+1) % 11 == 8  x附合条件

for x in range(100):
    if x * (x + 1) % 11 == 8:
        print(x)
