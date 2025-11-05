class myclass:
    __privateVar=27
    def __privatemethod(self):
        print("I am inside myclass.")
    def hello(self):
        print("Private Varible Value", myclass.__privateVar)

obj1=myclass()
obj1.hello()
obj1.__privatemethod()

