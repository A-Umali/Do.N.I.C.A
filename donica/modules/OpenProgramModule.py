import re


TITLE = ['OPEN-PROGRAM']


def is_valid(title):
    return bool(re.search('open-program', title, re.I))
