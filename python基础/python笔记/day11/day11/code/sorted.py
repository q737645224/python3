# sorted.py

L = [5, -2, -4, 0, 3, 1]
L2 = sorted(L)  # L = [-4, -2, 0, 1, 3, 5]
L3 = sorted(L, reverse=True)  # 降序排序

L4 = sorted(L, key=abs)  # L4 = [0, 1, -2, 3, -4, 5]

print(L4)
L5 = sorted(L, key=abs, reverse=True)  # L5 = [5, -4, 3, -2, 1, 0]
print("L5=", L5)
