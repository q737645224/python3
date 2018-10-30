# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([
    [1 + 1j, 2 + 4j, 3 + 7j],
    [4 + 2j, 5 + 5j, 6 + 8j],
    [7 + 3j, 8 + 6j, 9 + 9j]
])
print('a.dtype')
print(a.dtype)

print('a.dtype.char')
print(a.dtype.char)  # complex128 的字符码是D

print('a.dtype.str')
print(a.dtype.str)

print('a.dtype.name')
print(a.dtype.name)

print('a.shape')
print(a.shape)

print('a.ndim')
print(a.ndim)

print('a.size')
print(a.size)

print('a.itemsize')
print(a.itemsize)

print('a.nbytes')
print(a.nbytes)  # 9*16=144

print('a.real')
print(a.real)

print('a.imag')
print(a.imag)

print('a.T')
print(a.T)

print('flat')
for elem in a.flat:  # 性能最优,迭代器
    print(elem)

print('ravel')
for elem in a.ravel():  # 性能居中
    print(elem)

print('flatten')
for elem in a.flatten():  # 性能最差,创建一个容器,里面既有元数据也有实际数据
    print(elem)

b = a.tolist()  # 数组->列表
print('b')
print(b)
c = np.array(b)
print('c')
print(c)


d = []
for i in range(10):
    d.append(i)
print('d')
print(d)

e = np.array([], dtype=int)
for i in range(10):
    e = np.append(e, i)
print('e')
print(e)
# 当需要频繁的追加时,可以先用列表来追加元素,最后再转成数组
