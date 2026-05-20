import threading #Used to run multiple tasks at same time
import sys #print text in same line repeatedly
import time #delays
import pyaudio #Access Microphone, Capture Live Audio, Read Sound Data
import numpy as np #Numeric Operations
import matplotlib.pyplot as plt #Make Graphs
import wave #Make .wav file
import speech_recognition as sr #Speech to Text
from speech_recognition import AudioData

stopEvent=threading.Event()
def waitForEnter():
    input(f"Press Enter To Stop Recording")
    stopEvent.set()
def spinner():
    chars='|/-\\'
    i=0
    while not stopEvent.is_set():
        sys.stdout.write(f"\r Recording... {chars  [i%4]}")
        sys.stdout.flush()
        i=i+1
        time.sleep(0.1)
    print("\r Recording Completed")
def recordAudio():
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=1024)
    frames=[]
    threading.Thread(target=waitForEnter,daemon=True).start()
    threading.Thread(target=spinner,daemon=True).start()
    while not stopEvent.is_set():
        frames.append(stream.read(1024))
    stream.stop_stream()
    stream.close()
    width=p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames),16000,width
def saveAudio(data,rate,width,filename="recording.wav"):
    with wave.open(filename,'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(width)
        wf.setframerate(rate)
        wf.writeframes(data)
    print(f"Save: {filename}")
def transcribe(data,rate,width):
    recogizer=sr.Recognizer()
    audio=AudioData(data,rate,width)
    try:
        text=recogizer.recognize_google(audio)
        print(f"Transcribtion: {text}")
    except sr.UnknownValueError as error:
        print("Could Not Understand Audio")
    except sr.RequestError as error:
        print(f"API Error: {error}")
def plotWavForm(data,rate):
    samples=np.frombuffer(data,dtype=np.int16)
    timeAxis=np.linspace(0,len(samples)/rate,len(samples))
    plt.figure(figsize=(10,4))
    plt.plot(timeAxis,samples,color="green")
    plt.title("Your Voice Wav Form")
    plt.xlabel("Time (Seconds)")
    plt.ylabel("Amplitude")
    plt.grid(True,alpha=0.3)
    plt.tight_layout()
    plt.show()
def main():
    print("="*40)
    print("Hello Ai Can You Hear Me?")
    print("="*40)
    print("Speak Into Your Microphone.")
    AudioData,rate,width=recordAudio()
    saveAudio(AudioData,rate,width)
    transcribe(AudioData,rate,width)
    plotWavForm(AudioData,rate)
main()
