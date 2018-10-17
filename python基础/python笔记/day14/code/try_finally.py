# try_finally.py


# 以下以 煎蛋为例示意 try-finally语句的用法
# 必须要做的事情是,关闭天燃气

def fry_egg():
    print("打开天燃气点燃...")
    try:
        count = int(input("请输入鸡蛋个数: "))
        print("完成煎鸡蛋,共煎了%d个鸡蛋" % count)
    finally:
        print("关闭天燃气")


fry_egg()


