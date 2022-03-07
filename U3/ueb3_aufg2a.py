import turtle

def doingTheStep():
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    
def nextStep(n):
    if n == 0:
        return
    doingTheStep()
    nextStep(n-1)  

nextStep(6)  