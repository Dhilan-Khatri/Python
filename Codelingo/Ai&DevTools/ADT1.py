import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

print(Fore.CYAN + "Hello! I am an AI bot ready to assist you ")
name = input(Fore.GREEN + "What is your name? " + Style.RESET_ALL)
print(Fore.CYAN + f"\nHello {name}! How are you feeling today?")
mood  = input(Fore.YELLOW + "(good / great / okay / bad): " + Style.RESET_ALL).lower()
if mood == "good" or mood == "great":
    print(Fore.GREEN + "That's awesome to hear! ")
    print(Fore.CYAN + "What made your day so good?")
    reason = input(Fore.WHITE + "> ")

    print(Fore.CYAN + "Nice! One more question — are you busy today?")
    busy = input(Fore.YELLOW + "(yes / no): " + Style.RESET_ALL).lower()

    if busy == "yes":
        print(Fore.BLUE + "Got it! I’ll keep things quick for you ")
    else:
        print(Fore.GREEN + "That’s great! Enjoy your free time ")
elif mood == "okay":
    print(Fore.YELLOW + "Just okay, huh? ")
    print(Fore.CYAN + "Is there something you'd like to improve about your day?")
    improve = input(Fore.WHITE + "> ")

    print(Fore.CYAN + "That makes sense.")
    print(Fore.CYAN + "Do you want motivation or help with something specific?")
    choice = input(Fore.YELLOW + "(motivation / help): " + Style.RESET_ALL).lower()

    if choice == "motivation":
        print(Fore.GREEN + "You’re doing better than you think — keep going ")
    else:
        print(Fore.BLUE + "Alright! Tell me what you need help with.")
elif mood == "bad":
    print(Fore.RED + "I'm sorry to hear that ")
    print(Fore.CYAN + "Would you like to talk about what happened?")
    answer = input(Fore.YELLOW + "(yes / no): " + Style.RESET_ALL).lower()

    if answer == "yes":
        print(Fore.CYAN + "I'm listening. What happened?")
        problem = input(Fore.WHITE + "> ")
        print(Fore.GREEN + "Thank you for sharing.")
    else:
        print(Fore.BLUE + "That’s okay. I’m here whenever you need me.")
else:
    print(Fore.MAGENTA + "I may not fully understand, but I'm here to help ")
print(Fore.CYAN + "\nWould you like some weather information?")
location = input(
    Fore.YELLOW + "(New York City / London / Tokyo / Sydney / No): " + Style.RESET_ALL
).lower()
if location == "new york city":
    print(Fore.BLUE +
          "New York has cold, snowy winters and warm, humid summers.")
elif location == "london":
    print(Fore.BLUE +
          "London is often cloudy with light rain and mild temperatures.")
elif location == "tokyo":
    print(Fore.BLUE +
          "Tokyo has hot, humid summers and cold, dry winters.")
elif location == "sydney":
    print(Fore.BLUE +
          "Sydney has mild winters and warm summers.")
print(Fore.CYAN + "\nBefore you go, one last question:")
hobby = input(Fore.GREEN + "What is something you enjoy doing? " + Style.RESET_ALL)
print(Fore.GREEN + "That sounds fun! Keep doing what makes you happy ")
print(Fore.CYAN + f"It was great talking to you, {name}! Have an amazing day! ")