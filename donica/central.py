import os
import pyaudio
import struct
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
import logging
from donica.transcribe_mic import MicrophoneStream
from donica.text_results import TextResult
from donica.configuration import Config
from donica.porcupine.binding.python.porcupine import Porcupine
from donica.encode_speech import Speech


class Central:
    def __init__(self):
        logging.debug('Initializing first local variables')
        self.c = Config()
        """ Google's Cloud Speech """
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath('service_account.json')
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
        self.text_result = TextResult()
        self.speech = Speech()
        self.active_status = False
        self.sleep_status = True
        self.speech_active = False
        self.picovoice_lib_path = None
        self.picovoice_model_path = None
        self.picovoice_hotword = None

    def initiate(self):
        self.check_device()
        porcupine = Porcupine(self.picovoice_lib_path, self.picovoice_model_path, self.picovoice_hotword, 0.5)
        """ Main loop for the entire program """
        while True:
            while self.sleep_status == True:
                pa = pyaudio.PyAudio()
                audio_stream = pa.open(
                    rate=porcupine.sample_rate,
                    channels=1,
                    format=pyaudio.paInt16,
                    input=True,
                    frames_per_buffer=porcupine.frame_length)

                pcm = audio_stream.read(porcupine.frame_length)
                pcm = struct.unpack_from('h' * porcupine.frame_length, pcm)

                result = porcupine.process(pcm)
                if result:
                    print('Found word: {}'.format(result))
                    self.sleep_status = False
                    self.active_status = True
                    break
                else:
                    pass
            while self.sleep_status == False and self.active_status == True:
                if self.speech is False:
                    print()
                mic_manager = MicrophoneStream(MicrophoneStream.RATE, int(MicrophoneStream.RATE / 10))
                try:
                    with mic_manager as stream:
                        mic_generator = stream.generator()
                        requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                                    for content in mic_generator)
                        responses = self.google_speech_client.streaming_recognize(self.google_stream_config,
                                                                                  requests, timeout=55)
                        self.text_result.get_text_to_speech_google(responses, stream)
                        if stream.closed == True:
                            self.sleep_status = True
                            self.active_status = False
                # Really bad way to grab deadline from grpc but works enough
                # where the while loop resets to the hotword
                except Exception as e:
                    logging.error('Protocol error: {}'.format(e))
                    self.sleep_status = True
                    self.active_status = False
                    break

            while self.sleep_status == False and self.active_status == False:
                print('Speech talking')

    def check_device(self):
        if self.c.device_type == 'win32':
            self.picovoice_lib_path = os.path.abspath('donica/porcupine/lib/windows/amd64/libpv_porcupine.dll')
            self.picovoice_model_path = os.path.abspath('donica/porcupine/lib/common/porcupine_params.pv')
            self.picovoice_hotword = os.path.abspath('donica_windows.ppn')
            logging.debug('Launched Windows version')
            return self.picovoice_lib_path, self.picovoice_model_path, self.picovoice_hotword

        if self.c.device_type == 'xdg-open':
            logging.debug('Linux')
            return None

        if self.c.device_type == 'darwin':
            logging.debug('MacOS')
            return None

