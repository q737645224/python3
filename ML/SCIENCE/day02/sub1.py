# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import matplotlib.pyplot as mp


mp.figure('Subplot', facecolor='lightgray')

mp.subplot(2, 3, 1)
mp.xticks(())  # 不显示标签
mp.yticks(())
mp.text(0.5, 0.5, '1', ha='center', va='center',
        size=36, alpha=0.5)

mp.subplot(232)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '2', ha='center', va='center',
        size=36, alpha=0.5)

mp.subplot(233)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '3', ha='center', va='center',
        size=36, alpha=0.5)

mp.subplot(234)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '4', ha='center', va='center',
        size=36, alpha=0.5)

mp.subplot(235)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '5', ha='center', va='center',
        size=36, alpha=0.5)

mp.subplot(236)
mp.xticks(())
mp.yticks(())
mp.text(0.5, 0.5, '6', ha='center', va='center',
        size=36, alpha=0.5)

mp.tight_layout()  # 紧凑布局
mp.show()
