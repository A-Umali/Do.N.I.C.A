import boto3
import os
import pygame
import random
from contextlib import closing
import sys
import time
import subprocess
import platform
from playsound import playsound


class Speech(object):
    def __init__(self):
        self.session = boto3.Session(profile_name="AUmali")
        self.polly = self.session.client("polly")

    def send_speak(self, text):
        # ogg_vorbis
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
                            f.close()
                    except IOError:
                        sys.exit(0)
                        raise e

            else:
                print('Could not stream audio')
                sys.exit(0)


            pygame.mixer.init()
            pygame.mixer.music.load(output)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy() == True:
                print('Looping')
            pygame.mixer.stop()
            pygame.mixer.quit()
            pygame.quit()
            time.sleep(2)
            self.remove_file(dir=output)
        except Exception as e:
            raise e

    @staticmethod
    def remove_file(dir, retries=3000, sleep=3):
        for i in range(retries):
            print(i)
            try:
                os.remove(dir)
                print('Removed')
            except WindowsError:
                time.sleep(sleep)
                print('Trying again')
            if not os.path.exists(os.path.abspath(dir)):
                break
            else:
                pass
