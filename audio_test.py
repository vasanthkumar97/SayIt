import pyaudio
import wave
import speech_recognition as sr
'''
working code for recording and getting text
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print "recording..."
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print "finished recording"

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()
r = sr.Recognizer()
with sr.WavFile("file.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    list = r.recognize_google(audio, show_all=True)                  # generate a list of possible transcriptions
    print("Possible transcriptions:")
    speech= list["alternative"][0]

    # for prediction in list:
    #     print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
    print speech['transcript']
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
'''
from nltk.tokenize import sent_tokenize
sent_tokenize_list = sent_tokenize('good morning have a nice day')
print sent_tokenize_list
