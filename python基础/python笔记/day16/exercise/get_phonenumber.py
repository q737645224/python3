# 1. 写程序，循环输入很多个人的姓名，电话号码,
#   当输入结束后将这些信息存入到文件phonenumber.txt中
#   (建议先用列表暂存数据，格式自己定义)


def get_numbers():
    L = []
    while True:
        n = input("请输入姓名: ")
        if n == '':
            break
        number = input('请输入电话号码:　')
        L.append((n, number))
    return L


def save_to_file(lst, filename='phonenumber.txt'):
    f = open(filename, 'w')
    for n, number in lst:
        f.write(n)
        f.write(',')
        f.write(number)
        f.write('\n')
    f.close()  # 关闭文件


L = get_numbers()
print(L)
save_to_file(L)