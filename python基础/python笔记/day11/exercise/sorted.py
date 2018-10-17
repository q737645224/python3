# 练习:
#   names = ['Tom', 'Jerry', 'Spike', 'Tyke']
#   排序的依据为字符串的反序:
#            'moT'   yrreJ    ekipS    ekyT
#   结果:
#     ['Spike', 'Tyke', 'Tom', 'Jerry']


names = ['Tom', 'Jerry', 'Spike', 'Tyke']


def k(s):
    print("k()传入:", s, "返回去的", s[::-1])
    return s[::-1]


L = sorted(names, key=k)
print(L)  # ['Spike', 'Tyke', 'Tom', 'Jerry']

