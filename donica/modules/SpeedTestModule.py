import speedtest
import re
import time
from donica.encode_speech import Speech

TITLE = ['INTERNET-CONNECTION']


def handle(message):
    Speech().send_speak('Analyzing')
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    download_speed = str(round(s.results.download * (10**-6), 3))
    upload_speed = str(round(s.results.upload * (10**-6), 3))
    print('Your download speed is {} '.format(download_speed) +
          'And your upload speed is {}'.format(upload_speed))

    #Speech().send_speak('Your download speed is {}'.format(download_speed) +
    #                    'And your upload speed is {}'.format(upload_speed))


def is_valid(title):
    return bool(re.search('internet.connection', title, re.I))

