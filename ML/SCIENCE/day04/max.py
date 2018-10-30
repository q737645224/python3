# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.random.randint(10, 100, 27).reshape(3, 3, 3)
print(a)

b = a.max()
print('b')
print(b)
c = np.max(a)
print('c')
print(c)
d = a.min()
print('d')
print(d)
e = np.min(a)
print('e')
print(e)

f = a.ptp()
print('f')
print(f)
g = np.ptp(a)
print('g')
print(g)

# 3个页面找对应位置的最大值,注意只能有两个参数
h = np.maximum(np.maximum(a[0], a[1]), a[2])
print('h')
print(h)

i = np.minimum(np.minimum(a[0], a[1]), a[2])
print('i')
print(i)
