class animal:
    def __init__(self, name, location):
        self.name=name
        self.location=location
    def display(self):
        print(f"Name of animal is {self.name} and location is {self.location}")

class sheep(animal):
    def __init__(self, name, location, speed, noise):
        super().__init__(name, location)
        self.noise=noise
        self.speed=speed
    def display1(self):
        print(f"The {self.name} can go {self.speed} speed.")
    def sound(self):
        print(f"The {self.name} goes {self.noise}.")

class dog(animal):
    def __init__(self, name, location, speed, noise):
        super().__init__(name, location)
        self.noise=noise
        self.speed=speed
    def display1(self):
        print(f"The {self.name} can go {self.speed} speed.")
    def sound(self):
        print(f"The {self.name} goes {self.noise}.")

animal1=sheep("Sheep", "Land", "Slow", "Baaah")
animal2=dog("Dog", "Land", "Medium-Fast", "Woof")
animal1.display()
animal2.display()
animal1.display1()
animal2.display1()
animal1.sound()
animal2.sound()