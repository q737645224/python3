i=1
while i <=20:
    print(i,end=' ')
    i += 1
else:
    print()

i=1
while i<=20:
    print(i,end=' ')
    if i%5 == 0:
        print()
    i += 1
else:
    print()

print ("输入要计算的数：")
n=int(input())
i=1
sum=0
while i<= n:
    sum=sum +i
    i += 1
print(sum)   



if begin<end:
    i=begin
    whlie i < end:
        print(i,end＝"　")
        i +=1
else:
    begin,end=end,begin
    i=begin
    whlie i < end:
        print(i,end＝"　")
        i +=1