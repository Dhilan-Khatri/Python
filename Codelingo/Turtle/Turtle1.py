import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)
hex=turtle.Turtle()

num=int(input("Enter Number of Sides"))
len=70
ang=360/num

for i in range(num):
    hex.forward(len)
    hex.right(ang)


turtle.done()