# file_write.py


# 此示例示意文本文件的写操作

try:
    f = open('mynote.txt', 'w')  # 'w'代表只写模式
    print("文件打开成功")

    # f.write('hello')
    # f.write('world')
    # f.write("你好")
    f.write("中文")

    f.close()
except OSError:
    print("打开文件失败!")