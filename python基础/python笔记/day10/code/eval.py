# eval.py

x = 100
y = 200

a = eval('x + y')
print(a)  # 300

a = eval('x + y', {'x': 1, 'y': 2})
print(a)  # 3

a = eval('x + y',
         {'x': 1, 'y': 2},
         {'x': 10, 'y': 20})
print(a)  # 30

a = eval('x + y',
         {'x': 1, 'y': 2},
         {'x': 10})
print(a)  # 12
