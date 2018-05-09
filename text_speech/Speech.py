import boto3
import os
import mad
import tempfile as tf
import subprocess
import wave
from tempfile import gettempdir



def speak(text):
    session = boto3.Session(profile_name="AUmali")
    polly = session.client("polly")

    spoken_text = polly.synthesize_speech(Text=text,
                                          OutputFormat="mp3",
                                          VoiceId="Amy")
    try:
        output = os.path.join(gettempdir(), 'output.mp3')
        with open(output, 'wb') as f:
            f.write(spoken_text['AudioStream'].read())
            f.close()

        os.system(output)

    except PermissionError as e:
        print(e)


