import boto3
from pygame import mixer
import os

polly = boto3.client('polly')

def speak(text):
    spoken_text = polly.synthesize_speech(Text=text,
                                    OutputFormat='mp3',
                                    VoiceId='Amy')
    with open('output.mp3', 'wb') as f:
        f.write(spoken_text['AudioStream'].read())
        f.close()



