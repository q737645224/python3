# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

closing_prices = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',',
    usecols=(6),
    unpack=True
)

# 应用numpy的快速排序算法对给定数组中的
# 元素做升序排序O(nlogn)
sorted_prices = np.msort(closing_prices)
print(sorted_prices)
#test = sorted_prices[::-1]
# print(test)

L = sorted_prices.size   # 长度
median = (sorted_prices[int((L - 1) / 2)] +
          sorted_prices[int(L / 2)]) / 2
print(median)

median = np.median(closing_prices)
print(median)
