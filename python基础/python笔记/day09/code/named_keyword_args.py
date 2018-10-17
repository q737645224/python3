# named_keyword_args.py


# 此示例示意函数的形参为命名关键字形参
def fa(*, a, b):
    print('a=', a)
    print('b=', b)

def fb(*args, a, b):
    print("args=", args)
    print('a=', a)
    print('b=', b)

# fa(b=1, a=2)
# fa(**{'b': 200, 'a': 100})

fb(1, 2, 3, 4, b=200, a=100)