# 有一个集合:
#   s = {'唐僧', '悟空', '八戒', '沙僧'}
#   用 for语句来遍历所有元素如下:
#     for x in s:
#         print(x)
#     else:
#         print('遍历结束')
#   请将上面的for语句改写为 用while语句和迭代器实现


s = {'唐僧', '悟空', '八戒', '沙僧'}
# for x in s:
#     print(x)
# else:
#     print('遍历结束')

it = iter(s)  # 拿到迭代器
try:
    while True:
        x = next(it)
        print(x)
except StopIteration:
    print('遍历结束')

