# 1. 已知有两个等长的列表 list1  和 list2
# 以list1中的元素为键，以list2中的元素为值，生成相应的字典
# list1 = [1001, 1002, 1003, 1004]
# list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']
# 生成的字典为：
#   {1001: 'Tom', 1002:'Jerry', .....}


list1 = [1001, 1002, 1003, 1004]
list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']

# 方法1
# d = {}
# for i in range(len(list1)):  # i代表索引
#     k = list1[i]
#     d[k] = list2[i]

# 方法2
d = {list1[i]: list2[i] for i in range(len(list1))}

print(d)
