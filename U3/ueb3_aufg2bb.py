import turtle

turtle.speed(0)

"""
def kochCurve(length, recursionDepth):
    if recursionDepth == 0:
        turtle.forward(length)
        return
    kochCurve(length / 2, recursionDepth - 1)
    turtle.right(-60)
    kochCurve(length / 2, recursionDepth - 1)
    turtle.right(120)
    kochCurve(length / 2, recursionDepth - 1)
    turtle.right(-60)
    kochCurve(length / 2, recursionDepth - 1)
"""

def kochCurve(length):
    if length < 20:
        turtle.forward(length)
        return
    kochCurve(length / 3)
    turtle.right(-60)
    kochCurve(length / 3)
    turtle.right(120)
    kochCurve(length / 3)
    turtle.right(-60)
    kochCurve(length / 3)
    
turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()
turtle.setheading(0)

kochCurve(300)