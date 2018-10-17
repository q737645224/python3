# iterator.py

L = [2, 3, 5, 7]
for x in L:
    print(x)
else:
    print('循环结束')

it = iter(L)  # 从L中获取一个迭代器
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("循环结束")
        break
