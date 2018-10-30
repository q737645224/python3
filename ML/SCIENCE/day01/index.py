# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([[[1, 2],
               [3, 4]],
              [[5, 6],
               [7, 8]]])
print(a)
print('a[0]')
print(a[0])
# [[1 2]
#  [3 4]]
print('a[0][0]')
print(a[0][0])
# [1 2]
print(a[0][0][0])
print(a.shape)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i][j][k], a[i, j, k])  # 两种下标写法等价
print(a.size)
print(len(a))
