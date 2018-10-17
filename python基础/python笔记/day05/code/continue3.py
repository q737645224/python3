# continue3.py

# 用while循环打印10以内的偶数
i = 0
while i < 10:
    if i % 2 == 1:
        i += 1
        continue
    print(i)
    i += 1


# for n in range(10):
#     if n % 2 == 1:  # 奇数
#         continue  # 取一下数，后面的事情不做
#     print(n)

