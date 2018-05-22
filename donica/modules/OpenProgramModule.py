import re
from donica.configuration import Config

TITLE = ['OPEN-PROGRAM']

def handle(message):
    c = Config()
    if c.device_type == 'Windows':
        print('Found Windows')

    if c.device_type == 'Linux':
        print('Found Linux')

    if c.device_type == 'Mac':
        print('Found Mac')

def is_valid(title):
    return bool(re.search('open-program', title, re.I))
