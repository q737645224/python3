# file_open.py


# 此示例示意文件的打开和用 readlines '读' 操作
try:
    f = open('./myfile.txt')  # 不存在此文件
    print("打开文件成功")

    # 此处要进行读操作
    L = f.readlines()
    print("L=", L)

    f.close()  # 半闭文件
except OSError:
    print("文件打开失败")