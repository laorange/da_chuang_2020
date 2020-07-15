#autotracedraw.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)
#数据读取：
datals = []
data = open("data1.txt")
for line in data:
    line = line.replace("\n","")
    datals.append(list(map(eval,line.split(","))))
data.close()
#开始绘制：
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
t.done()