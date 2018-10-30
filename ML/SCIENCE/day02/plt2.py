# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-np.pi, np.pi, 200)

cos_y = np.cos(x) / 2
sin_y = np.sin(x)

mp.plot(x, cos_y, linestyle='--', linewidth=1,
        color='dodgerblue')
mp.plot(x, sin_y, linestyle=':', linewidth=1.5,
        color='orangered')

mp.show()
