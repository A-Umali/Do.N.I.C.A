from Modules.Task import ActiveTask
from Modules.module_list import Module


class AnswerLife(ActiveTask):
    def action(self, text):
        try:
            self.speak('Meaning of life is pi')
        except Exception as e:
            raise e('Something went wrong with life')


class LifeModule(Module):
    def __init__(self):
        tasks = [AnswerLife()]
        super(LifeModule, self).__init__('life, meaning', tasks)