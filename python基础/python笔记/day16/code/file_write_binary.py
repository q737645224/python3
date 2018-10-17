# file_write_binary.py


# 此示例示意以二进制文件操作方式进行写文件

f = open('mybinary.bin', 'wb')

b = bytes(range(0, 256))
print("字节串的内容是:", b)

f.write(b)  # 写入256个字节

f.close()  # 关闭文件

