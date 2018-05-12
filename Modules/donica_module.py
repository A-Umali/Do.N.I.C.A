from Modules import base_module
import random


class DonicaModule(base_module):
    def __init__(self, *args):
        super(DonicaModule, self).__init(*args)
        self.name = self.get_configuration(section='USER', key='NAME')

    @staticmethod
    def greetings(self):
        messages = ["Hi", "Hello", "Greetings"]
        return random.choice(messages)

    @staticmethod
    def name(self):
        message = "My name is Donica"
        return message

    @staticmethod
    def meaning(self):
        message = "Donica stands for Doing Nothing Intelligent Casual Assistant"
        return message

    @staticmethod
    def created(self):
        message = "I was created on may fifth two thousand eighteen"
        return message