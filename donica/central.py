import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from donica.transcribe_mic import MicrophoneStream
from donica.text_results import TextResult
from donica.configuration import Config


class Central:

    active_status = True

    def __init__(self):
        print('Initializing first local variables')
        self.c = Config()
        """ Google's Cloud Speech """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/Redd/Downloads/service_account.json"
        self.google_speech_client = speech.SpeechClient()
        self.google_config = types.cloud_speech_pb2.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=MicrophoneStream.RATE,
            language_code='en-US',
            max_alternatives=1,
            profanity_filter=False,
            enable_word_time_offsets=True)
        self.google_stream_config = types.cloud_speech_pb2.StreamingRecognitionConfig(config=self.google_config,
                                                                                      interim_results=True)

    def initiate(self):
        mic_manager = MicrophoneStream(MicrophoneStream.RATE, int(MicrophoneStream.RATE / 10))
        with mic_manager as stream:
            while True:
                if self.active_status is True:
                    mic_generator = stream.generator()
                    requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                                for content in mic_generator)
                    responses = self.google_speech_client.streaming_recognize(self.google_stream_config,
                                                                              requests)
                    TextResult().get_text_to_speech_google(responses, stream)
                    self.active_status = False
                    print('CLOSED')
                else:
                    print('WAKING UP')
                    self.active_status = True
