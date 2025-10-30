#make a class io string
#3 fucn 1 contructor, 1, get string method, 3 print
class IOString():
    def __init__(self):
        self.srt1=""
    def get_String(self):
        self.srt1=input("Enter A String of Letters: ")
    def print(self):
        print(f"{self.srt1}")

obj1=IOString()
obj1.get_String()
obj1.print()
