import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import grpc
import argparse
from user_recog import listen_mic, record_mic

"""This is Google's Cloud Speech API for reference because"""
"""it streamlines speech to text smoothly and has a more"""
"""success rate from other API sources"""

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="service_account.json"
resume = False


# Handling long codes into this file
def donica():
    language_code = 'en-US'

    client = speech.SpeechClient()
    config = types.cloud_speech_pb2.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=record_mic.RATE,
        language_code=language_code,
        max_alternatives=1,
        enable_word_time_offsets=True)
    streaming_config = types.cloud_speech_pb2.StreamingRecognitionConfig(config=config, interim_results=True)

    # Have to be online to use this service and connected to Google Account
    # Might make another one for offline mode

    mic_manager = record_mic.MicrophoneStream(record_mic.RATE, int(record_mic.RATE / 10))

    # Pause
    with mic_manager as stream:
        while True:
            audio_generator = stream.generator()
            requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)
            # Now, you can speak
            responses = client.streaming_recognize(streaming_config, requests)
            try:
                print("talk")
                # Loop to access Donica
                listen_mic.listen_print_loop(responses)
                break
            except grpc.RpcError as e:
                if e.code() not in (grpc.StatusCode.INVALID_ARGUMENT, grpc.StatusCode.OUT_OF_RANGE):
                    raise
                details = e.details()
                if e.code() is grpc.StatusCode.INVALID_ARGUMENT:
                    if 'deadline too short' not in details:
                        raise
                else:
                    if 'maximum allowed stream duration' not in details:
                        raise
                print('Resuming')


if __name__ == '__main__':
    donica()
