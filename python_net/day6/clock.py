from multiprocessing import Process 
import time 

class ClockProcess(Process):
    def __init__(self,value):
        #调用父类init
        super().__init__()
        self.value = value 
    #重写run方法
    def run(self):
        for i in range(5):
            time.sleep(self.value)
            print("The time is {}".format(time.ctime()))

p = ClockProcess(2)
#自动执行run
p.start()

p.join()

