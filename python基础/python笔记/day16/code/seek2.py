# seek.py


# 此示例示意用seek改变文件的读写位置,用tell来得到读写位置

f = open('myseek.txt', 'rb')
b = f.read(2)  # b'AB' 读取出来
print(b)  # b'AB

# 从头开始向后走5个字节
# f.seek(5, 0)

# 从当前位置向后走3个字节
# f.seek(3, 1)

# 从文件尾向前数15个字节
f.seek(-15, 2)

b = f.read(5)
print(b)  # b'abcde'

f.close()

