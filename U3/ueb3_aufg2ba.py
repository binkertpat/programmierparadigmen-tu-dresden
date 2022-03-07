import turtle

turtle.speed(0)

def kochCurve(length, recursionDepth):
    if recursionDepth == 0:
        turtle.forward(length)
        return
    kochCurve(length, recursionDepth - 1)
    turtle.right(-60)
    kochCurve(length, recursionDepth - 1)
    turtle.right(120)
    kochCurve(length, recursionDepth - 1)
    turtle.right(-60)
    kochCurve(length , recursionDepth - 1)

turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()
turtle.setheading(0)

kochCurve(100, 1)