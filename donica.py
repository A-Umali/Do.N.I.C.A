import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from transcribe_mic import MicrophoneStream
import text_results
import sys


class Donica:
    def __init__(self):
        self.sleep_status = True
        self.active_status = False
        """ This is google's cloud speech API being in use """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
        self.google_speech_client = speech.SpeechClient()
        self.google_config = types.cloud_speech_pb2.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=MicrophoneStream.RATE,
            language_code='en-US',
            max_alternatives=1,
            enable_word_time_offsets=True)
        self.google_stream_config = types.cloud_speech_pb2.StreamingRecognitionConfig(config=self.google_config,
                                                                                      interim_results=True)

    def initiate(self):
        print('Donica is loading up, wait for another print line')
        # Put check update method here

        # Have to be online to use this service and connected to Google Account
        # Might make another one for offline mode
        mic_manager = MicrophoneStream(MicrophoneStream.RATE, int(MicrophoneStream.RATE / 10))

        # Will put a pause on this when not active
        with mic_manager as stream:
            while True:
                audio_generator = stream.generator()
                requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                            for content in audio_generator)
                # Now, you can speak
                responses = self.google_speech_client.streaming_recognize(self.google_stream_config, requests)
                text_results.get_text_to_speech_google(responses)


if __name__ == '__main__':
    Donica().initiate()
