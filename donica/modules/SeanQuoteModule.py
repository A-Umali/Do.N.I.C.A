import re
import random
from donica.encode_speech import Speech

TITLE = ['SEAN-QUOTE']


def handle(message):
    text = ['If you need toes, look at your feet.',
            'What do you do? You should eat llamas of course.',
            'What happens if they are actually your mother.',
            'There is more papaya than nachos in the world.']
    get_text = random.choice(text)
    Speech().send_speak(get_text)


def is_valid(title):
    return bool(re.search('sean.quote', title, re.I))