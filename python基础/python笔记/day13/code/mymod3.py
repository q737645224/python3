# mymod3.py


'''此示例示意 mymod3的 __name__属性的用法'''
def test():
    pass


print("__name__属性绑定的值是:", __name__)


if __name__ == '__main__':
    print("当前mymod3.py 正在以主模块运行")
else:
    print("当前mymod3.py 正在被其它模块导入")
    print("我的模块名是", __name__)



