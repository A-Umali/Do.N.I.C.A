import re
import Response
import Speech

def commandlist(transcript):
    if re.search(r'\b(oh my god)\b', transcript, re.I):
        print("what do you mean")
        Speech.speak("What do you mean?")
    if re.search(r'\b(what is your name)\b', transcript, re.I):
        print(Response.NAME)
        Speech.speak(Response.NAME)
    if re.search(r'\b(when were you created)', transcript, re.I):
        print(Response.CREATED)
        Speech.speak(Response.CREATED)
    if re.search(r'\b(play country music)', transcript, re.I):
        print(Response.COUNTRY)
        Speech.speak(Response.COUNTRY)
    if re.search(r'\b(Who has the biggest nose)', transcript, re.I):
        print(Response.SEAN)
        Speech.speak(Response.SEAN)
