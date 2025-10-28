class words:
    def __init__(self, length, vowels, constonates, type, word):
        self.length=length
        self.vowels=vowels
        self.constonates=constonates
        self.type=type
        self.word=word
    def display(self):
        print(f"\nThe Length of the Word is: {self.length}")
        print(f"The number of Vowels of the Word is: {self.vowels}")
        print(f"The number of Constonates of the Word is: {self.constonates}")
        print(f"The Type of the Word is: {self.type}")
        print(f"The Word is: {self.word}")
class calulation:
    def __init__(self, number1, number2):
        self.number1=number1
        self.number2=number2
    def display(self):
        print(f"Number 1 is {self.number1}")
        print(f"Number 2 is {self.number2}")
    def addition(self):
        print(f"The sum is {self.number1+self.number2}")
    def subtraction(self):
        print(f"The result is {self.number1-self.number2}")
object1=calulation(18, 53)
object1.display()
object1.addition()
object1.subtraction()