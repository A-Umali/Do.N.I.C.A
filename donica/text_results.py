import logging
import sys
import re
import dialogflow_v2 as dialogflow
from donica.encode_speech import Speech
from donica.ModuleRouter import ModuleRouter


class TextResult:
    def __init__(self):
        logging.debug('Initializing Text Result class')
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path("donica-d6a80", "38d9b5565227fa8e67d1cdf23cd82cae5dd9d782")
        self.speech = Speech()
        self.module = ModuleRouter()

    def get_text_to_speech_google(self, responses, get_stream):
        num_chars_printed = 0
        for response in responses:
            if not response.results:
                continue

            result = response.results[0]

            if not result.alternatives:
                continue

            transcript = result.alternatives[0].transcript
            overwrite_chars = ' ' * (num_chars_printed - len(transcript))

            if not result.is_final:
                sys.stdout.write(transcript + overwrite_chars + '\r')
                sys.stdout.flush()
                num_chars_printed = len(transcript)
            else:
                texts = transcript+overwrite_chars
                text_input = dialogflow.types.session_pb2.TextInput(text=texts,
                                                                    language_code='en')
                query_input = dialogflow.types.session_pb2.QueryInput(text=text_input)

                dialog = self.session_client.detect_intent(session=self.session,
                                                           query_input=query_input)
                get_text = dialog.query_result.query_text
                print('Query text: {}'.format(get_text))
                intent_name = dialog.query_result.intent.display_name
                self.module.query(intent_name.split(), texts)
                print('Fulfillment text: {}'.format(intent_name))
                # print('Response: {}'.format(dialog.query_result.fulfillment_text))
                if re.search('command.exit.emergency', intent_name, re.IGNORECASE):
                    print('PROTOCOL: Emergency exit')
                    sys.exit(0)
                if re.search('command.exit', intent_name, re.IGNORECASE):
                    get_stream.closed = True
                    return get_stream
                break

