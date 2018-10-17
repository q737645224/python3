# 练习:
#   任意输入一些数字，存于列表L中。当输入负数时结束输入
#   1) 打印这些数的和 
#   2) 打印这些数有多少种(去重)
#   3) 除重复的数字后，打印这些剩余数字的和

#   提示,可以用集合去重

L = []
while True:
    n = int(input("请输入:"))
    if n < 0:
        break
    L.append(n)

print(L)
print("您刚才输入的这些数的和是:", sum(L))

s = set(L)  # 生成集合，直接去重
print("数字的种类有%d种" % len(s))
print("去重后的和是:", sum(s))



