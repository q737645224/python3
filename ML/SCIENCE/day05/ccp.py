# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(1, 6)
print(a)
b = a.clip(min=2)
print(b)
c = a.clip(max=4)
print(c)
d = a.clip(2, 4)
print(d)
print('*******')

e = a.compress(2 <= a)
print(e)
f = a.compress(a <= 4)
print(f)

g = a.compress((2 <= a) & (a <= 4))
print(g)
print('*******')

h = a.prod()
print(h)
i = a.cumprod()
print(i)

j = 1
for k in range(2, 11):
    j *= k
print(j)


def jiecheng(n):
    if n == 1:
        return 1
    return n * jiecheng(n - 1)
print(jiecheng(10))

print((np.arange(1, 11)).prod())
# numpy的方法在C语言里完成阶乘,效率高,
# 但需要先给数组分配空间,所以是牺牲空间换取时间
