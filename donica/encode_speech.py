import boto3
import os
import pygame
import random
from contextlib import closing
import sys
import time
import subprocess
import platform


class Speech(object):
    def __init__(self):
        self.session = boto3.Session(profile_name="AUmali")
        self.polly = self.session.client("polly")

    def send_speak(self, text):

        r1 = random.randint(1, 10000000)
        spoken_text = self.polly.synthesize_speech(Text=text,
                                                   OutputFormat="ogg_vorbis",
                                                   VoiceId="Amy")
        try:
            output = os.path.abspath('output.ogg')
            if 'AudioStream' in spoken_text:
                with closing(spoken_text['AudioStream']) as stream:
                    try:
                        with open(output, 'wb') as f:
                            f.write(stream.read())
                    except IOError:
                        sys.exit(0)
                        raise e

            else:
                print('Could not stream audio')
                sys.exit(0)
            if platform.system() == "Windows":
                os.startfile(output)
            """
            pygame.mixer.init()
            pygame.mixer.music.load(output)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                print('logging')
                pass
            pygame.mixer.quit()
            time.sleep(2)
            os.remove(output)
            """
        except PermissionError:
            sys.exit(0)

