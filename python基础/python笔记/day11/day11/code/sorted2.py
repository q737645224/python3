# sorted.py

names = ['Tom', 'Jerry', 'Spike', 'Tyke']

L1 = sorted(names, key=len)
print("L1=", L1)

L2 = sorted(names, key=lambda x: len(x))
print("L2=", L2)



