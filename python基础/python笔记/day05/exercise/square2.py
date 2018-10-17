# 2. 写程序来改写上题:
#   如输入: 5
#   打印如下:
#     1 2 3 4 5
#     2 3 4 5 6
#     3 4 5 6 7
#     4 5 6 7 8
#     5 6 7 8 9
#   如输入: 3
#   打印如下:
#     1 2 3
#     2 3 4
#     3 4 5

w = int(input("请输入: "))
for line in range(1, w + 1):
    for x in range(line, line + w):
        print('%2d' % x, end=' ')
    print()  # 打印完毕后换行


