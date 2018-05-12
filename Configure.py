import os
import configparser
import json


class Configurer:
    def __init__(self, filename='config.ini', modules_filename='modules.json'):
        print('initialized')
        self.abs_filename = self.get_abs_filename(filename)
        self.abs_mods_filename = self.get_abs_filename(modules_filename)
        self.config = configparser.ConfigParser()
        self.config.read(self.abs_filename)
        self.sections = self.config.sections()

    @staticmethod
    def get_abs_filename(filename):
        return os.path.abspath(filename)


config = Configurer()
