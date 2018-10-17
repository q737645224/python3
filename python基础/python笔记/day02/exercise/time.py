# 3. 分三次输入当前的小时，分钟和秒数,在终端
# 打印时此距离凌晨0:0:0 秒过了多少秒

hour = input("请输入小时: ")
hour = int(hour)  # 转为整数

minute = int(input("请输入分钟:"))
second = int(input("请输入秒:"))

s = hour * 60 * 60 + minute * 60 + second
print('从凌晨到现在经历了', s, '秒')

