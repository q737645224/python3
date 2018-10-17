# 练习:
#   自己写一个文件 'info.txt' 内部存一些文字信息
#     如:
#       张三 20 100
#       李四 21 96
#       小王 22 98
#     写程序将这些数据读取出来，打印到终端上

try:
    f = open('info.txt')
    while True:
        line = f.readline()  # 读取一行
        if line == '':
            break  # 已经到行尾，结束处理

        s = line.strip()
        n, a, s = s.split()  # 拆成列表
        a = int(a)
        s = int(s)
        print("姓名:", n, '年龄:', a, '成绩:', s)
        # print()
    f.close()
except OSError:
    print("打开文件失败")