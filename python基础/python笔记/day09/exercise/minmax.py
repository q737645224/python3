# 练习:
#   写一个函数minmax(a, b, c)  有三个参数，这回这三个参数中的最小值和最大值，
#   要求，形成元组，最小值在前，最大值在后，如:

#   def minmax(a, b, c):
#       ...

#   t = minmax(11, 33, 22)
#   print(t)  # (11, 33)  # <<< 打印元组
#   xiao, da = minmax(6, 5, 4)
#   print('最小值:', xiao, '最大值:', da)


def minmax(a, b, c):
    zuida = a
    if b > zuida:
        zuida = b
    if c > zuida:
        zuida = c

    zuixiao = a
    if b < zuixiao:
        zuixiao = b
    if c < zuixiao:
        zuixiao = c

    return (zuixiao, zuida)
    # return (min(a, b, c), max(a, b, c))


t = minmax(11, 33, 22)
print(t)  # (11, 33)  # <<< 打印元组
xiao, da = minmax(6, 5, 4)
print('最小值:', xiao, '最大值:', da)

t = minmax(2, 1, 3)
print(t)
