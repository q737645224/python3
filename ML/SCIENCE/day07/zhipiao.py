# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

times = 50000  # int(input('please input testing times:'))
L = [0, 1, 2, 3]


def guess_ch():
    real = random.randint(0, 3)
    L2 = L[:]
    choice_1 = random.randint(0, 3)
    while True:
        i = random.randint(0, 3)
        if i != real and i != choice_1:
            L2.pop(L2.index(i))
            break
    L2.pop(L2.index(choice_1))
    i = L2[random.randint(0, 1)]
    if i == real:
        return True
    else:
        return False

right_1 = 0
wrong_1 = 0
for i in range(times):
    if guess_ch():
        right_1 += 1
    else:
        wrong_1 += 1

print('Right_count%d' % right_1)
print('Right_rate:', right_1 / times)
