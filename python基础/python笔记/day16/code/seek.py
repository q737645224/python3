# seek.py


# 此示例示意用seek改变文件的读写位置,用tell来得到读写位置

f = open('mybinary.bin', 'rb')

f.seek(16, 0)
b = f.read(4)  # 读取从16~20的四个字节的内容
print(b)

f.close()

