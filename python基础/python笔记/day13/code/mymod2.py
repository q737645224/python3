# mymod.py
# 自示例示意模块的文档字符串

'''我的自定义模块mymod2

此模块有两个函数
  myfac和 mysum
...
'''

def myfac(n):
    '''自定义用来测试用的myfac的文档字符串'''
    print('正在计算', n, '的阶乘')


def mysum(n):
    print("正在计算1+2+3+...+%d的和" % n)


name1 = "Audi"
name2 = "TESLA"

print("mymod模块被加载!")
