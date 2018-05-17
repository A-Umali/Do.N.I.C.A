import re
import random

WORDS = ['SEAN', 'QUOTE']


def handle(text):
    messages = ['If you need toes, look at your feet.',
                'That is horrible',
                'Meeya, I don' + "'" + 't like that',
                'What do you do? You eat llamas of course.']
    message = random.choice(messages)
    return message


def is_valid(text):
    return bool(re.search(r'\b(sean|quote|tell|say)\b', text, re.I))