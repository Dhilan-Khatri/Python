import sys 
from groq import generateResponse
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
def biasMin():
    print(40*"=")
    print("Bias Minigation Activity")
    print(40*"=")
    prompt=input("Enter a prompt to explore bias (Explain Who Is A Ideal Doctor): ").strip()
    if not prompt:
        print("Please Enter A Prompt To Continue")
        return
    initResponse=generateResponse(prompt, temperature=0.5, maxToken=1024)
    print(f"\nInital Ai Response: \n{initResponse}")
    modPrompt=input("\nModify the prompt to make it more nuetral. (Explain Qualities Of A Good Doctor): ").strip()
    if not modPrompt:
            print("Please Enter A Prompt To Continue")
            return
    modResponse=generateResponse(modPrompt, temperature=0.5, maxToken=1024)
    print(f"\nModified Ai Response: \n{modResponse}")
def tokenLimt():
    print(40*"=")
    print("Token Limitation Activity")
    print(40*"=")
    prompt=input("Enter a long prompt to explore Token Limits (A Very Detailed Story): ")
    if not prompt:
            print("Please Enter A Prompt To Continue")
            return
    initResponse=generateResponse(prompt,temperature=0.5,maxToken=1024)
    modResponse=(initResponse[:500]+"...")
    if len(initResponse)<500:
        modResponse=initResponse
    print(f"\nAi Response: \n{modResponse}")
    srtPrompt=input("\nPlease Condense Your Prompt To Be More Precise: ").strip()
    if not srtPrompt:
        print("Please Enter A Prompt To Continue")
        return
    srtResponse=generateResponse(srtPrompt,temperature=0.5, maxToken=1024)
    print(f"\nShorten(Prompt) Ai Response: \n{srtResponse}")
def main():
    print("Welcome to Bias Minigation and Token Limit Activities.")
    print("Would You Like To Go To Bias Minigation(1), or Token Limit(2)?")
    choice=int(input("Please Enter A 1 Or 2: ").strip())
    if not choice or choice <1 or choice>2:
        print("Please Enter A Valid Number:")
    if choice==1:
         biasMin()
    else:
         tokenLimt()
main()