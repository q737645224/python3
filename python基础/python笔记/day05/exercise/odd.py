# 练习:
#   输入一个整数用begin绑定,
#   再输入一个整数用end绑定
#   打印从begin开始，到end结束内的全部奇数(不包含end)


begin = int(input("请输入开始整数: "))
end = int(input("请输入结束整数: "))

for x in range(begin, end):
    if x % 2 == 0:
        continue
    print(x)

