import turtle
import math

def quadrat(laenge):
    turtle.setheading(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(135)
    turtle.forward(laenge*math.sqrt(2))
    turtle.right(135)
    turtle.forward(laenge)
    turtle.right(135)
    turtle.forward(laenge*math.sqrt(2))
    pass

def dreieck(laenge):
    turtle.right(90)
    turtle.forward((laenge/2)*math.sqrt(2))
    turtle.right(90)
    turtle.forward((laenge/2)*math.sqrt(2))
    turtle.right(45)
    turtle.forward(laenge)
    pass

def haus():
    quadrat(40)
    dreieck(40)
    pass

haus()


    
    
    