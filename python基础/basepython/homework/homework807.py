#homework807.py
# n = int(input("输入任意一个数："))
L = list()
for n in range(100):
    i=2
    while i < n:
        if n % i == 0:
            # print("不是素数",n)
            break
        i += 1
    if i == n:
        L += [n]
        # print("为素数",n,L)
print(L)




#max_length = max(len(a),len(b),len(x))
#a.center(max_lengrh)

# i = int(input("输入树高："))
# m=1
# while m <= i:
#     a="*"*(m*2-1)
#     print(a.center(i*2-1))
#     m += 1
# j=1
# while j <= m:
#     print("*".center(i*2-1))
#     j += 1
# for i in range(1,i + 1):
#     stars = s * i - 1
#     blank = n - i
#     print(' ' * blank + '*' * stars)
# for _ in range(n):
#     print(' ' * (n - 1) + '*')


# sums = 0
# for i in range(100,1000):
#     j=str(i)
#     a = j[-1]
#     b = j[-2]
#     c = j[-3]
  #注：   bai = int(j[])
#     sums=int(a)**3+int(b)**3+int(c)**3
#     if sums == i:
#         print(i)

# j = int(input())


# sums=0
# for j in range(100,1000):
#     a = j%10
#     b = j//10   
#     c = b%10     
#     d = b//10 
#     #print(d,c,a)
    
#     #print(sums)
#     if j == sums=a ** 3 + c ** 3 + d ** 3 :
#         print("水仙花:",j)

# for bai in range(1,10):
#     for shi in range(10):
#         for ge in range(10):
#             #print(bai,shi,ge)
#             x  = bai ** 3 + shi ** 3 + ge ** 3
#             if x == bai ** 3 + shi ** 3 + ge ** 3:
#                 print(x)