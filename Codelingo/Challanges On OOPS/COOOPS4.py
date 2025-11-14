import random 
class fruit_quiz:
    def __init__(self):
        self.fruits={"Apple":"Red", "Banana":"Yellow", "Orange":"Orange", "Grape":"Purple"}
    def quiz(self):
        while True:
            fruit,color=random.choice(list(self.fruits.items()))
            ans=input(f"What is the Color of {fruit}? ")
            if ans==color:
                print("Correct")
            else:
                print("Incorrect")

            opt1=input("Do you want to keep going? (y/n)")
            if opt1=="n":
                break
obj1=fruit_quiz()
obj1.quiz()