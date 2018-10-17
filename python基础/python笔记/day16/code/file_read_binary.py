# file_read_binary.py


f = open('py.tar.gz', 'rb')  # 'b' 二进制模式

b = f.read(4)
print('b的类型是:', type(b))

print("b的内容是:", b)

f.close()

