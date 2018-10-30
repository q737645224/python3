# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([5, 5, -5, -5])
b = np.array([2, -2, 2, -2])
print(a, b)
# 真除:
c = np.true_divide(a, b)
d = np.divide(a, b)
e = a / b
print('c,d,e')
print(c, d, e)

# 地板除
f = np.floor_divide(a, b)
g = a // b
print('f,g')
print(f, g)

# 对a/b做天花板取整,再变成整数类型,实现天花板除
h = np.ceil(a / b).astype(int)
print('h')
print(h)

# 对a/b做截断,再变成整数类型
i = np.trunc(a / b).astype(int)
print(i)

j = (a / b).astype(int)  # 默认就是截断取整
print(j)
