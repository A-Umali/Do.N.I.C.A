import boto3
import os
from tempfile import gettempdir
from pygame import mixer
import random


class Speech:
    def __init__(self, events):
        print("Text To Speech: Amazon Initialized")
        self.events = events

    @staticmethod
    def speak(text):
        session = boto3.Session(profile_name="AUmali")
        polly = session.client("polly")

        r1 = random.randint(1, 10000000)
        r2 = random.randint(1, 10000000)
        spoken_text = polly.synthesize_speech(Text=text,
                                                   OutputFormat="mp3",
                                                   VoiceId="Amy")
        try:
            # This is a short fix, should make another one later
            output = os.path.join(gettempdir(), str(r1) + str(r2) + 'output.mp3')
            with open(output, 'wb') as f:
                f.write(spoken_text['AudioStream'].read())
                f.close()

            mixer.init()
            mixer.pause()
            mixer.music.load(output)
            mixer.music.play()

        except PermissionError as e:
            print(e)

