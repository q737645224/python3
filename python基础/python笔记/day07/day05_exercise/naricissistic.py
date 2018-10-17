# 4.算出100~1000以内的水仙化数(Naricissistic Number)
#   水仙花数是指百位的3次方 加上 十位的3次方 加上 个位
#   的3次方等于原数的数
#   如:
#     153 = 1**3 + 5**3 + 3**3
#   答案:
#     153, 370, ....

# 方法1
# for i in range(100, 1000):
#     s = str(i)  # 转为字符串
#     bai = int(s[0])  # 百位
#     shi = int(s[1])  # 十位
#     ge = int(s[2])  # 个位
#     if i == bai ** 3 + shi ** 3 + ge ** 3:
#         print(i)

# 方法2
# for i in range(100, 1000):
#     bai = i // 100  # 百位
#     shi = i % 100 // 10  # 十位
#     ge = i % 10  # 个位
#     if i == bai ** 3 + shi ** 3 + ge ** 3:
#         print(i)

# 方法3
for bai in range(1, 10):
    for shi in range(10):
        for ge in range(10):
            i = bai * 100 + shi * 10 + ge
            if i == bai ** 3 + shi ** 3 + ge ** 3:
                print(i)
            

