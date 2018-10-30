# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

poison_bottle = random.randint(1, 1000)

P = bin(poison_bottle)
dead_mouse = []

for i in P[2:]:  # 0b
    if i == '1':
        dead_mouse.append(1)
    else:
        dead_mouse.append(0)

find_bottle = 0
n = len(dead_mouse) - 1
for i in dead_mouse:
    if i == 1:
        find_bottle += 2**n
    n -= 1

print(poison_bottle)
print(find_bottle)
print(dead_mouse)
