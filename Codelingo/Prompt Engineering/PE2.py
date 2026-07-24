from groq import generateResponse
import time

def temperaturePromptActivity():
    print(70*"=")
    print("Advanced Prompt Engineering; Temperature + Instruction")
    print(70*"=")
    print("\nPart 1: Temperature Exploration")
    base=input("Enter a Creative Prompt: ").strip()
    for t,label in [(0.1,"Low (0.1)-Determind"),(0.5,"Medium (0.5)-Balanced"),(1,"High (1)-Creative")]:
        print(f"----{label}----")
        print(generateResponse(base,temperature=t,maxToken=512))
        time.sleep(1)

    print("\n\nPart 2: Instruction Based Prompts")
    topic=input("Enter a Topic (Climate, Space, Marine): ").strip()
    prompts=[
        f"Summerize Key Facts About {topic}, in 3 to 4 sentences.",
        f"Explain {topic}, as if i am a 10 year old child",
        f"Write a Pro and Con list about {topic}.",
        f"Create a fictional New Headline from 2050 about {topic}."
    ]
    for i,p in enumerate(prompts,1):
        print(f"\n---Instruction: {i}---\n{p}")
        print("\n"+generateResponse(p,temperature=t,maxToken=512))
        time.sleep(1)

    print("\n\nPart 3: Your Own Instruction Prompt")
    custom=input("Enter Your Instruction Based Prompt: ").strip()
    try:
        temp=float(input("Set A Temperature Between 0.1-1.0: ").strip())
        if temp>=0.1 and temp <=0.1:
            raise ValueError
    except ValueError:
        print("Invaid Input Temperature, Using 0.7")
        temp=0.7
    print(f"\n--Your Prompt; {custom}, at temperature; {temp}--")
    print(generateResponse(custom,temperature=temp,maxToken=512))
def puesdoStream(text,delay=0.03):
    for c in text:
        print(c,end="",flush=True)
        time.sleep(delay)
    print("")
def bonusStream():
    choice=input("\nBonus Streaming Like Output (y/n): ").lower().strip()
    if choice=="y":
        p=input("Enter a Prompt: ").strip()
        out=generateResponse(p,temperature=0,maxToken=512)
        print("\nStreaming Like Responce (Not Real Streaming)")
        puesdoStream(out)
bonusStream()
#temperaturePromptActivity()