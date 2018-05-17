import re


class BaseModule:
    def __init__(self, word):
        self.word = word

    def find_word(self, text):
        new_text = r'\b(%s)\b' % text
        return new_text
