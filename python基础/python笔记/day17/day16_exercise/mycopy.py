# 练习:
#   1. 写程序实现复制文件的功能
#     要求:
#        1. 要考虑特大文件问题
#        2. 要关闭文件
#        3. 要能复制二进制文件
#     如:
#       请输入源文件路径名:  /home/tarena/xxx.tar.gz
#       请输入目标文件路径名: ./a.tar.gz
#     显示:
#       文件已成功复制

src_filename = input("请输入源文件路径名: ")
dst_filename = input('请输入目标文件路径名: ')
try:
    src = open(src_filename, 'rb')  # 打开源文件用来读数据
    try:
        try:
            dst = open(dst_filename, 'wb')  # 打开目标文件用来写
            try:
                while True:
                    b = src.read(4096)
                    if not b:  # 已经再也读不到数据了
                        break
                    dst.write(b)
                print("复制成功")
            finally:
                dst.close()
        except OSError:
            print("打开写文件失败")
    finally:
        src.close()
except OSError:
    print("复制失败")