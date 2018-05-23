import os
import pyaudio
import struct
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from donica.transcribe_mic import MicrophoneStream
from donica.text_results import TextResult
from donica.configuration import Config
from donica.porcupine.binding.python.porcupine import Porcupine


class Central:
    active_status = True

    def __init__(self):
        print('Initializing first local variables')
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
                                                                                      interim_results=True,
                                                                                      single_utterance=True)
        self.text_result = TextResult()
        self.active_status = False
        self.sleep_status = True

    def initiate(self):
        picovoice_lib_path = os.path.abspath('donica/porcupine/lib/windows/amd64/libpv_porcupine.dll')
        picovoice_model_path = os.path.abspath('donica/porcupine/lib/common/porcupine_params.pv')
        picovoice_hotword = os.path.abspath('donica_windows.ppn')
        porcupine = Porcupine(picovoice_lib_path, picovoice_model_path, picovoice_hotword, 0.3)
        """ Main loop for the entire program """
        while True:
            while self.active_status == False:
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
                mic_manager = MicrophoneStream(MicrophoneStream.RATE, int(MicrophoneStream.RATE / 10))
                with mic_manager as stream:
                    mic_generator = stream.generator()
                    requests = (types.cloud_speech_pb2.StreamingRecognizeRequest(audio_content=content)
                                for content in mic_generator)
                    responses = self.google_speech_client.streaming_recognize(self.google_stream_config,
                                                                              requests)
                    self.text_result.get_text_to_speech_google(responses, stream)
                    if stream.closed == True:
                        self.sleep_status = True
                        self.active_status = False
                        print('Reset the status')
            while self.sleep_status == False and self.active_status == False:
                print('Speech talking')
