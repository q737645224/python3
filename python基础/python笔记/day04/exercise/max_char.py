# 1. 输入一行字符串，将字符串中Unicode编码值最大的一
#    个字符打印出来（不允许用max函数)
#   (提示: while语句内可以嵌入 if 语句进行判断)



s = input('请输入字符串: ')  # 'ABCD'

zuida = s[0]  # 先假设第一个字符最大
i = 1  # 循环变量，用于记录字符串第二个字符起的起始位置
       # i一定小于len(s) 字符串长度
while i < len(s):  # 当索引超出最大索引时结束循环
    next_char = s[i]  # 获取下一个字符
    # 如果下一个字符的编码值大于zuida的编码值，则改变zuida
    if ord(next_char) > ord(zuida):
        zuida = next_char
    i += 1  # 下标(索引)向后移动一个

print("编码值最大的一个字符是:", zuida)

