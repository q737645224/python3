# stdin.py


import sys

while True:
    s = sys.stdin.readline()
    if len(s) < 2:
        break
    print("刚才读入", len(s), '个字符')
    print("内容是:", s)

print("程序结束")