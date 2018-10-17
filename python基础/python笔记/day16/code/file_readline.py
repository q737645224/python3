# file_open.py


# 此示例示意文件的打开和 '读' 操作
try:
    f = open('./myfile.txt')  # 不存在此文件
    print("打开文件成功")

    # 此处要进行读操作
    s = f.readline()  # 读取一行数据，当读取的'\n'就返回
    print("len(s)=", len(s))
    print('s:', s)
    s = f.readline()  # 读取第二行
    print("第二行:", s)
    s = f.readline()  # 读取第三行
    print("第三行:", s)
    s = f.readline()  # 只能读取空字符串(表示已经到达文件尾)
    if s == '':
        print("--------已到达文件尾---------")
    f.close()  # 半闭文件
except OSError:
    print("文件打开失败")