import traceback 

a = 10 

try:
    b = a / 0
except Exception as e:
    # print(e)
    traceback.print_exc()

print("程序执行完毕")