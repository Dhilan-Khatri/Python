class fruits:
    def __init__(self, color, size, taste, name):
        self.color=color
        self.size=size
        self.taste=taste
        self.name=name
    def display(self):
        print(f"\nThe Color of the Fruit is: {self.color}")
        print(f"The Size of the Fruit is: {self.size}")
        print(f"The Taste of the Fruit is: {self.taste}")
        print(f"The Name of the Fruit is: {self.name}")

mango=fruits("Yellow", "Medium", "Sweet", "Mango")
mango.display()
apple=fruits("Red", "Medium-Small", "Sour/Sweet", "Apple")
apple.display()