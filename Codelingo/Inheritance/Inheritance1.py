class vehicle:
    def __init__(self, name, hp, millage):
        self.name=name
        self.hp=hp
        self.millage=millage
class bus(vehicle):
    pass
schoolbus=bus("School Bus", "180", "12")
print(f"The name of SchoolBus is {schoolbus.name}, Hp is {schoolbus.hp}, Millage is {schoolbus.millage}.")