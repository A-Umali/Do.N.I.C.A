import re

TITLE = ['DEFAULT']


def handle(message):
    print('handled')


def is_valid(title):
    return bool(re.search('put on hold for a bit', title, re.I))
