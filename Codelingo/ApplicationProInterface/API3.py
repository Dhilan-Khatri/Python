import requests
from textblob import TextBlob
from colorama import Fore, init
init(autoreset=True)
uselessSite="https://uselessfacts.jsph.pl/random.json?language=en"
catSite="https://catfact.ninja/fact"

def getUselessFact():
    response=requests.get(uselessSite)
    if response.status_code==200:
        fact=response.json()
        polarity=TextBlob(fact['text']).sentiment.polarity
        print(Fore.BLUE+f"Did you know {fact['text']}")
        if polarity>0.25: print(Fore.CYAN+"This Fact Is Positive.")
        elif polarity<-0.25: print(Fore.CYAN+"This Fact is Negative.")
        else: print(Fore.CYAN+"This Fact is Nuetral.")
    else:     print(Fore.RED+"Unable to Retrieve Fact.")
def getCatFact():
    response=requests.get(catSite)
    if response.status_code==200:
        jokeData=response.json()
        polarity=TextBlob(jokeData['fact']).sentiment.polarity
        print(Fore.BLUE+f"Did you know {jokeData['fact']}")
        if polarity>0.25: print(Fore.CYAN+"This Fact Is Positive.")
        elif polarity<-0.25: print(Fore.CYAN+"This Fact is Negative.")
        else: print(Fore.CYAN+"This Fact is Nuetral.")
    else:     print(Fore.RED+"Unable to Retrieve Fact.")
while True:
    userInput=input(Fore.GREEN+"Please Press '1' to Get A Random Fact\nPress '2' to Get A Cat Fact\nOr Press Any Other Key to Exit: ").strip().lower()
    if userInput == "1":
        getUselessFact()
    elif userInput =="2":
        getCatFact()
    else: 
        break
    