# 练习:
#   输入三行文字，让这三行文字依次以20个字符的宽度右对齐输出
#   如:
#     请输入第1行: hello world
#     请输入第2行: aaa
#     请输入第3行: ABCDEFG
#   输出结果如下:
#             hello world
#                     aaa
#                 ABCDEFG

#   做完上面的题后思考：
#    能否以最长的字符串的长度进行右对齐显示(左侧填充空格)

a = input("请输入第1行: ")
b = input("请输入第2行: ")
c = input("请输入第3行: ")

# 方法1
print("%20s" % a)
print("%20s" % b)
print("%20s" % c)

# 方法2
# print(' ' * (20 - len(a)) + a)
# print(' ' * (20 - len(b)) + b)
# print(' ' * (20 - len(c)) + c)

print('----------以最长字符串长度进行右对齐------')
# 方法1
# max_length = len(a)
# if len(b) > max_length:
#     max_length = len(b)
# if len(c) > max_length:
#     max_length = len(c)
# print("最长的字符串长度为:", max_length)
# print(' ' * (max_length - len(a)) + a)
# print(' ' * (max_length - len(b)) + b)
# print(' ' * (max_length - len(c)) + c)

# 方法2
max_length = max(len(a), len(b), len(c))

# fmt = '%' + str(max_length) + 's'  # "%数字s"
fmt = '%%%ds' % max_length  # "%数字s"
print('=====>', fmt)
print(fmt % a)
print(fmt % b)
print(fmt % c)
