import requests
from config import hf_api10_key
from colorama import Fore, Style, init
init(autoreset=True)
defaultModel="facebook/bart-large-cnn"
def buildAPIUrl(modelName):
    return f"https://router.huggingface.co/hf-inference/models/{modelName}"
def query(payload, modelName=defaultModel):
    apiURL=buildAPIUrl(modelName)
    headers={"Authorization":f"Bearer {hf_api10_key}"}
    response=requests.post(apiURL,headers=headers,json=payload,timeout=60)
    if response.status_code != 200:
        print(Fore.RED+Style.BRIGHT+f"API Error Sorry! {response.status_code} : {response.text}")
        return None
    try:
        return response.json()
    except Exception:
        print(Fore.RED+Style.BRIGHT+f"Could Not Parse API Response {response.text}")
        return None
def summerizeText(text,minLen,maxLen,modelName=defaultModel):
    payload={
        "inputs":text,
        "parameters":{
            "min_length":minLen,
            "max_length":maxLen
        }
    }
    result=query(payload,modelName=modelName)
    if result is None:
        return None
    else:
        if isinstance(result,list) and result and "summary_text" in result[0]:
            return result[0]["summary_text"]
        else:
            print(Fore.RED+Style.BRIGHT+f"Unexpected Response Format: {result}")
            return None
print(Fore.CYAN+Style.BRIGHT+"Hello There, What Is Your Name?")
userName=input(Fore.YELLOW+Style.NORMAL+"Your Name: ").strip()
if not userName:
    userName="User"
print(Fore.CYAN+Style.BRIGHT+f"Welcome {userName}, Lets Summerize Your Text!")
print(Fore.CYAN+Style.BRIGHT+"Please Enter The Text Your Want To Summerize.")
userText=input(Fore.YELLOW+Style.NORMAL+f"{userName}: ").strip()
if not userText:
    print(Fore.BLUE+Style.NORMAL+"No Text Given, Exiting...")
else:
    print(Fore.CYAN+Style.BRIGHT+"Enter Prefered Model (Leave Blank For Default)")
    modelChoice=input(Fore.YELLOW+Style.NORMAL+"Model Name: ").strip()
    if not modelChoice:
        modelChoice=defaultModel
    print(Fore.CYAN+Style.BRIGHT+"Chose Summerization Style.")
    print(Fore.CYAN+Style.BRIGHT+"1. Standard- Quick & Consise (50-150 Words). \n2. Enhanced-More Detail (80-200 Words).")
    styleChoice=input(Fore.YELLOW+Style.NORMAL+"Enter 1 Or 2: ").strip()
    if styleChoice=="2":
        minlen=80
        maxlen=200
        print(Fore.BLUE+Style.NORMAL+"Enhanced Summerization Selected.")
    else:
        minlen=50
        maxlen=150
        print(Fore.BLUE+Style.NORMAL+"Standard Summerization Selected.")
    summary=summerizeText(userText,minlen,maxlen,modelName=modelChoice)
    if summary:
        print(Fore.GREEN+Style.NORMAL+f"Summary For {userName}, ")
        print(Fore.GREEN+Style.NORMAL+summary)
    else:
        print(Fore.RED+Style.BRIGHT+"Failed To Generate Summary!")
