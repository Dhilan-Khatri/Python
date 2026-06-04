import speech_recognition as sr
import pyttsx3 
from datetime import datetime
def speak(text):
    engine=pyttsx3.init()
    engine.setProperty("rate",150)
    engine.say(text)
    engine.runAndWait()
def getAudio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Now.")
        audio=r.listen(source)
        try:
            command=r.recognize_google(audio)
            print(f"You Said, {command}.")
            return command.lower()
        except sr.UnknownValueError:
            print("Could Not Recognize Speach.")
        except sr.RequestError as p:
            print(f"API Error: '{p}'.")
    return ""
def responseToCommand(command):
    if "hello" in command:
        speak("Hello, How Can I Help You Today?")
    elif "your name" in command:
        speak("I Am Your Voice Assistance.")
    elif "date" in command:
        currentDate=datetime.now().date()
        print(currentDate)
        speak(f"The Date Currently Is {currentDate}")
    elif "time" in command:
        currentTime=datetime.now().strftime("%H:%M")
        print(currentTime)
        speak(f"The Time Currently is {currentTime}.")
    elif "exit" in command:
        speak("Okay Good Bye. Now Exiting.")
    else:
        speak("I Am Not Sure How I Can Help With That")
def main():
    speak("Voice Assistance Acivated, Say How I Can Help You.")
    go=True
    while go:
        command=getAudio()
        responseToCommand(command)
        if "exit" in command:
            break
main()