from gloq import generateResponse

def promptEngineering():
    print("Welcome To Prompt Engineering")
    vague=input("Enter A Vauge Prompt: ")
    print("AI responce to vauge prompt is...")
    print(generateResponse(vague))
    print(40*"=")
    specific=input("Enter A Specific Prompt: ")
    print("AI responce to specific prompt is...")
    print(generateResponse(specific))
    print(40*"=")
    context=input("Enter A Context Prompt: ")
    print("AI responce to context prompt is...")
    print(generateResponse(context))

promptEngineering()