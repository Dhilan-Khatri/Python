import speech_recognition as sr
import asyncio
import pyttsx3
from googletrans import Translator
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
def s2t():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now In English")
        audio=recognizer.listen(source)
    try:
        print("Recognizing Speach.")
        text=recognizer.recognize_google(audio,language="en-US")
        print(f"You Said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could Not Understand Audio.")
    except sr.RequestError as e:
        print(f"API Error: '{e}'.")
    return ""
async def translateAsync(text,dest):
    translator=Translator()
    return await translator.translate(text,dest=dest)
def translateText(text,targetLang="es"):
    translation=asyncio.run(translateAsync(text,targetLang))
    print(f"Translated Text: {translation.text}")
    return translation.text
def displayLangOptions():
    print("Avaible Translation Options")
    print("International Languages:")
    print("1. Spanish (es)")
    print("2. French (fr)")
    print("3. German (de)")
    print("4. Russian (ru)")
    print("5. Chinese (zh-cn)")
    print("6. Hindi (hi)")
    print("7. Japanese (ja)")
    print("8. Korean(ko)")
    choice=input("Please Type The Selected Language Number: ")
    languageDictionary={
        "1":"es",
        "2":"fr",
        "3":"de",
        "4":"ru",
        "5":"zh-cn",
        "6":"hi",
        "7":"ja",
        "8":"ko"}
    return languageDictionary.get(choice,"en")
def main():
    targetLanguage=displayLangOptions()
    orginalText=s2t()
    if orginalText:
        transText=translateText(orginalText,targetLanguage)
        speak(transText,lang="en")
        print("Translations Spoken Out.")
main()