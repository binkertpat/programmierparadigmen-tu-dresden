import turtle
import math  
import random

def movePen(x,y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
def quadrat(laenge):
    movePen(random.randint(-400,400),random.randint(-400,400))
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

def sterne():
    for i in range(1,40):
        groesse = random.randint(10,50)
        quadrat(groesse)
        dreieck(groesse)
        dreieck(groesse)
        dreieck(groesse)
        dreieck(groesse)
    turtle.right(45)    
    pass

sterne()









    
    
    

