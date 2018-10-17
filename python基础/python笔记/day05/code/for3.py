# for3.py

s = 'ABCDE'

for c in s:
    print(c)
    if c == 'D':
        break
else:
    print('for语句因为可迭代对象不能提供数据而结束')