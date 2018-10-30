# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

n = 35
# 递归求斐波那契


def fibo(n):
    return 1 if n < 3 else fibo(n - 1) + fibo(n - 2)
print(fibo(n))

# 循环求斐波那契
f1, f2 = 0, 1
for i in range(n - 1):
    fn = f1 + f2
    f2, f1 = fn, f2
print(fn)

# 矩阵方法求斐波那契
print(int((np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]))

# 第四种方法就是直接代入通项公式
r = np.sqrt(5)
print(int((((1 + r) / 2) ** n - ((1 - r) / 2)**n) / r))
