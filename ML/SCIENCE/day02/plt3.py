# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

# 生成曲线上各点的x,y坐标,然后用直线连接起来
x = np.linspace(-np.pi, np.pi, 200)  # 产生一个等差数列

# 根据曲线函数计算各点的y坐标
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

# 设置坐标范围
mp.xlim(x.min() * 1.1, x.max() * 1.1)
mp.ylim(min(cos_y.min(), sin_y.min()) * 1.1,
        max(cos_y.max(), sin_y.max()) * 1.1)

# 用直线连接曲线各点
mp.plot(x, cos_y, linestyle='-', linewidth=1,
        color='dodgerblue')
mp.plot(x, sin_y, linestyle='-', linewidth=1,
        color='orangered')

mp.show()
