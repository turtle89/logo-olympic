from turtle import *

c = ['blue', 'black', 'red', 'yellow', 'green']
pensize(15)
for n in range(5):
    color(c[n])
    penup()
    if n < 3:
        goto(-240+240*n, 0)
        pendown()
        left(45)
        circle(100, 180)
        left(135)
    else:
        goto(-260+240*(n-3), -100)
        pendown()
        left(-45)
        circle(100, -180)
        left(-135)
for n in range(5):
    color(c[n])
    penup()
    if n < 3:
        goto(-240+240*n, 0)
        pendown()
        left(45)
        circle(100, -180)
        left(135)
    else:
        goto(-260+240*(n-3), -100)
        pendown()
        left(-45)
        circle(100, 180)
        left(-135)
hideturtle()
input()
