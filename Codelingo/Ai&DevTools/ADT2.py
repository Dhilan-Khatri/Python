import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
print(f"{Fore.CYAN} Welcome to Sentiment Spy{Style.RESET_ALL}")
username=input(f"{Fore.GREEN} Input Your Username {Style.RESET_ALL}").strip()
if not username:
    username="Anonymous"
print(f"{Fore.CYAN}, Hello Agent {username} {Style.RESET_ALL}")
print(f"{Fore.CYAN} Type A Sentence And I will Return the Sentiment. {Style.RESET_ALL}")
print(f"{Fore.GREEN} Type Exit to Quit: {Style.RESET_ALL}")

positive_words = ["good", "great", "happy", "awesome", "excellent",]
negative_words = ["bad", "sad", "angry", "terrible", "awful",]
conversationHistory = []

while True:
    sentence = input(" ").lower()
    if sentence == "exit":
        print(f"{Fore.CYAN}Goodbye, Agent {username}.{Style.RESET_ALL}")
    conversationHistory.append(sentence)

    words = sentence.split()
    positive = 0
    negative = 0
    for word in words:
        if word in positive:
            positive += 1
        elif word in negative:
            negative += 1

    if positive > negative:
        choice = f"{Fore.WHITE}Positive"
    elif negative > positive:
        choice = f"{Fore.WHITE}Negative"
    else:
        choice = f"{Fore.WHITE}Neutral"

    print(f"Sentiment Spy: {choice}")