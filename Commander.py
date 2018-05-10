

class Commander:
    def __init__(self, stream, events):
        self.events = events
        self.mic_manager = stream

    def get_mic(self, source):
        mic = self.mic_manager
        return mic

    def get_text_to_speech_google(self, mic):
        text = self.audio_manager.get_text_from_speech(mic)

