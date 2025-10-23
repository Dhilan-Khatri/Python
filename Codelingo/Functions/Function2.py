def weather(temp):
    if temp <= 10:
        print("Weather is cold")
    elif temp <= 30:
        print("Weather is neutral")
    else:
        print("Weather is warm")
temp = int(input("Enter the tempature: "))
weather(temp)