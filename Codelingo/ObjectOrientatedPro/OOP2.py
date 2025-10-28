class student:
    def __init__(self, name, age, grade, city):
        self.name=name
        self.age=age
        self.grade=grade
        self.city=city
    def display(self):
        print(f"\nThe Name of the Student is: {self.name}")
        print(f"The Age of the Student is: {self.age}")
        print(f"The Grade of the Student is: {self.grade}")
        print(f"The City of the Student is: {self.city}")

Bill=student("Bill", "9", "4th", "Los Angles")
Bill.display()
Harry=student("Harry", "14", "9th", "London")
Harry.display()
Steve=student("Steve", "12", "7th", "New York City")
Steve.display()
Steve.grade="6th"
Steve.display()

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