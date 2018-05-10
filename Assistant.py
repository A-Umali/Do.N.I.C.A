import Commander


class Assistant(Commander):
    def __init__(self, speech_recognition, events):
        super(Assistant, self).__init__(speech_recognition, events)

    def main(self, response):
        print('something')
