# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def fun(a, b, c):
    d = a + b + c
    e = a * b * c
    return d, e


def fun2(a, b):
    return a + b, a - b, a * b

A = np.array([1, 3, 5, 7])
B = np.array([2, 4, 6, 8])
C = np.array([0, 1, 2, 3])
vfun = np.vectorize(fun)
D, E = vfun(A, B, C)  # 接收了两个数组
print(D, E)

F = np.vectorize(fun2)(A, B)
print(F)
