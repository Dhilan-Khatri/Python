import random
import pyttsx3
engine = pyttsx3.init()
engine.setProperty("rate", 100)
engine.setProperty("volume", 0.7)
def speak(text, lang="en"):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    voices=engine.getProperty("voices")
    if lang=="en":
        engine.setProperty("voice",voices[0].id)
    else:
        engine.setProperty("voice",voices[1].id)
    engine.say(text)
    engine.runAndWait()
def get_samples():
    return [
        "Suzie sells sixty-six salty, sizzling sausages by the seashore.",
        "Peter Piper picked a peck of perfectly pickled peppers.",
        "Testing, testing.",
        "Is this the real life? Is this just fantasy?",
        "Pop, pop, popsicle. Ice, ice, icicle.",
        "Red leather, yellow leather, purple leather.",
        "These pretzels are making me thirsty.",
        "This is an announcement, Thank you very much.",
        "Mic check."
    ]
def main():
    print("Welcome to Ai Voice")
    speak("Type something for me to say.")
    while True:
        user_input = input("User: ").strip().lower()
        if user_input == "exit":
            speak("Goodbye.")
            break
        elif user_input == "sample":
            phrase = random.choice(get_samples())
            print(f"{phrase}")
            speak(phrase)
        elif user_input == "speed up":
            speed = engine.getProperty("rate") +25
            engine.setProperty("rate", speed)
            speak("Speaking faster by 25.")
        elif user_input == "slow down":
            speed = engine.getProperty("rate") -25
            engine.setProperty("rate", speed)
            speak("Speaking slower by 25.")
        elif user_input == "increase volume":
            volume = engine.getProperty("volume") +0.1
            volume = min(1.0, volume)
            engine.setProperty("volume", volume)
            speak("Volume increased.")
        elif user_input == "decrease volume":
            volume = engine.getProperty("volume") -0.1
            volume = max(0.0, volume)
            engine.setProperty("volume", volume)
            speak("Volume decreased.")
        elif user_input == "tell a joke":
            jokes = [
                "Why did the chicken cross the playground: To get to the other slide.",
                "Why did the cake cross the road: It saw a fork up ahead.",
                "What do you call a boomerang that won't come back: A stick.",
                "What did the pirate say on his birthday: 'Aye, matey!'"
                "Why don't astronauts like gravity: It brings them down."
                "What do you call a fly without wings: A walk."
                "What's the easiest building to lift: A lighthouse."
                "Why are most people tired on April 1: They've just finished a 31-day March."
            ]
            joke = random.choice(jokes)
            print(f"{joke}")
            speak(joke)
        elif user_input:
            speak(user_input)
        else:
            print("Type 'sample' to get a pre-existing sentence, 'tell a joke' to get a dad joke, or 'exit' to exit the program.")
            speak("I didn’t quite catch that. Try again!")
main()