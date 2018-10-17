#day504.py
n = int(input("请输入长方形宽度："))
print("#"*n)
line = 1
while line <= (n-2):
    print("#"+" "*(n-2)+"#")
    line +=1
 