# 1. 写程序计算  1 + 3 + 5 + 7 + ...+ 99的和
#   （要求用for语句和while语句两种方式实现)

s = 0
for x in range(1, 100, 2):
    s += x
print("1 + 3 + 5 + ....+ 99=", s)

print('----以下用while语句实现-----')
s = 0
i = 1
while i < 100:
    x = i
    s += x
    i += 2
print("1 + 3 + 5 + ....+ 99=", s)
