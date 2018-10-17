# 练习:
#   写一个函数 myadd, 此函数可以计算两个数的和,也可
#     以计算三个数的和

#   def myadd(......):
#      ....
#   print(myadd(10, 20))  # 30
#   print(myadd(100, 200, 300))  # 600


def myadd(a, b, c=0):
    return a + b + c


print(myadd(10, 20))  # 30
print(myadd(100, 200, 300))  # 600

