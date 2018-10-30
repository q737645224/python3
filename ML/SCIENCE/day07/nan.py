# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([10, 20, np.nan, 30, 40])
print(np.max(a), np.min(a))
print(np.argmax(a), np.argmin(a))
print(np.nanmax(a), np.nanmin(a))
print(np.nanargmax(a), np.nanargmin(a))
