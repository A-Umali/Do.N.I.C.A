from Configure import config

class TextSorter:
    def __init__(self):
        self.raw_text_array = []
        self.sub_words = []
        self.key_words = []
        self.reserved_sub_words = self.get_reserved_sub_words()
        self.c = config

    def text_to_speech(self, text):
        print("Something")


