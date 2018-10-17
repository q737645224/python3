# if2.py

# 输入一个数，用程序来判断这个数是正数，负数，还是零
n = int(input("请输入一个数: "))

if n > 0:
    print('正数')
elif n < 0:
    print('负数')
else:
    print('零')

print("程序结束")