import boto3
from botocore.exceptions import  BotoCoreError, ClientError
from pygame import mixer
import os
from tempfile import gettempdir
import sys
import gtts
from contextlib import closing
from django.conf import settings



def speak(text):
    session = boto3.Session(profile_name="AUmali")
    polly = session.client('polly')

    spoken_text = polly.synthesize_speech(Text=text,
                                          OutputFormat='mp3',
                                          VoiceId='Amy')
    try:
        output = os.path.join(gettempdir(), 'output.mp3')
        with open(output, 'wb') as f:
            f.write(spoken_text['AudioStream'].read())
            f.close()
    except PermissionError as e:
        print(e)


    mixer.init()
    mixer.music.load(output)
    mixer.music.play()
