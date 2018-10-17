# 练习:
#   输入一个整数用begin绑定,
#   再输入一个整数用end绑定
#   打印从begin开始，到end结束内的全部奇数(不包含end)

# 2. 将上述练习改写为 用while语句实现

begin = int(input("请输入开始整数: "))
end = int(input("请输入结束整数: "))

# 方法1
# i = begin
# while i < end:
#     if i % 2 == 0:
#         i += 1
#         continue
#     print(i)
#     i += 1

# 方法:
i = begin
while i < end:
    i += 1
    if (i - 1) % 2 == 0:
        continue
    print(i - 1)


