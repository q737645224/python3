# 练习:
#   写一个函数, mysum可以传入任意个实参的数字,返回所有实参的和

#   def mysum(*args):
#      ...
#   print(mysum(1, 2, 3, 4))  # 10
#   print(mysum(10, 20, 30))  # 60

def mysum(*args):
    # s = 0
    # for x in args:
    #     s += x
    # return s
    return sum(args)

print(mysum(1, 2, 3, 4))  # 10
print(mysum(10, 20, 30))  # 60
