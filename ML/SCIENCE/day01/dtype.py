# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np

a = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print('a.dtype:', a.dtype)
b = a.astype(float)
print('b.dtype:', b.dtype)
c = a.astype(np.float32)
print('c.dtype:', c.dtype)
d = c.astype(np.str_)
print('d.dtype:', d.dtype, d)

# 以下三种写法都对:
#e = np.array([1234], dtype=np.int32)
#e = np.array([1234], dtype='int32')
e = np.array([1234], dtype='i4')
print('e', e.dtype, e.shape)

# dtype=(变长类型, 长度)
f = np.array(['1234'], dtype=(np.str_, 2))  # dtype='U2'
print('f', f.dtype, f[0])  # <U2 12

# dtype=(定长类型, (维度))
g = np.array([(1, 2, 3, 4)], dtype=(np.int32, 4))
# 每个元素的类型是4个int32
g = np.array([((1, 2), (3, 4))], dtype=(np.int32, (2, 2)))
print('g', g.dtype, g.shape)

# dtype='类型字符串1, 类型字符串2, ...'
h = np.array([('1234', (1, 2, 3, 4))], dtype='U4, 4i4')
print('h', h.dtype, h[0]['f0'], h[0]['f1'])

# dtype={'names':[字段名称表],'formats':[字段类型表]}
# 不用默认的f0,f1做字段名称
i = np.array([('1234', (1, 2, 3, 4)), ('5678', (5, 6, 7, 8))],
             dtype={'names': ['fa', 'fb'],
                    'formats': ['U4', '4i4']})
print('i:', i, i.shape, i.dtype, i[0]['fa'], i[0]['fb'])

# dtype=[(字段名称, 字段类型, 字段维度), ...]
j = np.array([('1234', (1, 2, 3, 4))], dtype=[
    ('fa', np.str_, 4), ('fb', np.int32, 4)])
print('j:', j.dtype, j[0]['fa'], j[0]['fb'])
k = np.array([('1234', (1, 2, 3, 4))], dtype=[
    ('fa', 'U4'), ('fb', '4i4')])
print('k:', k.dtype, k[0]['fa'], k[0]['fb'])

# (基本类型, 解释类型)
l = np.array([0x1234], dtype=('>u2', {'names': ['lo', 'hi'],
                                      'formats': ['u1', 'u1']}))
# 0x表示十六进制,'u1'整型1个字节
# 16进制数的一个位相当于二进制的4位,所以4位16进制是2个字节
# 低地址里拿到的是高数位的12,高地址拿到的是低数位34
print('{:x} {:x} {:x}'.format(l[0], l['lo'][0], l['hi'][0]))

l = np.array([0x1234], dtype=('<u2', {'names': ['lo', 'hi'],
                                      'formats': ['u1', 'u1']}))
print('{:x} {:x} {:x}'.format(l[0], l['lo'][0], l['hi'][0]))

m = np.array(['python'], dtype=('U6', {'names': ['codes'],
                                       'formats': ['6u4']}))
print(m[0], m['codes'][0])
