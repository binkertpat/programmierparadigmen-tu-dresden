import turtle

turtle.speed(0)

def baum(x):
    if x < 8:
        return
    turtle.forward(x)
    turtle.left(45)
    baum(x/2)
    turtle.right(90)
    baum(x/2)
    turtle.left(45)
    turtle.backward(x)

turtle.setheading(90)
baum(100)