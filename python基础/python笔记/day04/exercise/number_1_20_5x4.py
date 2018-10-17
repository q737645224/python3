# 4. 打印 1 ~ 20的整数，每行打印5个，打印四行如:
#   1 2 3 4 5
#   6 7 8 9 10
#   11 12 .....
#   .....
#   提示: while中可以嵌入if语句来换行

# 方法1
# i = 1
# while i <= 20:
#     print(i, end=' ')
#     if i == 5:
#         print()
#     if i == 10:
#         print()
#     if i == 15:
#         print()
#     if i == 20:
#         print()
#     i += 1


i = 1
while i <= 20:
    print(i, end=' ')
    if i % 5 == 0:
        print()
    i += 1
