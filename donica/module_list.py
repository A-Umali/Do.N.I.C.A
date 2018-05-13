class ModuleList:
    def __init__(self, keywords=[], name='', priority=0):
        self._keywords = keywords
        self._name = name
        self._priority = priority

    def get_list(self):
        self._name = []
        print('Life is pi')
