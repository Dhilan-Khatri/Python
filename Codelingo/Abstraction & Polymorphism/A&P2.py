from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk & Run.")
class snake(animal):
    def move(self):
        print("I can crawl.")
class dog(animal):
    def move(self):
        print("I can walk & Run.")
class bird(animal):
    def move(self):
        print("I can fly.")
class whale(animal):
    def move(self):
        print("I can swim.")
obj1=human()
obj1.move()
obj2=snake()
obj2.move()
obj3=dog()
obj3.move()
obj4=bird()
obj4.move()
obj5=whale()
obj5.move()