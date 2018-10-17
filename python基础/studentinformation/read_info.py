#read_info.py
# def read_info_txt():
#     rl = []
#     try:
#         f = open("info.txt")
#         L = f.readlines()
#         for line in L:
#             s = line.strip()
#             name, age, score = s.split()
#             age = int(age) #转为整数
#             score = int(score)
#             rl.append({'name':name,
#                         'age':age,
#                         'score': score})
#         return rl  #返回列表
#     except OSError:
#         print('读取文件失败！')
        
# L = read_info_txt()
# print(L)

f = open("info.txt", 'rt')
# f.write("hello")
# f.writelines(['\n112', 'afd', 'fd\n'])
# f.close

for line in f:
    print(line)
f.close()
