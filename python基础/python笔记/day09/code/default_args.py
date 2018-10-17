# default_args.py


def info(name, age=1, address='未填定'):
    print('我叫', name, '我今年', age,
          '岁， 我家住址:', address)


info("魏明择", 35, "北京市朝阳区")
info("Tarena", 15)
info('张飞')
# info()  # 出错
info('小张', age=20)



