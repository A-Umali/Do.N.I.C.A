import speech_recognition as sr
from gtts import gTTS
import os
import Commands as cog


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Recording Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Donica is prepared")
        audio = r.listen(source)
    # Speech Recognition using Google Speeche Recognizer
    data = " "
    try:
        # Uses default API
        print("debug")
        data = r.recognize_google(audio)
        print("You said: " + data)
        exitProtocol(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition couldn't recognize what you said")

def beginProtocol(data):
    if data in str(cog.COGNATE_DONICA):
        recordAudio()

def exitProtocol(data):
    variation = str(cog.COGNATE_EXIT) + " " + str(cog.COGNATE_DONICA)
    if data in str(cog.COGNATE_EXIT) or data in variation:
        print("Donica is shutting down")
        exit()


recordAudio()