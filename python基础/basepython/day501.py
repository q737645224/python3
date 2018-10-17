#day501.py
begin=int(input("输入开始整数："))
end=int(input("输入结束整数："))
i=begin
while i < end:
    print(i,end=" ")
    i += 1
else:
    print()

count=0
if begin<end:
    i=begin
    while i < end:
        print(i,end=' ')
        count +=1
        if count%5==0:
            print() #print(end='')
        i +=1
else:
    begin,end=end,begin
    i=begin
    while i < end:
        count +=1
        if count%5==0:
            print()
        i +=1
    








