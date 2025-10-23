import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(1000,1000)
hex=turtle.Turtle()
x=1
L=10
while x > 0:
    hex.forward(L)
    hex.right(90)
    L+=3


turtle.done()