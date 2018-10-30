# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

closing_prices, volumes = np.loadtxt(
    '../data/aapl.csv',
    delimiter=',',
    usecols=(6, 7),
    unpack=True
)

vwap, sw = 0, 0
for closing_price, volume in zip(closing_prices,
                                 volumes):
    vwap += closing_price * volume
    sw += volume  # 权重之和
vwap /= sw
print(vwap)

vwap = closing_prices.dot(volumes) / volumes.sum()
print(vwap)  # 点乘:两个向量对应元素相乘再相加

# 直接用numpy里加权平均函数:
vwap = np.average(closing_prices, weights=volumes)
print(vwap)
