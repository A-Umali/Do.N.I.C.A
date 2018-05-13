from donica.encode_speech import Speech
import re
from donica.central import Central
from donica.module_list import ModuleList
# Looking for keywords from modules
# Focus on this CLASS!!!


def analyze_speech(responses):
    """ Key to spliting the speech to multiple arrays """
    # if re.search(r'\b(and)\b', responses, re.I):
    #    responses = responses.split('and')
    #else:
    #    responses = responses

    fine_words(responses)
    print(responses)


# Find modules in response and then get
# the same module execution in the next line
def fine_words(responses):
    if re.search(r'\b%s\b' % 'Turn off', responses, re.I):
        Speech.speak('Turning off')


def module_test(responses):
    list = ModuleList().get_list()
    print(list)


