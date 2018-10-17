# 练习:
#   写一个程序,读入任意行的文字,当输入空行时结束输入
#   打印带有行号的输入结果:
#     如:
#       请输入: hello<回车>
#       请输入: world<回车>
#       请输入: tarena<回车>
#       请输入: <回车> # 直接回车结束输入
#     输出如下:
#       第1行: hello
#       第2行: world
#       第3行: tarena


def get_text():
    '''获取终端数据形成列表并返回列表'''
    L = []
    while True:
        s = input("请输入: ")
        if not s:
            break
        L.append(s)
    return L


def output_text(L):
    '''打印带有行号的结果 '''
    for t in enumerate(L, 1):
        print("第%d行: %s" % t)  # (1, 'hello')


if __name__ == '__main__':
    output_text(get_text())


