# 1. 一个球从100米高空落下,每次落地后反弹高度是原高度的
#     一半,再落下,
#    1) 写程序算出皮球在第10次落地后反弹高度是多高?
#    2) 打印出球共经过多少米的路程


def fantan(height, times):
    '''height 原始高度
    times 次数'''
    for _ in range(times):
        height /= 2
    return height


def lucheng(height, times):
    s = 0
    for _ in range(times):
        s += height + height / 2
        height /= 2
    return s

print('从100米反弹十次后高度是:', fantan(100, 10))
print('从100米反弹十次后经历的路程是:', lucheng(100, 10))











