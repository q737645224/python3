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

# 设置坐标轴刻度标签
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2,
           np.pi * 3 / 4, np.pi],
          [r'$-\pi$', r'$-\frac{\pi}{2}$', r'$0$',
           r'$\frac{\pi}{2}$', r'$\frac{3\pi}{4}$',
           r'$\pi$'])
# frac表示分数,第一个{}是分子,第二个{}是分母

mp.yticks([-1, -0.5, 0.5, 1])

# 将矩形坐标轴改成十字坐标轴:
# 获取当前坐标轴对象
ax = mp.gca()

# 将垂直坐标刻度置于左边框
ax.yaxis.set_ticks_position('left')

# 将左边框置于数据坐标原点
ax.spines['left'].set_position(('data', 0))

# 将水平坐标刻度x轴置于底边框
ax.xaxis.set_ticks_position('bottom')

# 将底边框置于数据坐标原点
ax.spines['bottom'].set_position(('data', 0))

# 将右边框和顶边框设置成无色
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

mp.plot(x, cos_y, linestyle='-', linewidth=1,
        color='dodgerblue')

mp.plot(x, sin_y, linestyle='-', linewidth=1,
        color='orangered')

mp.show()
