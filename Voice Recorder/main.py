import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wav
import time

freq = 44100

duration = int(input("Please enter duration time : "))

print("Starting in 3 seconds")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Go")
recording = sd.rec( int(freq * duration), samplerate=freq, channels=2)
sd.wait()
filename = input("Please name your audio file without filename extentions : ")
write(f"{filename}.wav", freq, recording)