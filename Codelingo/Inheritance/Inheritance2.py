class person:
    def __init__(self, name, id):
        self.name=name
        self.id=id
    def display(self):
        print(f"Name is {self.name} and Id is {self.id}")
class employ(person):
    def __init__(self, name, id, salary, post):
        super().__init__( name, id)
        self.salary=salary
        self.post=post
    def display1(self):
        print(f"Employ Salary is {self.salary} and Postiton is {self.post}.")
employ1=employ("Bill", 1242, 85000, "Mechanical Engineering")
employ1.display()
employ1.display1()