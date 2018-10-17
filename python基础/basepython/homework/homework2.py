#homework2.py
w=int(input("请输入:"))
sums2=0
i=1
while i <= w:
    sums2=sums2+(-1)**(i-1)*1/(2*i-1)
    i=i+1
else:
    print(sums2)