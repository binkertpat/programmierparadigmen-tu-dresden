import turtle

turtle.speed(0)

def kochCurve(length, recursionDepth):
    if recursionDepth == 0:
        turtle.forward(length)
        return
    kochCurve(length / 3, recursionDepth - 1)
    turtle.right(-60)
    kochCurve(length / 3, recursionDepth - 1)
    turtle.right(120)
    kochCurve(length / 3, recursionDepth - 1)
    turtle.right(-60)
    kochCurve(length / 3, recursionDepth - 1)

turtle.penup()
turtle.goto(-200, 200)
turtle.pendown()
turtle.setheading(0)

kochCurve(200,4)

