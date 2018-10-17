# break_while_embed.py

# 打印1 2 3 4 5 ... 20 打印10行

i = 1
while i <= 10:
    # 打印一行
    j = 1
    while j <= 20:
        print(j, end=' ')
        if j == 10:
            break
        j += 1
    print()

    i += 1