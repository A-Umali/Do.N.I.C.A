import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from user_recog import Microphone, Listening

"""This is Google's Cloud Speech API for reference because"""
"""it streamlines speech to text smoothly and has a more"""
"""success rate from other API sources"""

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"


# Handling long codes into this file
def donica():
    language_code = 'en-US'

    client = speech.SpeechClient()
    config = types.cloud_speech_pb2.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=Microphone.RATE,
        language_code=language_code)
    streaming_config = types.cloud_speech_pb2.StreamingRecognitionConfig(config=config, interim_results=True)

    # Have to be online to use this service and connected to Google Account
    # Might make another one for offline mode
    # PAUSE
    with Microphone.MicrophoneStream(Microphone.RATE, Microphone.CHUNK) as stream:
        audio_generator = stream.generator()
        requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content) for content in audio_generator)
        # Now, you can speak
        responses = client.streaming_recognize(streaming_config, requests)
        print("talk")
        # Loop to access Donica
        Listening.listen_print_loop(responses)


if __name__ == '__main__':
    donica()
