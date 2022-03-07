import turtle
import math

turtle.mode('logo')
turtle.speed(2)
turtle.shape('turtle')

def quadrat(laenge):
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(135)
    turtle.forward(laenge * math.sqrt(2))
    turtle.right(135)
    turtle.forward(laenge)
    turtle.right(135)
    turtle.forward(laenge * math.sqrt(2))
    pass

def dreieck(laenge):
    turtle.right(90)
    turtle.forward((laenge/2) * math.sqrt(2))
    turtle.right(90)
    turtle.forward((laenge/2) * math.sqrt(2))
    turtle.right(45)
    turtle.forward(laenge)
    turtle.left(90)
    turtle.left(90)
    pass

def haus():
    turtle.goto(-500, -200)
    laenge=20
    for i in range(2,6):
        quadrat(laenge)
        dreieck(laenge)
        laenge=laenge*i
    pass

haus()
