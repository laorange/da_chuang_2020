#数码管绘制1
import turtle as d
import random
def drawgap():
    d.penup()
    d.fd(5)
def drawline(draw): #绘制单段数码管
    drawgap()
    x = random.uniform(0,1)
    y = random.uniform(0,0.5)
    z = random.uniform(0,1)
    d.pencolor(x, y, z)
    d.pendown() if draw else d.penup()
    d.fd(40)
    drawgap()
    d.right(90)

def juge(dight,*b):
    if dight in b:
        drawline(True)
    else:
        drawline(False)
def drawdigit(dight): #根据数字来画
    juge(dight,2,3,4,5,6,8,9)
    juge(dight,0,1,3,4,5,6,7,8,9)
    juge(dight,0,2,3,5,6,8,9)
    juge(dight,0,2,6,8)
    d.left(90)
    juge(dight,0,4,5,6,8,9)
    juge(dight,0,2,3,5,6,7,8,9)
    juge(dight,0,1,2,3,4,7,8,9)
    d.left(180)
    d.penup()
    d.fd(20)
def drawdate(date):
    for i in date:
        drawdigit(eval(i))
def main():
    d.setup(800,350,200,200)
    d.penup()
    d.fd(-350)
    d.pensize(5)
    s=input("请输入一个整数：")
    drawdate(s)
    d.hideturtle()
    d.done()
main()