# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np


def add(a, b, c):
    return a + b + c

A = np.array([1, 2, 3, 4, 5])
B = np.array([10, 20, 30, 40, 50])
C = np.array([100, 200, 300, 400, 500])
D = np.apply_along_axis(add, 0, A, B, C)
print(D)
E = A + B + C
print(E)


def fun(a):
    return a[0] + a[-1]

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]])
b = np.apply_along_axis(fun, 0, a)
print('b')
print(b)
c = np.apply_along_axis(fun, 1, a)
print('c')
print(c)

d = fun(a)
print('d')
print(d)
