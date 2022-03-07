import turtle

turtle.speed(0)

def rect(length, recursionDepth, maxRepetitions=1):
  if recursionDepth >= maxRepetitions:
    for i in range(3):
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(180)
        rect(round(length/3), recursionDepth, maxRepetitions+1)
    if recursionDepth > 1:
      turtle.forward(length)
      turtle.left(90)
      turtle.forward(length)
      turtle.left(180)
  else:
    for i in range(4):
      turtle.forward(length)
      turtle.left(90)
    turtle.forward(length)
    turtle.left(180)
    
turtle.pu()
turtle.goto(0,-100)
turtle.pd()

turtle.setheading(0)
rect(150,4)