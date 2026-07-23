from groq import generateResponse as GroqPrompt
from hf import generateResponse as HFPrompt
def EngineeringGroq():
    print("Testing Different Groq Prompts")
    vague=input("Enter A Vauge Prompt: ")
    print(f"AI responce to vauge prompt is... \n{GroqPrompt(vague)}")
    print(40*"=")
    specific=input("Enter A Specific Prompt: ")
    print(f"AI responce to specific prompt is... \n{GroqPrompt(specific)}")
    print(40*"=")
    context=input("Enter A Context Prompt: ")
    print(f"AI responce to context prompt is... \n{GroqPrompt(context)}")

def EngineeringHF():
    print("Testing Different Hugging Face Prompts")
    vague=input("Enter A Vauge Prompt: ")
    print(f"AI responce to vauge prompt is... \n{HFPrompt(vague)}")
    print(40*"=")
    specific=input("Enter A Specific Prompt: ")
    print(f"AI responce to specific prompt is... \n{HFPrompt(specific)}")
    print(40*"=")
    context=input("Enter A Context Prompt: ")
    print(f"AI responce to context prompt is... \n{HFPrompt(context)}")

print("Welcome to Prompt Engineering!")
def main():
    model=input("Would you like to try a Groq model or a Hugging Face model? (g/h), Or type 'exit' to exit: ").lower().strip()
    if model=="g":
        EngineeringGroq()
    elif model=="h":
        EngineeringHF()
    elif model=="exit":
        print("Goodbye, See you soon.")
        exit
    else:
        print("Please type 'g' for Groq, 'h' for Hugging Face, or 'exit' to exit.")

main()