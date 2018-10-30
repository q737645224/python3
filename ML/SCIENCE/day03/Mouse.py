# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

poison_bottle = random.randint(1, 1000)

find_bottle = 0
dead_mouse = []
p_b = poison_bottle

M = {x: [] for x in range(1, 11)}
# print(M)

for i in range(1, 1001):
    i2 = i
    for j in range(1, 11):
        dp = i % 2
        if dp == 1:
            M[j].append(i2)
        i -= dp
        i /= 2


for i in range(1, 11):
    dp = p_b % 2
    if dp == 1:
        dead_mouse.insert(0, i)
    p_b -= dp
    p_b /= 2

for n in dead_mouse:
    find_bottle += 2 ** (n - 1)

print(dead_mouse)
print(find_bottle)
print(poison_bottle)

# for i in range(1, 11):
#     if find_bottle in M[i]:
#         print('%d号喝了它' % i)
