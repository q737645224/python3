# 2. 写一个程序，以电子时钟格式:
#   HH:MM:SS格式显示时间
#   要求每隔一秒变化一次

import time


def run():
    while True:
        t = time.localtime()
        # print("%02d:%02d:%02d" % (t[3], t[4], t[5]), end='\r')
        print("%02d:%02d:%02d" % t[3:6], end='\r')
        time.sleep(1)


run()
