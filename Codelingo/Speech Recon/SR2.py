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
def recordAudio(label):
    stopEvent.clear()
    p=pyaudio.PyAudio()
    stream=p.open(format=pyaudio.paInt16,channels=1,rate=16000,input=True,frames_per_buffer=1024)
    frames=[]
    print(label)
    threading.Thread(target=waitForEnter,daemon=True).start()
    threading.Thread(target=spinner,daemon=True).start()
    while not stopEvent.is_set():
        frames.append(stream.read(1024))
    print("Done.")
    stream.stop_stream()
    stream.close()
    width=p.get_sample_size(pyaudio.paInt16)
    p.terminate()
    return b''.join(frames),16000,width
def analyzeAudio(data,rate):
    samples=np.frombuffer(data,dtype=np.int16)
    return {
        "Duration":len(samples)/rate,
        "AverageVolume":np.mean(np.abs(samples)),
        "MaxVolume":np.max(np.abs(samples)),
        "Samples":samples
    }
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
        return text
    except sr.UnknownValueError as error:
        print("Could Not Understand Audio")
        return "Could Not Transcribe."
    except sr.RequestError as error:
        print(f"API Error: {error}")
        return "Could Not Transcribe."
def displayStats(stats,text,label):
    print("="*40)
    print(f"{label}")
    print("="*40)
    print(f"Duration: {stats["Duration"]:.2f} seconds")
    print(f"Average Volume: {stats["AverageVolume"]:.2f} ")
    print(f"Max Volume: {stats["MaxVolume"]:.2f} ")
    print(f"Transciption: {text}")
def compare(stats1,stats2):
    print("="*40)
    print("Comparason Results")
    print("="*40)
    if stats1["Duration"] > stats2["Duration"]:
        longer="Recording 1"
        difference=(( stats1["Duration"]- stats2["Duration"])/ stats2["Duration"])*100
    else:
        longer="Recording 2"
        difference=(( stats2["Duration"]- stats1["Duration"])/ stats1["Duration"])*100
    print(f"{longer} is longer by {difference:.1f}&")
    if stats1["AverageVolume"] > stats2["AverageVolume"]:
        louder="Recording 1"
        difference=(( stats1["AverageVolume"]- stats2["AverageVolume"])/ stats2["AverageVolume"])*100
    else:
        louder="Recording 2"
        difference=(( stats2["AverageVolume"]- stats1["AverageVolume"])/ stats1["AverageVolume"])*100
    print(f"{louder} is louder by {difference:.1f}&")
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
    print("Voice Analysis Lab")
    print("="*40)
    print("Record Twice and Compare Your Voice")
    audiodata,rate,width=recordAudio("Recording 1, Speak Normally.")
    saveAudio(audiodata,rate,width)
    stats1=analyzeAudio(audiodata,rate)
    text1=transcribe(audiodata,rate,width)
    displayStats(stats1,text1,"Recording 1 Result.")
    plotWavForm(audiodata,rate)
    audiodata2,rate,width=recordAudio("Recording 2, Speak Normally.")
    saveAudio(audiodata2,rate,width)
    stats2=analyzeAudio(audiodata2,rate)
    text2=transcribe(audiodata2,rate,width)
    displayStats(stats2,text2,"Recording 2 Result.")
    plotWavForm(audiodata2,rate)
    compare(stats1,stats2)
main()