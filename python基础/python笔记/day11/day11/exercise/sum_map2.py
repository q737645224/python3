# 2. 用map函数求:
#   1**4 + 2**4 + 3 ** 4 + .... 20**4 的和

s = sum(map(lambda x: x**4, range(1, 21)))

print('和是:', s)