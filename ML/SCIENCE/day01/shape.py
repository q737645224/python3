# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(1, 3)
print(a.shape, a, sep='\n')

b = [[1, 2, 3], [4, 5, 6]]
print('b')
print(b)
c = np.array(b)
print('c')
print(c)
print(c.shape)
d = np.array([
    [np.arange(1, 5), np.arange(5, 9), np.arange(9, 13)],
    [np.arange(13, 17), np.arange(17, 21), np.arange(21, 25)]])
print(d.shape, d, sep='\n')
