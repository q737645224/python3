# 2. 用while语句实现打印:
#    1 3 5 7 9. .... 19 
#    打印在一行内

i = 1
while i <= 19:
    print(i, end=' ')
    i += 2
else:
    print()  # 换行

# 3. 将上题用for语句来实现
for i in range(1, 20, 2):
    print(i, end=' ')
else:
    print()  # 换行
