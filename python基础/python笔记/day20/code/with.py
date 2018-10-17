# with.py


#  此示例示意用with语句打开文件和自动关闭文件的操作
# try:
#     f = open('a.txt')
#     try:
#         for x in f:
#             print(x)
#             int('abc')  # 出错异常
#     finally:
#         f.close()
# except OSError:
#     print("打开文件失败")
# except ValueError:
#     print('操作文件过程中失败')


try:
    with open('a.txt') as f:
        for x in f:
            print(x)
            int("abc")  # 出现异常
except OSError:
    print("打开文件失败")
except ValueError:
    print('操作文件过程中失败')

