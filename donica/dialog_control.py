import dialogflow_v2 as dialogflow
from donica.encode_speech import Speech


class Dialogflow:
    def __init__(self):
        self.session_client = dialogflow.SessionsClient()
        self.session = self.session_client.session_path("donica-d6a80", "38d9b5565227fa8e67d1cdf23cd82cae5dd9d782")
        self.speech = Speech()

    def detect_intent_texts(self, texts):
        text_input = dialogflow.types.session_pb2.TextInput(text=texts,
                                                            language_code='en_US')
        query_input = dialogflow.types.session_pb2.QueryInput(text=text_input)

        response = self.session_client.detect_intent(session=self.session,
                                                     query_input=query_input)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
        self.speech.send_speak(response.query_result.fulfillment_text)

    def output_intent_texts(self, response):
        print('Fulfillment text: {}\n'.format(response.query_result.fulfillment_text))
        self.speech.send_speak(response.query_result.fulfillment_text)
