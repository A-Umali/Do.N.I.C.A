import datetime as dt
from Modules import base_module


class TimeModule(base_module):
    def __init__(self, *args):
        super(TimeModule, self).__init(*args)
        self.name = self.get_configuration(section='USER', key='NAME')

    def list_quote(self):
        return self.dt

