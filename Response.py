import re
import donica
import Commands

def commandlist(transcript):
    if re.search(r'\b(oh my god)\b', transcript, re.I):
        print("what do you mean")
    if re.search(r'\b(|)\b'.join(Commands.COGNATE_EXIT), transcript, re.I):
        print("Exiting")
