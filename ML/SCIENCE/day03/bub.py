# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

n_samples = 100

# 生成100个气泡的描述数据:
data = np.zeros(n_samples, dtype=[
    ('position', float, 2),  # 位置,x和y两个维度
    ('size', float, 1),
    ('growth', float, 1),
    ('color', float, 4)  # 颜色,R,G,B,A四个维度
])
# dtype=[(字段名称,字段类型,字段维度),...]
# np.zeros()返回一个给定形状和类型的用0填充的数组

data['position'] = np.random.uniform(0, 1,
                                     (n_samples, 2))
data['size'] = np.random.uniform(50, 750, n_samples)
data['growth'] = np.random.uniform(30, 150, n_samples)
data['color'] = np.random.uniform(0, 1, (n_samples, 4))

mp.figure('Bubble', facecolor='lightgray')
mp.title('Bubble', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')

plot = mp.scatter(data['position'][:, 0],  # 所有元素的x值
                  data['position'][:, 1],  # 所有元素的y值
                  s=data['size'],
                  c=data['color'])


def update(number):
    data['size'] += data['growth']
    index = number % n_samples
    data['position'][index] = np.random.uniform(
        0, 1, 2)
    data['size'][index] = 0
    data['growth'][index] = np.random.uniform(30, 150)
    data['color'][index] = np.random.uniform(0, 1, 4)
    plot.set_offsets(data['position'])
    plot.set_sizes(data['size'])
    plot.set_facecolors(data['color'])

anim = ma.FuncAnimation(mp.gcf(), update, interval=10)

mp.show()
