from turtle import*
import random
b=0
for i in range(20):
    x=random.random()
    y=random.random()
    z=random.random()
    speed(100)
    penup()
    a=-300+b
    b=b+1
    fd(a)
    goto(a,100)
    pendown()
    pensize(25)
    pencolor(x,y,z)

    #P
    seth(-90)
    fd(200)
    bk(200)
    left(90)
    fd(50)
    circle(-50,180)
    fd(50)

    #A
    penup()
    goto(a+200,100)
    pendown()
    goto(a+120,-100)
    goto(a+200,100)
    goto(a+280,-100)
    penup()
    goto(a+150,-40)
    pendown()
    goto(a+250,-40)

    #U
    penup()
    goto(a+320,100)
    pendown()
    seth(-90)
    fd(150)
    circle(50,180)
    fd(150)

    #L
    penup()
    right(90)
    fd(60)
    right(90)
    pendown()
    fd(200)
    left(90)
    fd(100)

done()
