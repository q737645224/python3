# 3. 求 1~100 之间所有不被 5, 7, 11 整除的数的和
#   (可以考虑用continue实现)

s = 0  # 用于累加

for x in range(1, 101):
    if x % 5 == 0 or x % 7 == 0 or x % 11 == 0:
        continue
    # if x % 5 == 0:
    #     continue
    # if x % 7 == 0:
    #     continue
    # if x % 11 == 0:
    #     continue
    s += x

print("和是：", s)




