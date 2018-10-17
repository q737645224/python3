# file_write.py


# 此示例示意文本文件的写操作

try:
    f = open('mynote2.txt', 'w')  # 'w'代表只写模式
    print("文件打开成功")
    L = ['你好', 'tarena', 'abc']

    f.writelines(L)

    f.close()
except OSError:
    print("打开文件失败!")