# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(1, 9).reshape(2, 4)
print('a', a)
b = a.transpose()
print('b', b)
c = a.reshape(4, 2)
print('c', c)
d = a.T
print('d', d)
a *= 10
print(a, b, c, d, sep='\n')
print('###############')

arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print('*****')
arrt = arr.transpose((2, 1, 0))  # 调换几个轴
print(arrt)
print('*****')
arrtt = arr.transpose((2, 0, 1))
print(arrtt)
