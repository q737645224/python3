# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.arange(1, 6)
print(a)
b = np.arange(6, 9)
print(b)
print(np.convolve(a, b, 'full'))
print(np.convolve(a, b, 'same'))
print(np.convolve(a, b, 'valid'))
