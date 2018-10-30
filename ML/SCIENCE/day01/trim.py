# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 练习:实现一个函数,去除字符串首尾空格,注意不要使用strip()


def tri(s):
    for i in s[:]:
        if i == ' ':
            s = s[1:]
        else:
            break
    for i in s[::-1]:
        if i == ' ':
            s = s[:-1]
        else:
            break
    return s
print(tri('  hello  world   '))
print(len(tri('  hello  world   ')))
