# 练习:
#   写一个函数叫hello(name),部分代码如下:
#   count = 0
#   def hello(name):
#       print('你好', name)
#       ... 此处代码省略,需要同学们自己填写
#       ... 此处代码需要改变全局变量来记录此函数曾经被调用过多少次.
  
#   hello('小张')
#   hello('小李')
#   print('hello 函数被调用', count, '次')  # 2次



count = 0  # 此变量用于记录hello函数调用的次数


def hello(name):
    print('你好', name)
    global count
    count += 1  # count = count + 1


hello('小张')
hello('小李')
print('hello 函数被调用', count, '次')  # 2次

