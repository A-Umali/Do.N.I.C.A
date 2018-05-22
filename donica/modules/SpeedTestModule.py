import speedtest
import re
from math import expm1
from donica.encode_speech import Speech

TITLE = ['INTERNET-CONNECTION']


def handle(message):
    Speech().send_speak('Analyzing')
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    download_speed = s.results.download
    upload_speed = s.results.upload
    #Speech().send_speak('Your download speed is {}'.format(str(round([s.results.download].E[6], 3))))
    Speech().send_speak('Your download speed is {}'.format(str(round(download_speed * (10**-6), 3))))
    Speech().send_speak('And your upload speed is {}'.format(str(round(upload_speed * (10**-6), 3))))
    #Speech().send_speak('Your download speed is {}'.format(str(round([download_speed].E[6], 2))))
    results_dict = s.results.dict()
    #print('Results: {}'.format(results_dict))


def is_valid(title):
    return bool(re.search('internet-connection', title, re.I))

