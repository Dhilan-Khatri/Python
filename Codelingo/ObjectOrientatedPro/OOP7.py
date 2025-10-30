class circle():
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius

radius=int(input("Enter radius of the circle: "))
circle1=circle(radius)

print("Area of the circle:", circle1.area())
print("Perimeter of the circle:", circle1.perimeter())