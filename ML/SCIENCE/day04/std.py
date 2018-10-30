# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

closing_prices = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',',
    usecols=(6),
    unpack=True
)

# 算数平均值
mean = closing_prices.mean()
# 离差	(矢量运算)
devs = closing_prices - mean
# 离差方
sqrs = devs ** 2
# 方差
svar = sqrs.mean()  # 总体方差
pvar = sqrs.sum() / (sqrs.size - 1)  # 样本方差
# 标准差
sstd = np.sqrt(svar)  # 总体标准差
print(sstd)
pstd = np.sqrt(pvar)  # 样本标准差
print(pstd)

# 用内置函数计算标准差
sstd = np.std(closing_prices)
print(sstd)
pstd = np.std(closing_prices, ddof=1)
# 样本标准差,ddof=1非自由度为1,相当于(n-1)
print(pstd)
