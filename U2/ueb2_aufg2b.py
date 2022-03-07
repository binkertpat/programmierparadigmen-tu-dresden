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
    turtle.left(90)
    turtle.left(90)
    pass

def haus():
    for i in range(1,6):
        quadrat(20*i)
        dreieck(20*i)
    pass

haus()
    
    
    
