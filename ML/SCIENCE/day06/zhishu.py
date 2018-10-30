# -*- coding: utf-8 -*-
from __future__ import unicode_literals

end = 100
zhishu = []

for n in range(2, end + 1):
    for m in zhishu[:]:
        if m ** 2 > n:
            zhishu.append(n)
            break
        if n % m == 0:
            break
    else:
        zhishu.append(n)
print(zhishu)
