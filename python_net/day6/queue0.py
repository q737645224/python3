from multiprocessing import Queue 
from time import sleep 

#创建队列
q = Queue(3)

q.put(1)
sleep(0.1)
print(q.empty())
q.put("Process Queue")
q.put([1,2,3])
print(q.full())  
#如设置为非阻塞则产生Full异常
# q.put(666,False) #非阻塞
# q.put(666,True,3)  #超时
print(q.get())
print(q.qsize()) #查看消息数量
q.close()