import speech_recognition as sr
import pyttsx3
import asyncio
from googletrans import Translator
def speak(text, language= "en"):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    if voices:
        if language == "en":
            engine.setProperty("voice", voices[0].id)
        elif len(voices) > 1:
            engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()
def speech2text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak In English")
        audio = recognizer.listen(source)
    try:
        print("Recognizing Speech.")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could Not Understand Audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""
def translateText(text,targetLanguage="es"):
    translator=Translator()
    translation=translator.translate(text,dest=targetLanguage)
    print(f"Translated Text: {translation.text}")
    return translation.text
def displayLanguageOptions():
    print("Avaible Translation Languages: ")
    print("1. Hindi (hi)")
    print("2. Spanish (es)")
    print("3. Japanese (ja)")
    print("4. Korean (ko)")
    print("5. Portuguese (pt)")
    choice=input("Please Select The Target Language (1-5): ")
    languageDictionary={
        "1":"hi",
        "2":"es",
        "3":"ja",
        "4":"ko",
        "5":"pt"}
    return languageDictionary.get(choice,"en")
def translator():
    Name, Code = displayLanguageOptions()
    print(f"Target language selected: {Name} ({Code})")

    originalText = speech2text()
    if not originalText:
        return

    translation = translateText(originalText, Code)
    print("Speaking Translation.")
    speak(translation, language="en")
    print("Translation Finished.")

def main():
    print("Welcome To The AI Translator")
    while True:
        print("\n1. Start voice translation")
        print("2. Exit")
        choice = input("Choose a option: ").strip()
        if choice == "1":
            translator()
        elif choice == "2":
            print("Exiting translator")
            break
        else:
            print("Invaid Input Try Again")
main()