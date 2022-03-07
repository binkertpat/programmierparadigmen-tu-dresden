import turtle
import math  

def quadrat(laenge):
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(90)
    turtle.forward(laenge)
    turtle.right(45)
    
    pass

def dreieck(laenge):
    turtle.forward((laenge/2)*math.sqrt(2))
    turtle.right(90)
    turtle.forward((laenge/2)*math.sqrt(2))
    pass

def haus():
    quadrat(40)
    dreieck(40)
    dreieck(40)
    dreieck(40)
    dreieck(40)
    pass

haus()
    
    
    

