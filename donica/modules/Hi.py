import re


WORDS = ['HI|HELLO']


def handle(text):
    if re.search(r'\b(Hi)\b', text, re.I):
        return 'Detects hi'
    else:
        return 'Detects another word'


def is_valid(text):
    return bool(re.search(r'\b(HI|HELLO)\b', text, re.I))