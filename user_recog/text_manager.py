import Configure
from user_recog.mic_listen import ListenLoop
import grpc


class TextManager:
    def __init__(self):
        # self.text_recognizer = TextRecognizer(
        self.c = Configure

    def get_text_to_speech_google(self, text):
        try:
            print("talk")
            # text_rec
            ListenLoop.listen_print_loop(self, text)
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
