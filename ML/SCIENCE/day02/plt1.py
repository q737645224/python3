# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

# 生成曲线上各点的x,y坐标,然后用直线连接起来
x = np.linspace(-np.pi, np.pi, 200)  # 产生一个等差数列

# 根据曲线函数计算各点的y坐标
cos_y = np.cos(x) / 2
sin_y = np.sin(x)

# 用直线连接曲线上各点
mp.plot(x, cos_y)  # 绘制曲线的函数
mp.plot(x, sin_y)

# 显示图形
mp.show()
