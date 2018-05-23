import re

TITLE = ['DEFAULT']


def handle(message):
    print('handled')



def is_valid(title):
    return bool(re.fullmatch('', title, re.I))
