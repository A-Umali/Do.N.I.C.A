import re
import sys

WORDS = ['THANK YOU', 'STOP', 'GOOD BYE', 'SHUT UP']


def handle(text):
    message = 'Turning off'
    return message


def is_valid(text):
    return bool(re.search(r'\b(thank you|stop|good bye|shut up)\b', text, re.I))



