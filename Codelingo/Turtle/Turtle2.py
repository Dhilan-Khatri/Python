import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)
hex=turtle.Turtle()

for i in range (3):
    hex.forward(100)
    hex.right(120)
hex.right(90)
hex.penup()
hex.forward(50)
hex.left(90)
hex.pendown()
for i in range (3):
    hex.forward(100)
    hex.left(120)
turtle.done()