# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

n = 10000

# 产生均值为0标准差为1的n个服从正态分布的随机数
x = np.random.normal(0, 1, n)  # 正态分布随机数生成函数
y = np.random.normal(0, 1, n)

d = np.sqrt(x ** 2 + y ** 2)  # 每个点到原点的距离
mp.figure('Scatter', facecolor='lightgray')
mp.title('Scatter', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, s=60, c=d, cmap='jet_r', alpha=0.5)
# 颜色映射表cmap='jet_r'

mp.show()
