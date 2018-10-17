# 2. 输入三行文字，让这三行文字在一个方框内居中显示
#    如输入:
#      hello!
#      I'm studing python!
#      I like python
#   显示如下
#     +---------------------+
#     |       hello!        |
#     | I'm studing python! |
#     |    I like python    |
#     +---------------------+
#   注:请不要输入中文

a = input("请输入第一行文字: ")
b = input("请输入第二行文字: ")
c = input("请输入第三行文字: ")

max_length = max(len(a), len(b), len(c))
first_line = '+' + '-' * (max_length + 2) + '+'
print(first_line)
# 打印中间文字
print('| ' + a.center(max_length) + ' |')
print('| ' + b.center(max_length) + ' |')
print('| ' + c.center(max_length) + ' |')

print(first_line)


