import turtle as d
def drawgap():
    d.penup()
    d.fd(5)

def drawline(draw): #绘制单段数码管
    drawgap()
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
    d.pencolor("red")
    for i in date:
        if i == '-':
            d.write('年', font=("Arial",18,"normal"))
            d.pencolor("green")
            d.fd(17)
        elif i == '=':
            d.fd(23)
            d.write('月', font=("Arial", 18, "normal"))
            d.pencolor("purple")
            d.fd(40)
        elif i == '+':
            d.write('日', font=("Arial", 18, "normal"))
        else:
            drawdigit(eval(i))

def main():
    d.setup(800,350,200,200)
    d.penup()
    d.fd(-300)
    d.left(90)
    d.fd(30)
    d.right(90)
    d.pensize(5)
    drawdate('2020-1=25+')
    d.pencolor('black')
    d.penup()
    d.bk(390)
    d.right(90)
    d.fd(120)
    d.left(90)
    d.pendown()
    d.write('傻儿子生日快乐！', font=("Batang", 24, "normal"))
    d.hideturtle()
    d.done()
main()