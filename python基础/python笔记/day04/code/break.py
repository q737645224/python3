# break.py

# 此示例示意break语句的用法

i = 1
while i <= 6:
    print("循环开始时:", i)
    if i == 3:
        break
    print("循环结束时:", i)
    i += 1
else:
    print("这是else子句里的语句")