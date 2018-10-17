  # hday16.py
# try:
#     f = open("mynote.txt")
#     print('此文件打开成功')
#     s = f.read(line)

 # 1.写程序，读入任意行文字，当输入空时结束输入先将这些读入的文字存入列表中，然后再次列表里的内容存入到’input.txt'文件中

#  def input_to_list():
#     L = []
#     while True:
#         s = input("请输入：")
#         if s < 0: 
#             break
#         L.append(s)
#     return L
# def list_to_file(lst, filename='input.txt'):
#     fw =open(filename, 'w')
#     for s in lst:
#         #把s绑定的字符写入到input.txt文件中
#         fw.write(s)
#         fw.write('\n')   #写入换行符，用来区分行
#         fw.close()
#     except OSError:
#         print("写入文档失败")

# # 2.写程序，从上的input.txt中读取之前输入的数据，读取到列表中，在加上行号进行输出

# def read_from_file(filename='input.txt'):
#     L = []
#     try:
#         fr = open(filename, 'rt')
#         for line in fr:
#             s = line.rstrip()
#             L.append(s)
#         fr.close()
#         print('读取文件成功')
#     except OSError:
#         print('打开文件失败')
#     return L

# def print_text(lst):
#     for line_number, s in enumerate(lst, 1):
#         print(line_number, ':', s)

# if __name__ == '__main__':
#     print


# import sys
# sys.stdout.write("标准输出\n")

# sys.stderr.write("我的出现是个错误！！！\n")
# print("hello",'world', file=sys.stdout)

# f = open("myfile.txt", "w")
# print('你好', file=myfile.txt)


# try:
#     fr = open('mynote.txt', 'rb')
#     b = fr.read()   # b= b''   字节串
#     print(b)
#     fr.close()
# try:
# except OSError:
#     print("打开二进制失败")

# try:
#     fbw = open('mybinary.bin', 'wb')
#     s = '你好'
#     b = s.encode()
#     print(b)
#     # c = s.encode('ASCII')
#     fbw.write(b)
#     fbw.write(b'76')
#     ba = bytearray(range(256))
#     fbw.write(ba)
#     fbw.close()
#     print('文件写入成功')
# except OSError:
#     print("打开写文件失败")
# 

# 1.当是用户输入一系列整数，当输小于零的整数的时候，结束
# 1）将这些数字存于列表里
# 2）将列表中的数字写入到文件numbers.txt中
# l = []
# while True:
#     a = int(input("输入整数"))
#     if a < 0:
#         break
#     l.append(a)
# print(l)
# f = open('numbers.txt', "wt")
# str_ = ""
# for i in l:
#     str_ += str(i) + ' '
# print(str_)
# f.write(str_)

# # 2.写程序，将上题的numbers.txt中的整数读入到内存中形成列表计算这写数中的最大值，最小值和它们的和
# f = open('numbers.txt', 'rt')
# str_ = f.read()
# l = str_.split()
# print(l)
# l = [int(x) for x in l]
# print(max(l), min(l),sum(l))
   


# 3.写程序，实现复制文件功能
#  要求：
#   1）要考虑关闭文件问题
#   2）要考虑超大文复制问题
#   3）要能复制二进制文件（如：/usr/bin/python3等)
# try:
#     doc = input("请输入想要复制的文件名")
#     f = open(doc ,"r")
#     g = open("numbers2.txt", "w")
#     while True:
#         l = f.read(100)
#         f.flush()
#         if not l:
#             break    
#         g.write(l)
# except:
#     f = open(doc ,"rb")
#     g = open("numbers2.txt", "wb")
#     while True:
#         l = f.read(100)
#         f.flush()
#         if not l:
#             break    
#         g.write(l)
# finally:
#     f.close()
#     g.close()

def mycopy(src_filename,dst_filename):  #源文件名和目录文件名
    try:   
        fr = open(src_filename, 'rb')
        try:
            try:
                fw = open(dst_filename, 'wb')
                try:
                    while True:
                        b = fr.read(4096)
                        if not b:
                            break
                        fw.write(b)
                finally:
                    fw.close()
            except OSError:
                print("打开目录文件失败")
        finally:
            fr.close
    except OSError:
        print("打开源文件失败")

src = input("请输入源文件名：")
dst = input("请输入目标文件名：")
mycopy(src, dst)