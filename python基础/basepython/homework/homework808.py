#omework808.py
# L = [3, 5]
# L[0:0] = [1, 2]
# print (L)
# L[2:2] = [4]
# L[5:5] = [6]
# print(L)
# # j = 0
# # for i in range(5,0,-1):
# #     j = L[i]
# # str(j)
# # L[:]=j
# L[:] = L[::-1] # ＩＤ不变
# del L[123]
# print(L)

# L = list()
# while 1:
#     i = float(input("请输入整数："))
#     if i == -1:
#         break
#     L += [i]
# print("共输入%d" % len(L))
# print("最大数是%d" % max(L))
# print("最小数是%d" % min(L))
# print("平均数是%d" % (sum(L) / len(L)))


L = list()
while 1 :
    nub = float(input("请输入："))
    L.append(nub)
    #L += [i]
    if nub < 0:
        break
# print("最大的一个数是%d" % max(L))
# L2 = L.copy()
# L2.sort(reversed=True)
# print(L2[0])
# print(L2[1])
# L.remove(min(L))
# print('最后的结果是：')
D=0
print("最大的一个数是%d" % max(L))
L2 = L.copy
zuida = max(L2)
while True:
    if zuida in L2:
        L2.remove(zuida)
    else:
        break
#D = L2.index(max(L2))
#L2.remove(L2[D])
print(max(L2))
zuixiao = min(l)
while zuixiao in L:
    L.remove(zuixiao)
print(L)