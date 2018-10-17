# #homework
#题目一
# n=int(input("输入数字："))
# i=1
# sums1=1
# while i<=n:
#     sums1=sums1+1/2**i
#     i=i+1
# print(sums1)




 
# w=int(input("请输入:"))
# sums2=0
# i=1
# while i <= w:
#     sums2 = sums2 + (-1) ** (i-1) * 1/(2*i-1)
#     i=i+1
# else:
#     print("和为：",sums2)



n=int(input("请输三角形的宽度："))
i=1
while i<=n:
    print("*"*i)
    i=i+1
print()
i=1
while i<=n:
    print(" "*(n-i)+"*"*i)
    i=i+1
print()



j=1
while j<=n:
    print(" "*(j-1)+"*"*(n-(j-1)))
    j=j+1
print()
j=1
while j<=n:
    print("*"*(n-(j-1))+" "*(j-1))
    j=j+1
print()