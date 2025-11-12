class BMW():
    def fuel_type(self):
        print("Premiun unleaded gasoline (91 Octane)")
    def max_speed(self):
        print("180 mph")

class Ferrari():
    def fuel_type(self):
        print("Premiun unleaded gasoline (octante 91+)")
    def max_speed(self):
        print("211 mph")

obj1=BMW()
obj2=Ferrari()

for item in (obj1, obj2):
    item.fuel_type()
    item.max_speed()