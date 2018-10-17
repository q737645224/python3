#hday12.py
# 
import time
time.gmtime()

# 1.写一个程序，以电子时钟格式:
#    HH:MM:SS格式显示时间
#    要求每过一秒刷新一次
# def my_clo():
#     while True: 
#         l = time.localtime()
#         t = []
#         t.append(l[3])
#         t.append(l[4])
#         t.append(l[5])
#         # t += str(l[3]) + str(l[4])+str(l[5]) 
#         # t = time.asctime()
#         time.sleep(0.5)
#         print(t)
#         print(t[0], t[1], t[2], sep=":")

# def time():
# while True:
#     t = time.localtime()
#     # print("%02d:%02d:%02d" %(t[3], t[4], t[5]))
#     print("%02d:%02d:%02d" %(t[3:6]) ,end="\r")
#     time.sleep(1)

  # 2.编写一个闹钟程序，启动时设置定时间，到时间后打印一句：
  # “时间到了”，然后程序退出
def alarm(h, m):
    while True:
        t =time.localtime()
        print("%02d:%02d:%02d" %(t[3:6]), end="\r")
        time.sleep(1)
        # if h == t[3] and m ==t[4]:
        if (h, m) == t[3:5]: #切片切出元组
            print("\n时间到了")
            break
        time.sleep(2)
hour = int(input("请输入定时小时："))
minute = int(input("请输入定时分钟："))
alarm(hour, minute)




# def laozhong():
#     t = time.localtime
#     print("请输入想要提示的时间！")
#     h =int(input("小时"))
#     m = int(input("分钟"))
#     s = int(input("秒"))
#     L = (t[0], t[1], t[2] ,h , m, s,t[6], t[7],t[8])
#     while True: 
#         miao = time.time
#         if time.mktime(l) == miao:
#             print("时间到了")
#             break
# laozhong()