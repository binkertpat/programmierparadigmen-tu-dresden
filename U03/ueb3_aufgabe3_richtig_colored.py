import turtle

turtle.speed(-100)
turtle.setheading(90)

def rect(length, color) :
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.pu()
    turtle.forward(length)
    turtle.pd()


def triangle(length, color) :
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(length/2*pow(2,0.5))
    turtle.right(90)
    turtle.forward(length/2*pow(2,0.5))
    turtle.right(135)
    turtle.end_fill()
    
    
def zeichne(length) :

    if length < 40 :
        rect(length, 'green')    
    else :
        rect(length,'brown')
        triangle(length,'red')
        
        turtle.forward(length)
        turtle.right(45)
        
        oPos = turtle.pos()
        oHeading = turtle.heading()
        
        zeichne(length/2*pow(2,0.5))

        turtle.pu()
        turtle.setpos(oPos)
        turtle.setheading(oHeading)
        turtle.pd()
        turtle.right(90)
        turtle.forward(length/2*pow(2,0.5))
        
        zeichne(length/2*pow(2,0.5))  

zeichne(100)