# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

M = np.mat('4 11 14; 8 7 -2')
print(M)
U, s, V = np.linalg.svd(M, full_matrices=False)
print(s)

# 以参数的元素为主对角线,其它元素全填0,返回一个矩阵:
S = np.diag(s)
print('**************')

print(U, S, V, sep='\n')
print('**************')

print(U * U.T, V * V.T, sep='\n')
print(U * S * V)
