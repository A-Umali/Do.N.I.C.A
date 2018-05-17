import boto3
import os
from tempfile import gettempdir
from pygame import mixer
import random


class Speech(object):
    def __init__(self):
        self.session = boto3.Session(profile_name="AUmali")
        self.polly = self.session.client("polly")

    def send_speak(self, text):

        r1 = random.randint(1, 10000000)
        r2 = random.randint(1, 10000000)
        spoken_text = self.polly.synthesize_speech(Text=text,
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
