# make class called computer, max price is private, make method "sell", to show display price and max price.
#have to set max price
#max price = private
#take user input to make max price

class computer:
    def __init__(self):
        self.__maxPrice=900
    def sell(self):
        print(f"The price of the laptop is {self.__maxPrice}")
    def setMaxPrice(self, price):
        self.__maxPrice=price

computer1=computer()
computer1.sell()
computer1.setMaxPrice(7000)
computer1.sell()

#computer1.__maxPrice=800
#print(computer1.__maxPrice)
#computer1.sell()

print(dir(computer1))