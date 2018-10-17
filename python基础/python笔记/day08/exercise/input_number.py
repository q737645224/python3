# 2. 写一个函数 input_number
#     def input_number():
#         ....

#     此函数用来获取用户循环输入的整数，当用户输入负数时结束输入。将用户输入的数字以列表的形式返回，再用内建函数max, min, sum取出户输入的最大值，最小值及和

#     L = input_number()
#     print(L)  # 打印此列表
#     print("用户输入的最大数是:", max(L))
#     print("用户输入的最小数是:", min(L))
#     print("用户输入的数的和是:", sum(L))


def input_number():
    # 此处得到键盘输入的整数，最后以列表的形式返回回去
    lst = []
    while True:
        n = int(input("请输入一个大于零的整数: "))
        if n < 0:
            break
        lst.append(n)

    return lst


L = input_number()
print(L)  # 打印此列表
print("用户输入的最大数是:", max(L))
print("用户输入的最小数是:", min(L))
print("用户输入的数的和是:", sum(L))
