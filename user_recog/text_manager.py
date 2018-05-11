import Configure
import grpc
import sys
from user_recog.text_sorter import TextSorter


# Getting mic stream audio
class TextManager:
    def __init__(self):
        self.c = Configure

    @staticmethod
    def get_text_to_speech_google(responses):
        try:
            print("talk")
            # text_rec
            num_chars_printed = 0
            for response in responses:
                if not response.results:
                    continue

                result = response.results[0]
                if not result.alternatives:
                    continue

                transcript = result.alternatives[0].transcript
                overwrite_chars = ' ' * (num_chars_printed - len(transcript))

                if not result.is_final:
                    sys.stdout.write(transcript + overwrite_chars + '\r')
                    sys.stdout.flush()
                    num_chars_printed = len(transcript)
                else:
                    get_mic = transcript+overwrite_chars
                    TextSorter.analyze_speech(get_mic)
                    num_chars_printed = 0

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
