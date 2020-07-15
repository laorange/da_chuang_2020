#文本进度条v3
import time as t

scale = 50
print("执行开始".center(scale//2,"-"))
T = t.perf_counter()
t.sleep(0.5)

for i in range(scale+1):
    a = "*" * i
    b = "-" * (scale-i)
    progres = (i/scale)*100
    dur = t.perf_counter() - T
    print("\r{:^3.0f}%[{}→{}],已用时{:.2f}秒 ".format(progres,a,b,dur),end="")
    #print("已用时：{:.2f}".format(t).center(scale // 2, " "))
    t.sleep(2/(i+1)+0.05)

print("\n"+"执行结束".center(scale//2,"-"))
t.sleep(3)