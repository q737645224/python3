# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

t = np.linspace(0, 2 * np.pi, 201)
A, a, B, b = 10, 9, 5, 8
x = A * np.sin(a * t + np.pi / 2)  # np.sin()才能处理数组
y = B * np.sin(b * t)

mp.figure('Lissajous', facecolor='lightgray')
mp.title('Lissajous', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, c='orangered', label='Lissajous')
# x与y都分别与时间t形成正弦函数,
# x和y分别是这两个正弦函数的(y轴)值

mp.legend()
mp.show()
