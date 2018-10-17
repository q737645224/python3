

# 将之前的练习mycopy复制文件由try-finally 改为
# with语句来实现

src_filename = input("请输入源文件路径名: ")
dst_filename = input('请输入目标文件路径名: ')
try:
    with open(src_filename, 'rb') as src, \
            open(dst_filename, 'wb') as dst:
        while True:
            b = src.read(4096)
            if not b:  # 已经再也读不到数据了
                break
            dst.write(b)
        print("复制成功")
except OSError:
    print("复制失败")