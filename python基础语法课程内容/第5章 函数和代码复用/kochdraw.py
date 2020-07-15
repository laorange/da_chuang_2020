#kochdraw.py
import turtle as d
def koch(size,n):
    if n==0:
        d.fd(size)
    else:
        for angle in [0,60,-120,60]:
            d.left(angle)
            koch(size/3,n-1)
def main():
    d.setup(600,600)
    d.penup()
    d.goto(-200,100)
    d.pendown()
    d.pensize(2)
    level=3
    koch(400,level)
    d.right(120)
    koch(400,level)
    d.right(120)
    koch(400,level)
    d.hideturtle()
    d.done()
main()