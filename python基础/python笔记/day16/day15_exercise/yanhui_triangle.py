# 3. 写程序打印杨辉三角(只打印6层)
#       1
#      1 1
#     1 2 1
#    1 3　3 1
#   1 4　6 4 1
#  1 5　10 10 5 1

def get_yh_list(n):  # n代表层数
    R_List = []  # 用于存储每一行数据
    L = [1]  # L代表正要生成的行
    for _ in range(n):
        # print(L)
        R_List.append(L)
        # 计算下一行
        next_L = [1]  # 下一行的最左边的元素为1
        # 计算中间的数据元素
        for index in range(len(L) - 1):  # index 代表索引
            next_L.append(L[index] + L[index + 1])
        # 最后一个是1
        next_L.append(1)
        L = next_L  # L绑定新生成的一行
    return R_List


def get_string(L):
    # [1, 2, 1] ---> ['1', '2', '1']
    string_list = [str(x) for x in L]
    # ['1', '2', '1'] ---> '1 2 1'
    return ' '.join(string_list)


def print_YH_List(lst):
    last_line = get_string(lst[-1])
    max_len = len(last_line)  # 算出最后一行有多长

    for x in lst:
        line = get_string(x)
        print(line.center(max_len))


YH = get_yh_list(6)  # YH 绑定数据列表
print(YH)
print_YH_List(YH)















