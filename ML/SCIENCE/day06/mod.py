# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print(a, b)

# 地板除余数
c = np.remainder(a, b)
d = np.mod(a, b)
e = a % b
print('c,d,e')
print(c, d, e)

# 截断除余数
f = np.fmod(a, b)
print(f)
