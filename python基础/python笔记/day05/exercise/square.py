# 1. 输入一个数w代表正方形的宽度,打印如下正方形:
# 如输入:5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5
#   1 2 3 4 5

w = int(input("请输入: "))
for line in range(1, w + 1):
    for x in range(1, w + 1):
        print(x, end=' ')
    print()  # 打印完毕后换行


