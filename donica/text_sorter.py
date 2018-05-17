from donica.module_router import ModuleRouter
from donica.dialog_control import Dialogflow


def analyze_speech(responses):
    # words = responses.split('and')
    Dialogflow().detect_intent_texts(responses)
    # ModuleRouter().query(words)


