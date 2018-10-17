# month.py
# 2. 输入一年中的月份(1~12) 输出这个月在哪儿
# 个季度，如果输入的是其它数，则提示您输错了

n = int(input("请输入月份(1~12): "))
if 1 <= n <= 3:
    print("春季")
elif 4 <= n <= 6:
    print("夏季")
elif 7 <= n <= 9:
    print("秋季")
elif 10 <= n <= 12:
    print("冬季")
else:
    print("您的输入有误!")

