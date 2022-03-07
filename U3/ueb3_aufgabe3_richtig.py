import turtle
import math

def drawPythagorasTree(length, repetitions):
    if repetitions == 0:
        turtle.forward(length)
    else:
        turtle.fillcolor('#ad0000')
        turtle.begin_fill()
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90);
        turtle.forward(length)
        turtle.right(90);
        turtle.forward(length)
        turtle.right(180);
        turtle.forward(length)
        turtle.right(-45)
        turtle.end_fill()
        if (repetitions > 0):
            drawPythagorasTree(length/math.sqrt(2), repetitions - 1)
        else:
            turtle.forward(length/math.sqrt(2))
        turtle.right(-90)
        if (repetitions > 0):
            drawPythagorasTree(length/math.sqrt(2), repetitions - 1)
        else:
            turtle.forward(length/math.sqrt(2))
        turtle.right(-45)
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
        
turtle.setheading(180)
drawPythagorasTree(100, 3)