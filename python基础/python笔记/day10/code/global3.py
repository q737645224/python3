# global2.py


# 3. 不能先声明局部变量，再用global声明为全局变量，
# 此做法不附合规则
v = 100

def fn():
    v = 200  # 创建局部变量
    global v  # 此时至少是警告(不建议这样写)
    v = 300
    print(v)

fn()
print('v=', v)
