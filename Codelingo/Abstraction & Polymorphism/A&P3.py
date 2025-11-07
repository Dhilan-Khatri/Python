class square():
    def __init__(self, side):
        self.side=side
    def area(self):
        print(f"The area is {self.side**2}")
class circle():
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        print(f"The area is {3.14*self.radius**2}")
obj1=circle(23)
obj2=square(84)
for shape in (obj1, obj2):
    shape.area()