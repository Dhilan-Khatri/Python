
print("Hello, I am A Ai bot ready to assist you. What is your name?")
name = input()
print(f"Hello {name}, how are you doing today?")
mood=input()
if mood.lower() == "good" or "great":
    print("I am happy to hear that.")
elif mood.lower() == "bad":
    print("Oh, no. What happenen?")
else:
    print("I understand, how can I help you today?")