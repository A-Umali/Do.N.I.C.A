import speedtest
import re
import random
import asyncio
from donica.encode_speech import Speech

TITLE = ['INTERNET-CONNECTION']


def handle(title, message):
    Speech().send_speak('Analyzing')
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    download_speed = str(round(s.results.download * (10**-6), 3))
    upload_speed = str(round(s.results.upload * (10**-6), 3))
    text = 'Your download speed is {} '.format(download_speed) + 'And your upload speed is {}'.format(upload_speed)
    formality = ['Sir, {}'.format(text),
                 text + ' Sir']
    say = random.choice(formality)
    Speech().send_speak(say)


def is_valid(title):
    return bool(re.search('command.internet.connection', title, re.I))


async def speed_test():
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    print('up')