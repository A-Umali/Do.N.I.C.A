import re

WORDS = ['MEANING', "OF", "LIFE"]


def handle(text):
    return 'Meaning of Life is Pi'


def is_valid(text):
    return bool(re.search(r'\b(meaning|of|life)\b', text, re.IGNORECASE))
