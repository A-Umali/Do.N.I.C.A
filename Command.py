import re
import Response
from text_speech import Speech
import donica


def commandlist(transcript):
        if re.search(r'\b(oh my god)\b', transcript, re.I):
            print('what do you mean')
        if re.search(r'\b(ku ma sta ka na|hi|howdy|hey|hello)\b', transcript, re.I):
            Speech.speak('Hello, sir')
        if re.search(r'\b(how are you|are you good|how have you been|are you ok)\b', transcript, re.I):
            Speech.speak('I am ok, depends who is asking')
        if re.search(r'\b(what is your name|whats your name)\b', transcript, re.I):
            Speech.speak(Response.NAME)
        if re.search(r'\b(what does your name mean|what does your name stand for|what does it mean)\b', transcript, re.I):
            Speech.speak(Response.MEANING)
        if re.search(r'\b(when were you created)', transcript, re.I):
            Speech.speak(Response.CREATED)
        if re.search(r'\b(play country music)', transcript, re.I):
            Speech.speak(Response.COUNTRY)
        if re.search(r'\b(Who has the biggest nose)', transcript, re.I):
            Speech.speak(Response.SEAN)
        if re.search(r'\b(Tell me a quote)\b', transcript, re.I):
            Speech.speak('If you need toes, look at your feet')
        if re.search(r'\b(Good bye|bye|thank you|shut up|be quiet)', transcript, re.I):
                breakpoint()