# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(1, 7)
print(a)
b = np.add.reduce(a)
print('b')
print(b)
c = np.add.accumulate(a)
print('c')
print(c)

d = np.add.reduceat(a, [0, 2, 4])
#   3   7   11
# 1 2 3 4 5 6
# 0   2   4
print(d)

e = np.add.outer([10, 20, 30], a)
#  + 1  2  3  4  5  6
# 10 11 12 13 14 15 16
# 20 21 22
# 30 31 32
print('e')
print(e)

f = np.outer([10, 20, 30], a)
#  x  1  2  3  4  5  6
# 10 10 20
# 20 20
# 30 30 60           180
print(f)
