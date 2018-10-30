# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-10, 10, 1000)
y = x ** 2

mp.figure('Log', facecolor='lightgray')

mp.subplot(211)
mp.title('plot', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, y, c='orangered', label=r'$y=x^2$')
mp.legend()

mp.subplot(212)
mp.title('semilogy', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(x, y, c='dodgerblue', label=r'$y=x^2$')
mp.legend()
mp.tight_layout()
mp.show()
