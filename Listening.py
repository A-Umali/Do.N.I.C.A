import sys
import re
import Command
import Speech

# This is a loop for getting responses
def listen_print_loop(responses):
    num_chars_printed = 0
    idle = True
    for response in responses:
        # print("restarted loop")

        # The `results` list is consecutive
        result = response.results[0]
        # Display the transcription of the top alternative.
        # This is for more accuracy
        transcript = result.alternatives[0].transcript

        overwrite_chars = ' ' * (num_chars_printed - len(transcript))
        if (idle is False):

            # This is what streamline is
            if not result.is_final:
                sys.stdout.write(transcript + overwrite_chars + '\r')
                # sys.stdout.flush()

                num_chars_printed = len(transcript)

            else:
                print(transcript + overwrite_chars)
                # Looking for logic
                if re.search(r'\b(thank you|stop|shut up|be quiet|never mind|exit|goodbye|bye)\b', transcript, re.I):
                    print("Exiting")
                    idle = True

                Command.commandlist(transcript)

        else:
            if re.search(r'\b(donica|doneica|downica|dunica|stonica|danica|danica|donika)\b', transcript, re.I):
                print("Donica has awaken")
                idle = False


