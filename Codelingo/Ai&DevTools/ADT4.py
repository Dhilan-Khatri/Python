from colorama import Fore, init
import re, random
init(autoreset=True)

destination={
    "Beaches":["Bahamas", "Bali", "Maldives"], 
    "Mountains":["Swiss Allps.", "Rocky Mount.", "Himalayas"], 
    "Cities":["Toyko", "New York City", "Paris"]
    }
jokes=["Why don't programmers like nature? \n To many bugs.", "Knock knock! \nWho is there? \nYah! \nYah, who? \nNo not Yahoo, Google.", "How do robots eat pizza? \n One byte at a time."]

def normalizeInput(text):
    return re.sub(r"\s+", " ", text.strip().lower())
def recommend():
    print(Fore.BLUE+"Travel Bot: Beaches, Mountains, Cities")
    preference=input(Fore.GREEN+"You: ").lower
    preference=normalizeInput(preference)
    if preference in destination:
        suggestion=random.choice(destination[preference])
        print(Fore.RED+f"Travel Bot: How About {suggestion}")
        print(Fore.BLUE+"Travel Bot: Do you like it? (Yes/No)")
        answer=input(Fore.GREEN+"You: ").lower()
        if answer == "yes":
            print(Fore.BLUE+f"Travel Bot: Awesome! Enjoy {suggestion}.")
        elif answer == "no":
            print(Fore.RED+"Travel Bot: Lets Try Another.")
            recommend()
        else:
            print(Fore.RED+"Travel Bot: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED+"Travel Bot: Sorry I don't have that as a destination.")
def packingTips():
    print(Fore.BLUE+"Travel Bot: Where to?")
    location=normalizeInput(input(Fore.GREEN+"You: "))
    print(Fore.BLUE+"Travel Bot: How many days?")
    days=(Fore.GREEN+"You: ")
    print(Fore.BLUE+f"Travel Bot: Packing tips for {days} days in {location}")
    print(Fore.YELLOW+"-Pack Veratile Clothes")
    print(Fore.YELLOW+"-Carry Muti-Port Charger")
    print(Fore.YELLOW+"-Check Weather Forecast")
def tellJokes():
    print(Fore.MAGENTA+f"Travel Bot: {random.choice(jokes)}")
def showHelp():
    print(Fore.CYAN+"\n I can:")
    print(Fore.CYAN+"Suggest Travel Spots (Say'Recommend')")
    print(Fore.CYAN+"Offer Packing Tips (Say'Packing')")
    print(Fore.CYAN+"Tell Jokes (Say 'Jokes')")
    print(Fore.CYAN+"Show Help (Say 'help')")
    print(Fore.CYAN+"Type 'Exit' to end.")
def chat():
    print(Fore.BLUE+"Hello I am a travel bot")
    name=input(Fore.GREEN+"Your name? ")
    print(Fore.BLUE+f"Nice to meet you {name}.")
    showHelp()
    while True:
        userInput=input(Fore.GREEN+f"{name}")
        userInput=normalizeInput(userInput)
        if "recommend" in userInput or "suggest" in userInput:
            recommend()
        elif "packing" in userInput or "pack" in userInput:
            packingTips()
        elif "joke" in userInput or "funny" in userInput:
            tellJokes()
        elif "help" in userInput:
            showHelp()
        elif "exit" in userInput or "bye" in userInput:
            print(Fore.WHITE+"Travel Bot: Safe Travels GoodBye")
            break
        else:
            print(Fore.RED+"Travel Bot: Please Rephrase")
chat()