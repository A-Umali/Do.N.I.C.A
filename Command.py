import re
import donica
import Commands

def commandlist(transcript):
    if re.search(r'\b(oh my god)\b', transcript, re.I):
        print("what do you mean")
    if re.search(r'\b(what is your name)\b', transcript, re.I):
        print(Commands.NAME)
    if re.search(r'\b(exit|goodbye)\b', transcript, re.I):
        print("Exiting")
