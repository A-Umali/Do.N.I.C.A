import boto3
import os
from tempfile import gettempdir
import pygame
import random
import time
import sys


class Speech(object):
    def __init__(self):
        self.session = boto3.Session(profile_name="AUmali")
        self.polly = self.session.client("polly")

    def send_speak(self, text):

        r1 = random.randint(1, 10000000)
        spoken_text = self.polly.synthesize_speech(Text=text,
                                                   OutputFormat="mp3",
                                                   VoiceId="Amy")
        try:
            # This is a short fix, should make another one later
            output = os.path.join(gettempdir(), str(r1) + 'output.mp3')
            with open(output, 'wb') as f:
                f.write(spoken_text['AudioStream'].read())
                f.close()
            pygame.mixer.init()
            pygame.mixer.music.load(output)
            pygame.mixer.music.play()


        except PermissionError as e:
            print(e)

    @staticmethod
    def speech_active():
        while pygame.mixer.get_busy() == True:
            print('talking')
        pass
"""
    @staticmethod
    def test_wait(file):
        audio_file = eyed3.load(file)
        wait_period = audio_file.info.time_secs
        time.sleep(wait_period+2)
"""