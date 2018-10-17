# 1. 写一个闹钟程序，启动时设置定时时间,
#   到时间后打印一句"时间到...." 然后退出程序

import time


def alarm(h, m):
    while True:
        cur_time = time.localtime()  # 得到本地时间
        print("%02d:%02d:%02d" % cur_time[3:6],
              end='\r')
        time.sleep(1)
        # if h == cur_time[3] and m == cur_time[4]:
        if (h, m) == cur_time[3:5]:
            print("\n时间到....")
            return


if __name__ == '__main__':
    hour = int(input("请输入定时的小时: "))
    minute = int(input("请输入定时的分钟: "))
    alarm(hour, minute)

