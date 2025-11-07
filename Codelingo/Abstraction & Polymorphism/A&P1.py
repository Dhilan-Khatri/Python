from abc import ABC, abstractmethod 

class parent(ABC):
    def print(self,x):
        print(f"Past value is {x}.")
    @abstractmethod
    def task (self):
        print("We are in Absract Task.")

class child(parent):
    def task (self):
        print("We are in Child Absract Task.")

obj1=child()
obj1.task()
obj1.print(654)