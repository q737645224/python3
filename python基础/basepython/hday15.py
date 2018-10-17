#hday15.py
# 有一个集合:
#     s = {'唐僧', '悟空', '八戒', '沙僧'}
#     用 for语句来遍历所有元素如下:
#       for x in s:
#           print(x)
#       else:
#           print('遍历结束')
#     请将上面的for语句改写为 用while语句和迭代器实现
# import time
# s = {'唐僧', '悟空', '八戒', '沙僧'}
# it = iter(s)
# try:
#     while True:
#         s = next(it)
#         print(s)
# except StopIteration:
#     print("遍历结束")

# while True:
#     try:
#         s = next(it)
#         print(s)
#     except StopIteration:
#         print("遍历结束")
#         break

# 写一个生成器函数 myeven(start, stop)
#   此函数用来生成从 start开始到stop结束(不包含)区间内的一系列偶数
#   def myeven(start, stop):
#       ....

#   evens = list(myeven(10, 20))
#   print(evens)  # [10, 12, 14, 16, 18]
#   for x in myeven(21, 30):
#       print(x)  # 22, 24, 26, 28

#   L = [x**2 for x in myeven(3, 10)]
#   print(L)  # 16 36 64

# def myeven(start, stop):
#     # L = [x for x in range(start, stop) if x % 2 == 0]
#     # return L
#     x = start
#     while x < stop:
#         if x % 2 == 0:
#             yield x
#         x += 1
# evens = list(myeven(10, 20))
# print(evens)  # [10, 12, 14, 16, 18]
# for x in myeven(21, 30):
#     print(x)  # 22, 24, 26, 28

# L = [x**2 for x in myeven(3, 10)]
# print(L)  # 16 36 64

# def myfactorial(n):
#     i = 1
#     while i <= n:
#         sums = 1
#         for j in range(1,i + 1):
#             sums *= j
#         yield sums
#         i += 1 
# it =myfactorial(5)
# for _ in range(5):
#     print(next(it))


# L = [2, 3, 5, 7]
# def mypow():
#     for i in L:
#         yield i**2 + 1
# it = mypow()
# for _ in range(2):
#     print(next(it))
# print("+++++++++")
# for _ in range(2):
#     print(next(it))
# print("+++++++++")



# def mypow():
#     for i in L:
#         yield i**2 + 1
# it = mypow()
# for i in mypow():
#     print(i)
# print("+++++++++")
# for i in mypow():
#     print(i)
    



# g = (i**2 + 1 for i in L)
# for _ in range(4):
#     print(next(g))

# 写一个程序,读入任意行的文字,当输入空行时结束输入
#   打印带有行号的输入结果:
#     如:
#       请输入: hello<回车>
#       请输入: world<回车>
#       请输入: tarena<回车>
#       请输入: <回车> # 直接回车结束输入
#     输出如下:
#       第1行: hello
#       第2行: world
#       第3行: tarena

# def main():
#     l = []
#     while True:
#         s = input("请输入")
#         if s == "":
#             break
#         l.append(s)
#     for i in enumerate(l):
#         print("第%d行：" %i[0],i[1])

# main()







def prime(start, stop):
    i = start
    l = []
    while i <= stop:
        if i <= 1:
            i += 1
            continue
        j = 2
        while j ** 2 <=i:
            if i % j == 0:
                break
            j += 1
        if j ** 2 > i:
            l.append(i)
        i += 1    
    return l   #[11, 13, 17, 19, 23, 25, 29, 31, 37, 41, 43, 47, 49]
z = prime(10, 50)
print(z)


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
def prime(begin, end):
    for i in range(begin , end):
        #如果i是素数
        if is_prime(i):
            yield i





# 写一个生成器函数myxrange([start,], stop[, step])
#   来生成一系列整数
#   要求：
#     myxrange功能与range功能相同(不允许调用range函数)
#     用自己写的myxrange函数结合生成器表达式求1~10内奇数的平方和

# def myxrange(start , stop = 0,step = 1 ):
#     if stop == 0:
#         start , stop = stop , start
#     l = []
#     i = start
#     if step > 0:
#         while i < stop:
#             l.append(i)
#             i += step
#         return l
#     else:
#         while i > stop:
#             l.append(i)
#             i += (step)
#         return l

# z = myxrange(10,1,-2)
# print(z)

# sums = 0
# for i in it:
#     sums += i
# print(sums)



def myxrange(start , stop = 0,step = 1 ):
    if stop == 0:
        start , stop = stop , start
    l = []
    if step > 0:
        while start < stop:
            yield start
            start += step
        return l
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise ValueError
it = (x **2 for x in myxrange(10,1,-2))
sums = 0
for i in it:
    sums += i
print(sums) 