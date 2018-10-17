# star_tuple_args.py


# 此示例示意星号元组形参的用法
def func(*args):
    print("参数个数是:", len(args))
    print('args:', args)

func()  # 无参
func(1, 2, 3, 4)
func(*"ABC", 1, 2, 3, None, False)
