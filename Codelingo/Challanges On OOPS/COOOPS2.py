#make program to overload < and ==
#obj1=3 obj2=4
#if obj1 is less than 3 then say less tha

class overload:
    def __init__(self, x):
        self.x=x
    def __lt__(self, other):
        if self.x < other.x:
            print(f"{self.x}, is less than {other.x}.")
        else:
            print(f"{self.x} is not less than {other.x}.")
    def __eq__(self, other):
        if self.x == other.x:
            print(f"{self.x}, is equal to {other.x}.")
        else:
            print(f"{self.x}, is not equal to {other.x}.")

obj1=overload(4)
obj2=overload(2)

print(obj1<obj2)
print(obj1==obj2)