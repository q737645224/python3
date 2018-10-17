# 练习:
#   创建一个全局变量 L = []
#   写一个函数:
#     def input_number():
#         ....
#     此函数每次调用将从键盘读入一些数字追加到列表L中 

#   如:
#     L = []
#     def input_number():
#         ....
#     input_number()
#     print(L)  # [ .... 这些是您从键盘输入的数..]


L = []
def input_number():
    while True:
        x = int(input("请输入数字: "))
        if x == 0:
            break
        L.append(x)

# 思考:
# def input_number():
#     lst = []
#     while True:
#         x = int(input("请输入数字: "))
#         if x == 0:
#             break
#         lst.append(x)
#     L = lst


input_number()
print(L)  # [ .... 这些是您从键盘输入的数..]
