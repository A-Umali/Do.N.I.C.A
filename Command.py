import re
import Response
from text_speech import Speech


def commandlist(transcript):
        if re.search(r'\b(oh my god)\b', transcript, re.I):
            print("what do you mean")
        if re.search(r'\b(what is your name)\b', transcript, re.I):
            Speech.speak(Response.NAME)
        if re.search(r'\b(when were you created)', transcript, re.I):
            Speech.speak(Response.CREATED)
        if re.search(r'\b(play country music)', transcript, re.I):
            Speech.speak(Response.COUNTRY)
        if re.search(r'\b(Who has the biggest nose)', transcript, re.I):
            Speech.speak(Response.SEAN)
