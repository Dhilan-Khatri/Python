from groq import generateResponse

def getEssayDetails():
    print(70*"=")
    print("AI Writing Asistance")
    print(70*"=")
    topic=input("What is your topic: ").strip()
    lengths=["300 Words", "600 Words", "900 Words", "1200 Words", "1500 Words", "1800 Words"]
    essayType=input("What type of essay: ").strip()
    print("Select Word Count")
    for i,l in enumerate(lengths,1):
        print(f"{i}. {l}")
    try:
        index=int(input(">").strip())
        length=lengths[index-1]
        if 1<=index<=len(lengths):
            length=lengths[index-1]
        else:
            length="300 Words"
    except ValueError:
        length="300 Words"
    targetAudience=input("What is your Targer Audience (High School Students): ").strip()
    return {"topic":topic,"essay_Type":essayType,"length":length,"target_Audience":targetAudience}
def generateEssayContent(details):
    try:
        print(70*"=")
        temp=float(input("What Temperature (0.1-Structered, 0.7-Creative): ").strip())
        if not (0.0<=temp<=0.7):
            raise ValueError
    except ValueError:
        print("Invaild Temperature, Using 0.3")
        temp=0.3
    prompt=f"Write a Introduction for an {details["essay_Type"]} essay about {details["topic"]} on the length of {details["length"]}"
    introResponse=generateResponse(prompt=prompt,temperature=temp, maxToken=1024)
    print(70*"=")
    print(f"Introduction Ai Response:\n{introResponse}")
    print(70*"=")
    print("Would You Like a full draft or a step by step?")
    choice=int(input("1. Full Draft\n2. Step by Step: "))
    if choice==1:
        body=f"Write a full body for an essay on {details["topic"]}, with the stance of {details["target_Audience"]}"
        bodyResponse=generateResponse(prompt=body,temperature=temp, maxToken=1024)
        print(70*"=")
        print(f"Full Body AI Response:\n{bodyResponse}")
        print(70*"=")
    else:
        step=f"Write a step by step arguement for an essay on {details["topic"]}, provide and reasoning."
        stepResponse=generateResponse(prompt=step,temperature=temp,maxToken=1024)
        print(70*"=")
        print(f"Step by Step AI Response:\n{stepResponse}")
        print(70*"=")
    con=f"Write a conculsion for a {details["essay_Type"]}, about {details["topic"]} with the stance of {details["target_Audience"]}"
    conResponse=generateResponse(prompt=con, temperature=temp, maxToken=1024)
    print(70*"=")
    print(f"Conculsion AI Response:\n{conResponse}")
    print(70*"=")
def feedbackRefinement():
    rating=int(input("Rate the esssay on a scale of 1-5: "))
    if not rating: rating=3
    if rating !=5:
        feedback=input("Enter your feedback on the essay: ")
        print("Thank You For Providing Feeback.")
    else:
        print("Thank You!")
def main():
    print("Welcome To The AI Writng Assistance!")
    details=getEssayDetails()
    print(details)
    if not details["topic"] or not details["essay_Type"]:
        print("Please Enter At Least a Topic and A Essay Type to continue.")
        return
    generateEssayContent(details)
    feedbackRefinement()
main()