import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import Microphone
import Listening

"""This is Google's Cloud Speech API for reference because"""
"""it streamlines speech to text smoothly and has a more"""
"""success rate from other API sources"""

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"

# Handling long codes into this file
def donica():
    language_code = 'en-US'

    client = speech.SpeechClient()
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=Microphone.RATE,
        language_code=language_code)
    streaming_config = types.StreamingRecognitionConfig(
        config=config,
        interim_results=True)

    with Microphone.MicrophoneStream(Microphone.RATE, Microphone.CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.StreamingRecognizeRequest(audio_content=content)
                    for content in audio_generator)

        responses = client.streaming_recognize(streaming_config, requests)

        # Now, put the transcription responses to use.
        Listening.listen_print_loop(responses)

if __name__ == '__main__':
    donica()
