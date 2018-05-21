import speedtest
import re
from donica.encode_speech import Speech

TITLE = ['INTERNET-CONNECTION']


def handle(message):
    Speech().send_speak('Analyzing')
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()
    results_dict = s.results.dict()
    print('Result: {}'.format(results_dict))


def is_valid(title):
    return bool(re.search('internet-connection', title, re.I))

