# 　　２．　写程序，将phonenumber.txt文件中的数据读取出来．
# 　　　　　再用以下格式打印出来:
#       如:
#         小张 的电话是 13888888888
#         小李 的电话是 13999999999


def read_from_file(filename='phonenumber.txt'):
    L = []
    f = open(filename)
    while True:
        s = f.readline()
        # 判断是不是到文件尾
        if s == '':
            break
        s = s.strip()  # 去掉换行
        n, number = s.split(',')  # 切为字符串列表
        L.append((n, number))
    return L


L = read_from_file()
print(L)

for n, number in L:
    print(n, '的电话是', number)









