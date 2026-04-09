import requests
from colorama import Fore, init
init(autoreset=True)
site="https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def getUselessFact():
    response=requests.get(site)
    if response.status_code==200:
        fact=response.json()
        print(Fore.CYAN+f"UnEdited JSON: {fact}")
        print(Fore.BLUE+f"Did you know {fact['text']}")
    else:
        print(Fore.RED+"Unable to Retrieve Fact.")
while True:
    userInput=input(Fore.GREEN+"Please Enter to Get a Random Fact or Press 'q' to Exit: ").strip().lower()
    if userInput == "q":
        break
    else: getUselessFact()
    