from modules import base_module
import random


class SeanModule(base_module):
    def __init__(self, *args):
        super(SeanModule, self).__init(*args)
        self.name = self.get_configuration(section='USER', key='NAME')

    @staticmethod
    def list_quote(self):
        messages = ["If you need toes, look at your feet",
                    "Noooooooo",
                    "OOOOO SHHHIIN",
                    "I have no epidermis",
                    "cykya blyat"]
        return random.choice(messages)

