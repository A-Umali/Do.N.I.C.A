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
        self.modules = self.retrieve_modules(self.abs_mods_filename)

    @staticmethod
    def retrieve_modules(abs_mods_filename):
        print('modules retrieved')
        try:
            with open(abs_mods_filename, 'r') as file:
                modules = json.load(file)
                file.close()
        except Exception as e:
            raise e('modules.json file has not formatted correctly')
        return modules

    def get_modules(self, filename=None):
        if filename:
            abs_mods_filename = self.get_abs_filename(filename)
            return self.retrieve_modules(abs_mods_filename)
        return self.modules

    @staticmethod
    def get_abs_filename(filename):
        return os.path.abspath(filename)


config = Configurer()
