# 2. 模拟斗地主发牌,扑克牌共54张
#     黑桃('\u2660'), 梅花('\u2663'), 方块('\u2665'), 红桃('\u2666')
#     A2-10JQK
#     大王、小王
#   三个人玩，每人发17张牌，底牌留三张
#   输入回车, 打印出第1个人的17张牌
#   输入回车, 打印出第2个人的17张牌
#   输入回车, 打印出第3个人的17张牌
#   输入回车, 打印三张底牌

import random


kinds = ['\u2660', '\u2663', '\u2665', '\u2666']
numbers = ['A'] + [str(i) for i in range(2, 11)
                   ] + list("JQK")

pokes = ['大王', '小王']  # 用于存储扑克信息的列表
for k in kinds:
    for n in numbers:
        pokes.append(k + n)

# 洗牌:
random.shuffle(pokes)
# 发牌
input()
print("第1个人的17张牌是:", pokes[:17])
input()
print("第2个人的17张牌是:", pokes[17:34])
input()
print("第2个人的17张牌是:", pokes[34:51])
input()
print("底牌是:", pokes[51:])

