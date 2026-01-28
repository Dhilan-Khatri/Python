import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

print(f"{Fore.CYAN} Welcome to Sentiment Spy{Style.RESET_ALL}")
username=input(f"{Fore.GREEN} Input Your Username {Style.RESET_ALL}").strip()
if not username:
    username="Anonymous"
print(f"{Fore.CYAN} Hello Agent {username} {Style.RESET_ALL}")
print(f"{Fore.CYAN} Type A Sentence And I will Return the Sentiment. {Style.RESET_ALL}")
print(f"{Fore.GREEN} Type Exit to Quit: {Style.RESET_ALL}")

conservationHistory=[]
while True:
    userInput=input(f"{Fore.GREEN}>>{Style.RESET_ALL}").strip()
    if not userInput:
        print(f"{Fore.RED} Please Enter Some Text Or A Valid Command {Style.RESET_ALL}")
        continue
    if userInput.lower()=="exit":
        print(f"{Fore.CYAN} Exiting Sentiment Spy, Farewell {username}. {Style.RESET_ALL}")
        break
    elif userInput.lower()=="reset":
        conservationHistory.clear()
        print(f"{Fore.BLUE}All Converation History Is Cleared {Style.RESET_ALL}")
        continue
    elif userInput.lower()=="history":
        if not conservationHistory:
            print(f"{Fore.YELLOW} No Converation History Yet. {Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE} Conversation History: {Style.RESET_ALL}")
            for index,(text, polarity, sentimentType) in enumerate(conservationHistory, start=1):
                if sentimentType=="Postive":
                    color=Fore.GREEN
                    emoji="😃"
                elif sentimentType=="Negative":
                    color=Fore.RED
                    emoji="😢"
                else:
                    color=Fore.YELLOW
                    emoji="😐"
                print(f"{index}.{color}{emoji}{text}. polarity:{polarity:.2f}, {sentimentType}{Style.RESET_ALL}")
            continue
    polarity=TextBlob(userInput).sentiment.polarity
    if polarity>0.25:
        sentimentType="Positive"
        color=Fore.GREEN
        emoji="😃"
    elif polarity<-0.25:
        sentimentType="Negative"
        color=Fore.RED
        emoji="😢"
    else:
        sentimentType="Nuetral"
        color=Fore.YELLOW
        emoji="😐"
    conservationHistory.append((userInput, polarity, sentimentType))
    print(f"{color}{emoji}{sentimentType} Sentiment Detected. polarity:{polarity:.2f}{Style.RESET_ALL}")