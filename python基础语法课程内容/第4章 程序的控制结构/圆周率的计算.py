#Calpiv2.py
from random import random
from time import perf_counter
darts = 10000*10000
hits  = 0.0
start = perf_counter()
for i in range(1,darts+1):
    x,y = random(), random()
    dist= pow(x**2+y**2,0.5)
    if dist<=1.0:
        hits += 1
pi=4*(hits/darts)
print("圆周率的值是：{}".format(pi))
print("运行时间是：{}s".format(perf_counter()-start))