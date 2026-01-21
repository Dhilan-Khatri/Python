import colorama
from colorama import Fore, Style
#from Textblob import Textblob

colorama.init(autoreset=True)
print(f"{Fore.CYAN} Welcome to Sentiment Spy {Style.RESET_ALL}")
username=input(f"{Fore.GREEN} Input Your Username {Style.RESET_ALL}").strip()
if not username:
    username="Anonymous"
print(f"{Fore.CYAN}, Hello Agent {username} {Style.RESET_ALL}")
conversationHistory=[]
print(f"{Fore.CYAN} Type A Sentence And I will Return the Sentiment. {Style.RESET_ALL}")
print(f"{Fore.GREEN} Type Exit to Quit: {Style.RESET_ALL}")
