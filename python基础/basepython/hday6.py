#homework day6.py
# L = [1, 3, 2, 1, 6, 4, 2, 98, 82]
# L2 = list()
# L3 = list()
# for x in L:
#     if x in L2:
#         L3 = [x]
#     else:
#         L2 = [x]
# print(L2,L3)


# L = list()
# for x in range(100):
#     if x <= 2:
#         continue
#         i = 2
#     while i < x:
#         if x % i == 0:
#             break
#         i += 1
#     if i == x:
#         L += [x]
# print(L)

# for x in rsange(100):
#     #判断如果Ｘ是素数就打印，不是素数就跳过判断
#     if x < 2:
#         continue
#     for i in range(2, x):
#         if x % i == 0:
#             break
#         else:
#             L.append(x)





# i = 1
# j = k =1
# s = 0
# L = list()
# n = int(input())
# while i <= n:
#     j = k
#     k = s
#     s = j + k
#     L += [s]   #L.append(s)
#     i = i + 1
# print("输出的列表为：",L)


a = 0
b = 1
while len(L) < 40:
    L.append(b)
    c = a + b
    a = b
    b = c

a, b = b, a + b
print(L)

L = [1, 1]
while len(L) < 40:
    L.append(L[-1] + L[-2])