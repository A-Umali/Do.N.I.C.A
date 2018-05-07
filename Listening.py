import sys
import re
import Response

# This is a loop for getting responses

def listen_print_loop(responses):
    num_chars_printed = 0
    for response in responses:
        # Continuing if there is no response
        if not response.results:
            continue

        # The `results` list is consecutive
        result = response.results[0]

        # Display the transcription of the top alternative.
        # This is for more accuracy
        transcript = result.alternatives[0].transcript

        overwrite_chars = ' ' * (num_chars_printed - len(transcript))

        if not result.alternatives:
            continue

        # This is what streamline is
        if not result.is_final:
            sys.stdout.write(transcript + overwrite_chars + '\r')
            sys.stdout.flush()

            num_chars_printed = len(transcript)

        else:
            print(transcript + overwrite_chars)

            # Looking for logic
            Response.commandlist(transcript)

            num_chars_printed = 0

