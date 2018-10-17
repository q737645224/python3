# file_open.py


# 此示例示意文件的打开和关闭操作
try:
    f = open('./aaa.txt')  # 不存在此文件
    # f = open('./myfile.txt')  # 不存在此文件
    print("打开文件成功")

    # 此处要进行读/写操作

    f.close()  # 半闭文件
except OSError:
    print("文件打开失败")