import threading, sys, time, wave
import pyaudio, numpy as np, matplotlib.pyplot as plt
import speech_recognition as sr
from speech_recognition import AudioData
stop_event = threading.Event()
def wait():
    input("\nPress Enter To Stop Recording Audio.\n")
    stop_event.set()
def spinner():
    chars = "|/-\\"
    x = 0
    while not stop_event.is_set():
        sys.stdout.write("\rRecording Started: " + chars[x % len(chars)])
        sys.stdout.flush()
        x += 1
        time.sleep(0.1)
    sys.stdout.write("\rRecording Finished.\n")
def record():
    rate, fmt, buf = 16000, pyaudio.paInt16, 1024
    p = pyaudio.PyAudio()
    stream = p.open(format=fmt, channels=1, rate=rate, input=True, frames_per_buffer=buf)
    frames = []
    threading.Thread(target=wait).start()
    threading.Thread(target=spinner).start()
    while not stop_event.is_set():
        frames.append(stream.read(buf))
    stream.stop_stream(); stream.close(); width = p.get_sample_size(fmt); p.terminate()
    return b"".join(frames), rate, width
def save_wav(data, rate, width, name="speech.wav"):
    with wave.open(name, "wb") as wf:
        wf.setnchannels(1); wf.setsampwidth(width); wf.setframerate(rate); wf.writeframes(data)
    print(f"Audio saved → {name}")
def transcribe(data, rate, width, name="speech.txt"):
    recog = sr.Recognizer()
    audio = AudioData(data, rate, width)
    try:
        text = recog.recognize_google(audio)
    except sr.UnknownValueError:
        text = "Could Not Understand Audio."
    except sr.RequestError as e:
        text = f"API Error: {e}"
    print("Text:", text)
    with open(name, "w") as f: f.write(text)
    print(f"Text Saved: {name}")
def plot(data, rate):
    samples = np.frombuffer(data, dtype=np.int16)
    t = np.linspace(0, len(samples)/rate, num=len(samples))
    plt.plot(t, samples)
    plt.title("Voice Wave")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()
def main():
    print("Start speaking...")
    audio, rate, width = record()
    save_wav(audio, rate, width)
    transcribe(audio, rate, width)
    plot(audio, rate)
main()