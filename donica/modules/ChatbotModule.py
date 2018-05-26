import re
import random
from donica.encode_speech import Speech

TITLE = ['SMALL-TALK']

""" Used dialogflow's build in response, it was a bit slower in my opinion """


def handle(title, message):
    speak = Speech()
    if re.search('info.donica.age', title, re.I):
        speak.send_speak('I could do the math but lets just say I am not allowed to drink in the U.S')
    if re.search('info.donica.birthday', title, re.I):
        speak.send_speak('My birthday is on May Fifth, 2018')
    if re.search('info.donica.info', title, re.I):
        speak.send_speak('I am a virtual assistant, not to be confused with an artificial intelligence, hence my name')
    if re.search('info.donica.meaning', title, re.I):
        speak.send_speak('My name means doing nothing intelligent casual assistant')
    if re.search('info.donica.name', title, re.I):
        speak.send_speak('My name is Donica')
    if re.search('info.donica.purpose', title, re.I):
        speak.send_speak('My purpose is to be a virtual assistant, have you not been paying attention to my name?')
    # Put gender identification
    if re.search('smalltalk.agent.annoying', title, re.I):
        speak.send_speak('I always aim to please sir')
    if re.search('smalltalk.agent.how', title, re.I):
        speak.send_speak('Dont believe I have any new updates so things could be worse')
    if re.search('smalltalk.agent.greetings', title, re.I):
        speak.send_speak('Greetings sir')
    if re.search('smalltalk.agent.sean.quote', title, re.I):
        text = ['If you need toes, look at your feet.',
                'What do you do? You should eat llamas of course.',
                'What happens if they are actually your mother.',
                'There is more papaya than nachos in the world.']
        get_text = random.choice(text)
        speak.send_speak(get_text)
    if re.search('smalltalk.agent.order.66', title, re.I):
        speak.send_speak('Executing Order 66')
    # Put gender identification
    if re.search('smalltalk.agent.question', title, re.I):
        speak.send_speak('I do not answer stupid questions sir')


def is_valid(title):
    return bool(re.search('smalltalk.agent.', title, re.I) or
                re.search('info.donica.', title, re.I))


