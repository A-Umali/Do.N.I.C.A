import configparser
import platform


class Config:
    def __init__(self):
        print('Initialized Configuration file')
        self.filename = 'config.cfg'
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)
        self.sections = self.config.sections()
        self.device_type = platform.system()
        self.retrieve(self.filename)

    def retrieve(self, filename):
        try:
            self.config.sections = ['DEFAULT']
            self.config['DEFAULT'] = {}
            self.config['DEFAULT']['main_user'] = ''
            self.config['DEFAULT']['device_type'] = str(self.device_type)
            with open(filename, 'w') as configfile:
                self.config.write(configfile)
        except Exception as e:
            print(e)

    def write(self, filename):
        if self.config.get('DEFAULT', 'main_user') is NameError:
            print('Say your name please as clearly as possible')
            self.config['DEFAULT']['main_user'] = ''
            with open(filename, 'w') as configfile:
                self.config.write(configfile)

