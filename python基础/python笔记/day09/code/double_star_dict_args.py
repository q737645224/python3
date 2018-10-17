# double_star_dict_args.py


# 此示例示意用双星号字典形参来收集多余的关键字传参

def fa(**kwargs):
    print("关键字传参的个数是:", len(kwargs))
    print('kwargs=', kwargs)


fa(name='tarena', age=15)
fa(a=1, b='BBB', c=[2,3,4], d=True)

   
