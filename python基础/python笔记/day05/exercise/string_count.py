# 练习:
#   任意输入一段字符串
#     1) 计算您输入的字符'A' 的个数，并打印出来
#     2) 计算出空格的个数，并打印出来
#       (要求用for语句，不允许使用, S.count方法)

#   思考用while语句能否实现上述功能

# 任意输入一段字符串
s = input("请输入: ")  # "ABCABA"

# 1) 计算您输入的字符'A' 的个数，并打印出来
count_A = 0  # 准备用来记录个数的变量
for ch in s:
    if ch == 'A':
        count_A += 1
print("'A' 这个字符的个数是:", count_A)

# 2) 计算入空格的个数，并打印出来
count_space = 0  # 准备用来记录个数的变量
for ch in s:
    if ch == ' ':
        count_space += 1
print("空格 这个字符的个数是:", count_space)


# 思考用while语句能否实现上述功能
count_A = 0
count_space = 0
i = 0  # 获取字符串数据的索引
while i < len(s):
    ch = s[i]  # 取出字符
    # 先算判断ch是否是'A'
    if ch == 'A':
        count_A += 1
    if ch == ' ':
        count_space += 1
    i += 1

print("'A' 这个字符的个数是:", count_A)
print("空格 这个字符的个数是:", count_space)
