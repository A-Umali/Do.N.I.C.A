import speech_recognition as sr
from gtts import gTTS
import os
import webbrowser
import smtplib


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
#listens for commands

def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Donica is ready!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command + "\n")

    #looping back to listen to commands

    except sr.UnknownValueError:
        return command
