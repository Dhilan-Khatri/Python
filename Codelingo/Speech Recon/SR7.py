import speech_recognition as sr
import pyttsx3
from datetime import datetime
import random
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak Now")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Could Not Recognize Speach.")
            speak("Could Not Recognize Speach.")
        except sr.RequestError as p:
            print(f"API Error: '{p}'.")
            speak(f"API Error: '{p}'.")
    return ""
def r2c(command,user):
    if "hello" in command:
        if user:
            speak(f"Hello {user}, how can I help")
        else:
            speak("Hi, how can I help?")
    elif "your name" in command:
        speak("I am your Voice Assistant.")
    elif "time" in command:
        now = datetime.now().strftime("%H:%M")
        speak(f"Current Time: {now}")
    elif "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today: {today}")
    elif "my name is" in command:
        user = command.split("my name is")[-1].strip().capitalize()
        speak(f"Nice to meet you, {user}!")
    elif "fact" in command:
        facts = [
            "A day on Venus is longer than a year on Venus due to its slow rotation.",
            "Neutron stars are so dense that a sugar-cube-sized amount would weigh about as much as all of humanity.",
            "There are more stars in the universe than grains of sand on all the Earth's beaches combined.",
            "The footprints left by astronauts on the Moon will remain for millions of years due to the lack of atmosphere.",
            "A single teaspoon of a black hole's material would weigh about 6 billion tons.",
            "Saturn could float in water because it is mostly made of gas and has a low density."]
        speak(random.choice(facts))
    elif "male" in command:
        engine.setProperty('voice', voices[0].id)
        speak("Switched to male voice.")
    elif "female" in command:
        engine.setProperty('voice', voices[1].id)
        speak("Switched to female voice.")
    elif "exit" in command:
        speak("Bye.")
    else:
        speak("I Can Not Help With That.")
def main():
    speak("Start Speaking")
    while True:
        command = getAudio()
        r2c(command)
        if "exit" in command:
            break
main()