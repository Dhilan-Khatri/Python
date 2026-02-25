from colorama import Fore, init
import random
init(autoreset=True)

print(Fore.WHITE+"Welcome to Rock, Paper Scissors")
print(Fore.WHITE+"Do you Want to play? (Yes/No)")
play=input(Fore.CYAN+"You: ").lower()

choices=["rock", "paper", "scissors"]

if play == "yes":
    contin="yes"
    while contin=="yes":
        print(Fore.MAGENTA+"Lets Start: Rock! Paper! Scissors, Shoot!")
        botChoice=random.choice(choices)
        userChoice=input(Fore.CYAN+"You: ").lower()
        if userChoice == "rock":
            if botChoice == "rock":
                print(Fore.BLUE+f"Bot choose {botChoice}.")
                print(Fore.WHITE+"You Tie the game.")
            if botChoice == "paper":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Lose the game.") 
            if botChoice == "scissors":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Win the game.") 
        elif userChoice == "paper":
            if botChoice == "rock":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Win the game.") 
            if botChoice == "paper":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Tie the game.")
            if botChoice == "scissors":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Lose the game.")       
        elif userChoice == "scissors":
            if botChoice == "rock":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Lose the game.") 
            if botChoice == "paper":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Win the game.")  
            if botChoice == "scissors":
                print(Fore.BLUE+f"Bot choice was {botChoice}")
                print(Fore.WHITE+"You Tie the game.") 
        else:
            print(Fore.BLUE+"Next time enter a valid choice.")
        contin=input(Fore.WHITE+"Do you want to continue? (Yes/No)").lower()
    else:
        print(Fore.BLUE+"Okay, see you next time.")
else:
    print(Fore.WHITE+"Oh, okay. Bye!")