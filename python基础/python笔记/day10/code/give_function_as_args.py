# give_function_as_args.py


def f1():
    print("f1被调用")


def f2():
    print("f2被调用")


def fx(fn):
    print(fn)
    fn()  # 此时这是调用什么呢？


fx(f1)
fx(f2)


