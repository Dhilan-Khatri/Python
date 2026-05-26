import speech_recognition as sr
from speech_recognition import AudioData
import asyncio
import pyttsx3
from googletrans import Translator
def speak(text,language="en"):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    voices=engine.getProperty("voices")
    if language=="en":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()
def speak2Text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please Speak Now In English.")
        audio=recognizer.listen(source)
    try:
        print("Recognizing Speech.")
        text=recognizer.recognize_google(audio,language="en-US")
        print(f"You Said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could Not Understand Audio.")
    except sr.RequestError as e:
        print(f"API Error: {e}")
    return ""
async def translateASYNC(text,destination):
    translator=Translator()
    return await translator.translate(text,dest=destination)
def translateText(text,targetLanguage="es"):
    translation=asyncio.run(translateASYNC(text,targetLanguage))
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
def main():
    targetLanguage=displayLanguageOptions()
    orginalText=speak2Text()
    if orginalText:
        text=translateText(orginalText,targetLanguage=targetLanguage)
        speak(text,language="en")
        print("Translations Given Out.")
main()