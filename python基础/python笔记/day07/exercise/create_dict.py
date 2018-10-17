# 练习:
#   有字符串的列表如下:
#     L = ['tarena', 'xiaozhang', 'tyke']
#     用上述列表生成如下字典:
#       d = {'tarena': 6, 'xiaozhang': 9, 'tyke':4}
#     注:
#       字典的值为键的长度


L = ['tarena', 'xiaozhang', 'tyke']
# d = {}
# for s in L:
#     d[s] = len(s)

d = {s: len(s) for s in L}

print(d)

# d = {'tarena': 6, 'xiaozhang': 9, 'tyke':4}
