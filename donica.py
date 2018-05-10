import os
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import grpc
from Configure import config
from user_recog.mic_record import MicrophoneStream
from user_recog.mic_listen import ListenLoop
import speech_recognition as sr
from event.event_dispatch import EventDispatcher
from Assistant import Assistant


class Donica:
    def __init__(self):
        self.status = False
        self.active = False
        self.events = EventDispatcher()
        self.c = config

        """ This is google's cloud speech API being in use """
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
        language_code = 'en-US'
        self.google_speech_client = speech.SpeechClient()
        self.google_config = types.cloud_speech_pb2.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=MicrophoneStream.RATE,
            language_code=language_code,
            max_alternatives=1,
            enable_word_time_offsets=True)
        self.google_stream_config = types.cloud_speech_pb2.StreamingRecognitionConfig(config=self.google_config,
                                                                                      interim_results=True)

    def initiate(self):
        print('Donica is loading up, wait for another print line')
        # Put check update method here
        if self.c.config.getboolean("SYSTEM", "wake_up_engine"):
            self.status = False
            self.active = False
        if self.c.config.getboolean("SYSTEM", "always_on_engine"):
            self.status = False
            self.active = False

        # Have to be online to use this service and connected to Google Account
        # Might make another one for offline mode

        mic_manager = MicrophoneStream(MicrophoneStream.RATE, int(MicrophoneStream.RATE / 10))
        r = sr.Recognizer()
        assistant_online = Assistant(mic_manager, self.events)
        assistant_offline = r.listen()
        # Will put a pause on this when not active
        with mic_manager as stream:
            audio_generator = stream.generator()
            requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)
            # Now, you can speak
            responses = self.google_speech_client.streaming_recognize(self.google_stream_config, requests)
            assistant_online.main(self, responses)


if __name__ == '__main__':
    Donica().initiate()
