from encode_speech import Speech
import re

# Looking for keywords from modules
# Focus on this CLASS!!!

def analyze_speech(responses):
    #Speech.speak(responses)
    fine_words(responses)
    print(responses)

# Find modules in response and then get
# the same module execution in the next line
def fine_words(responses):
    if re.search(r'\b(%s)\b' % 'what is your name and what does it stand for', responses, re.I):
        Speech.speak('My name is Donica and it stands for Doing Nothing Intelligent Casual Assistant')


