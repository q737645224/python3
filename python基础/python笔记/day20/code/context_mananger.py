# context_mananger.py


# 此示例示意 让一个自定义的类创建的对象能够使用with语句
class A:
    '''此类的对象可用于with语句进行管'''
    def __enter__(self):
        print("已经进入with语句,资源分配成功!")
        return self  # <<<--此处返回的对象将由 as 变量绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("已经离开with语句,资源释放成功!")
        if exc_type is None:
            print("当离开with语句时没有发生异常")
        else:
            print('有异常发生,异常类型是:', exc_type,
                '异常值是:', exc_val)


with A() as a:
    print("这是with中的语句")
    raise ValueError("故意制造的异常")







