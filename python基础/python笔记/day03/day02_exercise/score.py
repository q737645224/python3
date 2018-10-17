# 2. 输入一个学生的三科成绩(三个整数):
#   打印出最高分是多少？
#   打印出最低分是多少？
#   打印出平均分是多少？

a = int(input("请输入第一科成绩: "))
b = int(input("请输入第二科成绩: "))
c = int(input("请输入第三科成绩: "))

# if a > b:
#     if a > c:
#         print("最大数是:", a)
#     else:
#         print("最大数是:", c)
# else:
#     if b > c:
#         print("最大数是:", b)
#     else:
#         print("最大数是:", c)

# 先假设 a最大
zuida = a
# 再用b去和zuida判断
if b > zuida:
    zuida = b

if c > zuida:
    zuida = c
print("最高分是:", zuida)
