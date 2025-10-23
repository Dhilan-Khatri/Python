def hotelcost(nights):
    return nights*140
def flightcost(city):
    if city == "New York City":
        return 500
    elif city == "Moscow":
        return 10
    elif city == "Tokyo":
        return 150
    elif city == "Madrid":
        return 200
city=input("Where are you travelling? \n A. New York City \n B. Moscow \n C. Tokyo \n D. Madrid \n")
nights = int(input("How many days are you staying at your city?"))
print(f"Total is equal to {hotelcost(nights)+flightcost(city)}")