#day502.py
n=int(input("输指定的整数："))
i=1
while i<=n:
    j=1
    while j<=n:
        print(j,end=' ')
        j +=1
    print()
    i +=1
          
i=1
while i<=n:
    if i=1:
    print("#"*n)
    elif 1<i<n:
        fmt=" "*(n-2)
        print("#"+fmt+"#")
        print("#",end=' ')
    else:
        print("#"*n)
    i +=1
