import requests
from colorama import init, Fore
init(autoreset=True)
def getRandomJokes():
    site="https://catfact.ninja/fact"
    response=requests.get(site)
    if response.status_code==200:
        print(Fore.LIGHTMAGENTA_EX+f"Full JSON Responce: {response.json()}")
        jokeData=response.json()
        return f"{jokeData['fact']}"
    else:
        return Fore.RED+"Failed to Fetch Joke"
name=input(Fore.CYAN+"Welcome, What is Your Name? ")
print(Fore.CYAN+f"Welcome {name} to the Random Cat Fact Generator")
while True:
    userInput=input(Fore.BLACK+"Press Enter to Get A New Fact\nOr press 'q' to exit: ").strip().lower()
    if userInput=="q":
        print(Fore.CYAN+f"Goodbye {name}, See You Again Soon")
        break
    else:
        joke=getRandomJokes()
        print(Fore.GREEN+joke)
