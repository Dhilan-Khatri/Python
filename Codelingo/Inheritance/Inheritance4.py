class vehicle:
    def __init__(self, capacity):
        self.capacity=capacity
    def fare(self):
        return self.capacity * 100
    
class bus(vehicle):
    def fare(self):
        bfare = super().fare()
        tfare = bfare + (0.1*bfare)
        return tfare

bus1 = bus(50)
print(f"The Total fare is: {bus1.fare()}")
