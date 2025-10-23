import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(1000,1000)
t=turtle.Turtle()
def triangle():
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
def triangle2():
    t.right(180)
    t.forward(100)
    t.right(30)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)
triangle()
t.left(30)
triangle()
triangle2()
triangle2()



turtle.done()