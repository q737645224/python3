# file_open.py


# 此示例示意文件的打开和 '读' 操作
try:
    f = open('./myfile.txt')  # 不存在此文件
    print("打开文件成功")

    # 此处要进行读操作
    s = f.read()  # 读取全部的内容，形成字符串用s绑定
    print("读取到", len(s), '个字符')
    print("内容是:　", s)

    f.close()  # 半闭文件
except OSError:
    print("文件打开失败")