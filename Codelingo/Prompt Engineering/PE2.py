from groq import generateResponse
import time

def temperaturePromptActivity():
    print(70*"=")
    puesdoStream("Advanced Prompt Engineering; Temperature + Instruction")
    print(70*"=")
    print(70*"-")
    puesdoStream("\nPart 1: Temperature Exploration")
    base=input("Enter a Creative Prompt: ").strip()
    for t,label in [(0.1,"Low (0.1)-Determind"),(0.5,"Medium (0.5)-Balanced"),(1,"High (1)-Creative")]:
        puesdoStream(f"----{label}----")
        puesdoStream(generateResponse(base,temperature=t,maxToken=512))
        time.sleep(1)
    print(70*"-")
    puesdoStream("\n\nPart 2: Instruction Based Prompts")
    topic=input("\nEnter a Topic (Climate, Space, Marine): ").strip()
    prompts=[
        f"Summerize Key Facts About {topic}, in 3 to 4 sentences.",
        f"Explain {topic}, as if i am a 10 year old child",
        f"Write a Pro and Con list about {topic}.",
        f"Create a fictional New Headline from 2050 about {topic}."
    ]
    for i,p in enumerate(prompts,1):
        puesdoStream(f"\n---Instruction: {i}---\n{p}")
        puesdoStream("\n"+generateResponse(p,temperature=t,maxToken=512))
        time.sleep(1)
    print(70*"-")
    puesdoStream("\n\nPart 3: Your Own Instruction Prompt")
    custom=input("Enter Your Instruction Based Prompt: ").strip()
    try:
        temp=float(input("Set A Temperature Between 0.1-1.0: ").strip())
        if temp>=0.1 and temp <=0.1:
            raise ValueError
    except ValueError:
        print("Invaid Input Temperature, Using 0.7")
        temp=0.7
    puesdoStream(f"\n--Your Prompt; {custom}, at temperature; {temp}--")
    puesdoStream(generateResponse(custom,temperature=temp,maxToken=512))
def puesdoStream(text,delay=0.02):
    for c in text:
        print(c,end="",flush=True)
        time.sleep(delay)
    print("")

temperaturePromptActivity()