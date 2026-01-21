print("Hello! I am an AI bot ready to assist you ")
name = input("What is your name? ")
print(f"\nHello {name}! How are you feeling today?")
mood = input("good / great / okay / bad ").lower()
if mood == "good" or "great":
    print("That's awesome to hear! ")
    print("What made your day so good?")
    reason = input()
    print("That’s great! Enjoy your free time ")
elif mood == "okay":
    print("Just okay, huh? ")
    print("Is there something you'd like to improve about your day?")
    improve = input()
    print("That makes sense.")
    print("Do you want motivation or help with something specific?")
    choice = input("motivation / help ").lower()
    if choice == "motivation":
        print("You’re doing better than you think — keep going ")
    else:
        print("Alright! Tell me what you need help with.")
elif mood == "bad":
    print("I'm sorry to hear that ")
        print("That’s okay. I’m here whenever you need me.")
else:
    print("I may not fully understand, but I'm here to help ")
print("\nBefore you go, one last question:")
hobby = input("What is something you enjoy doing? ")
print("That sounds fun! Keep doing what makes you happy ")
print(f"It was great talking to you, {name}! Have an amazing day! ")
