class dog:
    def __init__(self, breed, colour, detail):
        self.breed=breed
        self.colour=colour
        self.detail=detail
    def display(self):
        print(f"\nThe Breed of the Dog is: {self.breed}")
        print(f"The Colour of the Dog is: {self.colour}")
        print(f"The Details of the Dog is: {self.detail}")

DS=dog("Dachshund", "Brown or Black", "The dachshund, also known as the wiener dog, or sausage dog, badger dog, doxen and doxie, is a short-legged, long-bodied, hound-type dog breed. ")
PWC=dog("Pembroke Welsh Corgi", "Black, Brown, Golden, White", "The Pembroke Welsh Corgi is a cattle herding dog breed that originated in Pembrokeshire, Wales.")

DS.display()
PWC.display()