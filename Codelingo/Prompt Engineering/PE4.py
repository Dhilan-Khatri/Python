from groq import generateResponse
import sys 

try:
    sys.stdout.reconfigure(encoding="utf-8")
except:
    pass
def reenforcementLearning():
    print(40*"=")
    print("Reenforcement Learning Activity")
    print(40*"=")
    prompt=input("Enter a Prompt for a Ai Model (Ex: 'Explain a Lime'): ").strip()
    if not prompt:
        print("Please Enter A Prompt To Continue.")
        return
    response1=generateResponse(prompt, temperature=0.7, maxToken=512)
    print(f"Intial Ai Response: {response1}")
    try:
        rating=int(input("Rate The Response From 1 (Bad) To 5 (Good): ").strip())
        if rating <1 or rating >5:
            print("Invaild Rating, using 3 as default.")
            rating=3
    except ValueError:
        print("Invaild Rating, using 3 as default.")
        rating=3
    feedback=input("Please Provide FeedBack For The Ai Model: ").strip()
    improvedResponse=f"{response1} (Improve With Your FeedBack: {feedback})."
    print(f"\nYour Improved Ai Response: {improvedResponse}")
def roleBasedPrompt():
    print(40*"=")
    print("Role-Based Prompt Activity")
    print(40*"=")
    category=input("Enter a category (Math,Space,History): ").strip()
    item=input(f"Enter a specfic part of {category} (Science:Photosynthisis): ").strip()
    if not category or not item:
        print("Please Enter A Category Or Item To Proceed.")
        return
    teachPrompt=f"You Are A Teacher Explaing {item} from {category} in simple terms."
    expertPrompt=f"Your are a expert in {category}. Explaing {item} in a technical manor."
    teachResponse=generateResponse(teachPrompt, temperature=0.3, maxToken=1024)
    expertResponse=generateResponse(expertPrompt, temperature=0.3, maxToken=1024)
    print(f"\nTeacher-Like Response: \n{teachResponse}")
    print(f"\nExpert-Like Response: \n{expertResponse}")
def main():
    print("Welcome To ReEnforcement Learning and Role-Based Prompt Activities.")
    while True:
        print("Would you like to go to ReEnforcement Learning(1), or Role-Based Prompt(2)")
        choice=int(input("Please Enter Your Choice (1/2): ").strip())
        if choice <1 or choice>2:
            print("Invaild Choice, Please Enter A 1 or 2.")
        elif choice==1:
            reenforcementLearning()
        else:
            roleBasedPrompt()
        choice2=input("Do Your Want To Continue (y/n): ").strip().lower()
        if choice2=="y":
            continue
        else:
            break
main()